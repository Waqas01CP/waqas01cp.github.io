"""Build the site from structured content (ADR-0006).

Reads src/content/items.json, every dated item, and src/content/site.json,
the text that belongs to the page rather than to one item. Checks both
against the schema in src/content/README.md, computes the timeline and the
project grid, renders the templates in src/templates/, and writes
index.html and static/ at the repository root, which is where GitHub Pages
serves a user site (ADR-0002).

Run with the project venv active:

  python build.py                    as of the current UTC month
  python build.py --as-of YYYY-MM    as of the given month

The as-of month is what `present` resolves to and the top of the timeline,
and it is written into the output as <meta name="as-of">. The rebuild gate
reads it back from the staged index.html and rebuilds with it, so the gate
never consults the clock and does not fail on the first of each month
(ADR-0006 Changes).

Every check runs before anything is written, so a failed build exits
non-zero and leaves the previous output untouched.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from importlib import metadata
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "src" / "content" / "items.json"
SITE = ROOT / "src" / "content" / "site.json"
TEMPLATES = ROOT / "src" / "templates"
STATIC_SRC = ROOT / "src" / "static"
OUT_INDEX = ROOT / "index.html"
OUT_STATIC = ROOT / "static"
REQUIREMENTS = ROOT / "requirements.txt"

# The downloadable CV. The link renders in the Intro and the footer only when
# this file exists in the tree being built, so gate B's rebuild of the staged
# tree and the committed output agree on it (ADR-0008).
CV_FILE = ROOT / "cv" / "Waqas_Sharif_CV.pdf"
CV_URL = "/cv/Waqas_Sharif_CV.pdf"

# This site's own host. Nothing in the output may point at it absolutely:
# internal links are root-relative so a later custom domain is a DNS change,
# not a rewrite (ADR-0002).
SITE_HOST = "waqas01cp.github.io"

# Timeline scale from ADR-0003: four layout units per month, the axis
# running from the as-of month at the top down to January 2024 (Changes,
# 2026-10-03). The size of a unit is the stylesheet's.
AXIS_START = "2024-01"
UNITS_PER_MONTH = 4

# Lane keys and the text each carries (ADR-0003). Open source stays in the
# data model, but nothing renders in it until it holds a merged pull request.
LANE_LABELS = {
    "builds": "Builds",
    "opensource": "Open source",
    "work": "Work",
    "certifications": "Certifications",
    "band": "Degree",
}
# The timeline columns, left to right: Builds left of the spine, Work and
# Certifications right of it. The band is drawn behind all of them.
TIMELINE_LANES = ("builds", "work", "certifications")

# The eight sections in page order (ADR-0008 Changes, 2026-10-02), and the
# section each lane's items render in. The degree's lane, band, renders in
# Education. A lane with no section here fails the build rather than
# landing under a guessed heading: today that is opensource.
SECTIONS = (
    ("intro", "Intro"),
    ("projects", "Projects"),
    ("timeline", "Timeline"),
    ("work", "Work"),
    ("education", "Education"),
    ("certifications", "Certifications"),
    ("skills", "Skills"),
    ("contact", "Contact"),
)
LANE_SECTION = {"builds": "projects", "work": "work", "band": "education",
                "certifications": "certifications"}

# ADR-0010: HubIT, PAC Kamra and the degree carry neither a proof link nor a
# verification line; every other item carries a proof link. Naming the three
# here is what makes "any other item without one fails" enforceable.
NO_PROOF_IDS = {"hubit", "pac-kamra", "be-software-engineering"}

# Element ids the page uses itself, and the prefixes it builds ids from. An
# item id equal to one of these would silently break an anchor.
RESERVED_IDS = {"main", "top"} | {section_id for section_id, _ in SECTIONS}
RESERVED_PREFIXES = ("depth-", "toggle-", "tl-", "h-")

COMMON = ("id", "lane", "title", "start", "end", "source")
PROOF_ROUTES = ("proof", "verification", "no_proof")
LANE_FIELDS = {
    # lane: (required, optional)
    "builds": (("tier", "stack", "layer1", "bullets"), ("status", "layer2", "detail")),
    "work": (("org", "location", "bullets"), ("org_short", "date_style", "detail")),
    "band": (("org", "org_short", "cgpa", "cgpa_scale", "coursework"), ("date_style",)),
    "certifications": ((), ("org", "date_style")),
    "opensource": ((), ("org", "detail", "date_style")),
}
DATE_STYLES = ("compact", "full", "long")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
YM_RE = re.compile(r"^(\d{4})-(0[1-9]|1[0-2])$")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
MONTHS_LONG = ("January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December")

# The project grid: Rahzaan, tier 1, takes a full row; the rest flow three
# to a row on a wide screen and two on a medium one, and a short last row
# shares its width. Columns of a six-column grid, so 2, 3 or 6 per card.
GRID_COLUMNS = 6


class BuildError(Exception):
    """A failure the build reports by name and exits non-zero on."""


# Dates. Pure functions with no template knowledge, so they can be tested
# directly by importing this module.

def month_index(ym: str) -> int:
    """Count of months since year 0 for a YYYY-MM string."""
    match = YM_RE.match(ym)
    if not match:
        raise ValueError(f"'{ym}' is not a YYYY-MM date")
    return int(match[1]) * 12 + int(match[2]) - 1


def month_name(index: int, long: bool = False) -> str:
    return (MONTHS_LONG if long else MONTHS)[index % 12]


def grid_position(start: str, end: str, lane: str, as_of: str) -> tuple[int, int, bool]:
    """Return (start row, row span, starts before the axis) for one entry.

    Newest at the top (ADR-0003 Changes, 2026-10-03): row 1 is the as-of
    month, each month is UNITS_PER_MONTH rows going down, and the axis ends
    at January 2024. An entry's row is set by its end month and its span by
    its length, so moving an end date by a month moves only that entry's top
    edge, by four rows. `present` resolves to as_of. Only the degree band
    may start before the axis, or end after the as-of month; it is clipped
    to the axis and flagged so it can be drawn running past the bottom edge.
    """
    first = month_index(start)
    last = month_index(as_of if end == "present" else end)
    top, axis = month_index(as_of), month_index(AXIS_START)
    if last < first:
        raise ValueError(f"ends {end} before it starts {start}")
    if first > top:
        raise ValueError(f"starts {start}, after the as-of month {as_of}")
    if last > top:
        if lane != "band":
            raise ValueError(f"ends {end}, after the as-of month {as_of}")
        last = top
    before_axis = first < axis
    if before_axis:
        if lane != "band":
            raise ValueError(f"starts {start}, before the timeline opens at "
                             f"{AXIS_START}; only the band may")
        if last < axis:
            raise ValueError(f"ends {end}, before the timeline opens at {AXIS_START}")
        first = axis
    row = (top - last) * UNITS_PER_MONTH + 1
    span = (last - first + 1) * UNITS_PER_MONTH
    return row, span, before_axis


def date_phrase(start: str, end: str, style: str = "compact") -> dict:
    """The dates in the master CV's own forms, returned as parts so the
    template can wrap each date in <time>.

    compact: "Feb 2025", "Nov to Dec 2025", "Aug 2024 to Jan 2025",
             "Feb 2026 to Present". The default, and the timeline's form.
    full:    "Jan 2024 to Feb 2024": both years, as the master writes PAC
             Kamra and the degree.
    long:    "June 2026 to July 2026": month names in full, as the master
             writes HubIT.
    """
    long = style == "long"

    def label(ym: str, with_year: bool = True) -> str:
        year, month = ym.split("-")
        name = month_name(int(month) - 1, long)
        return f"{name} {year}" if with_year else name

    if end == "present":
        return {"start": start, "start_text": label(start), "end": None, "end_text": "Present"}
    if end == start:
        return {"start": start, "start_text": label(start), "end": None, "end_text": None}
    same_year = start[:4] == end[:4] and style == "compact"
    return {"start": start, "start_text": label(start, not same_year),
            "end": end, "end_text": label(end)}


def date_plain(phrase: dict) -> str:
    text = phrase["start_text"]
    return f"{text} to {phrase['end_text']}" if phrase["end_text"] else text


# Cuts. Text shortened from the master is stored as written, and the build
# refuses any that is not a cut of the item's own text: the same words in
# the same order with some left out. A number changed in one place and not
# the other fails here, so each fact keeps one authority (ADR-0006).

WORD_RE = re.compile(r"\d+(?:[.,]\d+)*%?|[^\W\d_]+")
TAG_RE = re.compile(r"<[^>]+>")


def plain(fragment: str) -> str:
    return html.unescape(TAG_RE.sub("", fragment))


def words(text: str) -> list[str]:
    return WORD_RE.findall(plain(text).lower())


def is_cut(part: str, source: str) -> bool:
    remaining = iter(words(source))
    return all(word in remaining for word in words(part))


# Fragments.

class _FragmentCheck(HTMLParser):
    """Accepts <strong> and <a href> only, properly nested. Bullets are
    rendered unescaped, so this is what stands between the content file and
    arbitrary markup in the page (Brief 1, 8a)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.problems: list[str] = []
        self.hrefs: list[str] = []
        self._open: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "strong" and not attrs:
            self._open.append(tag)
        elif tag == "a" and len(attrs) == 1 and attrs[0][0] == "href" and attrs[0][1]:
            self._open.append(tag)
            self.hrefs.append(attrs[0][1])
        else:
            names = "".join(f" {name}" for name, _ in attrs)
            self.problems.append(f"<{tag}{names}> is not allowed; only <strong> and <a href>")

    def handle_startendtag(self, tag, attrs):
        self.problems.append(f"<{tag}/> is not allowed; only <strong> and <a href>")

    def handle_endtag(self, tag):
        if self._open and self._open[-1] == tag:
            self._open.pop()
        else:
            self.problems.append(f"</{tag}> closes nothing that is open")

    def handle_comment(self, data):
        self.problems.append("an HTML comment is not allowed")

    def handle_decl(self, decl):
        self.problems.append("a declaration is not allowed")

    def handle_pi(self, data):
        self.problems.append("a processing instruction is not allowed")

    def unknown_decl(self, data):
        self.problems.append("a declaration is not allowed")

    def close(self):
        super().close()
        self.problems.extend(f"<{tag}> is never closed" for tag in self._open)


