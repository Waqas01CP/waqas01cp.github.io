---
status: accepted
topic: structure
description: The seven sections and their order, the CV download, the project tiers, no separate project pages, and the Rahzaan case study as the only deeper destination. Read before laying out the page or adding a project.
date: 2026-09-26
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0008: Sections, project tiers, and where depth lives

## Context and Problem Statement

ADR-0001 settled a sectioned site with projects ordered by importance, and
left three things open in its own words: which projects are main, which are
secondary and which are omitted, and the full section list. It said
"including projects, certifications and skills" and never closed the list.

The build now depends on both. It fails when an item arrives in a lane that
has no page section, and ADR-0005 makes tier an assertion the content file's
order must satisfy. Neither can be enforced against a list that does not
exist.

Two tensions shape the answer. Depth pulls toward giving each strong project
its own page; the operator's model of the reader pulls the other way, with
three destinations only: the CV hooks, the portfolio answers, the case study
carries the extreme detail. And ranking pulls toward visible labels, while a
label such as "secondary" tells a reader which items to skip.

## Decision Drivers

- ADR-0001: sectioned, ranked by importance, curated.
- ADR-0005: every item carries all three layers; tier controls order and
  prominence only.
- The operator's stated model, 2026-09-26: the CV hooks the reader, the
  portfolio shows capability and answers every question in detail, and the
  nuanced and extreme detail sits in the dedicated case study.
- The operator's stated purpose for tiers, 2026-09-26: a strong project is
  never hidden behind a weaker one. Dates play no part in rank, because the
  timeline already carries them.

## Assumptions

- A1. A downloadable CV belongs on a portfolio site. **Sourced**: WPI's
  Career Development Center says to include a downloadable PDF of the resume
  mirroring the experience and skills in the portfolio, and UC Irvine's
  Engineering Undergraduate Student Affairs says to always include the
  resume on the website. Both read 2026-09-26 **from search-result excerpts,
  not the full pages.** UC Irvine also recommends only three parts, a cover
  page, projects and an about; this record uses more, and that is a
  deliberate departure rather than an endorsement.
- A2. The tier order below is the operator's. **Stated** 2026-09-26: Rahzaan
  highest as the most complex and detailed; Applied LLM Workflow Research
  next; the Research Concierge level with it or slightly below; the Crypto
  scanner below those; WordPy lowest.
- A3. The job-aggregator's tier is tier 2. **Delegated**: the operator said
  on 2026-09-26 that its tier was the chat's to decide. The chat placed it
  in tier 2 because it is the only artefact that demonstrates the working
  method itself, with gates, logs and decision records, and placing it lower
  would hide it behind lesser work, against the operator's stated purpose.

## Considered Options

- Seven sections, tiers as order only, no separate project pages
- A page per main project, reached from the Projects section
- Visible tier headings such as "Main" and "Other"
- UC Irvine's three parts: cover page, projects, about

## Decision Outcome

Chosen option: "Seven sections, tiers as order only, no separate project
pages".

We will build the page from seven sections, in this order: Intro, Projects,
Timeline, Work, Certifications, Skills, Contact.
We will offer the CV as a downloadable PDF in the Intro and again in the
footer, and will not make it a section.
We will not create a separate page per project; every project lives in the
Projects section, and the Rahzaan case study, linked out, is the only deeper
destination.
We will order projects by tier: tier 1 Rahzaan; tier 2 Applied LLM Workflow
Research, the Autonomous Research Concierge and the job-aggregator, in that
order; tier 3 the Crypto Accumulation Scanner, then WordPy.
We will never show a tier as a visible label.
We will include the job-aggregator marked "In development" once it is in the
master CV, and not before.
We will not render an open-source section until it holds a merged pull
request, the same rule ADR-0003 applies to the timeline lane.

### Consequences

- Positive: three destinations, matching the operator's model exactly. The
  portfolio is never a stop between the Projects section and the case study.
- Positive: one fetch and one URL for the whole portfolio, which is simpler
  for crawlers per research 0001.
- Positive: rank is carried by order, silently, so no reader is told what to
  skip.
