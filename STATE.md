---
type: state
description: What exists right now for the portfolio site, what is blocked and on whom, and where the proof is. Where to start, then checked against the code and data.
status: current
---

# STATE

**Verified against commit 037a50e, the last commit before this file's
update, 2026-10-06T00:10Z, by the Brief 3 implementing session.** This is
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

**The styled site is built and committed, and not pushed.** Brief 3
rebuilt the approved Claude Design prototype in the generator: one page,
the eight sections of ADR-0008, every item from the master CV, styled to
ADR-0011, with every word in the first response. The ten checks of Brief 3
pass, each shown able to fail, and Lighthouse's medians meet ADR-0009 with
every heavy element. **The live site is still the earlier unstyled page,
serving Rahzaan alone, until the push**, which waits on the screen-reader
speech test and the chat's checks (Blocked, below).

A small Python generator builds the page from two content files
(ADR-0006), fails on a missing source, a missing proof link, a tier out of
order or shortened text that is not a cut of its source, and records the
month the page is as of. `tools/check_content.py` traces the built page to
the master CV. Ten decisions are in force, and ADR-0005 is superseded by
ADR-0010. Five repository gates guard
every commit and push (ADR-0007); they enforce only in a clone where
`core.hooksPath` is set. How the repository got here is in the session
logs, not in this file.

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
| Framework and rendering strategy decided | DONE | [VERIFIED] | 2026-09-26 | ADR-0006; row corrected by the Brief 1 session |
| Generator: reads content, computes timeline rows, renders, copies static files, byte-identical on rebuild | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md |
| Content schema, JSON, documented beside the content file | DONE | [VERIFIED] | 2026-09-26 | Same log |
| Gate: an item with no source fails the build, naming it | DONE | [VERIFIED] | 2026-09-26 | Same log; proven by deleting Rahzaan's source |
| Gate: an item with neither or both of proof and verification fails the build, naming it | DONE | [VERIFIED] | 2026-09-26 | Same log; proven both ways |
| Rahzaan rendered end to end, unstyled, every layer readable without scripts | DONE | [VERIFIED] | 2026-09-26 | Same log |
| Rahzaan layer 1 and layer 2 wording approved by the operator | DONE | [BELIEVED] | 2026-09-26 | Same log, round 2. Approved before Brief 1 was written; the brief's draft marker was left in by mistake. Stated by the architecture chat, not seen first-hand by the seat. Not in the master CV word for word; that is expected of layers 1 and 2. **Superseded 2026-10-05 by Brief 3**: Rahzaan's layer 1 is now the content pack's cut of its first bullet and its layer 2 the master's italic line, both checked against the master; logs/2026-10-05-styled-site.md |
| Tier order: the build fails when the content file's order contradicts tier | DONE | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md; ADR-0005 Changes, ADR-0008. Defeated by a synthetic tier 3 item above Rahzaan in a scratch copy; control: the same item below builds |
| As-of month: build.py --as-of, recorded in the output as a meta element | DONE | [VERIFIED] | 2026-09-26 | Same log; ADR-0006 Changes. With the clock a month ahead, the gate's rebuild is unchanged; --as-of with the next month changes the element and Rahzaan's span |
| Screen reader reaches the collapsed layer 3 | PARTIAL | [VERIFIED] | 2026-10-05 | logs/2026-10-05-styled-site.md. On the styled site, in headless Chrome by keyboard: each "In depth" control is a button named for its item, collapsed, its layer 3 absent from the accessibility tree; Enter expands it and layer 3 enters the tree. The speech half, NVDA's Speech Viewer, is not run: docs/deferred/screen-reader-speech-test.md, the operator's, before the push |
| Push of Brief 3's commits, replacing the live unstyled page | PENDING | | | Blocked, below. The commits are local only |
| What .nojekyll actually does when Pages is enabled | DONE | [VERIFIED] | 2026-09-26 | Same log, round 3 correction. Jekyll did not process the site: Markdown files are served raw with their front matter, /README.html is 404, and /.nojekyll itself is served. The live index.html and stylesheet are byte-identical to the committed ones. The cause is .nojekyll, settled by inference in ADR-0006 A3: the Pages source is "Deploy from a branch", which runs Jekyll by default, and Jekyll did not run |

## Blocked, and on whom

| Item | Blocked on | Who | Since |
|---|---|---|---|
| Push of Brief 3's commits | The screen-reader speech test, whose trigger is before the styled site replaces the live one, and the two checks Brief 3 reserves for the chat and the operator | Operator and chat | 2026-10-05 |

## Known unverified

- CSS `animation-timeline` is marked Limited availability by MDN and is not
  Baseline, checked 2026-09-23. Any use is progressive enhancement only.
- GSAP's licence text has not been read, only its pricing page.
- vis-timeline's keyboard accessibility, latest release, and mobile
  behaviour.
- The remaining open checks are listed in `docs/research/0002`, section
  "Not verified".

- Whether the Design artifact type keeps version history, and whether a
  shared link opens without a Claude account. Its standalone HTML export
  exists and was opened locally by Brief 3's session; the handoff to
  Claude Code through its MCP server was not available to that session.
- Lighthouse figures come from one machine (ADR-0009). Not measured on a
  real 2020 to 2022 phone, and the local server did not compress; GitHub
  Pages does.
- The knot's worker on Safari: OffscreenCanvas in a worker is documented
  for recent Safari but was not run there. A browser without it shows no
  knot. `content-visibility` and `:has()` were exercised in Chrome only.
- Whether the Vercel and MERJ crawler findings, measured Dec 2024, still
  hold. Re-measuring is not possible without a live site; the site's own
  server logs would check it after launch.
- Whether Anthropic's on-request fetcher behaves as ClaudeBot does. Not
  separately identified in the source.
- Every claim in the Portfolio Handoff of 2026-09-22 that was read in the
  architecture chat but not re-read since. Fifteen contradictions were found
  in that handoff and reported; they are listed in that chat, not here.
