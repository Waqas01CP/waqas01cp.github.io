---
type: state
description: What exists right now for the portfolio site, what is blocked and on whom, and where the proof is. Where to start, then checked against the code and data.
status: current
---

# STATE

**Verified against commit 6812c4f, the last commit before this file's
update, 2026-10-07T12:08Z, by the Brief 5 implementing session, round 2.** This is
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

**The styled site is live, with Brief 5's fix.** Brief 3 rebuilt the approved Claude Design prototype in the
generator: one page, the eight sections of ADR-0008, every item from the
master CV, styled to ADR-0011, with every word in the first response.
Brief 3's and Brief 4's commits, with the chat's 8909ec5, were pushed from
this clone at 2026-10-07T10:25:54Z; no session log records that push, and
it came before the screen-reader speech test its row waited on. The live
page was fetched at 10:31Z and is byte-identical to 8909ec5's output.

ADR-0009 keeps `content-visibility` on the sections on one condition: in
full accessibility mode, the tree at load matches the page without the
rule. 8909ec5's page failed it: a screen reader's tree at load held the
five collapsed "In depth" panels at 360 px, and at both widths the "No
lanes selected." line and the hidden theme's contact marks. Brief 5 makes
everything hidden inside the sections also `aria-hidden`. The operator
pushed it at 11:41:22Z; the live site serves its exact bytes, and on the
live site the tree matches at 360 and 1366 px, both themes, scripts on
and off, in Chrome 154 and Edge 154. What a real screen reader says is
the operator's NVDA test (Blocked, below).

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
| Screen reader reaches the collapsed layer 3 | PARTIAL | [VERIFIED] | 2026-10-07 | logs/2026-10-05-styled-site.md. On the styled site, in headless Chrome by keyboard: each "In depth" control is a button named for its item, collapsed, its layer 3 absent from the accessibility tree; Enter expands it and layer 3 enters the tree. **Corrected by logs/2026-10-06-before-push.md**: at load, in full accessibility mode, the five collapsed panels were in the tree. **Fixed by Brief 5**, logs/2026-10-07-tree-parity.md: at load, in full mode, no collapsed panel is in the tree, and the keyboard check passes for all five panels at 360 and 1366 px. The same holds on the live site in Edge 154 (round 2 of that log). The speech half, NVDA's Speech Viewer, is not run: docs/deferred/screen-reader-speech-test.md, the operator's, now with steps for this page. Its trigger, before the styled site replaces the unstyled one, passed unmet at the 2026-10-07T10:25Z push |

## Blocked, and on whom

| Item | Blocked on | Who | Since |
|---|---|---|---|
| The speech half of the layer 3 check | The operator running NVDA in Chrome and Edge, by the steps in the deferred entry, and sending back the Speech Viewer text | Operator | 2026-10-07 |
| Brief 5's report checked; ADR-0009's Changes row recording its condition met; the contact marks' alt text confirmed | The architecture chat | Chat | 2026-10-07 |

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
- Lighthouse figures come from this machine and the chat's container,
  which disagree on what content-visibility saves: TBT 31 ms with it and
  176 without here, pooled medians; 6 and 41 in the chat's. ADR-0009
  names neither machine; since 2026-10-06 a fail on either is a fail.
  Not measured on a real 2020 to
  2022 phone. On the live site, compressed by GitHub Pages, from this
  machine on 2026-10-07: TBT medians 138 and 95 ms (LCP 1721 and
  1739 ms), against 41 ms for the same bytes served locally in the same
  set. It meets ADR-0009 with a narrower margin; one run of ten reached
  208 ms. Why the live page blocks longer is not known.
- Why axe sometimes reports 22 contrast failures on the certificate cards
  at 1366 px, device dark, as loaded, with content-visibility: Brief 4,
  2 of 21 runs (0 of 9 without the rule); the chat, 0 of 20; Brief 5, 1 of
  20 on the page as built and 1 of 40 on its own page, each the first run
  after a browser started. axe read the card's text against its lime
  hover layer, ratio 1.64. Not caught on a screenshot. Bounded, not
  explained.
- The tree-at-load parity holds in headless Chrome 154 and Edge 154, on
  the live site. NVDA's reading, Firefox, and Safari with VoiceOver are
  not measured, and why Chromium
  ignores `hidden` and CSS in a skipped section is inferred from the
  measurements, not read in its source.
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
