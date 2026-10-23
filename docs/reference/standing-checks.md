---
type: reference
description: "The checks every change to the built page runs before it is committed, each with its pass line and the case built to defeat it. Includes the accessibility tree at load that ADR-0009 makes a condition of layout skipping, words a screen reader hears run together, a layout check for overlaps and stranded items, and a pixel check for changes meant to be invisible."
status: current
---

# Standing checks

Created 2026-10-07 by the Brief 5 session, because Brief 5 asked for the
tree-at-load check to be added "to wherever the standing checks are
written down" and they were written down nowhere but in briefs, which are
never committed, and in session logs. The list is the verification list of
Brief 5. Brief 3's ten checks, some not repeated every round, are in
`logs/2026-10-05-styled-site.md`.

Every check runs first on its defeat case, and a pass counts only once
that case has failed. A check whose defeat case passes is reported as
unproven, not as passed.

## Where the harnesses live

Only the build, the gates, the map and the content trace are commands in
this repository (`docs/reference/commands.md`). The browser checks drive Chrome
through puppeteer-core, Lighthouse and axe-core, which are not dependencies
of this repository and cannot become one without a record (scope floor
line 14, ADR-0006). Their scripts live in the session's scratch space and
are described here closely enough to rebuild. Each session log names the
versions it ran.

Variants are scratch copies of the built `index.html` and `static/`,
served locally without compression, each from its own root so the
root-relative paths resolve. "Without the rule" means the built page with
these two lines removed from `static/site.css`, and nothing else:

```
.page > .sec { content-visibility: auto; contain-intrinsic-size: auto 1400px; }
html:has(:target) .page > .sec { content-visibility: visible; }
```

## The checks

