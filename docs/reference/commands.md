---
type: reference
description: Every command that exists in this repository, each with what it exits and why. The environment, the gates, the architecture chat's commits, the build, the monthly refresh, the map, the one-dependency check and the content trace. Read before running anything.
status: current
---

# Commands

Moved word for word from `CLAUDE.md`'s Commands section on 2026-10-11
(UTC), which the operator approved on 2026-10-10 (UTC). `CLAUDE.md` points
here. Do not infer a command that is not here, and do not treat its
absence as permission.

Recorded by Brief 1 and Brief 2, 2026-09-26 (UTC), and by Brief 3,
2026-10-05 (UTC). Every command runs from the repository root. Each was run
in the session that recorded it and exited as described.

**Environment.** The build runs only inside the project venv at `.venv/`,
with the versions pinned in `requirements.txt`: Jinja2, and MarkupSafe,
which is Jinja2's own requirement. `build.py` reads those pins from
`requirements.txt` and refuses to run outside a virtual environment or
against any other installed version, because a different version can
produce different output with no visible cause. Create or recreate the venv:

```
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

Activate it before building:

```
.venv\Scripts\Activate.ps1          PowerShell
source .venv/Scripts/activate       Git Bash
```

**Gates.** Activate the hooks once per clone:

```
git config core.hooksPath .githooks
```

**A fresh clone has no gates until this is run, and nothing catches the
omission.** ADR-0007 accepts that weakness. `--no-verify` bypasses every
gate and is never used.

**Commits carried for the architecture chat.** Added by the chat on
2026-09-26 (UTC) at the operator's instruction; revised 2026-10-02. The
chat edits files but does not commit or push. When it leaves changes
uncommitted, it writes one message file per commit in `.commitmsg/` at the
repository root, gitignored, numbered in the order they are to be made
(`1-...txt`, `2-...txt`). Each subject starts with `[chat]` and each body
lists that commit's files under `Files:`. **The operator runs these
commits himself**, from commands the chat gives him; the implementing seat
does so only when he hands them over. For each file, in number order:

```
git status --short --untracked-files=all
git add <each file listed in the message>
git commit -F .commitmsg/<n>-<name>.txt
```

The commit runs the gates like any other. When all are made, push, then
delete the message files and the folder. A chat commit stays separate:
never amended, squashed or combined with other changes, and its message is
not edited. If the tree differs from the lists, or a gate refuses, stop and
report; nobody fixes the chat's files in passing. Only chat commits start
with `[chat]`.

**Build.** Writes `index.html` and `static/` at the root. Exit 0 on
success. On any content failure it exits 1, names every failing item, and
writes nothing.

```
python build.py                    as of the current UTC month
python build.py --as-of YYYY-MM    as of the given month
```

The as-of month is what `present` resolves to, and the output records it
as `<meta name="as-of">`. The rebuild gate reads that month back and
rebuilds with it, never with the clock.

**Monthly refresh.** While an item ends `present`, the page stays as of the
month it was built. To move it on, run `python build.py` in the new month
and commit `index.html` and `static/`. The gate reads the new month from the
output like any other build.

**Map.** `MAP.md` is generated from every tracked Markdown file's
frontmatter. Stage the files first, then regenerate and stage `MAP.md`.

```
python tools/generate_map.py            write MAP.md
python tools/generate_map.py --check    compare the staged MAP.md with the staged files
```

Exit 0 means current, 1 means a file needs fixing (no frontmatter or no
description), 2 means stale.

**One-dependency check** (ADR-0006). Expected: `Jinja2` and `pip`, nothing
else. MarkupSafe is Jinja2's own requirement and so is not listed.

```
python -m pip list --not-required
```

**Content trace.** Added by Brief 3. Reads the built `index.html` and traces
every block of text on it, the title, description, alt text and labels
included, to the master CV, or to the interface text the tool names;
then checks that every master bullet, the summary, the Portfolio Intro,
each sentence of each italic line, each skills line, course and
certificate appears on the page whole, in the master's word order. The master is given by its path each time and never stored, because
this repository is public. Run it after any content change, before
committing it.

```
python tools/check_content.py --master <path to the master CV>
```

Exit 0 means every block traces and nothing is missing; 1 means a block
does not trace or master text is missing, each printed; 2 means no file at
the path given.