- Negative: the Rahzaan case study currently breaks three standing rules. It
  says multi-agent where the master says agentic, names model providers in
  its stack, and leads with 26 reasoning steps where the canonical figure is
  24. Linking to it sends readers there. The operator will update it; it
  lives in its own repository and is outside this project.
- Negative: a single page carrying every layer of seven projects is long,
  which puts weight on the page-weight budget that does not exist yet.
- Negative: the job-aggregator cannot appear until the operator writes its
  master CV entry, per scope floor line 1.
- Neutral: the `work` lane's page section is Work, from the section list
  above. Still undecided: where an `opensource` item appears on the page once
  one qualifies, and whether the degree (`band`) appears anywhere outside the
  timeline. Brief 1's build refuses an item in a lane with no section, which
  is the correct behaviour until they are.

### Confirmation

- The built page has exactly the seven sections, in the order above. A build
  whose section order differs fails inspection.
- The CV link appears in the Intro and in the footer. Either missing fails.
- No generated file other than `index.html` holds project content. A second
  HTML file carrying a project fails.
- The build fails when the content file's order contradicts tier (ADR-0005
  Changes). Test: move a tier 3 item above a tier 2 item and build. **Pass:
  failure naming both. Fail: a successful build.**
- No tier number or tier word appears in the rendered text.

## Pros and Cons of the Options

### Seven sections, tiers as order only, no separate project pages

- Good: matches the operator's three-destination model and ADR-0005.
- Bad: one long page.

### A page per main project

- Good: a linkable address per project, and a lighter front page.
- Bad: four destinations, with the portfolio page between the section entry
  and the case study doing nothing either does not. Approved by the operator
  and then reversed by him on the same day, 2026-09-26 UTC, for exactly that
  reason.

### Visible tier headings

- Good: rank is explicit.
- Bad: tells a reader which work to skip, which spends their attention on the
  wrong thing.

### Three parts only

- Good: UC Irvine recommends it and it is the leanest.
- Bad: the site exists to carry what the one-page CV cannot, and three parts
  cannot hold certifications, a timeline and skills as distinct things.

## More Information

- Extends ADR-0001, which stays accepted with a Changes row pointing here.
  None of ADR-0001's rules is reversed.
- The external case study lives at `/Rahzaan/`, a project site from a
  separate repository, root-relative per ADR-0002.
- Still open and not decided here: the page placement of the `opensource`
  lane, and navigation. The visible date on each project entry and the
  degree's place in the Intro were decided afterwards; see Changes.
- Revisit if a second project grows a standalone case study, which would
  make the case for a per-project page again.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-09-26 | Closes one item this record left open: **each project entry shows its dates**, in the master CV's own forms such as "Feb 2026 to Present", rendered from the same `start` and `end` fields as the timeline. Already produced by Brief 1's `date_phrase()` and item template; this row records it as decided rather than incidental. | Decided by the operator 2026-09-26. The timeline and the entry answer different questions: the timeline shows what ran concurrently, visually and at length; the entry states when this one ran, in a line. The chat had recommended against, arguing it wrote a fact twice. That confused display with storage: the date is stored once, in `items.json`, and rendered twice, which ADR-0006 permits. |
| 2026-09-26 | Consequences and More Information corrected. The `work` lane was listed as having no heading although the section list above gives it the Work section. The visible project date is closed by the row above and no longer listed as open. What remains open is named: page placement for `opensource` and `band` items, and navigation. | The record contradicted itself, and the build acts on it: its section list still omits `work` and must gain it, with Timeline placed between Projects and Work. Found on the chat's re-read after the implementing seat's Brief 2 report. No decision changes. |
| 2026-09-27 | The degree appears as one line in the Intro, worded from the master CV, and is not a section. The section count stays seven. This closes the `band` lane's placement: the band renders on the timeline, and the Intro line is its only other appearance. | Decided by the operator 2026-09-27. The section list above had no place for the degree, so it existed only as the timeline band. The chat's reasoning, not sourced: the degree is among the first things a Masters admissions reader, the site's second audience, looks for, and one Intro line gives it without an eighth section. |
