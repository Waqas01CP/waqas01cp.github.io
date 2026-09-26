---
type: index
description: The session log index. Read this first for what prior sessions did, then chain backwards through the most recent relevant log only as far as needed.
status: current
---

# Session logs

One log per session, newest at the top. This table is the navigation index
for all session history.

## How to use this file

Read this table first. It tells you what prior sessions did.

When you need detail beyond this table, read the most recent relevant log.
That log references the one before it. Chain backwards only as far as you
need, and stop when you have enough. Do not read the directory.

This rule is what keeps the reading cost flat as the log count grows.

## How to maintain it

Append your row in the same commit as your work. A log with no row here is
invisible.

Never delete or modify an existing row. A correction is a new row saying so.

Rows are compressed: no prose, no reasoning, nothing beyond what a future
session needs to decide whether to open the log.

If a log file exists with no row here, read it and add the row before doing
anything else.

One session, one file. A session that continues across several rounds adds
a row per round, each naming the same file.

## Log format

The session-log template in the operator's cross-project Working Method,
which lives in his private vault and is deliberately not linked from here.
File name `logs/YYYY-MM-DD-short-description.md`, dated in UTC. There is no
project-specific log-format record yet.

## Reorganisation

When this directory passes about 80 files at its root, split by lane into
subdirectories and leave this index at the top pointing into them. Decide it
before the root becomes unscannable, not after.

## Index

| Date (UTC) | Log file | Session | What was done | Outcome |
|---|---|---|---|---|
| 2026-09-26 | [2026-09-26-gates-map-and-as-of.md](2026-09-26-gates-map-and-as-of.md) | Brief 2 | Five gates from ADR-0007, map generator, build --as-of recorded in the output, tier order enforced; records committed through the live gates | 45 of 45 gate checks and 6 of 6 sabotage proofs pass; brief's commit order swapped; vault root name held as a digest |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 4 | Chat's removal of the last three Working Method paths committed; push authorised; the held commits found already pushed | No vault pointer left in the tree; all Brief 1 commits pushed |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 3 correction | Found the round 2 commits already pushed (20:46Z, not by the seat) and the site live; measured what .nojekyll does | Corrects round 3's "nothing is pushed". Site live at the root, byte-identical to committed output; Jekyll did not run |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 3 | Chat's record and README corrections committed; decisions noted (tier-order check, pre-push state gate, as-of month in Brief 2, no push yet); vault-pointer scan of all history | Committed, not pushed; three named Working Method paths remain, awaiting a ruling |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 2 | Chat's answers applied: MarkupSafe pinned, .gitattributes LF, vault path removed from README.md, draft status dropped; nine commits by concern | Committed; version check confirmed to read requirements.txt; round 1's git diff finding corrected |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1 | Python generator, JSON content schema, two content gates, Rahzaan rendered unstyled, CLAUDE.md commands | Built and verified, uncommitted pending operator; YAML replaced by JSON; case-study link made root-relative |

The architecture chat's own history is in `CHAT_STATE.md`, not here.
