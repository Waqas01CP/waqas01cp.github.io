---
type: log
description: Brief 5. content-visibility kept on the sections, and the accessibility tree at load in full mode made to match the page without it, at 360 and 1366 px, both themes, scripts on and off, by marking everything hidden inside the sections aria-hidden. Found the styled site already pushed before the speech test. Standing checks written down. Round 2, after the operator's push: checked on the live site in Chrome and Edge; NVDA steps written into the deferred entry.
status: current
---

# 2026-10-07 (UTC): The accessibility tree, matched

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: 8909ec5, working
tree clean, origin/main also at 8909ec5 (below), `.commitmsg/` holding
`1-records-after-report-3.txt` and `2-adr-0009-layout-skipping.txt`, both
left in place as the brief says. HEAD at end: the commit carrying this
log. Mode: mutating. Brief: 5. Previous log: 2026-10-06-before-push.md.

The session ran from about 10:28Z on 2026-10-07. The local date (UTC+5)
was the same throughout.

## What was asked

Brief 5, which is never committed, so its substance is here.

The chat checked Report 4 against the repository on 2026-10-06 UTC: the
five commits and their diff, the site.css comment, the two date
corrections, and the 44-row move by diffstat only. It answered Report 4's
four questions.

- **Q1: option (c).** Keep `content-visibility` on the sections and fix
  what a screen reader meets. ADR-0009 now says a fail on any measuring
  machine is a fail (8909ec5); without the rule this machine fails, so the
  rule is needed. The record keeps it on a condition: in full
  accessibility mode, the tree at load matches the page without the rule,
  at 360 and 1366 px. Accepted residual: a browser that turns
  accessibility on only after load meets the lower sections when they
  render.
- **Q2:** the speech test runs once, after this, on the page that ships.
- **Q3:** the intermittent axe result did not reproduce in the chat's
  harness (0 of 20 at 1366 px, device dark, as loaded). Settled hover on
  the certificate cards is 14.93:1; a reading mid-transition would match
  the failing colours, consistent with Report 4's 2 of 21 but not proven
  as its cause. No change asked; log it as unexplained but bounded.
- **Q4: yes.** Add the tree-at-load check, both modes, both widths, to
  wherever the standing checks are written down. Pass line for full mode:
  the parity criterion. Its defeat case: the page as built at 0403c68.

The chat's measurements, to start from: headless Chromium 141, Playwright,
`--force-renderer-accessibility`, a fresh browser per load, CDP
`getFullAXTree` 1.5 s after load, no scrolling, four loads per cell.

| Build | 360 px: headings, hidden Close buttons, text chars | 1366 px |
|---|---|---|
| As built | 31, 5, 19,973 | 26, 0, 9,164 |
| Without the rule | 26, 0, 8,685 | 26, 0, 8,725 |
| Rule plus aria-hidden on hidden panels | 26, 0, 9,288 | 26, 0, 9,164 |

Left over against the page without the rule, node by node: whitespace-only
nodes; labels without their CSS text-transform; and "No lanes selected.",
exposed with the rule and not without it.

The criterion: at load, in full mode, the tree's text matches the page
without the rule, apart from whitespace and letter case, at both widths.
Check any other element hidden by `hidden` or by CSS inside the sections
the same way. If aria-hidden is used, the seat checks: an open panel
carries no `aria-hidden="false"`; with scripts off, nothing is hidden and
nothing carries the attribute; focus never lands inside an aria-hidden
element. How to get there was left to the seat.

Verification, each check on its defeat case first: build twice
byte-identical; gates; the content trace; the parity check; axe at both
widths and themes, every panel open and all closed; keyboard through
every panel, focus returning; anchors; Lighthouse, median of five, against
ADR-0009, showing a one-attribute change does not move TBT. Commit in a
series, session log, Report 5 in Report 4's form, do not push.

The brief also named three errors of the chat's in Brief 4: one machine's
"roughly 35 ms" written as general; "NVDA will most likely not show this"
measured at 1366 px only; and the content pack's file time overwritten by
the chat's own edit, so Brief 4's upper bound from Brief 3's scratch file
stands.

## Found at the start: the styled site is already live

