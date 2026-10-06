---
type: log
description: Brief 4. Three changes before the styled site is pushed. content-visibility on the sections removed, found to fail ADR-0009 on this machine, and restored with a comment saying what was measured, its accessibility cost put to the chat; the Intro paragraph's approval dated in UTC; STATE.md's 44 DONE rows moved to completed.md. Committed in series, not pushed.
status: current
---

# 2026-10-06 (UTC): Before the push

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: 35d54dd, working
tree clean, `.commitmsg/1-records-after-report-3.txt` present and left in
place. HEAD at end: the commit carrying this log. Mode: mutating. Brief: 4.
Previous log: 2026-10-05-styled-site.md.

The session ran from about 09:55Z on 2026-10-06. The local date (UTC+5)
was the same throughout.

## What was asked

Brief 4, which is never committed, so its substance is here.

The chat checked Report 3 on 2026-10-06 from a `git archive` of 918b81c:
byte-identical rebuild with Jinja2 3.1.6, the content trace passing, links
matching the master, no em or en dash, axe 0 at 1366 and 360 px in both
themes with every panel open, no off-origin request or storage, the device
setting back after the switch and a reload, every list item visible
without scripts, identical frames under reduced motion. Its Lighthouse
12.8.2, default mobile, median of five: LCP 2125 ms, CLS 0, TBT 6 ms.

Three changes, committed locally, **not pushed**; the operator's
screen-reader speech test runs on what is committed, and the push after it.
How each is done was left to this seat, with each choice logged.

1. **`content-visibility` on the sections.** The chat recommended removing
   it. Its measurements, headless Chromium 141 through Playwright, CDP
   `Accessibility.getFullAXTree` straight after load: 1 of 26 headings at
   360 px and 8 of 26 at 1366 px as built; 26 of 26 with
   `--force-renderer-accessibility` or with the rule overridden; the
   Skills heading ignored with role "none"; all 26 present after scrolling
   to the bottom and back. Without the rule, six Lighthouse runs gave TBT
   204, 41, 29, 53, 1 and 36 ms, a median of 41 ms over runs 1 to 5. Its
   reasoning: the rule buys about 35 ms the goals do not need, against a
   measured gap in the accessibility tree; NVDA would most likely not show
   the gap, since a screen reader switches on full accessibility mode.
   `html:has(:target)` likely goes with it; anchors must still land. The
   seat could push back: if its measurements showed the goals fail without
   the rule, say so with the numbers. If the rule stayed, its comment had
   to say what was measured and no more. The chat records the outcome in
   ADR-0009's Changes.
2. **A date.** The chat wrote 2026-10-06, its local date, for the
   operator's approval of the Intro paragraph on 2026-10-05 UTC (21:59Z by
   the content pack's file time). Correct `src/content/site.json`
   `approved.approved_by` and `src/content/README.md` line 27.
3. **STATE.md's finished rows.** About forty DONE rows to
   `docs/reference/completed.md`, approved by the operator on 2026-10-06;
   PARTIAL and PENDING rows stay.

Verification, each check shown able to fail first: build twice
byte-identical; gates on every commit; the content trace; axe at 1366 and
360 px, light and dark, waiting out the theme transition (the chat saw 23
to 34 contrast failures within 200 ms of the switch and 0 after 3 s);
anchors by link and by a URL with a hash; the accessibility-tree count at
load with and without full accessibility mode; Lighthouse, median of five,
against ADR-0009. Then this log, and Report 4.

## What was done

Commits, each through gates A, B and C: 06f97c6 the date; e0e876c the
rule removed; 9a2043b the rule restored; 9d06c61 the rows
moved; then this bookkeeping. [VERIFIED]

**Change 1: removed, failed ADR-0009, restored.** [VERIFIED] The rule was
removed in e0e876c on the first three Lighthouse sets, below, which put
the page inside ADR-0009 in two of three. The verification run on the
committed build then gave a median of 249 ms, a fail, so the rule is back
exactly as at 35d54dd. Only its comment changes: it now says what was
measured, both the speed it buys and its accessibility cost, and no
longer claims the content stays in the accessibility tree and in
find-in-page. `site.js` and `index.html` are byte-identical to 35d54dd.

The numbers from this machine differ from the chat's, so all of them are
here. Tools: Chrome 154 headless, driven by puppeteer-core 25.12.0;
Lighthouse 13.5.0, default mobile; axe-core 4.14.0; each variant a
scratch copy served locally without compression.

*Lighthouse, TBT in ms, variants interleaved within a set so drift on
this machine falls on all alike.* [VERIFIED]

| Set | With the rule | Without the rule |
|---|---|---|
| 1 | 0, 31, 0, 51, 29: median 29 | 229, 148, 164, 179, 132: median 164 |
| 2 | | 555, 250, 103, 260, 150: median 250, fails |
| 3 | 41, 88, 0, 192, 1: median 41 | 421, 171, 126, 403, 141: median 171 |
| 4, committed builds | 63, 0, 54, 27, 158: median 54 (9a2043b) | 249, 173, 129, 274, 250: median 249, fails (e0e876c) |

