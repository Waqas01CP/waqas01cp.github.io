---
status: accepted
topic: structure
description: The eight sections and their order, the CV download, the project tiers with the three projects of 2026-10-31, the site and the gallery listed as projects, the open-source bar, no separate project pages and the Rahzaan case study as the only deeper destination. Supersedes ADR-0008. Read before laying out the page or adding a project.
date: 2026-11-04
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0013: Sections, project tiers, and where depth lives, consolidated

## Context and Problem Statement

ADR-0008 settled the sections, the tiers and where depth lives, and seven
Changes rows then amended it: dates on each entry, the degree in the
Intro, an Education section, navigation, the word "tier" in master text,
and the footer line. On 2026-10-31 Waqas added three projects to the
master CV and made two decisions that reverse earlier ones. Recording
them would be ADR-0008's eighth Changes row, the supersession trigger
of the Decision Record Standard, so this record replaces it and holds
every rule still in force in one place, as amended.

The two reversals. Before 2026-10-20 he had decided this site would not
list itself as a project (research 0004, decision 1;
`docs/reference/completed.md`); on 2026-10-31 he put this site and
portfolio-gallery into the master as projects. ADR-0008 would render an
open-source section once it held a merged pull request; on 2026-10-31 he
set a higher bar, because a merged listing pull request is not a code
contribution.

Two tensions remain from ADR-0008. Depth pulls toward a page per strong
project; his model of the reader keeps three destinations: the CV hooks,
the portfolio answers, the case study carries the extreme detail. And
ranking pulls toward visible labels, while a label such as "secondary"
tells a reader what to skip. A third is new: a site that lists itself
describes itself twice, once in the footer and once as a project.

## Decision Drivers

- ADR-0001: sectioned, ranked by importance, curated.
- ADR-0010: every item carries a checkable fact; tier controls order and
  prominence only.
- His model of the reader, 2026-09-26: the CV hooks, the portfolio shows
  capability in detail, the case study holds the extreme detail.
- His purpose for tiers, 2026-09-26: a strong project is never hidden
  behind a weaker one. Dates play no part in rank.
- Scope floor line 1 (ADR-0004): nothing appears that the master does not
  hold. The three new projects are in the master since 2026-10-31.

## Assumptions

- A1. A downloadable CV belongs on a portfolio site. **Sourced**, carried
  from ADR-0008: WPI's Career Development Center and UC Irvine's
  Engineering Undergraduate Student Affairs, read 2026-09-26 **from
  search-result excerpts, not the full pages.**
- A2. The tier order below is his. **Stated** 2026-10-31 and 2026-11-02
  UTC (Brief 15): Rahzaan highest; then Applied LLM Workflow Research,
  the ChatGPT Deep Research Provenance Case Study, the Job Aggregator,
  Portfolio Gallery, Portfolio Site and the Autonomous Research
  Concierge; then the Crypto Accumulation Scanner and WordPy. The
  Concierge moves from second to last in tier 2.
