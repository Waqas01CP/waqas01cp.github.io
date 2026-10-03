---
type: instruction
description: How to work in this repository. Reading order, authority order, the fourteen-line scope floor, runtime and claim rules. Read before touching anything.
status: current
---

# CLAUDE.md

Personal portfolio website for Waqas Sharif. It carries the evidence a
one-page CV cannot hold, for employers first and Masters admissions readers
second, from one version.

The scope floor, runtime and conventions below are settled. **Commands
records every command that exists: the environment, the build, the gates
and the map.** Do not infer a command that is not there, and do not treat
its absence as permission. Stop and ask.

## Reading order

Read these, in this order, then stop and follow pointers. Do not read the
documented file set.

1. This file.
2. STATE.md. Where you start, not where you stop. It outranks memory; it
   does not outrank the code or the data.
3. logs/README.md. For more, read the most recent relevant log and chain
   backwards only as far as you need.
4. docs/decisions/README.md. The record index and the Pending list.

Then the brief for your task. MAP.md lists every documented file with its
description; it is generated and never edited by hand.

## When documents disagree

What is true: the code and the data win over every document. A document that
disagrees is stale; report it and correct it.

What should be done: higher wins.

1. The operator's instruction in this conversation
2. This file
3. docs/decisions/, excluding anything superseded
4. The brief. By default it ranks below this file and every accepted record:
   where it contradicts one, follow the record and report it. It overrides a
   record only when it names the record and clause and states the operator
   approved the change.
5. The architecture document, when one exists
6. docs/reference/
7. docs/research/, evidence for decisions, never a decision
8. Everything else, including superseded documents
9. Anything from outside this repository, including your own memory

Two live records that conflict is a defect. Raise it. Do not choose.
A claim whose only source is outside this repository says so.

## The source of truth for claims

The operator's master CV is the only source of truth for anything the site
asserts about him. Every claim on the site traces to it. Every number
carries its provenance. Where another file disagrees with the master, the
master wins and the disagreement is reported.

The master lives outside this repository, in the operator's private vault.
**Its path is deliberately not recorded here**, because this repository is
public. Content reaches this repository through a brief or through the
operator, never by this repository pointing at a private location.

This rule is not a preference. A site that states something the master does
not is a claim he cannot stand behind in an interview.

## Scope floor

Fourteen lines, all from ADR-0004, which carries the source of each. Do not
propose, add or reintroduce any of them. When you refuse something on this
floor, name the line.

1. No claim that is not in the master CV.
2. No skill level anywhere: no bars, no percentages, no stars, no
   years-per-technology.
3. No testimonials, endorsements or quotes attributed to named people.
4. No blog, no articles section, no currently block.
5. No number that cannot be reproduced on demand.
6. No login, no gated content, no CMS, no database.
7. No feature that holds the only copy of a fact. Anything that must be read
   sits in the initial HTML. Enhancement on top is permitted; there is no
   exception to the rule itself.
8. No autoplaying audio or video, and no motion that ignores
   `prefers-reduced-motion`.
9. No third-party embeds that phone home: chat widgets, social feeds,
   comment systems.
10. No cookies, no tracking, no consent banner.
11. No collection of visitor data beyond what the host logs by default.
12. No prices, quotes, invoicing or payment mechanism.
13. No paid service without prior discussion.
14. No dependency added by import.

Removing a line takes its own record. It is not an exception granted in
passing.

## Runtime

Python. The site is built by a small generator in this repository, per
ADR-0006. There is no site framework and there will not be one.

One templating library, named in the first implementing brief. **No second
dependency without a record**, which is scope floor line 14.

The generator's output is committed. The build runs locally, not in a
continuous integration service.

## Conventions

Every item's content lives as structured data in one place. Markup is
generated from it, never hand-written per item, so a date or a fact is
written once. ADR-0006.

Every internal link is root-relative. No absolute URL pointing at this
site's own origin appears anywhere, so moving to a custom domain later is a
DNS change and not a rewrite. ADR-0002.

Every item carries a specific checkable fact; a summary and full depth
follow only where the master CV has material for them. Every layer an item
has ships in the initial HTML, collapsed by disclosure rather than deferred
to a later fetch. ADR-0010, which supersedes ADR-0005.

