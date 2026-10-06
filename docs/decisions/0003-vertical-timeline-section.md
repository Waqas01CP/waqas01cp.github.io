---
status: accepted
topic: structure
description: A dedicated vertical timeline section, hand-built in CSS Grid, four lanes plus a degree band, fixed month scale, no zoom or drag. Reverses one clause of ADR-0001. Read before building the timeline.
date: 2026-09-23
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0003: A hand-built vertical timeline section

## Context and Problem Statement

ADR-0001 ruled out a timeline because the material looked wrong for one:
the dated items were few, crowded into a single year, and uneven in length.
The operator reopened the question on 2026-09-23, asking for a dedicated
timeline section with a vertical spine, lanes either side, lane headers that
travel down the page, and enough space per month that overlaps stay legible.

Two things changed the material itself. The degree gained a start date of
Sep 2022, and three of the four certificate dates in the master CV were
found to be wrong by one to two years. Corrected, the certificates are
spans rather than undated points, and Sep to Dec 2025 holds five or six
concurrent items where it previously appeared to hold two. The concurrency
a timeline exists to show is now present in the data.

The remaining question is how to render it. The operator asked whether
vis-timeline could be used, either directly or rotated ninety degrees into a
vertical axis.

## Decision Drivers

- The operator's stated design: vertical spine, lanes either side, lane
  headers travelling down the page, collapse controls, a fixed number of
  layout units per month. Stated 2026-09-23.
- Research 0001: the major AI crawlers execute no JavaScript, so anything
  that must be read has to exist in the initial HTML.
- W3C WAI, Complex Images: a complex graphic requires a text equivalent.
- The standing free-by-default constraint, which makes a dependency a cost
  to justify rather than a default.

## Assumptions

- A1. The corrected certificate dates are accurate. **Stated** by the
  operator 2026-09-23, who says he read them from the credential pages
  before supplying them. Not independently verified here: Coursera
  disallows automated fetching of its accomplishment pages, checked
  2026-09-23. The Kaggle badge page was fetched and confirms the holder,
  the certification and the year 2025, but prints no date.
- A2. The item inventory and spans are as listed in More Information.
  **Measured** from the master CV as corrected 2026-09-23.
- A3. Zoom and dragging would reveal nothing. **Measured**: 14 dated items
  across 33 months, no lane holding more than five, all of them visible at
  the default view.

## Considered Options

- Hand-built vertical spine in CSS Grid
- vis-timeline used directly, accepting a horizontal axis
- vis-timeline rotated ninety degrees by CSS transform
- TimelineJS
- No timeline, which is ADR-0001's position

## Decision Outcome

Chosen option: "Hand-built vertical spine in CSS Grid".

We will add a dedicated timeline section with a vertical time axis running
down the page.
We will build it by hand in CSS Grid and will not take a timeline library as
a dependency.
We will render four lanes: Builds and Open source to the left of the spine,
Work and Certifications to the right, with the degree drawn as a background
band behind all of them.
We will keep the Open source lane in the data model but will not render it
until it holds at least one merged pull request.
We will scale the axis at a fixed four layout units per month, with zooming
and dragging absent rather than disabled.
We will start the axis at January 2024, with the degree band running past
the top edge carrying a marker that says it starts earlier.
We will mark the timeline up as an ordered list of dated entries in the
initial HTML and draw the visual on top of that list.

### Consequences

- Positive: the concurrency the CV flattens becomes visible, including the
  Kaggle capstone running into the Research Concierge in Nov to Dec 2025.
- Positive: the ordered list satisfies both the crawler constraint and the
  text-equivalent requirement with one artefact rather than two.
- Positive: no dependency, so no licence to track, no bundle to ship, and no
  library redraw to fight.
- Positive: with no zoom bound to the wheel, scrolling the page over the
  timeline scrolls the page.
- Negative: spacing, responsive behaviour and the collapse controls are all
  work to be built rather than configuration to be set.
- Negative: a fixed scale means a long empty stretch if a future gap opens
  in the record.
- Negative: PAC Kamra returns to the timeline as its opening item, which the
  operator had previously excluded for showing a gap. The gap is now framed
  by items on both sides rather than standing alone.
- Neutral: vis-timeline is used as a reference for its data model, its
  within-lane stacking behaviour and its class naming, without being taken
  as a dependency.

### Confirmation

- The built page contains an ordered list of every timeline entry in the
  initial HTML response. Checked by fetching the page with JavaScript
  disabled and confirming every entry is present. A build where any entry
  exists only after script execution fails this check.
- Every entry on the timeline appears in the master CV with the same dates.
  An entry whose dates differ from the master fails.
- Scrolling the page with the pointer over the timeline scrolls the page and
  does not change the timeline's scale or position.
- The Open source lane does not render while it holds no items. A build that
  renders an empty lane fails.
- The spacing claim is checkable: the distance between the Nov 2025 and Dec
  2025 gridlines equals four layout units, the same as every other month.

## Pros and Cons of the Options

### Hand-built vertical spine in CSS Grid

- Good: matches the stated design exactly, including the vertical axis, the
  travelling lane headers and the collapse controls.
- Good: 33 months at four units each is 132 grid rows, and an item spanning
  Sep to Dec 2025 is a span of sixteen. The mechanism is that simple.
- Good: vertical scroll is what a phone does natively.
- Bad: everything is built, including the accessibility work.

### vis-timeline used directly, horizontal

- Good: nested groups give collapsible lanes, `timeAxis.scale: 'month'`
  gives month labelling, and `zoomable: false` with `moveable: false` gives
  a fixed view. All documented, read 2026-09-23.