- A3. A merged pull request that adds a listing to someone else's list is
  not a code contribution. **Stated** 2026-10-31: his listing on
  emmabostian/developer-portfolios (#4350) appears nowhere in the master.
- A4. The master's research entries belong in Projects. **Stated**
  2026-11-02 (Brief 15): the site has no Research section, as Applied
  LLM Workflow Research already sat in Projects.

## Considered Options

- Supersede ADR-0008 with one record holding every rule as amended
- An eighth Changes row on ADR-0008
- A Research section for the master's research entries

## Decision Outcome

Chosen option: "Supersede ADR-0008 with one record holding every rule as
amended".

We will build the page from eight sections, in this order: Intro,
Projects, Timeline, Work, Education, Certifications, Skills, Contact.
We will reach them from one page with a section menu that stays in view,
lists the eight, marks the one in view and jumps to each; projects open
their depth in place.
We will offer the CV as a downloadable PDF in the Intro and again in the
footer, and will not make it a section.
We will show the degree as one line in the Intro, worded from the master,
and in the Education section with the master's Relevant Coursework.
We will not create a separate page per project; every project lives in
Projects, and the Rahzaan case study, linked out, is the only deeper
destination.
We will list this site and portfolio-gallery as projects, as the master
does.
We will put the master's research entries in Projects; there is no
Research section.
We will order projects by tier: tier 1 Rahzaan; tier 2 Applied LLM
Workflow Research, the ChatGPT Deep Research Provenance Case Study, the
Job Aggregator, Portfolio Gallery, Portfolio Site and the Autonomous
Research Concierge, in that order; tier 3 the Crypto Accumulation
Scanner, then WordPy.
We will never show a tier as a visible label.
We will show each project entry's dates in the master's own forms,
rendered from the same fields as the timeline.
We will mark a project "In development" only while the master does.
We will carry the master's Portfolio Footer in the footer, word for word,
its repository address a link to this repository.
We will render no open-source label, section or lane until his first
code contribution to someone else's project merges, or a project of his
has real adoption; a listing pull request does not count.

### Consequences

- Positive: three destinations, matching his model. The portfolio is
  never a stop between Projects and the case study.
- Positive: rank is carried by order, silently.
- Positive: every rule about sections and tiers is in one record again.
- Negative: the site describes itself twice, in the footer and as the
  Portfolio Site project. Both are master text the content trace
  requires; neither can go without a master change.
- Negative: five builds now run at once from Sep 2026, which narrowed the
  timeline's cards until the layout changed (Brief 15; no record fixes
  the timeline's widths).
- Negative: the Rahzaan case study, carried from ADR-0008, said
  multi-agent where the master says agentic and led with 26 reasoning
  steps where the master says 24. It lives in its own repository; not
  rechecked for this record.
- Neutral: "real adoption" is his bar and is not yet measured; the
  record that first renders an open-source item says what it was.

### Confirmation

- **Sections.** The built page has exactly the eight sections, in the
  order above. A build whose section order differs fails inspection.
- **The CV link.** It appears in the Intro and in the footer. Either
  missing fails.
- **One page.** No generated file other than `index.html` holds project
  content. A second HTML file carrying a project fails.
- **Tier order.** The build fails when the content file's order
  contradicts tier. Test: move a tier 3 item above a tier 2 item and
  build. **Pass: failure naming both. Fail: a successful build.**
- **No tier label.** No tier number or tier label appears in the
  rendered text. The master's own "two-tier", "merit-tier", "reasoning
  tier", "tier validation" and "market-cap tier" are content.
- **The order as set.** Projects render in the order of A2. A page whose
  project order differs fails inspection.
- **No open-source lane.** No item has the `opensource` lane, and no
  open-source label, section or lane renders. A build with one fails
  inspection until the bar above is met and recorded.
- **The footer line.** The content trace requires the Portfolio Footer
  on the page whole, its address a link.

## Pros and Cons of the Options

### Supersede with one consolidated record

- Good: one place to read; the trigger the standard sets.
- Bad: a reader of older logs follows ADR-0008's pointer here.

### An eighth Changes row on ADR-0008

- Good: no new file.
- Bad: the standard forbids it: reaching eight is a trigger that fires.

### A Research section

- Good: mirrors the master's own headings.
- Bad: a ninth section for two entries, and he decided against it
  (Brief 15).

## More Information

- **Supersedes ADR-0008.** Carried forward from it unchanged: the CV in
  the Intro and the footer and not a section; no page per project and the
  Rahzaan case study as the only deeper destination; tiers as order only,
  never a visible label; A1. Carried as amended by its Changes rows: each
  entry's dates (2026-09-26); the degree's Intro line (2026-09-27); eight
  sections with Education (2026-10-02); navigation by one page and a
  section menu (2026-10-03); "tier label" in Confirmation, and 26 courses
  as the master's count of 2026-10-05 (2026-10-06); the footer line
  (2026-10-15). Changed: the tier order (A2); the open-source rule (A3);
  this site and the gallery listed; research entries in Projects (A4).
  Dropped as settled: "include the job-aggregator once it is in the
  master" (it is, since 2026-09-26's Changes; kept as "In development
  only while the master says so"); the open placement of the `opensource`
  lane, answered by the bar above; the page-weight budget "that does not
  exist yet", settled by ADR-0009.
- ADR-0003's Open source lane carries the same bar (its Changes,
  2026-11-04).
- Reverses research 0004's decision 1 and the row in
  `docs/reference/completed.md`, by his statement of 2026-10-31; research
  0004 keeps its evidence with a dated note.
- ADR-0001 stays accepted; this record, like ADR-0008, extends it.
- Written by the implementing seat at Brief 15's instruction, recording
  his decisions; the architecture chat checks it.
- Revisit if a second project grows a standalone case study, or when the
  open-source bar is met.

## Changes

| Date | Change | Why |
|---|---|---|
