"""The repository gates (ADR-0007). Called by the thin hooks in .githooks/.

  python tools/gates.py pre-commit    gates A, B, C, F and G, with D throughout
  python tools/gates.py pre-push      gate E, reading git's pre-push input

Each gate, what it blocks, and the case built to defeat it:

  A  Never-commit paths, pre-commit. Refuses CHAT_STATE.md at any path,
     anything under briefs/, its README included since 2026-10-21, and
     any staged text file whose content holds a filesystem path into
     Waqas Sharif's private material. Prints the file, line and matched
     text, so a false positive can be seen for what it is. Defeated by
     staging CHAT_STATE.md or briefs/README.md with -f, and by a planted
     template path. Control: a sentence naming the Working Method in
     prose passes.
  B  Rebuild, pre-commit. Reads the as-of month from the staged index.html,
     rebuilds the staged tree in a temporary directory with that month,
     and refuses unless every generated file matches what is staged, byte
     for byte. Defeated by a one-character hand edit to index.html, and by
     changing items.json without rebuilding.
  C  Map, pre-commit. Runs tools/generate_map.py --check against the staged
     files. Refuses a stale map, and since 2026-10-12 a staged Markdown
     header GitHub would refuse to read (the generator's docstring lists
     the patterns; ADR-0007 Changes). Defeated by adding a Markdown file
     without regenerating MAP.md, and by a description holding an
     unquoted ": ".
  D  Missing tool, every gate. A missing git, build.py or map generator is
     a refusal naming what is missing, never a skip. The hooks apply the
     same rule to the venv interpreter and to this file. Defeated by
     renaming the map generator, and by moving the venv.
  E  STATE.md moved, pre-push. Across every commit being pushed, if any
     touches an implementation path and none touches STATE.md, refuses.
     Pre-push, not pre-commit, so a series of commits by concern with the
     bookkeeping last passes (ADR-0007). Defeated by pushing a src/ change
     with no STATE.md change. Control: several commits where only the last
     touches STATE.md pass.
  F  Every claim readable, pre-commit: scope floor line 7 (ADR-0007
     Changes, 2026-10-23). On gate B's fresh build, every string in the
     content files, markup stripped, appears in index.html's readable
     text, so no claim exists only for a script to insert. Defeated by a
     template that renders a field only into a data attribute. Control:
     the same field in a data attribute and in the text passes.
  G  No third-party source, no cookie or tracking, pre-commit: scope floor
     lines 9 and 10, the same row. Reads the staged index.html and
     static/'s scripts and stylesheets. Defeated by a planted Google Tag
     Manager script, and by document.cookie in site.js. Control: an
     external plain link passes.

Standard library only; scope floor line 14 applies to tooling too.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Gate A. Every pattern is written so this file's own source cannot match
# it, which is how the gate avoids matching itself: by construction, not by
# exempting this file. A folder name is always followed by a character
# class, never by a literal separator, and a climb is written with escaped
# dots. Patterns match path forms only, so prose that names the Working
# Method in a sentence passes.
POINTER_PATTERNS = (
    ("a drive-letter absolute path", re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]")),
    ("a path segment naming the Working Method", re.compile(r"Working Method[\\/]", re.I)),
    ("a path segment naming the Operating Plan", re.compile(r"Operating Plan[\\/]", re.I)),
    ("the master CV's file name", re.compile(r"Waqas_Sharif_Maste[r]", re.I)),
)
CLIMB = re.compile(r"(?:\.\.[\\/]){2,}")

# The vault's root folder name has never been committed. Written here as
# text it would be published for the first time, so it is held only as the
# SHA-256 of its lower-cased form and matched by hashing every window of its
# length. The other names above have been public since the first commit.
VAULT_ROOT_SHA256 = "aa0a76ea62d79adc150ad95e5a2239acc44ad5e15e692c93d00f1c096a5faaf8"
VAULT_ROOT_LENGTH = 17

# Gate B.
AS_OF_RE = re.compile(rb'<meta name="as-of" content="(\d{4}-(?:0[1-9]|1[0-2]))">')

# Gate E. Its scope is recorded in ADR-0007 Changes, 2026-09-26.
IMPLEMENTATION_FILES = {"build.py", "requirements.txt", "index.html"}
IMPLEMENTATION_DIRS = ("src/", "static/", "tools/", ".githooks/")

# Gate F. Every string in the content files is a claim the page must print,
# unless its key is one of these, which are never printed as written. A key
# not named here is checked, so a new field counts as a claim until it is
# named here with its reason.
CONTENT_FILES = ("src/content/site.json", "src/content/items.json")
UNPRINTED_KEYS = {
    "id", "lane", "route", "date_style",   # choose markup: anchors, sections, the contact route, a date's form
    "start", "end",                        # months, printed as the date phrases build.py derives
    "source", "from", "item", "no_proof",  # provenance: the master's section, a bullet, a record
    "url",                                 # addresses, printed as a link's href beside its checked text
}
# Text no visitor reads with scripts off: script and style bodies, a template,
# and anything inside an element marked hidden, which only a script reveals.
UNREAD_TAGS = {"script", "style", "template"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "source", "track", "wbr"}

# Gate G. An absolute address, a scheme-relative one included, is one the
# browser fetches from another host. Only a plain link may carry one. The
# allowlist is empty: a third-party source takes a floor line 9 record
# first. XML namespace names look like addresses and are never fetched.
ABSOLUTE_RE = re.compile(r"(?i)(?:https?:)?//[\w-]+(?:\.[\w-]+)+")
ALLOWED_HOSTS: tuple[str, ...] = ()
NAMESPACES = ("http://www.w3.org/2000/svg", "http://www.w3.org/1999/xlink",
              "http://www.w3.org/1999/xhtml")
QUOTED_ABSOLUTE_RE = re.compile(r"""['"`]\s*((?:https?:)?//[\w-]+(?:\.[\w-]+)+)""", re.I)
CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
# Floor line 10 in script code: the cookie, storage and network interfaces.
# Matched in code only, never in the page's prose, which says "a fetch skill".
TRACKING_API_RE = re.compile(r"\b(?:document\s*\.\s*cookie|cookieStore|localStorage|sessionStorage|"
                             r"indexedDB|sendBeacon|fetch|XMLHttpRequest|WebSocket)\b")
# Analytics and tracking hosts, refused anywhere in the built files: the
# known ones, not every one.
ANALYTICS_HOSTS = (
    "googletagmanager.com", "google-analytics.com", "analytics.google.com", "doubleclick.net",
    "googlesyndication.com", "plausible.io", "usefathom.com", "simpleanalyticscdn.com",
    "cloudflareinsights.com", "hotjar.com", "clarity.ms", "segment.com", "segment.io",
    "mixpanel.com", "amplitude.com", "heapanalytics.com", "posthog.com", "matomo.cloud",
    "gc.zgo.at", "statcounter.com", "quantserve.com", "scorecardresearch.com",
    "connect.facebook.net", "snap.licdn.com", "ads-twitter.com", "analytics.tiktok.com",
    "mc.yandex.ru", "umami.is", "nr-data.net", "fullstory.com", "mouseflow.com",
    "hs-analytics.net", "stats.wp.com",
)


class MissingTool(Exception):
    """Gate D: a tool a gate needs is absent. Always a refusal."""


def git(*args: str) -> bytes:
    try:
        result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    except FileNotFoundError:
        raise MissingTool("git is not on the PATH") from None
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: "
                           f"{result.stderr.decode('utf-8', 'replace').strip()}")
    return result.stdout


