"""Build the site from structured content (ADR-0006).

Reads src/content/items.json, checks every item against the schema in
src/content/README.md, computes each item's timeline grid position, renders
the templates in src/templates/, and writes index.html and static/ at the
repository root, which is where GitHub Pages serves a user site (ADR-0002).

Run with the project venv active:  python build.py

Every check runs before anything is written, so a failed build exits
non-zero and leaves the previous output untouched.
"""

from __future__ import annotations

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
TEMPLATES = ROOT / "src" / "templates"
STATIC_SRC = ROOT / "src" / "static"
OUT_INDEX = ROOT / "index.html"
OUT_STATIC = ROOT / "static"
REQUIREMENTS = ROOT / "requirements.txt"

# This site's own host. Nothing in the output may point at it absolutely:
# internal links are root-relative so a later custom domain is a DNS change,
# not a rewrite (ADR-0002).
SITE_HOST = "waqas01cp.github.io"

# Timeline scale, both figures from ADR-0003.
AXIS_START = "2024-01"
UNITS_PER_MONTH = 4

# Lane keys and the text each carries on the timeline (ADR-0003). Open source
# stays in the data model even though nothing renders in it until it holds a
# merged pull request. Brief 1 listed four lanes without it; the record wins.
LANE_LABELS = {
    "builds": "Builds",
    "opensource": "Open source",
    "work": "Work",
    "certifications": "Certifications",
    "band": "Degree",
}

# Page sections in page order: (lane, section id, heading). ADR-0001 names
# projects and certifications. No heading has been decided for the other
# lanes, so an item in one of them fails the build rather than landing under
# a guessed heading.
SECTIONS = (
    ("builds", "projects", "Projects"),
    ("certifications", "certifications", "Certifications"),
)

# Element ids the page already uses. An item id equal to one of these would
# silently break an anchor.
RESERVED_IDS = {"main", "timeline"} | {section_id for _, section_id, _ in SECTIONS}

REQUIRED = ("id", "title", "tier", "lane", "start", "end", "source",
            "layer1", "layer2", "layer3")
OPTIONAL = ("stack", "proof", "verification")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
YM_RE = re.compile(r"^(\d{4})-(0[1-9]|1[0-2])$")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


class BuildError(Exception):
    """A failure the build reports by name and exits non-zero on."""


# Timeline arithmetic. Pure functions with no template knowledge, so they can
# be tested directly by importing this module.

def month_index(ym: str) -> int:
    """Count of months since year 0 for a YYYY-MM string."""
    match = YM_RE.match(ym)
    if not match:
        raise ValueError(f"'{ym}' is not a YYYY-MM date")
    return int(match[1]) * 12 + int(match[2]) - 1


def grid_position(start: str, end: str, lane: str, as_of: str) -> tuple[int, int, bool]:
    """Return (start row, row span, starts before the axis) for one entry.

    Row 1 is January 2024 and each month is UNITS_PER_MONTH rows, so a
    single-month entry spans 4. `present` resolves to as_of, the build's
    month. Only the degree band may start before the axis. It is placed from
    row 1 and flagged, so it can be drawn running past the top edge.
    """
    first = month_index(start)
    last = month_index(as_of if end == "present" else end)
    axis = month_index(AXIS_START)
    if last < first:
        raise ValueError(f"ends {end} before it starts {start}")
    before_axis = first < axis
    if before_axis:
        if lane != "band":
            raise ValueError(f"starts {start}, before the timeline opens at "
                             f"{AXIS_START}; only the band may")
        if last < axis:
            raise ValueError(f"ends {end}, before the timeline opens at {AXIS_START}")
        first = axis
    row = (first - axis) * UNITS_PER_MONTH + 1
    span = (last - first + 1) * UNITS_PER_MONTH
    return row, span, before_axis


def date_phrase(start: str, end: str) -> dict:
    """The dates in the master CV's own forms: "Feb 2025", "Nov to Dec 2025",
    "Aug 2024 to Jan 2025", "Feb 2026 to Present". Returned as parts so the
    template can wrap each date in <time>."""
    def label(ym: str, with_year: bool = True) -> str:
        year, month = ym.split("-")
        name = MONTHS[int(month) - 1]
        return f"{name} {year}" if with_year else name

    if end == "present":
        return {"start": start, "start_text": label(start), "end": None, "end_text": "Present"}
    if end == start:
        return {"start": start, "start_text": label(start), "end": None, "end_text": None}
    same_year = start[:4] == end[:4]
    return {"start": start, "start_text": label(start, not same_year),
            "end": end, "end_text": label(end)}


# Content checks.

