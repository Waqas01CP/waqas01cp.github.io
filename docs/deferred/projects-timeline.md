---
type: deferred
description: A date-ordered timeline of projects and roles. Deferred 2026-09-22, reopened and built 2026-09-23 as ADR-0003. Kept as the record of why it was refused first.
status: closed
---

# A date-ordered timeline of projects and roles

**Deferred 2026-09-22. Reopened and decided in favour 2026-09-23, as
ADR-0003.** This entry is kept rather than deleted, because the reason it
was refused the first time is the useful part.

## What closed it

The trigger written below was "a reader asks, in writing, when a piece of
work happened or how two pieces overlap". The operator fired it himself on
2026-09-23.

But the trigger is not what made the decision change. Two facts in the
material changed. The degree gained a Sep 2022 start date, and three of the
four certificate dates in the master CV turned out to be wrong by one to two
years. Corrected, the certificates became spans rather than undated points,
and Sep to Dec 2025 holds five or six concurrent items where it had appeared
to hold two.

That is worth recording plainly: **the original refusal was correct on the
evidence available, and the evidence was wrong.** The reasoning below was
not bad reasoning. It rested on dates that did not hold.

What was built is not what was proposed below either. ADR-0003 is a vertical
spine with four lanes and a degree band, hand-built in CSS Grid, not a
library timeline.

---

*Everything below is the entry as written on 2026-09-22, unchanged.*

## What was proposed

Any view that orders the operator's work by date rather than by importance:
a horizontal or vertical time axis, a career timeline, a set of grouped
rows showing overlapping engagements, or a switchable second view beside
the ranked one. All of these are the same proposal.

Three implementations were researched before it was deferred: TimelineJS
(Northwestern Knight Lab, MPL 2.0), vis-timeline (dual Apache-2.0 or MIT),
and a hand-built SVG or CSS component.

## Why it was not built

ADR-0001 states: "We will not build a timeline view."

Its Decision Outcome orders projects by importance, with main projects
first, because NN/g's 2019 survey of 204 hiring managers found readers
skim and prefer curated work, and because the operator stated that
structure on 2026-09-22.

Two properties of the material worked against a timeline independently of
that. Six of eight dated items fall between Sep 2025 and Aug 2026, so a
true time axis is mostly empty. Several items overlap: Rahzaan with both
the Crypto scanner and HubIT, and the research project with the Research
Concierge. Counted from the master CV, read 2026-09-23.

Nothing was built in its place. Projects are ordered by importance.

## What could and could not be compared

**Known.** The library options and their licences were read from their own
documentation. TimelineJS presents one slide per event and its own guidance
says it works poorly for stories that jump around, which describes
overlapping threads. vis-timeline renders ranges and points together with
grouped rows, so overlap is visible, at the cost of a heavier dependency.
A complex graphic requires a full text equivalent under W3C WAI's Complex
Images tutorial, which means the underlying list has to exist anyway.

**Unknown.** Whether any hiring reader wants chronology from a portfolio
site. No source located measures this. The claim that a timeline would help
and the claim that it would not are both unsupported by evidence. The
decision rests on curation evidence and the operator's stated structure, not
on a measurement of timeline value.

**Unknown.** Whether vis-timeline is keyboard accessible. Not checked.

## The trigger

Revisit when the site carries more than about fifteen dated items, so that
ordering by importance alone stops being scannable, **or** when a reader
asks, in writing, when a piece of work happened or how two pieces overlap.

The second is the real trigger. The first is a proxy for it and is easier
to notice.

## What revisiting would have to produce

Not the timeline itself. First, evidence that ranked sections plus a date
on each entry are insufficient, which is the cheaper intermediate step and
is still open in ADR-0001's More Information. Second, ADR-0001 would have
to be amended or superseded, since "We will not build a timeline view" is
one of its four rules.