def zsplit(output: bytes) -> list[str]:
    return [p for p in output.decode("utf-8").split("\0") if p]


def staged_paths(*pathspec: str) -> list[str]:
    return zsplit(git("ls-files", "-z", "--cached", "--", *pathspec))


def staged_blob(path: str) -> bytes:
    return git("cat-file", "blob", f":{path}")


# Gate A: never-commit paths.

def never_commit_reason(path: str) -> str | None:
    lowered = path.lower()
    if lowered.rsplit("/", 1)[-1] == "chat_state.md":
        return "CHAT_STATE.md is the architecture chat's ledger and is never committed (ADR-0002)"
    if lowered.startswith("briefs/"):
        return "briefs are working space and are never committed (CLAUDE.md, Briefs)"
    return None


def pointers_in(path: str, text: str) -> list[str]:
    """Every filesystem path into private material in one file's text."""
    depth = path.count("/")
    found = []
    for number, line in enumerate(text.splitlines(), start=1):
        hits = [(label, m.group(0)) for label, pattern in POINTER_PATTERNS
                for m in pattern.finditer(line)]
        # A climb of two or more levels is a path out of the repository only
        # if it rises above the root from this file's folder. A link two
        # levels up from docs/decisions/ to the root README stays inside and
        # passes.
        hits += [("a climb out of the repository", m.group(0)) for m in CLIMB.finditer(line)
                 if m.group(0).count("..") > depth]
        lowered = line.lower()
        for i in range(len(lowered) - VAULT_ROOT_LENGTH + 1):
            window = lowered[i:i + VAULT_ROOT_LENGTH]
            if hashlib.sha256(window.encode("utf-8")).hexdigest() == VAULT_ROOT_SHA256:
                hits.append(("the vault's root folder name", line[i:i + VAULT_ROOT_LENGTH]))
        for label, matched in hits:
            shown = line.strip()
            shown = shown if len(shown) <= 120 else shown[:117] + "..."
            found.append(f"{path}, line {number}: {label}: {matched!r}\n      in: {shown}")
    return found