def fragment_problems(fragment: str) -> list[str]:
    checker = _FragmentCheck()
    checker.feed(fragment)
    checker.close()
    return checker.problems + [p for p in map(url_problem, checker.hrefs) if p]


def url_problem(url: str) -> str | None:
    """Why a link target is not allowed, or None if it is."""
    if url.startswith("/") and not url.startswith("//"):
        return None  # root-relative
    parts = urlsplit(url)
    if parts.scheme == "mailto" and parts.path:
        return None
    if parts.scheme not in ("http", "https") or not parts.hostname:
        return f"'{url}' is neither root-relative nor an absolute http(s) URL"
    if parts.hostname == SITE_HOST:
        return f"'{url}' points at this site's own origin; write it root-relative (ADR-0002)"
    return None


def _filled(value) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    return value not in (None, [], {})


def _text(value) -> bool:
    return isinstance(value, str) and _filled(value)


def _text_list(value) -> bool:
    return isinstance(value, list) and bool(value) and all(_text(v) for v in value)


# Items.

def check_item(raw, position: int, as_of: str) -> dict:
    """Check one raw item and return it normalised for the templates.

    Raises BuildError naming the item, by id where it has one."""
    name = raw.get("id") if isinstance(raw, dict) and _filled(raw.get("id")) else f"#{position}"

    def fail(message: str):
        raise BuildError(f"item '{name}': {message}")

    if not isinstance(raw, dict):
        fail("is not a JSON object")

    # The two content gates (ADR-0006), checked first so they report even on
    # an item that is broken in other ways too. ADR-0010 names the only items
    # that may carry no proof link.
    if not _filled(raw.get("source")):
        fail("has no source. Every item must trace to the master CV (ADR-0006)")
    routes = [route for route in PROOF_ROUTES if _filled(raw.get(route))]
    if len(routes) > 1:
        fail(f"has {' and '.join(routes)}. Give exactly one proof route (ADR-0006)")
    if not routes:
        fail("has no proof link, verification or no_proof. Give exactly one (ADR-0006, ADR-0010)")
    if routes == ["no_proof"] and raw.get("id") not in NO_PROOF_IDS:
        fail("may not go without a proof link: ADR-0010 exempts only HubIT, PAC Kamra "
             "and the degree")

    lane = raw.get("lane")
    if lane not in LANE_FIELDS:
        fail(f"lane must be one of: {', '.join(LANE_FIELDS)}")
    required, optional = LANE_FIELDS[lane]
    allowed = set(COMMON) | set(PROOF_ROUTES) | set(required) | set(optional)
    unknown = sorted(set(raw) - allowed)
    if unknown:
        fail(f"has fields the schema does not define for the {lane} lane: {', '.join(unknown)}")
    missing = [field for field in COMMON + required if field not in raw]
    if missing:
        fail(f"is missing required fields: {', '.join(missing)}")

    for field in ("id", "title", "source", "org", "org_short", "location", "layer1",
                  "layer2", "status", "detail", "verification", "no_proof", "cgpa",
                  "cgpa_scale"):
        if field in raw and not _text(raw[field]):
            fail(f"{field} must be non-empty text")
    for field in ("stack", "bullets", "coursework"):
        if field in raw and not _text_list(raw[field]):
            fail(f"{field} must be a non-empty list of non-empty text")
    if not ID_RE.match(raw["id"]):
        fail("id must be a lowercase slug: letters, digits and single hyphens")
    if raw["id"] in RESERVED_IDS or raw["id"].startswith(RESERVED_PREFIXES):
        fail(f"id '{raw['id']}' is already used, or reserved, by the page itself")
    if "tier" in raw and (type(raw["tier"]) is not int or raw["tier"] not in (1, 2, 3)):
        fail("tier must be 1, 2 or 3")
    style = raw.get("date_style", "compact")
    if style not in DATE_STYLES:
        fail(f"date_style must be one of: {', '.join(DATE_STYLES)}")
    if not (isinstance(raw["end"], str) and (raw["end"] == "present" or YM_RE.match(raw["end"]))):
        fail("end must be YYYY-MM or present")
    if not isinstance(raw["start"], str):
        fail("start must be YYYY-MM")
    try:
        row, span, before_axis = grid_position(raw["start"], raw["end"], lane, as_of)
    except ValueError as error:
        fail(str(error))

    proof = raw.get("proof")
    if "proof" in routes:
        if not isinstance(proof, list):
            fail("proof must be a list of {label, url}")
        for link in proof:
            if not (isinstance(link, dict) and set(link) == {"label", "url"}
                    and all(_text(link[k]) for k in link)):
                fail("each proof entry must be exactly {label, url}, both non-empty text")
            if problem := url_problem(link["url"]):
                fail(f"proof link {problem}")

    bullets = raw.get("bullets", [])
    for number, bullet in enumerate(bullets, start=1):
        if problems := fragment_problems(bullet):
            fail(f"bullet {number}: {'; '.join(problems)}")

    # Shortened text must be a cut of the item's own text.
    if "layer1" in raw and not any(is_cut(raw["layer1"], b) for b in bullets):
        fail("layer1 is not a cut of any of its bullets: the same words in the same "
             "order with some left out")
    if lane == "builds" and len(bullets) == 1:
        # One bullet renders no disclosure (ADR-0010), so the visible layers
        # must carry all of it.
        shown = words(raw.get("layer2", "")) + words(raw["layer1"])
        if shown != words(bullets[0]):
            fail("has one bullet and no disclosure, so layer2 then layer1 must carry "
                 "the whole bullet, word for word")
    if "detail" in raw:
        sources = [f"{raw.get('status', '')} {raw.get('layer2', '')}", raw.get("layer1", "")] + bullets
        if not any(is_cut(raw["detail"], s) for s in sources if s.strip()):
            fail("detail is not a cut of its status and layer2, its layer1 or a bullet")
    if "org_short" in raw and not is_cut(raw["org_short"], raw["org"]):
        fail("org_short is not a cut of org")

    title_name, _, title_sub = raw["title"].partition(": ")
    phrase = date_phrase(raw["start"], raw["end"], style)
    compact = date_phrase(raw["start"], raw["end"])
    first = month_index(raw["start"])
    last = month_index(as_of if raw["end"] == "present" else raw["end"])
    return {
        **{k: raw.get(k) for k in ("id", "lane", "title", "source", "tier", "status", "org",
                                   "location", "layer1", "layer2", "detail", "verification",
                                   "cgpa", "cgpa_scale")},
        "name": title_name,
        "sub": title_sub or None,
        "org_short": raw.get("org_short") or raw.get("org"),
        "stack": raw.get("stack", []),
        "bullets": bullets,
        "coursework": raw.get("coursework", []),
        "proof": proof if "proof" in routes else [],
        "lane_label": LANE_LABELS[lane],
        "start": raw["start"],
        "end": raw["end"],
        "when": phrase,
        "when_text": date_plain(phrase),
        "when_compact": compact,
        "when_compact_text": date_plain(compact),
        "months": last - first + 1,
        "first": first,
        "last": last,
        "row": row,
        "span": span,
        "before_axis": before_axis,
        "has_depth": len(bullets) > 1,
    }