[VERIFIED] `origin/main` was at 8909ec5, moved by `update by push` at
2026-10-07T10:25:54Z (15:25:54 local) per this clone's reflog, so the push
was made from this clone. `git ls-remote origin` agreed. No session log
records it. The live page, fetched at 10:31:55Z (Last-Modified
10:26:12Z), and its `static/site.js` are byte-identical to 8909ec5's
output (SHA-256 `bd10d0b2...` and `51cd2d92...`).

So Brief 3's and Brief 4's commits replaced the unstyled page before the
screen-reader speech test, whose recorded trigger is "before the styled
site replaces the unstyled one", and before the condition ADR-0009 now
sets on the rule was met. The live page fails that condition (below).
This session's commits are local; it did not push.

## What was done

Commits, each through gates A, B and C: e3af5c2 the fix; d2fca3f the
standing checks; 67ea21b a correction to its axe row, which had named
the WCAG rules where axe runs its default set; then this bookkeeping.
[VERIFIED]

### Measured first

Tools: Chrome 154.0.8037.97 headless, driven by puppeteer-core 25.12.0
(CDP `Accessibility.getFullAXTree`), axe-core 4.14.0, Lighthouse 13.5.0,
the npx cache Brief 4 used. Variants were scratch copies of the built page
served locally without compression, each from its own root. "Without the
rule" is the built page with the rule and its `:has(:target)` undo
removed, the two lines e0e876c removed, and nothing else.

A harness compares two lists from each tree, walked from the root in
order: the non-ignored text nodes, and every other non-ignored node that
has a name, as role and name; whitespace collapsed, empty entries dropped,
lower-cased. It also lists every element inside the sections that is
hidden (the `hidden` attribute, `display: none`, `visibility: hidden`, or
the closed part of a `<details>`) and not under aria-hidden, and any node
of one that the tree holds. The full method is in
`docs/reference/standing-checks.md`.

*Control.* The page without the rule against itself, full mode, both
widths: equal in every load. [VERIFIED]

*The chat's numbers reproduced exactly on this machine.* [VERIFIED] As
built: 31, 5, 19,973 at 360 px and 26, 0, 9,164 at 1366 px. Without the
rule: 26, 0, 8,685 and 26, 0, 8,725. The chat's one line: 26, 0, 9,288 and
26, 0, 9,164.

*What the chat's comparison did not show.* [VERIFIED] The chat compared
text. Names show more. With the chat's line, in full mode at both widths
and in both themes, three differences remain against the page without
the rule, in every load:

- "No lanes selected." (`p.tl-empty`, `hidden` in the HTML itself);
- the contact mark of the other theme, one image of each pair, hidden by
  CSS: the LinkedIn link's name became "LinkedIn LinkedIn Let's connect
  ..." with an extra image named "LinkedIn", and the same for GitHub. The
  alt text is a name, not a text node, so a text comparison misses it.

With scripts off, the page as built also exposed, in full mode (light
theme, two loads per width): the five
"In depth" controls and five Close buttons at 360 px, the lane filter
group and its three buttons at both widths, the empty-lanes line and the
two marks. All are hidden without a script.

*Whitespace and case.* [VERIFIED] Without lower-casing, the only text
differences on the final page are text-transform ones ("RAHZAAN" in the
reference, "Rahzaan" with the rule). Keeping whitespace adds 593
whitespace-only nodes at 360 px and 429 at 1366 px.

*The mechanism, inferred, not tested in Chromium's source.* In a section
that skips its layout, the full tree at load is built from the DOM
without the section's style. It honours `aria-hidden`, `alt=""` and a
closed `<details>` there (the 13 closed timeline cards were never
exposed), but not what `hidden` or CSS hides. Brief 4 inferred that the
panels were exposed because the script hid them after the first style
pass; the empty-lanes line is `hidden` in the HTML from the start and was
exposed too, so that inference was wrong or incomplete.

### The fix

One rule: inside the sections, anything hidden also carries
`aria-hidden="true"`, and the two change together.

- `src/static/site.js`: `setShown(el, shown)` sets `hidden` and adds or
  removes `aria-hidden`; a shown element carries none, never
  `aria-hidden="false"`. Used for the panels (`setDepth`), the
  empty-lanes line (`applyFilters`), and the start-up reveal of controls
  that need a script inside the sections. The rail in the menu keeps its
  permanent aria-hidden: it is decoration, and the reveal only sets
  `hidden` there.