def gate_a(staged: list[str]) -> list[str]:
    refusals = []
    for path in staged:
        reason = never_commit_reason(path)
        if reason:
            refusals.append(f"A  {path}: {reason}")
            continue
        data = staged_blob(path)
        if b"\0" in data[:8000]:
            continue  # binary: no text path can be read from it
        refusals += [f"A  {hit}" for hit in pointers_in(path, data.decode("utf-8", "replace"))]
    return refusals


# Gate B: the staged output is what a fresh build of the staged source makes.
# Returns its refusals and the freshly built page, which gate F reads; no
# page when the staged tree could not be built, which B has already refused.

def gate_b() -> tuple[list[str], bytes | None]:
    if "index.html" not in staged_paths("index.html"):
        return ["B  index.html is not staged, so there is no as-of month to rebuild with"], None
    recorded = AS_OF_RE.search(staged_blob("index.html"))
    if not recorded:
        return ['B  the staged index.html records no as-of month (<meta name="as-of">). '
                "Rebuild with the current build.py and stage the output"], None
    as_of = recorded.group(1).decode()
    with tempfile.TemporaryDirectory(prefix="gate-b-") as tmp:
        tree = Path(tmp)
        git("checkout-index", "--all", "--force", f"--prefix={tree.as_posix()}/")
        if not (tree / "build.py").is_file():
            raise MissingTool("build.py is not in the staged tree")
        result = subprocess.run([sys.executable, "build.py", "--as-of", as_of],
                                cwd=tree, capture_output=True, text=True)
        if result.returncode != 0:
            output = (result.stdout + result.stderr).strip()
            return [f"B  the staged source does not build as of {as_of}:\n      {output}"], None
        fresh = {"index.html"} | {p.relative_to(tree).as_posix()
                                  for p in (tree / "static").rglob("*") if p.is_file()}
        staged = {"index.html"} | set(staged_paths("static/"))
        differ = []
        for path in sorted(fresh | staged):
            built = (tree / path).read_bytes() if path in fresh else None
            committed = staged_blob(path) if path in staged else None
            if built != committed:
                differ.append(path)
        page = (tree / "index.html").read_bytes()
    if differ:
        return [f"B  staged output differs from a fresh build of the staged source as of "
                f"{as_of}: {', '.join(differ)}. Run python build.py --as-of {as_of}, or plain "
                f"python build.py for a monthly refresh, then stage index.html and static/"], page
    return [], page


# Gate F: floor line 7, every claim in the page's readable text.

class ReadableText(HTMLParser):
    """The page's text as a visitor reads it with scripts off."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.inside: list[str] = []  # an unread element's tag, once more for each nested repeat
        self.chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in VOID_TAGS:
            return
        if self.inside:
            if tag == self.inside[0]:
                self.inside.append(tag)
        elif tag in UNREAD_TAGS or any(name == "hidden" for name, _ in attrs):
            self.inside.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if self.inside and tag == self.inside[0]:
            self.inside.pop()

    def handle_data(self, data: str) -> None:
        if not self.inside:
            self.chunks.append(data)


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", text))).strip()


def claims(node, where: str):
    """Every printed string under a content node, with where it sits."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in UNPRINTED_KEYS:
                continue
            if key == "title" and isinstance(value, str):
                # build.py prints a title as its name and its subtitle, split
                # at the first ": ", in two elements.
                yield from ((f"{where}.title", part) for part in value.partition(": ")[::2] if part)
            else:
                yield from claims(value, f"{where}.{key}")
    elif isinstance(node, list):
        for i, value in enumerate(node):
            label = value.get("id") if isinstance(value, dict) else None
            yield from claims(value, f"{where}[{label or i}]")
    elif isinstance(node, str):
        yield where, node


