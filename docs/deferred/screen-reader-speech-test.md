---
type: deferred
description: Hearing a real screen reader announce a collapsed and an expanded disclosure. Deferred 2026-10-02 to the styled site. Passed 2026-10-07 in NVDA 2026.2 on the live styled site, Chrome; closed. Method and record inside.
status: closed
---

# Screen reader speech test of the disclosures

**Deferred 2026-10-02, by the operator's decision.** ADR-0005's
Confirmation asks for a collapsed disclosure to be opened with a screen
reader and its content confirmed reachable and announced. Half of that has
been run; the half that needs a real screen reader's speech is deferred here.

## What has been run

2026-10-02, by the architecture chat, against the live `index.html` at
`9971416`, in headless Chromium driven by keyboard only, reading Chromium's
accessibility tree, which is what a screen reader reads from:

- The summary is exposed as a disclosure control, named by its text, with
  its collapsed state reported.
- Tab reaches it. Enter expands it, and the layer 3 text enters the
  accessibility tree. Space collapses it again.
- Collapsed, the layer 3 text is absent from the tree and present in the
  HTML source, which is the intended behaviour.

2026-10-07, by the Brief 5 implementing session, against the live page at
6812c4f, in headless Chrome 154 and Edge 154 in full accessibility mode,
at 360 and 1366 px: at load, no collapsed "In depth" panel is in the tree,
and the tree matches the page without layout skipping, as ADR-0009's
condition requires; by keyboard, each control is named for its item,
Enter opens it and its text enters the tree, Close returns focus to it.
logs/2026-10-07-tree-parity.md.

2026-10-07, by the operator, in NVDA 2026.2 with its laptop keyboard layout, on
the live page at 6812c4f, reported as passing: at load, the Elements
list's headings held none beginning "In depth", at normal zoom and at
300%; the LinkedIn and GitHub contact links read their names once. Not
yet run: steps 3 and 4 of the method (each control's spoken state, Enter,
reading on into the panel); the laptop has no Home key. His Speech Viewer
capture showed words run together wherever pieces of one line are laid
out as separate boxes, such as "WaqasSharif" and "Nov to Dec 20255-Day";
fixed in c97b99e, round 3 of the same log.

**Passed, 2026-10-07**, by the operator, in NVDA 2026.2 (2026.2.0.57664)
with its laptop layout, in Chrome, on the live page at eaee932, which
carries c97b99e (deployed 15:40Z). Reported heard: each "In depth"
control spoken with its item's name and collapsed state; Enter spoken as
expanded, reading continuing into the panel; Close returning to the
control, spoken collapsed; all five controls; a Say All read with no
words run together. The text he sent reads the Rahzaan panel once
opened and none of the four closed ones, names each of the five
controls differently, and matches a model of NVDA's lines on 45 of 45
sampled lines, with no joined words. It holds no role or state words, so
the spoken states rest on his report of what he heard; asked, he
confirmed hearing "collapsed" and "expanded". He declined a run in
Edge, which the method does not ask for. Method step 5,
no two disclosures sharing a name, was met by hearing each control
named for its item; the Elements list was opened for headings and links,
not buttons. logs/2026-10-07-tree-parity.md, round 5.

## What is deferred, and why

What a real screen reader actually says. The accessibility tree is the input
to that speech, so the remaining risk is in the last step only. The design
work will restyle these controls, and styling can change what a browser
exposes, so a speech test on the unstyled page would have to be repeated.
It is run once, on the styled site.

## Trigger

**Before the styled site replaces the unstyled one.** The deploy that
introduces the design does not go live until this has passed.

Annotation, 2026-10-07, Brief 5 session: the styled site replaced the
unstyled one at 10:25:54Z on 2026-10-07, before this had run (origin's
reflog; logs/2026-10-07-tree-parity.md). Brief 5 rules that the test runs
once, on the page that ships, after its fix, which went live at
11:41:22Z.

## Method

NVDA, free from NV Access, runs on 64-bit Windows 10 and 11 (nvaccess.org,
read 2026-10-02). Its Speech Viewer, under Tools, shows every spoken
phrase as text, so the result can be captured and recorded.

1. Open the styled build in Chrome and start NVDA.
2. Open Speech Viewer.
3. Tab to each item's disclosure. Pass: the item's own name is spoken, with
   its collapsed state.
4. Press Enter. Pass: the expanded state is spoken and reading continues
   into the layer 3 text.
5. List the page's controls with NVDA's elements list. Pass: no two
   disclosures share a name.

Record the Speech Viewer text and the result in ADR-0010's Changes table
and close this entry. Closed 2026-10-07 on the result above; its ADR-0010
Changes row is the architecture chat's to write (drafted in Report 5). (Reference corrected 2026-10-07 from ADR-0005,
which ADR-0010 superseded on 2026-10-03 and whose Confirmation carries
this test.)

## Steps on the styled site

Added 2026-10-07 by the Brief 5 session. They carry out the method above
on this page, and add one check at load: ADR-0009 keeps layout skipping on
condition that a screen reader at load meets the same page as without it.

1. Start NVDA first, then open the browser, so the browser has its
   accessibility on from the first load. Open Speech Viewer. NVDA should
   be heard as you move; if it is silent, check the Windows volume and
   press NVDA+S until it reports speech mode talk. Copy the record from
   the Speech Viewer window, not from the page: the page's own text has
   no roles or states.
2. Open `https://waqas01cp.github.io/` and reload with Ctrl+F5. Do not
   scroll. Wait three seconds.
3. At load: NVDA+F7, Headings. Pass: no heading begins "In depth".
   Links: the LinkedIn and GitHub links each say their name once.
4. Steps 3 to 5 of the method, for each of the five "In depth" controls.
   To start from the top without a Home key, reload with Ctrl+F5; or press
   B, which in browse mode moves to the next button. After Enter, press
   Down Arrow: reading continues into the panel, starting with its "In
   depth" heading. Press B to reach its Close button and press Enter.
   Pass: focus returns and the control is spoken as collapsed. Keep the
   mouse pointer still: NVDA also reads whatever is under it.
5. Zoom to 300% with Ctrl and Plus, reload with Ctrl+F5, and repeat step
   3. This gives the phone layout, where the panels were once exposed.
   Ctrl+0 restores the zoom.
6. Reading: reload with Ctrl+F5 and start Say All (NVDA+Down Arrow on
   the desktop layout, NVDA+A on the laptop layout); Ctrl stops it. Pass:
   no words run together, for example "Waqas Sharif", "592 automated
   tests" and "Nov to Dec 2025 5-Day AI Agents Intensive".
7. Repeat in Microsoft Edge.