Without the rule: two medians of five pass and two fail; pooled, a median
of 176 ms over 20 runs, 9 of them over 200. With it, a pooled median of
31 ms over 15 runs, none over 200. LCP stayed between 1988 and 2493 ms
and CLS at 0 to 0.0001 throughout. Set 3 ran with the operator's own
browser open on this machine (41 processes), and its spread was wider for
every variant.

*Where the time goes.* [VERIFIED] Main-thread layout over a load at a
real 4x slowdown, phone viewport, median of five loads: 167 ms with the
rule, 551 ms without. A single trace showed the first layout covering
1032 layout objects without the rule and 163 with it. The script's own
forced layouts were 2 to 3 ms either way. The cost is the browser laying
out the whole page.

*Accessibility tree at load, headings not ignored, five fresh browsers per
cell.* [VERIFIED]

| Setup | 360 px | 1366 px |
|---|---|---|
| With the rule, default mode | 1 of 26 in all five | 1 of 26 in all five |
| With the rule, full accessibility mode | 31 in all five | 31 in four, 26 in one |
| Without the rule, either mode | 26 in all five | 26 in all five |

The rows with the rule are the page at 35d54dd. The committed page,
9a2043b, repeated them: 1 of 26 in default mode and 31 in full mode, in
all five loads at each width.

- The chat's 8 of 26 at 1366 px reproduced only in a browser that had
  already loaded a page; fresh, it was 1 every time.
- **The 31 are a second effect the chat did not see.** In full
  accessibility mode, the mode a screen reader switches on, the tree at
  load held the five collapsed "In depth" panels: their headings, and at
  360 px their "Close in depth" buttons, all inside elements the DOM has
  `hidden`. The deferred speech test records the intended behaviour as
  "collapsed, the layer 3 text is absent from the tree", and ADR-0010 A2
  rests on it. So NVDA would most likely meet this, contrary to the
  brief's expectation. The mechanism, inferred and not tested: the script
  hides the panels after the first style pass, and a skipped section's
  style is not recomputed until it is rendered.
- After scrolling to the bottom and back, the count depended on speed: 9
  and 15 of 26 for a fast scroll, 25 and 26 for a slow one. The chat saw
  26.
- The Skills heading with the rule: ignored, role "none", as the chat
  found.

*The decision.* ADR-0009 is an accepted record and outranks the brief;
its Confirmation is a median of five under 200 ms, and on this machine
the page without the rule failed that in two of four attempts, the last
on the committed build. The brief keeps the rule when the goals fail
without it. The accessibility cost is real and now measured further than
the brief had it, but no record's decision forbids it, so it is not this
seat's to trade against ADR-0009. It goes to the chat (Findings 1).

**Change 2: the date.** [VERIFIED] `approved_by` and the README now say
2026-10-05. The 2026-10-06 date is wrong by evidence found this session:
Brief 3's session wrote the approved paragraph into a scratch file at
2026-10-05T22:43:22Z, so the approval was no later than that. The 21:59Z
time is taken from the brief: the content pack was rewritten at
2026-10-06T09:40:38Z, so its file time no longer shows it. `approved_by`
is not rendered; the content trace prints it. Finding 1 of the previous
log repeated the pack's date and is annotated in place, its words kept.
That log's own dates are right: it is dated by the session's start,
2026-10-05 UTC, and says its commits fell after 00:00Z on 2026-10-06.

**Change 3: the rows.** [VERIFIED] All 44 DONE rows moved: Documents 22,
Repository 12, Build 10. A script compared every removed line with the
added ones: 44 of 44 found verbatim, with only the Status column dropped,
since `completed.md` has none. They sit under headings naming their
table. The PARTIAL and PENDING rows stay; the two tables left empty say
so.

**Verification.** Each check was first run against a case built to
defeat it, in scratch copies, never in the repository. "Without" is
e0e876c's build; "final" is the committed state, with the rule.