def load_json(path: Path, kind: type):
    shown = path.relative_to(ROOT).as_posix()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise BuildError(f"content file not found: {shown}") from None
    except json.JSONDecodeError as error:
        raise BuildError(f"{shown} is not valid JSON: {error}") from None
    if not isinstance(data, kind) or not data:
        raise BuildError(f"{shown} must be a non-empty JSON {kind.__name__}")
    return data


def load_items(path: Path, as_of: str) -> list[dict]:
    """Read and check every item. Reports every failing item, not only the first."""
    raw_items = load_json(path, list)
    items, problems, seen = [], [], set()
    for position, raw in enumerate(raw_items, start=1):
        try:
            item = check_item(raw, position, as_of)
        except BuildError as error:
            problems.append(str(error))
            continue
        if item["id"] in seen:
            problems.append(f"item '{item['id']}': id is used by an earlier item")
        seen.add(item["id"])
        items.append(item)

    problems += [f"item '{item['id']}': lane '{item['lane']}' has no page section; "
                 f"ADR-0008 places builds, work, the degree band and certifications, and "
                 f"nothing else yet" for item in items if item["lane"] not in LANE_SECTION]
    bands = [item for item in items if item["lane"] == "band"]
    if len(bands) > 1:
        problems.append("more than one item is in the band lane; the timeline draws one degree band")

    # Tier is an assertion about the content file's order, never a second
    # order: down the file, tier must not decrease. Sorting by tier instead
    # would let the file and the page disagree silently (ADR-0010).
    highest = None
    for item in (item for item in items if item["lane"] == "builds"):
        if highest and item["tier"] < highest["tier"]:
            problems.append(f"item '{highest['id']}' (tier {highest['tier']}) is above "
                            f"item '{item['id']}' (tier {item['tier']}) in Projects; "
                            f"tier must not decrease down the content file")
        if highest is None or item["tier"] > highest["tier"]:
            highest = item
    if problems:
        raise BuildError("\n".join(problems))
    return items


