---
status: accepted
topic: content
description: The reading layers as they now stand. Layer 1 on every item, layers 2 and 3 only where the master has material, all in the initial HTML, layer 3 scoped to what an interviewer probes and named per item. Supersedes ADR-0005. Read before writing any page content.
date: 2026-10-03
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0010: Reading layers, consolidated

## Context and Problem Statement

ADR-0005 settled that each item is read at three depths, all present in the
first HTML response. Between 2026-09-26 and 2026-10-03 it gained eight
Changes rows. Four of them changed what its rules say: layers became
conditional, layer 3's scope widened, each disclosure gained a name, and
three items lost their verification route. A reader of ADR-0005 now has to
reconcile its Decision Outcome against its Changes table to learn the rule.

The operator's Decision Record Standard treats an eighth Changes row as a
supersession trigger, for exactly that reason. This record restates every
rule still in force in one place, as amended, and ADR-0005 is superseded by
it.

The tensions are unchanged from ADR-0005. Depth is what the CV cannot hold
and what a skimming reader will not read. A crawler sees only the first
response. An interviewer wants the detail a recruiter skips.

## Decision Drivers

- Research 0001: the major AI crawlers parse the initial HTML only, and
  recruiters distrust generic, too-polished prose.
- ADR-0004 lines 1, 5 and 7: every claim from the master, every number
  reproducible, everything readable in the first response.
- The operator's decisions of 2026-10-02 and 2026-10-03, listed in ADR-0005's
  Changes table.
- The supersession rule: eight Changes rows.

## Assumptions

- A1. Three reader types matter: the AI summariser, the skimming recruiter,
  and the interviewer. **Sourced**: research 0001. The Masters admissions
  reader is served by layer 3 with different emphasis; that mapping is
  **assumed, not evidenced**, carried from ADR-0005.
- A2. Content inside a collapsed disclosure is read the same as visible
  content. **Sourced for crawlers**: it is in the first response.
  **Partly verified for assistive technology**: 2026-10-02, in headless
  Chromium with keyboard only, the disclosure is exposed with its name and
  state and its text enters the accessibility tree when opened. **Speech
  heard** 2026-10-07 in NVDA 2026.2 (Changes),
  `docs/deferred/screen-reader-speech-test.md`, closed. **Not verified for AI
  summarisers' weighting.**
- A3. Eleven items carry a public artefact and three cannot. **Measured**
  from the master CV, read 2026-10-03: Rahzaan (case study and live app),
  Applied LLM Workflow Research (live app), the Research Concierge, the
  Crypto scanner, WordPy and the job aggregator (repositories, links now in
  the master), and the five certificates (credential links). HubIT, PAC
  Kamra and the degree cannot.

## Considered Options

- Supersede ADR-0005 with one record holding every rule as amended
- Keep amending ADR-0005

## Decision Outcome

Chosen option: "Supersede ADR-0005 with one record holding every rule as
amended".

We will give every item a layer 1: a short, checkable fact, written to be
specific rather than plain.
We will add layer 2, a summary for a reader deciding whether to go further,
and layer 3, full depth, only where the master CV holds more than the layer
above already shows.
We will place every layer an item has in the initial HTML response, using
disclosure to keep the page scannable, and will defer none to a later fetch.
We will link layer 1 to a public artefact for every item that has one.
HubIT, PAC Kamra and the degree carry neither a proof link nor a
verification line.
We will limit layer 3 to what a reader would question in an interview:
decisions, trade-offs, what failed, how each was verified, and
production-scope facts an interviewer would probe.
We will name each layer 3 disclosure control for its item, so that no two
controls share a name.
We will let tier control order and prominence only, never which layers
render, and the build will fail when the content file's order contradicts
tier rather than sorting by it.

### Consequences

- Positive: one artefact still serves the crawler, the skimmer and the
  interviewer, now without padding small items to three layers.
- Positive: the rules are readable in one place again.
- Negative: the page ships its full depth on first load; ADR-0009's goals
  are the check on that.
- Negative: the numbers burden stands. Layer 3 carries most of the figures,
  and ADR-0004 line 5 requires each to be reproducible on demand.
- Negative: three items show claims with no way for a reader to check them,
  beside items that link out. The operator accepted that on 2026-10-03.
- Neutral: this record governs what content exists at what depth, not how
  it looks.

### Confirmation

- Fetch the built page with JavaScript disabled. Every layer of every item
  is present.
- Every layer-1 fact appears in the master CV with the same wording or a
  faithful shortening.
- Every item except HubIT, PAC Kamra and the degree carries a proof link.
  Any other item without one fails.
- An item whose master entry has nothing beyond layer 1 renders no empty
  layer 2 and no disclosure.
- No two disclosure controls share an accessible name. Test: list the
  page's controls in the accessibility tree.
- Speech test, per the deferred entry, before the styled site replaces the
  unstyled one.
- Audit layer 3 against its scope. A changelog in layer 3 fails.
- Move a tier 3 item above a tier 2 item and build. Pass: failure naming
  both.

## Pros and Cons of the Options

### Supersede with one consolidated record

- Good: the rule is readable without reconciling a table against an
  outcome.
- Bad: two records to follow for the history; ADR-0005 keeps the audit
  and the reasoning, this one keeps the rules.

### Keep amending ADR-0005

- Good: one file.
- Bad: against the operator's standard, and the reason the standard exists:
  a reader of the Decision Outcome would be misled by it.

## More Information

- **Supersedes ADR-0005.** Every rule of ADR-0005 still in force is carried
  into the Decision Outcome above, as amended: rules 2 (initial HTML,
  disclosed), 3 (specific, not plain) and 5 (layer 3 scope) carry forward
  with rule 5 widened; rule 1 (three layers on every item) and rule 4
  (verification route where no link) carry forward as amended by its
  Changes rows of 2026-10-02 and 2026-10-03; its Changes rows on tier carry
  forward unchanged.
- ADR-0005 keeps the reasoning this record does not repeat: the audit of
  2026-09-25 and why each considered option was rejected. Read it for why;
  read this for what.
- Revisit if a page's first load fails ADR-0009's goals, since that is the
  pressure that would push layer 3 out of the initial HTML.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-10-07 | **A2's speech half verified; the deferred speech test is closed.** NVDA 2026.2 in Chrome, on the live styled site at eaee932: each "In depth" control spoken with its item's name and collapsed state; Enter spoken as expanded, and reading continued into layer 3; Close returned focus, spoken collapsed; all five, each named differently. The first run, on 6812c4f, found words run together between separately laid-out pieces, such as "592automated"; fixed in c97b99e before the passing run. The test ran after the styled site went live: the operator pushed it on 2026-10-07 at 10:25:54Z, which he confirmed on 2026-10-10, so the deferral's trigger passed unmet. | The operator's report of what he heard, confirmed on asking; his copied Speech Viewer text shows content and names, not states. Report 5, rounds 3 and 5; `logs/2026-10-07-tree-parity.md`. |