| Check | Pass line | Defeat case |
|---|---|---|
| Build twice | Every generated file byte-identical across builds at the recorded month | A build as of another month: hashes differ |
| Gates | Every commit passes A, B and C; a push passes E (ADR-0007) | The proofs in `logs/2026-09-26-gates-map-and-as-of.md` |
| Content trace | `tools/check_content.py` exits 0: every block traces to the master, and every master bullet, sentence, skills line, course, certificate and project link, the Portfolio Intro and the Portfolio Footer with its address as a link, is on the page | One number changed in a scratch copy of the page, 592 to 593: exit 1. For the project links: a master copy with a wrong address, and a page copy missing a link: exit 1, the link named |
| Accessibility tree at load, full mode | Matches the page without the rule (below), in every load | The page as built at 0403c68. It differs from its reference in all four cells, 360 and 1366 px, light and dark (2026-10-21; the first audit's F18 asked, since a defeat it built fired at 360 px only) |
| Accessibility tree at load, default mode | Holds no node the page without the rule lacks | A paragraph planted in the Intro that the reference lacks |
| Keyboard | Every "In depth" panel: Tab reaches its control; Enter opens it and its text enters the tree; Tab moves into it; Close closes it and focus returns to the control; the control closes it too. A Tab walk to the footer never stops inside `aria-hidden`, and `aria-hidden="true"` is never set on an element holding focus | The Close handler hiding the panel before moving focus; for the walk, the contact links marked `aria-hidden` |
| axe-core, its default rules, which include the WCAG 2.x A and AA ones | 0 violations at 1366 and 360 px; light, dark by the device, dark by the switch (read 3 s after it, once the colours have settled); as loaded, and with every panel and timeline card open, each opened as the script opens it | Faint text and an image without alt planted in the page |
| Contrast, measured | `contrastcheck.js`: every visible text element's colour, its alpha and its ancestors' opacity applied, against the nearest solid background behind it, meets WCAG 2 AA (4.5:1; 3:1 at 24 px or 18.66 px bold), light and dark, at 360 and 1366 px. Added 2026-10-21 because axe leaves most of this page's contrast as "needs review" (the first audit, F8). Text over a gradient, or in a bar that floats over the page, has no single background and is counted as unmeasured, not passed: 17 elements at 360 px and 94 at 1366 px on 2026-10-21, most of them the dark Intro's | A `#c8c8c8` span planted in the Skills heading: 1.48:1 in light theme, at both widths |
| Anchors | Every in-page target, by a link and by a URL with its hash, scripts on and off, at 1366 and 360 px, lands within 3 px of its scroll margin or at the page's end | The rule without its `:has(:target)` undo |
| Words run together for a screen reader | No join at 360 and 1366 px, in Chrome and Edge, by the model of NVDA's lines below | The page at 6812c4f: 58 joins at 1366 px, 45 at 360 px |
| Visually unchanged, for a change meant to be invisible | Full-page screenshots under reduced motion at 360 and 1366 px, light and dark, with every section made to render first (`.page > .sec { content-visibility: visible }` added for the capture: a full-page capture paints only near the viewport, and a skipped section comes out blank in both images alike): same size, and no pixel differs by more than 2 of 255 in any channel, the noise two captures of one unchanged page show | A visible change in a lower section that keeps the page's height, such as the timeline fix of 7e97c5b: about 10,500 pixels change inside the timeline |
| Layout | `layoutcheck.js`, below: at 320, 360, 375, 390, 414, 768, 1024, 1040, 1060, 1065, 1100, 1180, 1366 and 1920 px, scripts on and off, no finding outside its named list of deliberate cases | The page before Brief 13's fix (78f13ce's parent), with the "In depth" button stranded on its own row (W1); a copy with the probes card moved up over "592"; a copy with the timeline to scale from 960 px and its cards at a fixed height, which cuts off one-month cards' titles |
| Words broken mid-word | `wordbreak.js`: no word of a timeline card's title, organisation or dates falls on two lines, at 1060 to 1920 px, read from each word's own range | The timeline to scale from 960 px, at 980 px: "Specialization" and "Professional" each split across two lines |
| The reading marker | `chipcheck.js`: with motion on, at 1065, 1180, 1366 and 1521 px, the reading line moved onto each year badge and every fifth month label; with the marker shown, that label is faded | The build before the fix (fd73058): 10 of 10 labels still visible under the marker at each width |
| Lighthouse | Default mobile, median of five, meets ADR-0009: LCP at most 2.5 s, CLS at most 0.1, TBT under 200 ms. Variants run interleaved so drift falls on all alike. A set counts only with the machine at light or medium load, read over the 60 s before it; a fail there is a fail, a set at heavy load is void (ADR-0009 Changes, 2026-10-06 and 2026-10-20) | A 600 ms synchronous script at the end of the head, after the stylesheets: it fails by TBT (medians about 1,850 ms, 2026-10-19 to 21), so it shows the TBT check able to fail. A script at the top of the head delays first paint instead and fails by LCP, leaving TBT untested (the first audit's variant, F19) |

## The accessibility tree at load

ADR-0009 keeps `content-visibility` on the sections on one condition: in
full accessibility mode, the tree at load matches the page without the
rule, at 360 and 1366 px. This is how that is checked.

**Setup.** Headless Chrome, a fresh browser for every load. Viewport
360 by 780 and 1366 by 900, device scale 1. Light and dark by the device
setting. Scripts on and scripts off. Full mode is the browser launched
with `--force-renderer-accessibility`, as a screen reader would switch it
on; default mode is without it. The tree is CDP
`Accessibility.getFullAXTree`, read 1.5 s after the load event, with no
scrolling. Four loads per cell.

**Compared.** From each tree, walked from the root in order, two lists of
non-ignored nodes: the text nodes' text, and every other node that has a
name, as role and name. Each entry has its whitespace collapsed, is
dropped if then empty, and is lower-cased, because a section not yet laid
out exposes whitespace-only text and does not apply `text-transform`.
The two lists are compared entry by entry with the same lists from the
page without the rule, loaded in the same cell.

**Pass, full mode.** Both lists equal the reference's, in every load.

**Pass, default mode.** No entry the reference lacks. Entries the
reference has and the page lacks are expected: a browser that turns
accessibility on only after load meets the lower sections when they
render, the residual ADR-0009 accepts.

**Also listed.** Every element inside the sections that is hidden, by the
`hidden` attribute, by `display: none` or `visibility: hidden`, or as the
closed part of a `<details>`, and not under `aria-hidden`; and any node of
one that the tree holds. A text comparison alone misses an exposed image,
whose alt text is a name, not a text node.

**Why it can fail.** In a section that skips its layout, Chromium's full
tree at load is built from the DOM without the section's style. It reads
`aria-hidden`, `alt` and the `open` state of a `<details>` there, but not
what `hidden` or CSS hides. So anything hidden inside a section must also
carry `aria-hidden`; `setShown` in `static/site.js` keeps the two
together. Mechanism inferred from the measurements in
`logs/2026-10-07-tree-parity.md`, not from Chromium's source.

## The layout check

Added 2026-10-21 (Brief 13), after Waqas found a fault the first audit's
eye-read visual pass had on screen and did not report: the "In depth"
button stranded on a row of its own when a card's links wrapped (W1).

**What it measures.** A geometric scan of the page, every section laid
out first, light theme, reduced motion, at fourteen widths, with scripts
on and off; 1040, 1060, 1065 and 1100 px since 2026-10-22, around the
width where the timeline turns to scale. Five kinds of finding:
- **overlap**: the ink of a line of text intersected by another line's
  ink, or by a painted box (a background or a border) it is not inside.
  Ink, not the font's box: each text box is tightened to the letters'
  measured ascent and descent around the baseline, because at display
  sizes the font's box reaches far past the letters, and a check on it
  reports overlaps nobody can see;
- **orphan**: a flex item pushed right by `margin-left: auto` that has
  wrapped onto a row of its own, the pattern of W1;
- **clipped**: text cut off by an element that hides its overflow;
- **cut off**: a line's ink reaching past the box of the nearest ancestor
  that clips its overflow, at any edge. Added 2026-10-22, when a one-month
  timeline card cut its title's third line at 1065 px, which the sideways
  test above could not see;
- **wide**: anything past the viewport's right edge that nothing clips,
  and a page that scrolls sideways.

Skipped: `aria-hidden` decoration, the fixed or sticky menu, the 3D
canvas, and screen-reader-only text (`.vh`, or a box 1 px wide; an
element with `display: contents` has no box and is not skipped).

**The named list of deliberate cases**, each matched by kind and
element, never by width: the name's two lines, a tight lockup in the
approved design (ADR-0011); text over the timeline's month and year
bands, painted behind its entries; the Intro clipping the 3D knot; the
desktop timeline's 1 px lane labels. Anything else fails. A new case is
added to the list only with its reason, in this file.

**What it cannot see.** Taste: spacing, alignment and balance are not
geometry. A screenshot read by a person remains the test for those.

## Words run together for a screen reader

Added 2026-10-07. NVDA's browse mode reads a line as the text pieces of
the accessibility tree joined end to end. A space between two pieces that
the page lays out as separate boxes (flex or grid items, or blocks) is
never rendered, so it is not in the tree, and NVDA reads "WaqasSharif" or
"Dec 20255-Day". The fix is `m.sp()` in `src/templates/macros.html.j2`.

**The model.** Every section laid out first. The text pieces are the
non-ignored text nodes of Chrome's full tree, in order. A line breaks at
the start and end of any non-ignored node whose element's computed display
is not inline; ignored nodes, such as plain spans, never break a line.
Within a line pieces are joined with nothing between them. A join is two
touching pieces, neither with a space at the touching end, where the DOM
between them holds whitespace, read with a Range in the page.

**Validated, not proven.** Against the operator's Speech Viewer capture
of 2026-10-07 in NVDA at desktop width, the model reproduced 94 of 94
sampled lines, every join among them, and no join he did not hear. It is
a model of one NVDA version at one width; NVDA itself remains the test.
`logs/2026-10-07-tree-parity.md`, round 3.

**Lighthouse and page size.** A change that adds bytes moves Lighthouse's
simulated paint time in steps, by size alone: on 2026-10-07, 1.4 kB more
HTML served uncompressed raised the LCP median by 150 ms, and the same
bytes added as a comment did the same; served gzip-compressed, as GitHub
Pages serves it, LCP did not move. Measure size-sensitive changes
compressed as well.
