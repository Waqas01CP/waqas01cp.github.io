"""The repository gates (ADR-0007). Called by the thin hooks in .githooks/.

  python tools/gates.py pre-commit    gates A, B and C, with D throughout
  python tools/gates.py pre-push      gate E, reading git's pre-push input

Each gate, what it blocks, and the case built to defeat it:

  A  Never-commit paths, pre-commit. Refuses CHAT_STATE.md at any path,
     anything under briefs/ except briefs/README.md, and any staged text
     file whose content holds a filesystem path into the operator's
     private material. Prints the file, line and matched text, so a false
     positive can be seen for what it is. Defeated by staging CHAT_STATE.md
     with -f, and by a planted template path. Control: a sentence naming
     the Working Method in prose passes.
  B  Rebuild, pre-commit. Reads the as-of month from the staged index.html,
     rebuilds the staged tree in a temporary directory with that month,
     and refuses unless every generated file matches what is staged, byte
     for byte. Defeated by a one-character hand edit to index.html, and by
     changing items.json without rebuilding.
  C  Map, pre-commit. Runs tools/generate_map.py --check against the staged
     files. Defeated by adding a Markdown file without regenerating MAP.md.
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

Standard library only; scope floor line 14 applies to tooling too.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
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

# Gate E. This scope is Brief 2's, not a record's.
IMPLEMENTATION_FILES = {"build.py", "requirements.txt", "index.html"}
IMPLEMENTATION_DIRS = ("src/", "static/", "tools/", ".githooks/")


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
    if lowered.startswith("briefs/") and lowered != "briefs/readme.md":
        return "briefs are working space and are never committed (briefs/README.md)"
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

def gate_b() -> list[str]:
    if "index.html" not in staged_paths("index.html"):
        return ["B  index.html is not staged, so there is no as-of month to rebuild with"]
    recorded = AS_OF_RE.search(staged_blob("index.html"))
    if not recorded:
        return ['B  the staged index.html records no as-of month (<meta name="as-of">). '
                "Rebuild with the current build.py and stage the output"]
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
            return [f"B  the staged source does not build as of {as_of}:\n      {output}"]
        fresh = {"index.html"} | {p.relative_to(tree).as_posix()
                                  for p in (tree / "static").rglob("*") if p.is_file()}
        staged = {"index.html"} | set(staged_paths("static/"))
        differ = []
        for path in sorted(fresh | staged):
            built = (tree / path).read_bytes() if path in fresh else None
            committed = staged_blob(path) if path in staged else None
            if built != committed:
                differ.append(path)
    if differ:
        return [f"B  staged output differs from a fresh build of the staged source as of "
                f"{as_of}: {', '.join(differ)}. Run python build.py --as-of {as_of}, or plain "
                f"python build.py for a monthly refresh, then stage index.html and static/"]
    return []


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
        refusals += gate_b()
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
    print("gates A, B, C passed", file=sys.stderr)
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