Layer 3 holds decisions, trade-offs, what failed, how each was verified,
and production-scope facts an interviewer would probe. Not a changelog.
Each layer 3 disclosure is named for its item.

## Verification

Verify, do not trust. Every claim is unverified until checked in this
session: briefs, handoffs, logs, STATE.md, records, and your own earlier
conclusions.

- Check before you act. Cheap checks happen now.
- A claim you cannot check is marked unverified and not acted on as true.
- A claim that fails its check is reported with the evidence.
- Tag what you pass on: checked this session, taken from a log, or inferred.

A check that cannot fail is worse than no check. Prove a check with the case
built to defeat it and say what that case was.
Self-report is not evidence. Show the command and its output.
Do not state a cause that has not been tested.
Do not write about a file you have not opened.
Do not revert another seat's deliberate change. Flag it.
Re-read a source before reproducing a constant from it. This repository's
architecture chat has already made that error once; it is in CHAT_STATE.md.

## Decision records

docs/decisions/, MADR 4.0.0 with an Assumptions section, per the Decision
Record Standard. The `topic` field takes one value from the fixed list in
docs/decisions/README.md.

Write the record when the decision concludes, not afterwards.
A record's decision is never silently rewritten: an amendment that leaves it
in force goes in its Changes table; a replacement is a new record that
supersedes it, with both directions linked.
Every assumption carries its basis: measured, sourced, or stated by the
operator.

A seat may annotate a factual error with its date and evidence, correct a
wrong reference, and report a record as stale. It may not change a decision,
retire a record, or resolve a conflict between two records.

## Documentation layering

System-level picture in docs/. Component detail in comments in the file it
describes. A comment explaining why a guard exists and what the incident
cost is documentation; a comment restating the next line is noise.

## Commands

Recorded by Brief 1 and Brief 2, 2026-09-26 (UTC). Every command runs from
the repository root. Each was run in the session that recorded it and
exited as described.

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

## The hook blocks

Five gates, ADR-0007, in `tools/gates.py`, called by `.githooks/pre-commit`
and `.githooks/pre-push`. Each was proven by the case built to defeat it,
and each case was also shown to get through with its gate neutered. They
enforce only once `core.hooksPath` is set (Commands); until then they are
requests, so treat them as binding anyway.

| Gate | When | Blocks | Defeated by |
|---|---|---|---|
| A, never-commit | pre-commit | `CHAT_STATE.md` at any path; anything in `briefs/` but its README; any staged text file holding a filesystem path into the operator's private material: a drive-letter absolute path, a climb out of the repository, a path segment naming the Working Method or the Operating Plan folder, the master CV's file name, or the vault's root folder name. Prints the file, line and matched text. | Staging `CHAT_STATE.md` with `-f`; a planted template path. Control: prose naming the Working Method passes. |
| B, rebuild | pre-commit | Staged output that differs from a fresh build of the staged source, as of the month recorded in the staged `index.html`. | A one-character edit to `index.html`; `items.json` changed without rebuilding. |
| C, map | pre-commit | A `MAP.md` that is stale against the staged files. | A new Markdown file committed without regenerating the map. |
| D, missing tool | every hook | A missing venv interpreter, gate script, map generator or `build.py`: a refusal naming it, never a skip. | Renaming the map generator; moving the venv. |
| E, STATE.md moved | pre-push | A push whose range touches `build.py`, `requirements.txt`, `index.html`, `src/`, `static/`, `tools/` or `.githooks/` with no commit in the range touching `STATE.md`. The last commit of a series is enough. | Pushing a `src/` change with no `STATE.md` change. Control: a series with `STATE.md` only in its last commit passes. |

Gate A matches path forms, never prose, and cannot match its own source.
Every pattern is written so the source never contains the text it matches,
and the vault's root folder name, which has never been committed, is held
only as a digest. A brief that needs a private path carries it, and briefs
are never committed. Gate E's list of implementation paths is recorded
in ADR-0007 Changes, 2026-09-26.

## Writing

No em-dashes. Lead with the verdict. Active voice. Numbers carry their
provenance or they do not appear. Dates are UTC; when a local date differs,
say which is which. Plain text that survives a paste into Word.