# Site-level content.

def resolve(ref: str, site: dict, by_id: dict) -> str:
    """The text a highlight is cut from: 'site/summary' or '<item>/bullets/<n>'."""
    if ref == "site/summary":
        return site["summary"]
    match = re.match(r"^([a-z0-9-]+)/bullets/(\d+)$", ref)
    if not match or match[1] not in by_id:
        raise BuildError(f"site.json: '{ref}' names no source; use site/summary or <item>/bullets/<n>")
    bullets = by_id[match[1]]["bullets"]
    number = int(match[2])
    if not 1 <= number <= len(bullets):
        raise BuildError(f"site.json: '{ref}': {match[1]} has {len(bullets)} bullet(s)")
    return bullets[number - 1]


def split_figure(figure: str) -> dict:
    """'24-node' becomes a number set large and a suffix set small; a figure
    with no digits, such as 'three', is set as a word."""
    match = re.match(r"^(\d+(?:[.,]\d+)*%?\+?)(.*)$", figure)
    if match:
        return {"number": match[1], "suffix": match[2], "word": None}
    return {"number": None, "suffix": "", "word": figure}


def load_site(path: Path, items: list[dict]) -> dict:
    site = load_json(path, dict)
    by_id = {item["id"]: item for item in items}
    problems = []

    def need(key, check, what):
        if not check(site.get(key)):
            problems.append(f"site.json: {key} must be {what}")

    need("source", _text, "non-empty text tracing it to the master CV")
    for key in ("name", "location", "availability", "summary", "email"):
        need(key, _text, "non-empty text")
    need("headline", _text_list, "a non-empty list of text")
    for key in ("linkedin", "github"):
        value = site.get(key)
        if not (isinstance(value, dict) and _text(value.get("url")) and _text(value.get("text"))):
            problems.append(f"site.json: {key} must be {{url, text}}")
        elif problem := url_problem(value["url"]):
            problems.append(f"site.json: {key}: {problem}")
    approved = site.get("approved")
    if approved is not None and not (isinstance(approved, dict) and _text(approved.get("text"))
                                     and _text(approved.get("approved_by"))):
        problems.append("site.json: approved must be {text, approved_by}")
    skills = site.get("skills")
    if not (isinstance(skills, list) and skills and all(
            isinstance(g, dict) and set(g) == {"label", "items"} and _text(g["label"])
            and _text_list(g["items"]) for g in skills)):
        problems.append("site.json: skills must be a list of {label, items}")
    contact = site.get("contact")
    routes = [c.get("route") for c in contact] if isinstance(contact, list) else []
    if routes != ["email", "linkedin", "github"]:
        problems.append("site.json: contact must list email, linkedin and github, in that "
                        "order (ADR-0002 Changes)")
    if problems:
        raise BuildError("\n".join(problems))

    def cut_checked(where: str, entry: dict, parts: list[str]) -> str:
        if entry.get("item") not in by_id:
            raise BuildError(f"site.json: {where}: item '{entry.get('item')}' does not exist")
        source = resolve(entry.get("from", ""), site, by_id)
        for part in parts:
            if not is_cut(part, source):
                raise BuildError(f"site.json: {where}: '{part}' is not a cut of {entry['from']}")
        return by_id[entry["item"]]["name"]

    highlights = []
    for number, entry in enumerate(site.get("highlights", []), start=1):
        whole = " ".join(filter(None, (entry.get("before"), entry.get("figure"), entry.get("text"))))
        label = cut_checked(f"highlight {number}", entry, [whole])
        highlights.append({"before": None, **entry, "label": label,
                           "figure_parts": split_figure(entry["figure"])})
    feature = site.get("feature")
    if feature:
        parts = [feature["label"], f"{feature['figure']} {feature['text']}", feature["note"]]
        parts += [f"{p['figure']} {p['text']}" for p in feature["pairs"]]
        feature = {**feature, "name": cut_checked("feature", feature, parts)}
    return {**site, "highlights": highlights, "feature": feature}