def gate_f(page: bytes | None) -> list[str]:
    if page is None:
        return []
    reader = ReadableText()
    reader.feed(page.decode("utf-8"))
    text = re.sub(r"\s+", " ", "".join(reader.chunks))
    refusals = []
    for path in CONTENT_FILES:
        for where, value in claims(json.loads(staged_blob(path)), path.rsplit("/", 1)[-1]):
            shown = plain(value)
            if shown and shown not in text:
                shown = shown if len(shown) <= 80 else shown[:77] + "..."
                refusals.append(f"F  {where} is not in index.html's readable text (scripts off, "
                                f"hidden elements left out), so only a script could show it "
                                f"(floor line 7): {shown!r}")
    return refusals


# Gate G: floor lines 9 and 10 in the staged built files.

class BuiltPage(HTMLParser):
    """Every attribute of index.html with its line, and each script and style body."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.attributes: list[tuple[int, str, str, str]] = []
        self.code: list[tuple[int, str, str]] = []
        self.open: tuple[int, str] | None = None

    def handle_starttag(self, tag: str, attrs: list) -> None:
        line = self.getpos()[0]
        self.attributes += [(line, tag, name, value or "") for name, value in attrs]
        if tag in ("script", "style"):
            self.open = (line, tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style"):
            self.open = None

    def handle_data(self, data: str) -> None:
        if self.open:
            self.code.append((*self.open, data))


def addresses(pattern: re.Pattern, text: str) -> list[str]:
    """The absolute addresses the pattern finds, namespace names and allowed hosts aside."""
    for name in NAMESPACES:
        text = text.replace(name, "")
    found = [(m, m.split("//", 1)[1].lower()) for m in pattern.findall(text)]
    return [m for m, host in found
            if not any(host == h or host.endswith("." + h) for h in ALLOWED_HOSTS)]


def in_code(path: str, first_line: int, kind: str, code: str) -> list[str]:
    """Gate G's refusals for a stylesheet ("css") or a script ("js")."""
    if kind == "css":
        # Comments go, their line breaks kept, so a line number still points true.
        code = CSS_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), code)
    hits = []
    for number, line in enumerate(code.split("\n"), start=first_line):
        if kind == "css":
            hits += [(number, "an absolute address in a stylesheet (floor line 9)", m)
                     for m in addresses(ABSOLUTE_RE, line)]
        else:
            hits += [(number, "an absolute address in a script's string (floor line 9)", m)
                     for m in addresses(QUOTED_ABSOLUTE_RE, line)]
            hits += [(number, "a cookie, storage or network interface (floor line 10)", m.group(0))
                     for m in TRACKING_API_RE.finditer(line)]
    return [f"G  {path}, line {n}: {label}: {m!r}" for n, label, m in hits]


def gate_g() -> list[str]:
    files = {p: staged_blob(p).decode("utf-8") for p in staged_paths("index.html", "static/")
             if p == "index.html" or p.endswith((".js", ".css"))}
    refusals = []
    built = BuiltPage()
    built.feed(files.get("index.html", ""))
    for line, tag, name, value in built.attributes:
        if not (tag == "a" and name == "href"):
            refusals += [f"G  index.html, line {line}: an absolute address on <{tag} {name}>, "
                         f"which only a plain link may carry (floor line 9): {m!r}"
                         for m in addresses(ABSOLUTE_RE, value)]
        if name.startswith("on") or value.lower().lstrip().startswith("javascript:"):
            refusals += in_code("index.html", line, "js", value)
    for line, tag, body in built.code:
        refusals += in_code("index.html", line, "css" if tag == "style" else "js", body)
    for path, text in files.items():
        if path != "index.html":
            refusals += in_code(path, 1, path.rsplit(".", 1)[1], text)
        lowered = text.lower()
        for host in ANALYTICS_HOSTS:
            at = lowered.find(host)
            if at >= 0:
                refusals.append(f"G  {path}, line {lowered.count(chr(10), 0, at) + 1}: "
                                f"a known analytics host (floor line 10): {host!r}")
    return refusals