| Check | Defeated by | Result |
|---|---|---|
| Build twice | The same build as of 2026-11: hashes differ | Three builds at 2026-10 identical, hashed over every generated file; `index.html` and `site.js` byte-identical to 35d54dd |
| Gates | (gate proofs: Brief 2) | Passed on every commit |
| Content trace | 592 made 593 in a copy of the page: exit 1, 3 blocks not traced, bullets 27 of 28 | Exit 0; 396 blocks traced, 0 not; bullets 28 of 28, italic-line sentences 17 of 17, skills lines 8 of 8, courses 26 of 26, certificates 5 of 5; the approval printed as 2026-10-05 |
| axe | Faint text and an image without alt: 2 violations | Without: 0 in all 12 (1366 and 360 px; light, dark by the device, dark by the switch after 3 s; as loaded and with every panel and card open). Final: 0 in 11 of the 12. The twelfth, 1366 px, device dark, as loaded, gave 22 contrast failures on the certificate cards in 2 of 21 runs (Findings 4) |
| Anchors, 22 targets by link and by hash, scripts on and off | The rule without its `:has(:target)` undo: 74 of 132 landed, targets 650 to 1,900 px off | Without: 132 of 132. Final: 132 of 132 |
| Accessibility tree at load | The page with the rule, against the page without: 1 of 26, and the five collapsed panels in full mode | Without: 26 of 26 in all 20 loads, no collapsed panel. Final: 1 of 26 at load in default mode, and the five collapsed panels in the tree in full mode, in all ten loads: the cost its comment records |
| Lighthouse | A 600 ms script in the head: medians 1861 ms (without) and 1851 ms (final), both failing | Without: 249 ms, fails. Final: 54 ms (63, 0, 54, 27, 158), LCP 2115 ms, CLS 0: meets |

## Rejected alternatives

- **Keeping the rule removed** after the failing run. It fixes the tree,
  but the committed page would fail ADR-0009's own test on this machine,
  and the brief keeps the rule in that case.
- **Hiding the panels before the first style pass** by a script in the
  head, so the rule could stay without exposing them. It fixes the five
  panels only; most of the page would still be missing from the tree in
  default mode. A design change to put to the chat, not to make here.
- **Removing `text-wrap: pretty` and `balance` to win back time.** One
  Lighthouse set suggested it (median 100 ms); the next contradicted it
  (445 ms), and layout traces showed no reliable saving (416 to 624 ms
  across the variants, against 551). Both come from the approved
  prototype, so it would also have been a design change.
- **Excluding Projects from the rule**, so its panels render at load. Not
  measured; ad hoc; the other sections' gap would stay.
- **Rewriting e0e876c away**, since nothing is pushed. A new commit keeps
  the trial and its measurements in history.

## Checked and found already correct

- The brief's starting state: `main` at 35d54dd, origin at ca5e461,
  `assets/` gone, the chat's message file present, hooks active.
- A fresh build at the recorded month, 2026-10, matched the committed
  output before any change.
- `pip list --not-required` shows Jinja2 and pip only.
- The chat's 1 of 26 at 360 px, Skills ignored with role "none", and 26 of
  26 under `--force-renderer-accessibility` all reproduced.

## Not done

- **Push.** Not asked; the speech test comes first.
- **The screen-reader speech test.** The operator's, with NVDA. On the
  committed page, NVDA will most likely find the five collapsed panels in
  its reading at load (above). Whether it should run before the chat rules
  on Findings 1 is the operator's call.
- **ADR-0009's Changes row.** The chat's to write.
- **Find-in-page** with the rule was not tested.

## Findings and recommendations

1. **The rule's accessibility cost is a decision for the chat.** With it,
   ADR-0009 holds on this machine (medians 29, 41 and 54);
   without it, every section is in the tree and no collapsed panel is,
   but ADR-0009 fails in two of four medians here while passing on the
   chat's machine (41 ms). Options: (a) keep the rule and accept the cost;
   (b) remove it and amend ADR-0009, for example to name the machine its
   test runs on or to accept this margin, which needs a record; (c) keep
   the rule and hide the panels before the first style pass, which fixes
   only what a screen reader meets. Recommendation: (b) if the chat's
   machine is to be the reference, since the cost of the rule falls on
   readers and the saving on a lab proxy (ADR-0009 A3); otherwise (c),
   measured, as the smallest change that stops a screen reader hearing
   collapsed content.
2. Brief 3's accessibility check (keyboard, 10 of 10) read the tree after
   tabbing to each panel, so, inferred and not tested, its section was
   already rendered. The state at load was not checked. A check of the
   tree straight after load, in both modes, catches the panels.
   Recommendation: add it to the standing checks.
3. Lighthouse on this machine moves with what else the machine is doing.
   Interleaving variants and repeating sets made that visible; a single
   median of five near a threshold is not a stable verdict here.
4. **An intermittent axe failure on the committed page.** At 1366 px,
   device dark, as loaded, axe twice reported 22 contrast failures on the
   certificate cards: the cards' light text read against their lime
   hover layer, ratio 1.64. Two of 21 runs with content-visibility, one
   of them while the anchor check ran alongside; 0 of 9 without it; 0 in
   Brief 3's and the chat's runs. The layer sits below each card,
   translated out of view and clipped. Twelve further tries to catch it
   on a screenshot found nothing, so whether the layer ever showed or
   axe misread a clipped layer is not known. Recommendation: the chat
   repeats this case in its own harness.

## Noticed and not investigated

- Which single extra heading remained in the tree, with the rule, in full
  mode at 360 px after one panel was opened and closed (31 became 27).