- The Close button moves focus to its control before hiding the panel, so
  focus never rests in an aria-hidden element. Before, it hid first.
- `src/templates/projects.html.j2`, `timeline.html.j2`: every element
  inside a section that ships `hidden` also ships `aria-hidden="true"`:
  the five "In depth" controls, the five Close buttons, the lane filter
  group, the thirteen timeline close buttons and the empty-lanes line. So
  the page without a script matches too.
- `src/templates/contact.html.j2`: both images of each mark pair are
  `alt=""`, and the name is visually hidden text beside them. CSS alone
  picks the image by theme, so no attribute on the hidden one can follow
  the device setting without a script. Each link's name is unchanged;
  what a listener no longer hears is "graphic".
- `src/static/site.css`: the comment above the rule says what is now
  measured, and no more.

### Results

*Parity, full mode, final page against the final page without the rule,
four loads per cell.* [VERIFIED]

| Scripts | Theme | 360 px | 1366 px |
|---|---|---|---|
| On | Light | 4 of 4 match: 26 headings, 0 Close buttons | 4 of 4 match: 26, 0 |
| On | Dark | 4 of 4 match | 4 of 4 match |
| Off | Light | 4 of 4 match: 31 headings, every panel open | 4 of 4 match: 31 |
| Off | Dark | 4 of 4 match | 4 of 4 match |

No hidden element inside the sections is exposed in any load. Text chars
with the rule, 9,284 and 9,160, differ from the reference's 8,699 and
8,739 by whitespace-only nodes alone.

*Default mode, the same cells, four loads each.* [VERIFIED] 1 of 26
headings in the tree at load at 360 px and 8 of 26 at 1366 px, scripts
on; 1 and 13 of 31, scripts off. No node the reference lacks, in any of
the 32 loads: the residual ADR-0009 accepts, and nothing more. The 8 at
1366 px differs from Brief 4's 1: this harness reads the tree 1.5 s after
load, Brief 4's straight after it. Not investigated further.

*The change seen on the page without the rule.* [VERIFIED] Before and
after this change, without the rule, full mode, both widths, both themes,
scripts on and off: the only differences are the two image nodes leaving
and their names arriving as text. No link's name changed.

### Verification

Each check was first run against a case built to defeat it, in scratch
copies, never in the repository.

| Check | Defeated by | Result |
|---|---|---|
| Build twice | The same build as of 2026-11: hashes differ | Three builds at 2026-10 identical, hashed over every generated file |
| Gates | (gate proofs: Brief 2) | Passed on every commit |
| Content trace | 592 made 593 in a scratch copy of the page: exit 1, the summary 0 of 1 | Exit 0; 394 blocks traced, 0 not; coverage whole. Brief 4 had 396: four alt blocks became two text blocks |
| Tree at load, full mode | The page as built at 0403c68: differs in all 32 loads (2 widths, 2 themes, 2 modes, 4 loads) | Matches in all 32 full-mode loads, scripts on and off |
| Tree at load, default mode | A paragraph planted in the Intro: 1 added node at each width | No added node in 32 loads |
| Keyboard, all five panels, 360 and 1366 px, full mode | Close hiding the panel before moving focus: aria-hidden set on the panel holding focus, every panel, both widths. For the walk, the contact links marked aria-hidden: 3 stops inside it at each width | 60 of 60: Tab reaches each control; Enter opens it with no aria-hidden attribute and its heading enters the tree; Tab moves in and on to Close; Close closes it, focus returns, the heading leaves the tree; the control opens and closes it again; a second panel closes the first; the empty-lanes line enters the tree only with every lane off; a Tab walk to the footer (46 stops at 360 px, 53 at 1366) never stops inside aria-hidden; aria-hidden never set on an element holding focus |
| axe-core 4.14.0, its default rules | Faint text and an image without alt: a violation in all 12 cells | 0 in all 12: 1366 and 360 px; light, dark by the device, dark by the switch after 3 s; as loaded, and every panel and card open as the script opens them |
| Anchors, 22 targets by link and by hash, scripts on and off | The rule without its `:has(:target)` undo: 76 of 132 landed | 132 of 132 |
| Lighthouse, default mobile, median of five, interleaved | A 600 ms script in the head: TBT median 1848 ms (1870, 1848, 1764, 1860, 1751), fails | Final: TBT median 25 ms (50, 25, 21, 21, 35), LCP 2104 ms, CLS 0: meets. The page as built at 8909ec5, same set: 56 ms (132, 56, 45, 35, 57). The change does not raise TBT |

