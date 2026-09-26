---
type: state
description: What exists right now for the portfolio site, what is blocked and on whom, and where the proof is. Where to start, then checked against the code and data.
status: current
---

# STATE

**Verified against commit e843533, the last commit before this file's
update, 2026-09-26T21:12Z, by the Brief 1 implementing session.** This is
the only line in this file that names a commit. Created 2026-09-23T01:00Z by the
architecture chat, from the new-project setup procedure in the operator's cross-project Working
Method, which lives in his private vault and is deliberately not linked from
here.

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

**Superseded 2026-09-26 (UTC), Brief 1.** The repository has commits, six
decisions are accepted, and ADR-0006 settled the build. The generator now
exists and renders one item, Rahzaan, as unstyled HTML with both content
gates proven. It is committed as a series of commits by concern. The
commits through the end of round 2 were pushed on 2026-09-26 at 20:46Z,
not by the implementing seat, and **the site is live at the domain root**,
serving that unstyled output. Every later Brief 1 commit is pushed too,
the chat having withdrawn its hold. Next, Brief 2: the four gates, the map generator,
verification of .gitattributes, and the as-of month.

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
| CLAUDE.md scope floor section | DONE | [VERIFIED] | 2026-09-26 | Written before Brief 1; this row was stale and was corrected by that session, evidence in logs/2026-09-26-generator-and-content-model.md |
| CLAUDE.md runtime and conventions sections | DONE | [VERIFIED] | 2026-09-26 | ADR-0006; written before Brief 1, row corrected by that session, same log |
| CLAUDE.md commands section | PARTIAL | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md. Environment, build and dependency check recorded and each run. The map generator and rebuild gate the section requires are Brief 2 |
| CLAUDE.md hook blocks section | PENDING | | | Describes four gates that do not exist yet; completed when Brief 2 builds them |
| MAP.md and its generator | PENDING | | | Not started; no generator written. Brief 2 |
| Named Working Method paths in this file's header, briefs/README.md and logs/README.md | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 4. Ruled pointers by the chat and removed by it; a scan of the working tree finds none left. They remain in pushed history. The Brief 2 never-commit gate must catch any path segment naming the Working Method or its templates |

## Repository

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Repository name chosen | DONE | [VERIFIED] | 2026-09-23 | ADR-0002; folder renamed to waqas01cp.github.io |
| Public or private decided | DONE | [VERIFIED] | 2026-09-23 | ADR-0002; public, with CHAT_STATE.md never committed |
| .gitignore excluding CHAT_STATE.md written | DONE | [VERIFIED] | 2026-09-23 | ADR-0002 |
| git init and first commit | DONE | [VERIFIED] | 2026-09-25 | Done before Brief 1; this row was stale and was corrected by that session, evidence in logs/2026-09-26-generator-and-content-model.md |
| Project venv at .venv/, requirements.txt pinning Jinja2 as the one top-level dependency and MarkupSafe as its requirement | DONE | [VERIFIED] | 2026-09-26 | ADR-0006 Changes; logs/2026-09-26-generator-and-content-model.md |
| .gitattributes forcing LF, so a checkout under autocrlf matches a fresh build | DONE | [VERIFIED] | 2026-09-26 | Same log, round 2; proven by fresh clones with and without it |
| Gates: state file moves with work, map is current, never-commit paths, missing tool is a hard failure | PENDING | | | Brief 2. Built before the first feature, each proven to fire. The state-file gate is a pre-push hook over the whole range being pushed, not a pre-commit hook, so a series of commits by concern with bookkeeping last passes (chat's decision after Brief 1 round 2) |
| First push of the Brief 1 commits | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 3 correction. Pushed from this clone at 20:46:30Z through the end of round 2, per the local reflog and git ls-remote, and not by the seat. It happened before the chat's instruction to hold the first push for Brief 2. Round 3's four commits were then pushed from this clone at 20:59:48Z, also not by the seat. The chat has since withdrawn the hold and authorised pushing |

## Build

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Design prototype | PENDING | | | Gated on where it is built, CHAT_STATE item 4 |
| Framework and rendering strategy decided | DONE | [VERIFIED] | 2026-09-26 | ADR-0006; row corrected by the Brief 1 session |
| Generator: reads content, computes timeline rows, renders, copies static files, byte-identical on rebuild | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md |
| Content schema, JSON, documented beside the content file | DONE | [VERIFIED] | 2026-09-26 | Same log |
| Gate: an item with no source fails the build, naming it | DONE | [VERIFIED] | 2026-09-26 | Same log; proven by deleting Rahzaan's source |
| Gate: an item with neither or both of proof and verification fails the build, naming it | DONE | [VERIFIED] | 2026-09-26 | Same log; proven both ways |
| Rahzaan rendered end to end, unstyled, every layer readable without scripts | DONE | [VERIFIED] | 2026-09-26 | Same log |
| Rahzaan layer 1 and layer 2 wording approved by the operator | DONE | [BELIEVED] | 2026-09-26 | Same log, round 2. Approved before Brief 1 was written; the brief's draft marker was left in by mistake. Stated by the architecture chat, not seen first-hand by the seat. Not in the master CV word for word; that is expected of layers 1 and 2 |
| Tier applied to order and prominence | PENDING | | | ADR-0005 Changes. Decided by the chat after Brief 1 round 2: the build fails when the content file's order contradicts tier, rather than sorting by tier, so there is one source of order. Not built; due when a second item arrives. Not yet in a record |
| Rebuild gate: committed output equals a fresh build | PENDING | | | Brief 2. Reads the as-of month recorded in the output, not the build date (ADR-0006 Changes). The recording format and the build's as-of input land together in Brief 2 |
| Screen reader reaches the collapsed layer 3 | PENDING | | | ADR-0005 Confirmation; must be done before the first content page ships. Not run |
| What .nojekyll actually does when Pages is enabled | DONE | [VERIFIED] | 2026-09-26 | Same log, round 3 correction. Jekyll did not process the site: Markdown files are served raw with their front matter, /README.html is 404, and /.nojekyll itself is served. The live index.html and stylesheet are byte-identical to the committed ones. Whether .nojekyll is the cause, rather than a workflow-based Pages source, is not verified |

## Blocked, and on whom

| Item | Blocked on | Who | Since |
|---|---|---|---|
| The design prototype | The four-check test on Claude Design | Operator | 2026-09-22 |

## Known unverified

- The Pages source setting (a branch or a workflow) and who enabled Pages.
  The GitHub CLI is not installed here, so the configuration was not read.
  What Pages serves was measured instead: on 2026-09-26 at 20:56Z it served
  the committed index.html and stylesheet byte for byte from the root,
  which settles the gap ADR-0006 A3 records.
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