# Layout.

def sub_columns(entries: list[dict]) -> None:
    """Within one lane, give overlapping entries side-by-side columns, the
    longest placed first. Writes x and w, as percentages of the lane, onto
    each entry. Builds sits left of the spine, so its first column is the
    one nearest the spine, on the right."""
    def overlaps(a, b):
        return a["first"] <= b["last"] and b["first"] <= a["last"]

    columns: list[list[dict]] = []
    for entry in sorted(entries, key=lambda e: (-e["months"], -e["last"])):
        index = 0
        while index < len(columns) and any(overlaps(o, entry) for o in columns[index]):
            index += 1
        if index == len(columns):
            columns.append([])
        columns[index].append(entry)
        entry["column"] = index
    shares = [45, 55] if len(columns) == 2 else [100 / max(1, len(columns))] * len(columns)
    for entry in entries:
        entry["gl"] = entry["gr"] = 0
        if not any(o is not entry and overlaps(o, entry) for o in entries):
            entry["x"], entry["w"] = 0, 100
            continue
        start, width = sum(shares[:entry["column"]]), shares[entry["column"]]
        if entry["lane"] == "builds":
            start = 100 - start - width
        entry["x"], entry["w"] = round(start, 3), round(width, 3)
        # A 3px gutter on each side that meets a neighbouring column.
        entry["gl"] = 3 if start > 0 else 0
        entry["gr"] = 3 if start + width < 100 else 0