*Lighthouse, the set before.* [VERIFIED] A first interleaved set was cut
short in its fifth round, when the scratch server reached its background
time limit and was stopped; that round failed on an error page. Its four
whole rounds: as built 225, 27, 33, 35 (and 24 in round 5); final 175,
25, 28, 32. Both sets ran with the operator's Chrome open on this
machine (30 `chrome.exe` processes counted, a handful of them
Lighthouse's), as in Brief 4's set 3. Bytes, uncompressed: 224,375 as
built, 226,149 final.

*On the committed bytes.* [VERIFIED] The parity, keyboard, axe and anchor
runs used a scratch copy made before the site.css comment was rewritten.
The full-mode parity was repeated on the committed bytes, one load per
cell, against a reference made from them: 8 of 8 cells match. Lighthouse
ran on the committed bytes.

Chrome's console warning for aria-hidden on a focused element's ancestor
was also collected. It stayed silent in the defeat case, so it is not
counted as evidence; the setAttribute wrapper is.

*The intermittent axe cell.* [VERIFIED] 1366 px, device dark, as loaded,
20 fresh contexts per batch: the page as built 1 of 20; the final page 1
of 20, then 0 of 20. Each failure was the first run after a new browser
process started, with 22 contrast failures on the certificate cards; on
the page as built, where the colours were printed, ratio 1.64, #a6afd7 on
#c6f135. The chat's 0 of 20 and Brief 4's 2 of 21 stand beside these.
Unexplained, bounded: it appears with and without this change, never
after the first load of a browser here; Brief 4 never caught it on a
screenshot, and this session took none.

## Rejected alternatives

- **The chat's one line alone.** Measured as this session's rendition
  of it, the attribute set from `!open` after `panel.hidden = !open;`: it
  restores the heading and button counts but leaves the empty-lanes line
  and the two marks exposed.
- **Marking the hidden mark by script on each theme change.** It fails
  with scripts off and must track the device setting and the switch;
  `alt=""` with text needs neither.
- **Creating "No lanes selected." from the script.** It removes interface
  text from the HTML to fix one attribute's worth of problem.
- **`hidden="until-found"` or `inert` on the panels.** Neither was
  measured in this tree; `hidden="until-found"` also changes what
  find-in-page does. aria-hidden was measured by the chat and is read
  from the DOM.
- **Making default mode match too**, by laying the sections out at load.
  That is the cost the rule exists to avoid, and ADR-0009 accepts the
  residual.
- **A browser check committed in `tools/`.** It needs a browser driver,
  a second dependency (scope floor line 14, ADR-0006). The method is
  written down instead.

## Checked and found already correct

- A fresh build at the recorded month, 2026-10, matched the committed
  output before any change.
- `pip list --not-required` shows Jinja2 and pip only.
- 8909ec5 touches ADR-0009 only, as the brief says; 0403c68 and 8909ec5
  build the same page.
- The chat's three rows of numbers, reproduced exactly.
- The 13 closed timeline cards are not exposed at load in full mode, with
  or without the rule.

## Not done

- **Push.** Not asked; the speech test comes first.
- **The screen-reader speech test.** The operator's, with NVDA, on the
  page this session commits, served locally.
- **ADR-0009's Changes row** recording the condition met. The chat's.
- **Find-in-page** with the rule: not tested.
- **Any browser but Chrome.** The parity holds in headless Chrome 154;
  Firefox, Safari with VoiceOver and NVDA's own reading are not measured.
- **The cause of the intermittent axe cell.** Counted, not explained.

## Findings and recommendations

1. **The styled site went live before its speech test**, from this
   clone at 10:25:54Z, not by an implementing seat. Until Brief 5 is
   pushed, the live page exposes to a screen reader at load the five
   collapsed panels at 360 px, and at both widths the empty-lanes line
   and doubled contact names.
   Recommendation: the operator runs the speech test on this session's
   commits served locally, and pushes them after it.
2. **The parity criterion needs names, not only text.** The doubled
   contact names passed the brief's text-only criterion. The standing
   check compares names too. Recommendation: the chat's harness does the
   same.
3. **Scripts off is a case of its own.** The brief expected that with
   scripts off nothing is hidden. The controls that need a script are,
   and they were exposed; they now carry aria-hidden beside `hidden` in
   the HTML. No visible element gained the attribute.
4. **The contact marks changed from named images to decorative images
   with a text name.** Names are unchanged; the "graphic" role is gone.
   ADR-0011 does not cover alt text. Recommendation: the chat confirms.

## Noticed and not investigated

- Why default mode at 1366 px gives 8 headings here and 1 in Brief 4's
  harness; the reading time differs.
- Brief 4's open question, which extra heading stayed after opening and
  closing one panel with the rule (31 became 27): not re-examined; the
  keyboard check now finds each panel's heading out of the tree after it
  closes.

## Round 2: after the push

From about 11:50Z. The operator reported that everything was pushed,
said that launching Chrome directly opens its profile picker (he has
several profiles), asked for the NVDA test's steps, asked about Edge and
whether GitHub needs any setting, and asked this seat to do all work not
waiting on him or the chat, with full steps for what does.

**The push.** [VERIFIED] origin/main is at 6812c4f, moved by a push from
this clone at 2026-10-07T11:41:22Z. All 14 live files (the page and
`static/`) are byte-identical to the committed output; Last-Modified
11:41:39Z. GitHub Pages serves them gzip-compressed.

**GitHub settings.** [VERIFIED] Nothing to set. The repository is public,
`has_pages` is true, its default branch is main, and the live site took
the pushed commit's exact bytes 17 seconds after the push. The Pages
settings endpoint itself needs a login and was not read.

**Edge.** Microsoft Edge 154.0.4258.62, headless, through the same
harnesses with only the executable changed. [VERIFIED]

- The page as built at 0403c68, served locally: the same defect as in
  Chrome, to the number (31 headings and 5 Close buttons at 360 px; the
  empty-lanes line and the marks at both widths; the controls without a
  script). So Edge needed the fix as much as Chrome.
- The live site, against the committed bytes without the rule served
  locally, both widths, both themes, scripts on and off, two loads per
  cell: full mode matches in 16 of 16 loads; default mode adds no node in
  16 of 16.
- Keyboard and focus on the live site: 60 of 60. The Tab-walk defeat
  (contact links marked aria-hidden) fails at both widths.
- axe on the live site: 0 in all 12 cells. The planted defeat is flagged
  in all 12.

**Chrome on the live site.** [VERIFIED] The same parity run: full mode 16
of 16 match, default mode no added node in 16.

**Lighthouse on the live site**, Chrome 154, default mobile. [VERIFIED]

| Set | Live, compressed | Same bytes, local, uncompressed |
|---|---|---|
| 1 | TBT 138, 102, 139, 208, 21: median 138 ms; LCP median 1721 ms; CLS 0; 113,387 bytes | not run |
| 2, interleaved | TBT 144, 95, 117, 87, 44: median 95 ms; LCP median 1739 ms; CLS 0 | TBT 144, 6, 41, 165, 22: median 41 ms; LCP median 2107 ms |

Both medians meet ADR-0009. The live page blocks longer than the same
bytes served locally and paints sooner; one live run of ten reached
208 ms. Why is not known and was not investigated. 24 `chrome.exe`
processes were running during set 2, the operator's browser among them.

**`.commitmsg/`.** Both files were compared with their commits' messages,
35d54dd and 8909ec5, found identical, both commits on origin, and then
deleted with the folder, as CLAUDE.md's chat-commit procedure says once
they are pushed. Brief 5 had kept them "until the push".

**The deferred speech test.** `docs/deferred/screen-reader-speech-test.md`:

- its "What has been run" section records this session's browser half;
- a dated annotation records that its trigger passed unmet;
- its reference to ADR-0005's Changes table is corrected to ADR-0010,
  which superseded ADR-0005 and carries the test in its Confirmation;
- steps for this page are added below the unchanged method.

**Memory.** Two notes saved outside the repository for later sessions: do
not launch the operator's visible Chrome, and give full steps for
anything only he can do.

**Waiting.** The NVDA test, on the operator. Report 5's check, ADR-0009's
Changes row and the contact marks' alt text, on the chat.
