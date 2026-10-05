---
status: accepted
topic: design
description: The site's visual system as settled from the Claude Design prototype: typefaces, colour, theme behaviour, the one 3D element and the motion rules, each tied to the goals it must meet. Read before styling any template.
date: 2026-10-06
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0011: The visual system

## Context and Problem Statement

`docs/design/DESIGN.md` set goals and six hard limits and left the look
open. Claude Design built a full prototype from it, the operator's six
reference sites and the content pack, and the operator reviewed it on
2026-10-05 and 2026-10-06. The look now has to be fixed in one place before
the generator is styled, or the build will re-decide it.

Two tensions shape it. The operator wants a polished, current site with
depth and motion; ADR-0009 holds every heavy element to measured speed
goals. And a dark, dramatic opening reads well, while readers who set their
device to light or dark for comfort expect the page to respect it.

## Decision Drivers

- `docs/design/DESIGN.md`: goals, six hard limits, 3D as depth in the
  interface.
- ADR-0009: Core Web Vitals goals; heavy elements added one at a time.
- ADR-0004 lines 7 to 10: content as real text, reduced motion, nothing
  loaded from other sites, no cookies.
- The operator's choices on the prototype, 2026-10-05 and 2026-10-06.

## Assumptions

- A1. The three typefaces are free to self-host. **Sourced**: the prototype
  ships them from its own fonts folder; Manrope, Instrument Serif and
  JetBrains Mono are published under the SIL Open Font License. **Not
  re-verified by the chat**; the build brief checks each licence file.
- A2. The prototype's colours pass WCAG AA. **Measured** 2026-10-06 by an
  automated accessibility check (axe-core 4) on the rendered prototype in
  light and dark at 1366 and 360 px: no contrast violations.
- A3. The 3D knot's cost on a phone is unknown. **Not measured**: the
  prototype renders through a design framework, so its Lighthouse figures
  (LCP 3.6 to 3.8 s, TBT 296 to 413 ms, three runs, 2026-10-06) measure
  the framework, not the knot. The build measures it per ADR-0009.

## Considered Options

- The prototype's system as reviewed, with the operator's changes
- The earlier design-system draft (Source Serif 4, teal accent)

## Decision Outcome

Chosen option: "The prototype's system as reviewed, with the operator's
changes".

We will set prose and interface text in Manrope, large display words in
Instrument Serif, and dates, figures and labels in JetBrains Mono, all
served from the site's own files as Latin subsets.
We will use one bright lime accent, with a darker olive wherever accent
text sits on the light page, and tell lanes, states and the active section
apart by shape, label and weight as well as colour.
We will open on a dark first screen and let the rest of the page follow the
device's light or dark setting; the switch overrides it for the visit only,
and nothing is stored on the visitor's device.
We will allow one decorative 3D element, a wireframe torus knot drawn on a
canvas with no library, started after the content is visible, paused when
off screen, and still under reduced motion; it stays only if the built page
meets ADR-0009 with it.
We will treat card tilt, the moving availability strip and scroll effects
the same way: each works by touch as well as hover, stops under reduced
motion, and stays only if the goals still hold with it.
We will give the degree's name the visual weight in Education; the CGPA is
shown at the size of the other facts, not as a display figure.

### Consequences

- Positive: the build has one reference for the look, and the prototype is
  no longer needed once the styled site is live.
- Positive: every heavy element has a named test it must pass.
- Negative: three web fonts cost bytes on first load; the build measures
  them.
- Negative: the knot and the strip are motion on a reading page; reduced
  motion and the pause control are the safeguards.
- Neutral: the earlier design-system draft in `docs/design/system/` is
  superseded in practice and kept as history.

### Confirmation

- The built page uses only the three typefaces, loaded from the site.
- axe-core reports no contrast violation in either theme at 1366 and
  360 px.
- With the device set to dark, the page below the opening is dark; after
  using the switch and reloading, the device setting applies again, and
  browser storage and cookies are empty.
- Under reduced motion, no animation frame is requested in three seconds.
- Lighthouse, default mobile, median of five, with and without each heavy
  element, recorded per ADR-0009.

## Pros and Cons of the Options

### The prototype's system

- Good: chosen by the operator from the real content; meets the brief's
  limits as measured.
- Bad: heavier than the draft; its speed is still to be measured on the
  build.

### The earlier design-system draft

- Good: lighter, already measured on a specimen page.
- Bad: the operator found it basic and restrictive.

## More Information

- Implements the goals of `docs/design/DESIGN.md` and the phone timeline of
  ADR-0003's Changes row of 2026-10-05.
- The prototype export is kept locally in `docs/design/prototype/`,
  gitignored, as the build's visual reference; the operator decided on
  2026-10-06 not to keep it in history.
- Revisit if the built page fails ADR-0009 with the knot or the fonts.

## Changes

| Date | Change | Why |
|---|---|---|