- Bad: horizontal only. The `orientation` option's values place the axis at
  the top or bottom of a horizontal chart; there is no vertical axis in the
  documented option set.
- Bad: 33 months at a readable month width is wider than a phone screen, so
  the chart scrolls sideways on mobile.
- Bad: no accessibility or keyboard support is documented, and every event
  the library exposes is a pointer event.

### vis-timeline rotated by CSS transform

- Good: would in principle reuse the library's layout engine.
- Bad: the library derives time from unrotated pointer coordinates, redraws
  its own DOM so counter-rotating labels fights it, and a transform does not
  change the layout box, so sizing becomes manual. **None of this was
  tested**, so it is reasoning from the documentation rather than a measured
  result.
- Bad: the decisive objection needs no test. With zoom, drag, the window and
  the scale all fixed, every feature the library provides is switched off,
  leaving positioned boxes on a scale, which is what CSS Grid does.

### TimelineJS

- Bad: slide-based, showing one event at a time rather than the whole span.
  Its own guidance says it suits a strong chronological narrative and works
  poorly for stories that jump around.

### No timeline

- Good: ADR-0001's reasoning, which still holds for the ordering of the
  projects section.
- Bad: the corrected dates removed the premise. The concurrency is real and
  the record now shows it.

## More Information

**Reverses one clause of ADR-0001.** That record's rule "We will not build a
timeline view" no longer holds. Its other three rules, sectioned structure,
projects ordered by importance, and a curated set, remain in force and are
not carried into this record, so this is not a supersession. ADR-0001 stays
accepted with a row in its Changes table.

**The inventory, from the master CV as corrected 2026-09-23.** Fourteen
dated items, plus the degree as a band.

| Item | Lane | From | To |
|---|---|---|---|
| BE Software Engineering, KIET | Band | Sep 2022 | Aug 2026 |
| Engineering Intern, PAC Kamra | Work | Jan 2024 | Feb 2024 |
| Python 3 Programming Specialization, Michigan | Certifications | Aug 2024 | Jan 2025 |
| WordPy Autonomous Solver | Builds | Feb 2025 | Feb 2025 |
| Professional Skills for the Workplace, UC Davis | Certifications | Jun 2025 | Sep 2025 |
| Google Prompting Essentials | Certifications | Sep 2025 | Sep 2025 |
| Applied LLM Workflow Research | Builds | Sep 2025 | Dec 2025 |
| Prompt Engineering Specialization, Vanderbilt | Certifications | Oct 2025 | Dec 2025 |
| 5-Day AI Agents Intensive, Google and Kaggle | Certifications | Nov 2025 | Dec 2025 |
| Autonomous Research Concierge | Builds | Nov 2025 | Dec 2025 |
| Rahzaan | Builds | Feb 2026 | Present |
| Crypto Accumulation Scanner | Builds | Feb 2026 | Feb 2026 |
| AI Automation Engineer, HubIT | Work | Jun 2026 | Jul 2026 |
| BE completion | Band end | | Aug 2026 |

- Not decided here: the pixel size of a layout unit, the collapse control's
  behaviour at each breakpoint, and whether the Kaggle capstone's link to
  the Research Concierge is drawn or only stated.
- **Open, and blocking one entry:** the UC Davis certificate has no
  credential URL in the master CV, while the other four do. The site gives
  every claim a proof link, so this entry cannot carry one until the URL
  exists.
- Evidence: `docs/research/0002-tools-and-libraries.md`, sections 4 and its
  vis-timeline option check.
- Superseded by this record: `docs/deferred/projects-timeline.md`, whose
  trigger the operator fired on 2026-09-23.
- Revisit if the record develops a gap longer than about six months, which a
  fixed scale will display at full length.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-09-23 | Professional Skills for the Workplace, UC Davis, Jun to Sep 2025, added to the inventory in the Certifications lane. Item count in assumption A3 corrected from 13 to 14. | The record was written while that certificate was absent from the master CV and flagged as blocking. The operator authorised adding it to the master the same day, so the inventory the build works from had to follow. No Decision Outcome rule changed. |
| 2026-10-03 | The UC Davis certificate is **no longer blocked**: the master CV carries its credential link, https://coursera.org/verify/specialization/LAM1PDD8F3JA, read 2026-09-27 and again 2026-10-03. The "Open, and blocking one entry" line in More Information is closed by this row. | Raised by the design-system session of 2026-10-03, checked by the chat against the master the same day. |
| 2026-10-03 | **Newest at the top.** The axis runs from the as-of month at the top down to January 2024, with the degree band running past the bottom edge carrying the marker that it starts earlier. The ordered list in the HTML follows the same order, newest first. This reverses the axis direction implied by "start the axis at January 2024" and "running past the top edge"; scale, lanes and the list-first markup stand. | Decided by the operator 2026-10-03, on seeing the design-system specimen: the latest work should be what a reader meets first. |
| 2026-10-05 | **On a phone, one spine with all lanes interleaved**, newest at the top, each entry marked with its lane by icon and label, and filter chips to show or hide lanes. Not to scale on a phone; the desktop timeline stays to scale. Closes the collapse-behaviour question this record left open. | Chosen by the operator 2026-10-05 from the prototype's two phone versions (option 2a), after viewing both on his phone. The other, one lane at a time behind tabs, was not chosen. |
| 2026-10-06 | Inventory name corrected to the master's: **Python 3 Programming Specialization**. Name only; lane and dates unchanged. | Found by the implementing seat in Report 3; checked by the chat against the master. |