class _FragmentCheck(HTMLParser):
    """Accepts <strong> and <a href> only, properly nested. Layer 3 blocks are
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


def url_problem(url: str) -> str | None:
    """Why a link target is not allowed, or None if it is."""
    if url.startswith("/") and not url.startswith("//"):
        return None  # root-relative
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        return f"'{url}' is neither root-relative nor an absolute http(s) URL"
    if parts.hostname == SITE_HOST:
        return f"'{url}' points at this site's own origin; write it root-relative (ADR-0002)"
    return None


def _filled(value) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    return value not in (None, [], {})


def check_item(raw, position: int, as_of: str) -> dict:
    """Check one raw item and return it normalised for the templates.

    Raises BuildError naming the item, by id where it has one."""
    name = raw.get("id") if isinstance(raw, dict) and _filled(raw.get("id")) else f"#{position}"

    def fail(message: str):
        raise BuildError(f"item '{name}': {message}")

    if not isinstance(raw, dict):
        fail("is not a JSON object")

    # The two content gates (ADR-0006, Brief 1 task 7). Checked first, so they
    # report even on an item that is broken in other ways too.
    if not _filled(raw.get("source")):
        fail("has no source. Every item must trace to the master CV (ADR-0006)")
    has_proof, has_verification = _filled(raw.get("proof")), _filled(raw.get("verification"))
    if has_proof and has_verification:
        fail("has both proof and verification. Give exactly one (ADR-0006)")
    if not has_proof and not has_verification:
        fail("has neither proof nor verification. Give exactly one (ADR-0006)")

    unknown = sorted(set(raw) - set(REQUIRED) - set(OPTIONAL))
    if unknown:
        fail(f"has fields the schema does not define: {', '.join(unknown)}")
    missing = [field for field in REQUIRED if field not in raw]
    if missing:
        fail(f"is missing required fields: {', '.join(missing)}")

    for field in ("id", "title", "source", "layer1", "layer2", "stack", "verification"):
        if field in raw and not (isinstance(raw[field], str) and _filled(raw[field])):
            fail(f"{field} must be non-empty text")
    if not ID_RE.match(raw["id"]):
        fail("id must be a lowercase slug: letters, digits and single hyphens")
    if raw["id"] in RESERVED_IDS:
        fail(f"id '{raw['id']}' is already used by the page itself")
    if type(raw["tier"]) is not int or raw["tier"] not in (1, 2, 3):
        fail("tier must be 1, 2 or 3")
    if raw["lane"] not in LANE_LABELS:
        fail(f"lane must be one of: {', '.join(LANE_LABELS)}")
    if not (isinstance(raw["end"], str) and (raw["end"] == "present" or YM_RE.match(raw["end"]))):
        fail("end must be YYYY-MM or present")
    if not isinstance(raw["start"], str):
        fail("start must be YYYY-MM")
    try:
        row, span, before_axis = grid_position(raw["start"], raw["end"], raw["lane"], as_of)
    except ValueError as error:
        fail(str(error))

    proof = raw.get("proof")
    if has_proof:
        if not isinstance(proof, list):
            fail("proof must be a list of {label, url}")
        for link in proof:
            if not (isinstance(link, dict) and set(link) == {"label", "url"}
                    and all(isinstance(link[k], str) and _filled(link[k]) for k in link)):
                fail("each proof entry must be exactly {label, url}, both non-empty text")
            if problem := url_problem(link["url"]):
                fail(f"proof link {problem}")

    blocks = raw["layer3"]
    if not (isinstance(blocks, list) and blocks
            and all(isinstance(b, str) and _filled(b) for b in blocks)):
        fail("layer3 must be a non-empty list of non-empty text blocks")
    for number, block in enumerate(blocks, start=1):
        checker = _FragmentCheck()
        checker.feed(block)
        checker.close()
        problems = checker.problems + [p for p in map(url_problem, checker.hrefs) if p]
        if problems:
            fail(f"layer3 block {number}: {'; '.join(problems)}")

    return {
        "id": raw["id"],
        "title": raw["title"],
        "lane": raw["lane"],
        "lane_label": LANE_LABELS[raw["lane"]],
        "start": raw["start"],
        "stack": raw.get("stack"),
        "proof": proof if has_proof else None,
        "verification": raw.get("verification"),
        "layer1": raw["layer1"],
        "layer2": raw["layer2"],
        "layer3": blocks,
        "when": date_phrase(raw["start"], raw["end"]),
        "row": row,
        "span": span,
        "before_axis": before_axis,
    }


def load_items(path: Path, as_of: str) -> list[dict]:
    """Read and check every item. Reports every failing item, not only the first."""
    shown = path.relative_to(ROOT).as_posix()
    try:
        raw_items = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise BuildError(f"content file not found: {shown}") from None
    except json.JSONDecodeError as error:
        raise BuildError(f"{shown} is not valid JSON: {error}") from None
    if not isinstance(raw_items, list) or not raw_items:
        raise BuildError(f"{shown} must be a non-empty JSON array, one entry per item")

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

    placed = {lane for lane, _, _ in SECTIONS}
    problems += [f"item '{item['id']}': lane '{item['lane']}' has no page section yet; "
                 f"ADR-0001 names projects and certifications, and no heading is "
                 f"decided for this lane" for item in items if item["lane"] not in placed]
    if problems:
        raise BuildError("\n".join(problems))
    return items


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


def render(sections: list[dict], timeline: list[dict]) -> str:
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
        return env.get_template("base.html.j2").render(sections=sections, timeline=timeline)
    except jinja2.TemplateError as error:
        raise BuildError(f"template error: {error}") from None


def main() -> int:
    as_of = datetime.now(timezone.utc).strftime("%Y-%m")
    try:
        check_environment()
        items = load_items(CONTENT, as_of)
        sections = []
        for lane, section_id, heading in SECTIONS:
            members = [item for item in items if item["lane"] == lane]
            if members:
                # "members", not "items": Jinja resolves section.items to dict.items.
                sections.append({"id": section_id, "heading": heading, "members": members})
        # Date order by start month; items starting in the same month keep
        # their content-file order.
        timeline = sorted(items, key=lambda item: month_index(item["start"]))
        html = render(sections, timeline)
    except BuildError as error:
        print(f"build failed:\n{error}", file=sys.stderr)
        return 1

    OUT_INDEX.write_text(html, encoding="utf-8", newline="\n")
    if OUT_STATIC.exists():
        shutil.rmtree(OUT_STATIC)
    shutil.copytree(STATIC_SRC, OUT_STATIC, copy_function=shutil.copyfile)
    copied = sum(1 for path in OUT_STATIC.rglob("*") if path.is_file())
    print(f"built index.html: {len(items)} item(s), timeline as of {as_of} UTC; "
          f"copied {copied} static file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
