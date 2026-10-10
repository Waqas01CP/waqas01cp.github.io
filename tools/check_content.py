"""Trace every piece of text on the built page to the master CV.

  python tools/check_content.py --master <path to the master CV>

The master lives outside this repository and its path is never written into
it (CLAUDE.md), so it is given on the command line each time. Reads the
built index.html, not the source, because the page is what a reader and a
crawler see. Standard library only (scope floor line 14).

Two checks, both reported in full:

  Trace. The page is split into blocks of text: every paragraph, heading,
  list item, summary and button, plus the machine-readable text a crawler
  also reads (title, meta description, alt and aria-label). Each block must
  be one of:
    - a cut of one master paragraph: the same words in the same order, some
      left out, with every number still followed by the word that follows
      it in the master, so "592 automated tests" cannot become "60
      automated tests";
    - a run of such cuts from one master entry, split where the page's own
      markup splits it, such as a timeline entry's dates, then its title;
    - approved interface text: section names, labels, the contact lines,
      "In depth", year and month markers and the like, listed below;
    - the operator-approved text named in src/content/site.json, which is
      reported as not in the master, and whose every number must still be
      in the master, followed by the same word.
  Anything else fails, with the block printed.

  Coverage. Every master bullet, the summary, every sentence of every
  project's italic line, every skills line, every course and every
  certificate must appear on the page whole, in the master's word order;
  and every link that ends a project's italic line must be on the page as
  a link, with its label and its address.

Exit 0 when both pass, 1 when either fails, 2 on a usage error.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
SITE = ROOT / "src" / "content" / "site.json"

# This site's host is written once, in build.py (ADR-0002).
sys.path.insert(0, str(ROOT))
from build import SITE_HOST  # noqa: E402

# A project's italic line in the master ends in its links:
# "([GitHub](url))", or since 2026-10-10 "([Case study](url) | [Live app](url))".
LINK_GROUP_RE = re.compile(r"\s*\(((?:\[[^\]]+\]\([^)]+\)\s*(?:\|\s*)?)+)\)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

LONG_MONTHS = {"january": "jan", "february": "feb", "march": "mar", "april": "apr",
               "june": "jun", "july": "jul", "august": "aug", "september": "sep",
               "october": "oct", "november": "nov", "december": "dec"}
MONTHS = set(LONG_MONTHS.values()) | {"may"}
WORD_RE = re.compile(r"\d+(?:[.,]\d+)*%?|[^\W\d_]+")
NUMBER_RE = re.compile(r"^\d")

# Interface text: what the page says about itself rather than about the
# operator. Removed from a block only when the block fails as it stands.
INTERFACE = sorted([
    "Skip to main content", "Sections menu", "Sections", "Dark theme", "Dark",
    "Intro", "Projects", "Timeline", "Work", "Education", "Certifications", "Skills",
    "Contact", "Results", "Stack", "Close in depth", "In depth", "Close",
    "Case study", "Live app", "GitHub", "LinkedIn", "View credential", "Credential",
    "Go to full entry", "Show or hide lanes", "Builds", "Degree", "Open source",
    "Months to scale", "No lanes selected", "Email me", "Let's connect", "See the code",
    "Work history, education and certifications", "Public repositories and project code",
    "Back to top", "Pause the moving strip", "Pause", "Play", "Download CV (PDF)",
], key=len, reverse=True)
# Zero-padded section and item numbers, decoration beside the real name.
ORDINAL_RE = re.compile(r"\b0[1-9]\b")
YEAR_RE = re.compile(r"^20\d\d$")

BLOCK_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "div", "section", "article",
              "header", "footer", "nav", "main", "ul", "ol", "summary", "details", "button",
              "title", "body", "html", "head", "dl", "dt", "dd", "figure", "figcaption"}
TEXT_ATTRIBUTES = ("alt", "aria-label", "title")


def words(text: str) -> list[str]:
    return [LONG_MONTHS.get(w, w) for w in WORD_RE.findall(html.unescape(text).lower())]


def sentences(text: str) -> list[list[str]]:
    """The words of each sentence or clause, split at a full stop, colon or
    semicolon followed by a space."""
    return [words(part) for part in re.split(r"(?<=[.:;])\s+", html.unescape(text))]


def is_subsequence(part: list[str], source: list[str]) -> bool:
    remaining = iter(source)
    return all(word in remaining for word in part)


def numbers_hold(text: str, source: list[str]) -> bool:
    """Every number in the text that has a next word in its own sentence
    keeps that next word, as in the source."""
    pairs = set(zip(source, source[1:]))
    return all((a, b) in pairs for part in sentences(text)
               for a, b in zip(part, part[1:]) if NUMBER_RE.match(a))


# The master.

def plain(line: str) -> str:
    """A master line as text: emphasis dropped, a link kept as its text."""
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", line)
    return text.replace("**", "").replace("*", "").lstrip("- ").strip()


def read_master(path: Path) -> tuple[list[list[str]], list[dict]]:
    """Paragraphs, as word lists, and entries: a heading with the lines
    under it. Markdown emphasis is dropped; a link keeps its text."""
    paragraphs, entries, entry = [], [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        text = plain(line)
        heading = re.fullmatch(r"\*\*[^*].*\*\*", line) is not None
        if heading:
            entry = {"heading": text, "lines": [], "raw": [line]}
            entries.append(entry)
        elif entry is not None:
            entry["lines"].append(text)
            entry["raw"].append(line)
        paragraphs.append(words(text))
    return paragraphs, entries


# The page.

class Blocks(HTMLParser):
    """Blocks of text, each with the pieces its inline markup splits it into."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, list[str]]] = []
        self.hrefs: list[str] = []
        self._pieces: list[str] = [""]
        self._skip = 0

    def _flush(self) -> None:
        text = re.sub(r"\s+", " ", "".join(self._pieces)).strip()
        if text:
            self.blocks.append((text, [p.strip() for p in self._pieces if p.strip()]))
        self._pieces = [""]

    def _attribute(self, text: str) -> None:
        if text.strip():
            self.blocks.append((text.strip(), [text.strip()]))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self._skip += 1
        if tag in BLOCK_TAGS:
            self._flush()
        elif tag == "br":
            self._pieces.append(" ")
        else:
            self._pieces.append("")
        for name in TEXT_ATTRIBUTES:
            self._attribute(attrs.get(name) or "")
        if tag == "meta" and attrs.get("name") == "description":
            self._attribute(attrs.get("content") or "")
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1
        if tag in BLOCK_TAGS:
            self._flush()
        else:
            self._pieces.append("")

    def handle_data(self, data):
        if not self._skip:
            self._pieces[-1] += data


