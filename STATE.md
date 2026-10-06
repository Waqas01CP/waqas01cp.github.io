---
type: state
description: What exists right now for the portfolio site, what is blocked and on whom, and where the proof is. Where to start, then checked against the code and data.
status: current
---

# STATE

**Verified against commit 9a2043b, the last commit before this file's
update, 2026-10-06T10:55Z, by the Brief 4 implementing session.** This is
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

No open rows. Finished ones are in `docs/reference/completed.md`.

## Repository

No open rows. Finished ones are in `docs/reference/completed.md`.

## Build

| Task | Status | Evidence | Date | Proof |
|---|---|---|---|---|
| Screen reader reaches the collapsed layer 3 | PARTIAL | [VERIFIED] | 2026-10-05 | logs/2026-10-05-styled-site.md. On the styled site, in headless Chrome by keyboard: each "In depth" control is a button named for its item, collapsed, its layer 3 absent from the accessibility tree; Enter expands it and layer 3 enters the tree. The speech half, NVDA's Speech Viewer, is not run: docs/deferred/screen-reader-speech-test.md, the operator's, before the push |
| Push of Brief 3's commits, replacing the live unstyled page | PENDING | | | Blocked, below. The commits are local only |

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