def timeline_layout(items: list[dict], as_of: str) -> dict:
    """Everything the timeline template places: the entries newest first, the
    month and year marks on the axis, and the band."""
    top, axis = month_index(as_of), month_index(AXIS_START)
    order = {item["id"]: n for n, item in enumerate(items)}
    # Newest first by start month, then by end month; ties keep the content
    # file's order. This is the order of the list in the HTML.
    entries = sorted(items, key=lambda i: (-i["first"], -i["last"], order[i["id"]]))
    for lane in TIMELINE_LANES:
        sub_columns([e for e in entries if e["lane"] == lane])

    band = next((e for e in entries if e["lane"] == "band"), None)
    seen_years = set()
    for entry in entries:
        entry["year"] = entry["start"][:4]
        entry["year_mark"] = entry["lane"] != "band" and entry["year"] not in seen_years
        if entry["year_mark"]:
            seen_years.add(entry["year"])
        if band and entry is not band:
            entry["band_place"] = ("after-band" if entry["first"] > band["last"]
                                   else "in-band" if entry["last"] >= band["first"] else "before-band")
        else:
            entry["band_place"] = None

    months = top - axis + 1
    marks = [{"label": month_name(m), "row": (top - m) * UNITS_PER_MONTH + 1}
             for m in range(top, axis - 1, -1)]
    years = []
    for year in range(top // 12, axis // 12 - 1, -1):
        december = min(year * 12 + 11, top)
        years.append({"year": year, "row": (top - december) * UNITS_PER_MONTH + 1,
                      "line": december != top})
    return {"entries": entries, "band": band, "rows": months * UNITS_PER_MONTH,
            "months": months, "marks": marks, "years": years,
            "lanes": [{"key": k, "label": LANE_LABELS[k]} for k in TIMELINE_LANES
                      if any(e["lane"] == k for e in entries)],
            "band_start_text": date_plain(date_phrase(band["start"], band["start"])) if band else None}


def project_grid(projects: list[dict]) -> None:
    """How many of the six grid columns each project card spans, on a wide
    screen (three to a row) and a medium one (two to a row). Tier 1 takes a
    full row; in a short last row the cards share its width."""
    rest = [p for p in projects if p["tier"] != 1]
    for project in projects:
        project["span_wide"] = project["span_mid"] = GRID_COLUMNS
    for per_row, key in ((3, "span_wide"), (2, "span_mid")):
        for start in range(0, len(rest), per_row):
            row = rest[start:start + per_row]
            for project in row:
                project[key] = GRID_COLUMNS // len(row)


# Environment and output.

def check_environment() -> None:
    """Refuse to build outside a virtual environment or against a package
    version other than the pinned one. The output depends on the templating
    version, and a build that silently used another would differ from the
    committed output with no visible cause (Brief 1, task 2)."""
    if sys.prefix == sys.base_prefix:
        raise BuildError("not running inside a virtual environment. "
                         "Activate .venv first; see CLAUDE.md, Commands")
    for line in REQUIREMENTS.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        name, _, pinned = (part.strip() for part in line.partition("=="))
        if not pinned:
            raise BuildError(f"requirements.txt: '{line}' is not pinned with ==")
        try:
            installed = metadata.version(name)
        except metadata.PackageNotFoundError:
            raise BuildError(f"{name} is not installed in this environment. "
                             "Run: pip install -r requirements.txt") from None
        if installed != pinned:
            raise BuildError(f"{name} {installed} is installed but requirements.txt pins {pinned}")


def render(context: dict) -> str:
    # Imported here, after check_environment, so a build outside the venv
    # reports that rather than a bare ImportError.
    import jinja2

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES),
        # Always on. select_autoescape() keys on the file extension and would
        # leave these .html.j2 templates unescaped.
        autoescape=True,
        undefined=jinja2.StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    try:
        return env.get_template("base.html.j2").render(**context)
    except jinja2.TemplateError as error:
        raise BuildError(f"template error: {error}") from None


