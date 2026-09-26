---
type: state
description: What exists right now for the portfolio site, what is blocked and on whom, and where the proof is. Where to start, then checked against the code and data.
status: current
---

# STATE

**Verified against commit cb20f35, the last commit before this file's
update, 2026-09-26T22:15Z, by the Brief 2 implementing session.** This is
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

**The site is live at the domain root**, serving one item, Rahzaan, as
unstyled semantic HTML. A small Python generator builds it from structured
content (ADR-0006), fails the build on a missing source, a missing proof
route or a tier out of order, and records the month the page is as of.
Eight decisions are accepted. Five repository gates guard every commit and
push (ADR-0007), each proven by the case built to defeat it. They enforce
only in a clone where `core.hooksPath` is set.

Not started: visual design, which is the operator's to run in Claude
Design, and every item other than Rahzaan, which arrives with the sections
ADR-0008 names. How the repository got here is in the session logs, not in
this file.

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
| CLAUDE.md commands section | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md. Environment, gates activation, build with and without --as-of, monthly refresh, map and dependency check, each run |
| CLAUDE.md hook blocks section | DONE | [VERIFIED] | 2026-09-26 | Same log. Each of the five gates with what it blocks and the case that defeats it |
| MAP.md and its generator, with a check mode against the staged files | DONE | [VERIFIED] | 2026-09-26 | Same log. No file needed frontmatter added |
| ADR-0005 concluded and written | DONE | [VERIFIED] | 2026-09-25 | ADR-0005 |
| ADR-0007, the repository gates, concluded and written | DONE | [VERIFIED] | 2026-09-26 | ADR-0007 |
| ADR-0008, sections, tiers and depth, concluded and written | DONE | [VERIFIED] | 2026-09-26 | ADR-0008 |
| Named Working Method paths in this file's header, briefs/README.md and logs/README.md | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 4. Ruled pointers by the chat and removed by it; a scan of the working tree finds none left. They remain in pushed history. The Brief 2 never-commit gate must catch any path segment naming the Working Method or its templates |

## Repository

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Repository name chosen | DONE | [VERIFIED] | 2026-09-23 | ADR-0002; folder renamed to waqas01cp.github.io |
| Public or private decided | DONE | [VERIFIED] | 2026-09-23 | ADR-0002; public, with CHAT_STATE.md never committed |
| .gitignore excluding CHAT_STATE.md written | DONE | [VERIFIED] | 2026-09-23 | ADR-0002 |
| git init and first commit | DONE | [VERIFIED] | 2026-09-25 | Done before Brief 1; this row was stale and was corrected by that session, evidence in logs/2026-09-26-generator-and-content-model.md |
| Project venv at .venv/, requirements.txt pinning Jinja2 as the one top-level dependency and MarkupSafe as its requirement | DONE | [VERIFIED] | 2026-09-26 | ADR-0006 Changes; logs/2026-09-26-generator-and-content-model.md |
| .gitattributes forcing LF, so a checkout under autocrlf matches a fresh build | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 2, fresh clones with and without it; logs/2026-09-26-gates-map-and-as-of.md, a fresh clone under the machine's system-level autocrlf checks out every text file as LF |
| Gate A, never-commit paths and private paths in content, pre-commit | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md; ADR-0007. Defeated by CHAT_STATE.md staged with -f and by a planted template path; control: prose naming the Working Method passes |
| Gate B, rebuild against the recorded as-of month, pre-commit | DONE | [VERIFIED] | 2026-09-26 | Same log. Defeated by a one-character edit to index.html and by items.json changed without rebuilding; control: rebuilt and staged passes |
| Gate C, map current against the staged files, pre-commit | DONE | [VERIFIED] | 2026-09-26 | Same log. Defeated by a new Markdown file without a regenerated map |
| Gate D, a missing tool is a hard failure, every hook | DONE | [VERIFIED] | 2026-09-26 | Same log. Defeated by renaming the map generator and by moving the venv |
| Gate E, STATE.md moved across the pushed range, pre-push | DONE | [VERIFIED] | 2026-09-26 | Same log. Defeated by pushing a src/ change with no STATE.md change; control: a series with STATE.md only in its last commit passes. Its implementation-path list is Brief 2's, not yet a record's |
| First push of the Brief 1 commits | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 3 correction. Pushed from this clone at 20:46:30Z through the end of round 2, per the local reflog and git ls-remote, and not by the seat. It happened before the chat's instruction to hold the first push for Brief 2. Round 3's four commits were then pushed from this clone at 20:59:48Z, also not by the seat. The chat has since withdrawn the hold and authorised pushing |

## Build

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Design prototype | PENDING | | | Not blocked. Built in Claude Design's standalone experience, design system first (docs/decisions/README.md, Pending, closed 2026-09-26); the operator's to run |
| Framework and rendering strategy decided | DONE | [VERIFIED] | 2026-09-26 | ADR-0006; row corrected by the Brief 1 session |
| Generator: reads content, computes timeline rows, renders, copies static files, byte-identical on rebuild | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md |
| Content schema, JSON, documented beside the content file | DONE | [VERIFIED] | 2026-09-26 | Same log |
| Gate: an item with no source fails the build, naming it | DONE | [VERIFIED] | 2026-09-26 | Same log; proven by deleting Rahzaan's source |
| Gate: an item with neither or both of proof and verification fails the build, naming it | DONE | [VERIFIED] | 2026-09-26 | Same log; proven both ways |
| Rahzaan rendered end to end, unstyled, every layer readable without scripts | DONE | [VERIFIED] | 2026-09-26 | Same log |
| Rahzaan layer 1 and layer 2 wording approved by the operator | DONE | [BELIEVED] | 2026-09-26 | Same log, round 2. Approved before Brief 1 was written; the brief's draft marker was left in by mistake. Stated by the architecture chat, not seen first-hand by the seat. Not in the master CV word for word; that is expected of layers 1 and 2 |
| Tier order: the build fails when the content file's order contradicts tier | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md; ADR-0005 Changes, ADR-0008. Defeated by a synthetic tier 3 item above Rahzaan in a scratch copy; control: the same item below builds |
| As-of month: build.py --as-of, recorded in the output as a meta element | DONE | [VERIFIED] | 2026-09-26 | Same log; ADR-0006 Changes. With the clock a month ahead, the gate's rebuild is unchanged; --as-of with the next month changes the element and Rahzaan's span |
| Screen reader reaches the collapsed layer 3 | PENDING | | | ADR-0005 Confirmation; must be done before the first content page ships. Not run |
| What .nojekyll actually does when Pages is enabled | DONE | [VERIFIED] | 2026-09-26 | Same log, round 3 correction. Jekyll did not process the site: Markdown files are served raw with their front matter, /README.html is 404, and /.nojekyll itself is served. The live index.html and stylesheet are byte-identical to the committed ones. The cause is .nojekyll, settled by inference in ADR-0006 A3: the Pages source is "Deploy from a branch", which runs Jekyll by default, and Jekyll did not run |

## Blocked, and on whom

| Item | Blocked on | Who | Since |
|---|---|---|---|

Nothing is blocked. The design prototype was listed here, blocked on a
four-check test; that question closed on 2026-09-26 and the design system
is the operator's to run.

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
