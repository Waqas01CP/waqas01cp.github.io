---
type: deferred
description: Hearing a real screen reader announce a collapsed and an expanded disclosure. Deferred 2026-10-02 to the styled site, because styling can change what is exposed. Trigger and method inside.
status: open
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

## What is deferred, and why

What a real screen reader actually says. The accessibility tree is the input
to that speech, so the remaining risk is in the last step only. The design
work will restyle these controls, and styling can change what a browser
exposes, so a speech test on the unstyled page would have to be repeated.
It is run once, on the styled site.

## Trigger

**Before the styled site replaces the unstyled one.** The deploy that
introduces the design does not go live until this has passed.

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

Record the Speech Viewer text and the result in ADR-0005's Changes table
and close this entry.
