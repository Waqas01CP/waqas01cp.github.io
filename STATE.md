---
type: state
description: What exists right now for the portfolio site, what is blocked and on whom, and where the proof is. Where to start, then checked against the code and data.
status: current
---

# STATE

**Not yet verified against any commit.** This folder is not a git repository
yet: no `git init` has been run and no commit exists. Created
2026-09-23T01:00Z by the architecture chat, from the procedure in
`Working Method\03 New Project Setup.md`. When the repository is
initialised, this line becomes the verified-against line and is the only
line in this file that names a commit.

This file is where to start, not where to stop. It outranks memory. It does
not outrank the code or the data: where a row disagrees with them, the row
is stale; report it and correct it.

Organised by task, not by session.

## How to read a row

STATUS is DONE, PARTIAL or PENDING. DONE only when built and exercised,
never when merely examined.

Evidence is [VERIFIED] (exercised and observed) or [BELIEVED] (reasoned
from reading, not run). Unmarked means believed.

Proof is a commit, a decision record or a log filename. Never a file path.

## How to maintain it

Update the affected rows in the same commit as the work. A commit that
completes a task without updating its row is incomplete.

When a row becomes DONE, move it to `docs/reference/completed.md` in the
same commit. Never delete one.

When a blocker clears, remove it from Blocked in the same commit and record
the clearing in the task's row.

Update the verified-against line whenever you touch this file.

## Headline

Nothing is built. No site, no prototype, no repository, no code of any kind.
What exists is the document skeleton and three accepted decisions. ADR-0001
settles the sectioned structure with projects ranked by importance. ADR-0002
settles that it is a public GitHub Pages user site at waqas01cp.github.io,
on no budget, contacted by email. ADR-0003 settles a hand-built vertical
timeline section, which reverses one clause of ADR-0001.

The master CV was corrected on 2026-09-23: the degree gained its Sep 2022
start date, and three of four certificate dates were wrong by one to two
years. That correction is the reason ADR-0003 exists.

What still blocks everything downstream is the scope floor: twelve of
fifteen proposed lines are agreed, and three need research before they can
be concluded.

**Superseded 2026-09-25.** The floor closed as ADR-0004 at **fourteen**
lines, not fifteen. The count of fifteen came from the original proposal of
2026-09-23, which included "no timeline" as line 6; ADR-0003 reversed that
line the same day and the count was carried forward without recounting. The
chat made this error twice before catching it. What now blocks the first
commit is `CLAUDE.md`, whose runtime and commands sections are still
undecided.

## Documents

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Decision index and topic list created | DONE | [VERIFIED] | 2026-09-23 | docs/decisions/README.md, read back after writing |
| ADR-0001 concluded and written | DONE | [VERIFIED] | 2026-09-23 | ADR-0001 |
| ADR-0002 concluded and written | DONE | [VERIFIED] | 2026-09-23 | ADR-0002 |
| ADR-0003 concluded and written | DONE | [VERIFIED] | 2026-09-23 | ADR-0003 |
| ADR-0004, the scope floor, concluded and written | DONE | [VERIFIED] | 2026-09-25 | ADR-0004 |
| Research 0003 written, skill display and writing settled | DONE | [VERIFIED] | 2026-09-25 | docs/research/0003-skill-display-and-writing.md |
| Master CV: UC Davis certificate and its credential link added | DONE | [VERIFIED] | 2026-09-25 | Diff returned by the edit |
| ADR-0001 annotated with the reversed clause | DONE | [VERIFIED] | 2026-09-23 | ADR-0001 Changes table |
| Master CV corrected: degree start, four certificate dates | DONE | [VERIFIED] | 2026-09-23 | Diff returned by the edit, reviewed line by line |
| Research 0001 written | DONE | [VERIFIED] | 2026-09-23 | docs/research/0001-how-hiring-readers-read-candidate-material.md, read back after writing |
| Research 0002 written, tool findings captured before loss | DONE | [VERIFIED] | 2026-09-23 | docs/research/0002-tools-and-libraries.md |
| Deferred entry for the timeline written | DONE | [VERIFIED] | 2026-09-23 | docs/deferred/projects-timeline.md, read back after writing |
| Log index created, no logs yet | DONE | [VERIFIED] | 2026-09-23 | logs/README.md, read back after writing |
| CLAUDE.md scope floor section | PENDING | | | Unblocked 2026-09-25 by ADR-0004; not yet written into the file |
| CLAUDE.md runtime, conventions, commands, hooks | PENDING | | | Blocked on the framework decision |
| MAP.md and its generator | PENDING | | | Not started; no generator written |

## Repository

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Repository name chosen | DONE | [VERIFIED] | 2026-09-23 | ADR-0002; folder renamed to waqas01cp.github.io |
| Public or private decided | DONE | [VERIFIED] | 2026-09-23 | ADR-0002; public, with CHAT_STATE.md never committed |
| .gitignore excluding CHAT_STATE.md written | DONE | [VERIFIED] | 2026-09-23 | ADR-0002 |
| git init and first commit | PENDING | | | Blocked on the scope floor, since CLAUDE.md carries it |
| Gates: state file moves with work, map is current, never-commit paths, missing tool is a hard failure | PENDING | | | Built before the first feature, each proven to fire |

## Build

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Design prototype | PENDING | | | Gated on where it is built, CHAT_STATE item 4 |
| Framework and rendering strategy decided | PENDING | | | Constrained by research 0001 |
| Any site code | PENDING | | | Nothing written |

## Blocked, and on whom

| Item | Blocked on | Who | Since |
|---|---|---|---|
| CLAUDE.md being finished, the first commit, and every brief | The runtime and commands sections, which need the framework decision | Chat, then operator | 2026-09-25 |
| The design prototype | The four-check test on Claude Design | Operator | 2026-09-22 |

## Known unverified

- CSS `animation-timeline` is marked Limited availability by MDN and is not
  Baseline, checked 2026-09-23. Any use is progressive enhancement only.
- GSAP's licence text has not been read, only its pricing page.
- vis-timeline's keyboard accessibility, latest release, and mobile
  behaviour.
- The remaining open checks are listed in `docs/research/0002`, section
  "Not verified".

- Whether the Design artifact type exports a Claude Code handoff bundle and
  standalone HTML, whether it keeps version history, and whether a shared
  link opens without a Claude account. The four-check test in `CHAT_STATE.md`
  item 4 would check all four.
- Whether the Vercel and MERJ crawler findings, measured Dec 2024, still
  hold. Re-measuring is not possible without a live site; the site's own
  server logs would check it after launch.
- Whether Anthropic's on-request fetcher behaves as ClaudeBot does. Not
  separately identified in the source.
- Every claim in the Portfolio Handoff of 2026-09-22 that was read in the
  architecture chat but not re-read since. Fifteen contradictions were found
  in that handoff and reported; they are listed in that chat, not here.