def strip_interface(text: str) -> str:
    for phrase in INTERFACE:
        text = re.sub(r"(?<![\w'])" + re.escape(phrase) + r"(?![\w'])", " ", text, flags=re.I)
    return ORDINAL_RE.sub(" ", text)


def is_cut(text: str, paragraphs: list[list[str]]) -> bool:
    block = words(text)
    return bool(block) and any(is_subsequence(block, p) and numbers_hold(text, p) for p in paragraphs)


def interface_only(text: str) -> bool:
    remainder = words(strip_interface(text))
    return not remainder or all(w in MONTHS or YEAR_RE.match(w) for w in remainder)


def joined(pieces: list[str], entries: list[list[list[str]]]) -> bool:
    """Every piece the markup splits a block into is interface text or a cut
    of a paragraph, all from one master entry. The split points are the
    page's, never chosen here, so words cannot be gathered from anywhere."""
    for entry in entries:
        if all(interface_only(piece) or is_cut(piece, entry)
               or is_cut(strip_interface(piece), entry) for piece in pieces):
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Trace the built page to the master CV.")
    parser.add_argument("--master", required=True, type=Path, help="path to the master CV")
    parser.add_argument("--page", type=Path, default=PAGE, help="the built page; default index.html")
    args = parser.parse_args(argv)
    if not args.master.is_file():
        print(f"no master CV at the path given", file=sys.stderr)
        return 2

    paragraphs, entries = read_master(args.master)
    entry_paragraphs = [[words(e["heading"])] + [words(l) for l in e["lines"]] for e in entries]
    master_words = [w for p in paragraphs for w in p]
    site = json.loads(SITE.read_text(encoding="utf-8"))
    approved = site.get("approved") or {}
    approved_words = words(approved.get("text", ""))

    page = Blocks()
    page.feed(args.page.read_text(encoding="utf-8"))
    page.close()

    failures, counts, approved_hits = [], {"cut": 0, "joined": 0, "interface": 0, "approved": 0}, 0
    for text, pieces in page.blocks:
        block = words(text)
        if not block:
            continue
        stripped = strip_interface(text)
        remainder = words(stripped)
        if is_cut(text, paragraphs):
            how = "cut"
        elif interface_only(text):
            how = "interface"
        elif is_cut(stripped, paragraphs):
            how = "cut"
        elif joined(pieces, entry_paragraphs):
            how = "joined"
        elif (approved_words and is_subsequence(remainder, approved_words)
              and all(w in master_words for w in remainder if NUMBER_RE.match(w))
              and numbers_hold(stripped, master_words)):
            how = "approved"
            approved_hits += 1
        else:
            how = None
        if how is None:
            failures.append(text)
        else:
            counts[how] += 1

    print(f"Trace: {sum(counts.values())} blocks traced, {len(failures)} not traced.")
    print(f"  cut of one master paragraph:  {counts['cut']}")
    print(f"  pieces cut from one entry:    {counts['joined']}")
    print(f"  interface text only:          {counts['interface']}")
    print(f"  operator-approved, not in the master: {counts['approved']}")
    if approved_hits:
        print(f"    approved by {approved.get('approved_by')}:")
        print(f"    \"{approved.get('text')}\"")
    for text in failures:
        print(f"  NOT TRACED: {text[:160]}")

    # Coverage.
    page_words = words(" ".join(text for text, _ in page.blocks))
    page_text = " " + " ".join(page_words) + " "

    def present(text: str) -> bool:
        w = words(text)
        return bool(w) and (" " + " ".join(w) + " ") in page_text

    groups: dict[str, list[tuple[str, bool]]] = {}

    def add(group: str, text: str, ok: bool | None = None) -> None:
        groups.setdefault(group, []).append((text, present(text) if ok is None else ok))

    for e in entries:
        raw_lines = e["raw"][1:]
        if e["heading"] == "PROFESSIONAL SUMMARY":
            add("summary", e["lines"][0])
        elif e["heading"] == "TECHNICAL SKILLS":
            for line in e["lines"]:
                add("skills lines", line)
        elif e["heading"] == "CERTIFICATIONS":
            for raw in raw_lines:
                for title, url, dates in re.findall(r"\[(.+?)\]\((.+?)\) \((.+?)\)", raw):
                    url = url.split("?utm_", 1)[0]
                    ok = present(title) and present(dates) and url in page.hrefs
                    add("certificates", f"{title} ({dates})", ok)
        elif "|" in e["heading"]:
            title, dates = (part.strip() for part in e["heading"].split("|", 1))
            add("headings", title.split(", ")[0] if e["heading"].startswith("BE ") else title.split(": ")[0])
            add("heading dates", dates)
            for raw, line in zip(raw_lines, e["lines"]):
                if raw.startswith("-   "):
                    add("bullets", line)
                elif raw.startswith("*") and not raw.startswith("**"):
                    # The links ending the line are checked as links: the
                    # label on the page, and the address among the page's
                    # links, this site's own in the root-relative form the
                    # site uses (ADR-0002). The words before them are the
                    # italic line.
                    italic = line
                    tail = LINK_GROUP_RE.search(raw)
                    if tail:
                        for label, url in LINK_RE.findall(tail.group(1)):
                            parts = urlsplit(url)
                            href = (parts.path or "/") if parts.hostname == SITE_HOST else url
                            add("project links", f"{label} ({url})", present(label) and href in page.hrefs)
                        italic = plain(raw[:tail.start()])
                    for sentence in re.split(r"(?<=\.) ", italic):
                        add("italic-line sentences", sentence)
                elif raw.startswith("**Relevant Coursework"):
                    for course in line.split(":", 1)[1].split(","):
                        add("courses", course)
                else:
                    add("other lines", line)
    missing = 0
    print("\nCoverage: master text found whole on the page, in the master's word order.")
    for group, results in groups.items():
        found = sum(ok for _, ok in results)
        missing += len(results) - found
        print(f"  {group}: {found} of {len(results)}")
        for text, ok in results:
            if not ok:
                print(f"    MISSING: {text[:160]}")

    passed = not failures and not missing
    print("\nPASS" if passed else "\nFAIL")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
