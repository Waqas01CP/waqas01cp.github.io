---
status: accepted
topic: build
description: The site's speed is held to Google's "good" Core Web Vitals under Lighthouse's default mobile run, not to a page-weight figure. Heavy elements, 3D included, are added one at a time and kept only if the goals still hold. Read before adding any heavy element or motion.
date: 2026-10-02
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0009: Performance goals instead of a page-weight figure

## Context and Problem Statement

ADR-0005 puts every layer of every item in the first response, so the page
is as heavy as all of its content together. A budget was left open on
2026-09-26 with the operator's stance that it should not be extremely
conservative: the oldest phone worth designing for is a 2020 to 2022 model.
He also prefers a polished site and would like 3D if it can be afforded.

Two pulls meet here. Polish, depth and 3D add weight and work for the
phone. A reader on an ordinary phone and a weak connection is the one who
pays for them. And a budget can be written as bytes, which are easy to
count but say nothing directly about what the reader waits for, or as
timings of what the reader experiences, which need a defined test to mean
anything.

On 2026-10-02 the operator set the direction for the design brief: goals
rather than prescribed style, few hard limits, and 3D tested one element at
a time against a measured budget.

## Decision Drivers

- ADR-0005: everything ships on first load.
- The operator's stance of 2026-09-26 on phones, and his direction of
  2026-10-02 that the design be held by goals, not style rules.
- Scope floor lines 10 and 11: no tracking and no visitor data, so the site
  will never have measurements from real visitors.
- The standing rule to measure rather than estimate.

## Assumptions

- A1. Google's "good" thresholds are the right bar. **Sourced**: web.dev,
  Web Vitals, read 2026-10-02: largest contentful paint within 2.5
  seconds, interaction to next paint of 200 milliseconds or less, and
  cumulative layout shift of 0.1 or less, at the 75th percentile of page
  loads.
- A2. Lighthouse's default mobile run is a fair stand-in for the operator's
  2020 to 2022 phone on a weak connection. **Partly sourced**: Lighthouse's
  throttling documentation, read 2026-10-02, gives the defaults as 150 ms
  latency, 1.6 Mbps down and 750 Kbps up, described as roughly the bottom
  quarter of 4G and the top quarter of 3G, with a constant 4x CPU
  slowdown. **Not verified**: how a 4x slowdown of the test machine
  compares with a 2020 to 2022 phone, which depends on the machine running
  the test. Approved by the operator 2026-10-02 with this stated.
- A3. Total Blocking Time stands in for input responsiveness in the lab.
  **Sourced**: web.dev, Total Blocking Time, read 2026-10-02: a reasonable
  lab proxy for interaction to next paint, not a substitute for it, with
  sites to strive for under 200 milliseconds on average mobile hardware.
- A4. The median of five runs is stable enough to decide on. **Sourced**:
  Lighthouse's variability documentation, read 2026-10-02: the median of
  five runs is twice as stable as one run.

## Considered Options

- Core Web Vitals goals under Lighthouse's default mobile run
- A page-weight figure in kilobytes
- No budget; judge by eye

## Decision Outcome

Chosen option: "Core Web Vitals goals under Lighthouse's default mobile
run".

We will hold the page to largest contentful paint within 2.5 seconds,
cumulative layout shift of 0.1 or less, and Total Blocking Time under 200
milliseconds, each the median of five Lighthouse runs with its default
mobile settings.
We will add any heavy element, 3D, motion or large media, one at a time,
measured with and without it, and keep it only if the page still meets all
three.
We will measure each Claude Design prototype export that adds such an
element, and each build that does.
We will not set a page-weight figure in bytes.

### Consequences

- Positive: the budget is in the reader's terms, what they wait for, and
  every number in it comes from a published source.
- Positive: 3D is decided by measurement, element by element, rather than
  argued in advance.
- Negative: interaction to next paint is never measured from real
  visitors, because the site collects nothing (floor lines 10 and 11).
  Total Blocking Time is a proxy and can miss real problems.
- Negative: lab results depend on the machine running them (A2). Results
  from different machines are not compared with each other.
- Neutral: a byte count is still worth reporting beside the timings, as a
  diagnostic, but it does not pass or fail anything.

### Confirmation

- Run Lighthouse five times on the built page with default mobile
  settings and record the medians. Pass: all three under their thresholds.
- Before keeping a heavy element, record the medians with and without it.
  An element kept without both sets of numbers fails.
- Make the page deliberately slow, for example with a large unoptimised
  image, and run the check. Pass: it fails. A check that cannot fail is
  worse than none.

## Pros and Cons of the Options

### Core Web Vitals goals under Lighthouse's default mobile run

- Good: measures what the reader experiences, against a published bar.
- Bad: lab only, and the test machine affects the result.

### A page-weight figure in kilobytes

- Good: trivial to measure and to enforce in the build.
- Bad: no source found for a figure that fits this site, and bytes do not
  map directly to waiting time: a small script can block longer than a
  large image.

### No budget; judge by eye

- Good: no tooling.
- Bad: against the rule to measure rather than estimate, and it leaves 3D
  to taste alone.

## More Information

- Closes the page-weight item in docs/decisions/README.md's Pending list,
  open since 2026-09-26.
- The goals are written into `docs/design/DESIGN.md`, the brief Claude
  Design works from, so the design is held by them from the start.
- A 3D or animation library would be a new dependency, which scope floor
  line 14 forbids without its own record. 3D with the browser's own CSS,
  SVG and WebGL needs no record.
- Revisit if a byte figure from a primary source turns up, or if the site
  ever gains field measurements, which would itself need a change to
  floor lines 10 and 11.

## Changes

| Date | Change | Why |
|---|---|---|