# Gate C: the map is current against the staged files.

def gate_c() -> list[str]:
    generator = ROOT / "tools" / "generate_map.py"
    if not generator.is_file():
        raise MissingTool("tools/generate_map.py")
    result = subprocess.run([sys.executable, str(generator), "--check"],
                            cwd=ROOT, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    if result.returncode == 0:
        return []
    if result.returncode == 2:
        return [f"C  {output}"]
    return [f"C  the map check failed (exit {result.returncode}), which is not a "
            f"staleness report. Fix the cause:\n      {output}"]


def pre_commit() -> int:
    refusals = []
    try:
        staged = zsplit(git("diff", "--cached", "--name-only", "-z", "--diff-filter=ACMRT"))
        refusals += gate_a(staged)
        b_refusals, page = gate_b()
        refusals += b_refusals
        refusals += gate_f(page)
        refusals += gate_g()
        refusals += gate_c()
    except MissingTool as error:
        refusals.append(f"D  missing tool: {error}")
    except RuntimeError as error:
        refusals.append(f"   {error}")
    if refusals:
        print("COMMIT REFUSED by the repository gates (ADR-0007):", file=sys.stderr)
        for refusal in refusals:
            print(f"  {refusal}", file=sys.stderr)
        return 1
    print("gates A, B, C, F, G passed", file=sys.stderr)
    return 0


# Gate E: STATE.md moved, across the whole range being pushed.

def touched(commit: str) -> list[str]:
    parents = git("rev-list", "--parents", "-n", "1", commit).decode().split()[1:]
    if parents:
        return zsplit(git("diff", "--name-only", "-z", parents[0], commit))
    return zsplit(git("diff-tree", "--root", "--no-commit-id", "--name-only", "-r", "-z", commit))


def is_implementation(path: str) -> bool:
    return path in IMPLEMENTATION_FILES or path.startswith(IMPLEMENTATION_DIRS)


def pre_push(stdin: str) -> int:
    refusals = []
    try:
        for line in stdin.splitlines():
            local_ref, local_sha, remote_ref, remote_sha = line.split()
            if set(local_sha) == {"0"}:
                continue  # deleting a remote ref sends no commits
            if set(remote_sha) == {"0"}:
                # A new branch: the range is every commit on no remote at all.
                range_args = [local_sha, "--not", "--remotes"]
            else:
                if subprocess.run(["git", "cat-file", "-e", f"{remote_sha}^{{commit}}"],
                                  cwd=ROOT, capture_output=True).returncode != 0:
                    refusals.append(f"E  {remote_ref}: the remote is at {remote_sha[:7]}, which this "
                                    f"clone does not have, so the range cannot be computed. Fetch first")
                    continue
                range_args = [f"{remote_sha}..{local_sha}"]
            commits = git("rev-list", *range_args).decode().split()
            by_commit = {c: touched(c) for c in commits}
            if any("STATE.md" in paths for paths in by_commit.values()):
                continue
            work = []
            for commit, paths in by_commit.items():
                hits = [p for p in paths if is_implementation(p)]
                if hits:
                    subject = git("log", "-1", "--format=%s", commit).decode().strip()
                    work.append(f"{commit[:7]} {subject}: {', '.join(hits)}")
            if work:
                refusals.append(
                    f"E  {remote_ref}: implementation work is being pushed and no commit in the "
                    f"range touches STATE.md. Update it in a commit on this branch (the last of "
                    f"the series is fine) and push again. The work:\n      " + "\n      ".join(work))
    except MissingTool as error:
        refusals.append(f"D  missing tool: {error}")
    except RuntimeError as error:
        refusals.append(f"   {error}")
    if refusals:
        print("PUSH REFUSED by the repository gates (ADR-0007):", file=sys.stderr)
        for refusal in refusals:
            print(f"  {refusal}", file=sys.stderr)
        return 1
    print("gate E passed", file=sys.stderr)
    return 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["pre-commit"]:
        return pre_commit()
    if argv[:1] == ["pre-push"]:
        return pre_push(sys.stdin.read())
    print("usage: gates.py pre-commit | pre-push <remote> <url>", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
