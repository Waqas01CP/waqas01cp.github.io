---
type: reference
description: The checks every change to the built page runs before it is committed, each with its pass line and the case built to defeat it. Includes the accessibility tree at load, in both modes, that ADR-0009 makes a condition of layout skipping.
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
this repository (CLAUDE.md, Commands). The browser checks drive Chrome
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
| Content trace | `tools/check_content.py` exits 0 | One number changed in a scratch copy of the page, 592 to 593: exit 1 |
| Accessibility tree at load, full mode | Matches the page without the rule (below), in every load | The page as built at 0403c68 |
| Accessibility tree at load, default mode | Holds no node the page without the rule lacks | A paragraph planted in the Intro that the reference lacks |
| Keyboard | Every "In depth" panel: Tab reaches its control; Enter opens it and its text enters the tree; Tab moves into it; Close closes it and focus returns to the control; the control closes it too. A Tab walk to the footer never stops inside `aria-hidden`, and `aria-hidden="true"` is never set on an element holding focus | The Close handler hiding the panel before moving focus; for the walk, the contact links marked `aria-hidden` |
| axe-core, WCAG 2.x A and AA rules | 0 violations at 1366 and 360 px; light, dark by the device, dark by the switch (read 3 s after it, once the colours have settled); as loaded, and with every panel and timeline card open, each opened as the script opens it | Faint text and an image without alt planted in the page |
| Anchors | Every in-page target, by a link and by a URL with its hash, scripts on and off, at 1366 and 360 px, lands within 3 px of its scroll margin or at the page's end | The rule without its `:has(:target)` undo |
| Lighthouse | Default mobile, median of five, meets ADR-0009: LCP at most 2.5 s, CLS at most 0.1, TBT under 200 ms. Variants run interleaved so drift falls on all alike. A fail on any machine is a fail (ADR-0009 Changes, 2026-10-06) | A 600 ms synchronous script in the head |

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