def _year_month(value: str) -> str:
    if not YM_RE.match(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not a YYYY-MM month")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build index.html and static/ from src/.")
    parser.add_argument("--as-of", type=_year_month, metavar="YYYY-MM",
                        help="the month 'present' resolves to; default: the current UTC month")
    args = parser.parse_args(argv)
    as_of = args.as_of or datetime.now(timezone.utc).strftime("%Y-%m")
    try:
        check_environment()
        items = load_items(CONTENT, as_of)
        site = load_site(SITE, items)
        by_lane = {lane: [i for i in items if i["lane"] == lane] for lane in LANE_LABELS}
        project_grid(by_lane["builds"])
        timeline = timeline_layout(items, as_of)
        context = {
            "as_of": as_of,
            "site": site,
            "sections": [{"id": sid, "label": label, "n": f"{n:02d}"}
                         for n, (sid, label) in enumerate(SECTIONS, start=1)],
            "projects": by_lane["builds"],
            "work": by_lane["work"],
            "degree": by_lane["band"][0] if by_lane["band"] else None,
            "certifications": by_lane["certifications"],
            "timeline": timeline,
            "cv": CV_URL if CV_FILE.is_file() else None,
        }
        html_out = render(context)
    except BuildError as error:
        print(f"build failed:\n{error}", file=sys.stderr)
        return 1

    OUT_INDEX.write_text(html_out, encoding="utf-8", newline="\n")
    if OUT_STATIC.exists():
        shutil.rmtree(OUT_STATIC)
    shutil.copytree(STATIC_SRC, OUT_STATIC, copy_function=shutil.copyfile)
    copied = sum(1 for path in OUT_STATIC.rglob("*") if path.is_file())
    print(f"built index.html: {len(items)} item(s), as of {as_of}; "
          f"copied {copied} static file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
