---
status: accepted
topic: content
description: Every item on the site carries three reading layers, all in the initial HTML, disclosed rather than deferred. Read before writing any page content.
date: 2026-09-25
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0005: Three reading layers for every item

## Context and Problem Statement

The site must carry the evidence a one-page CV drops while still answering
a reader in the manner that reader wants. Those two goals pull against each
other: depth is what the CV cannot hold, and depth is what a skimming reader
will not read.

Research 0001 identifies three readers with incompatible needs. An AI
summariser, which is often the first contact and executes no JavaScript. A
recruiter who rarely reads word for word and is deciding whether to go
further. An engineer or supervisor who will question the work in an
interview, which Google's reported 2026 loop makes explicit by adding a
technical conversation about a candidate's prior work.

A single depth serves none of them. This record settles how many depths
exist, what goes in each, and where they live in the document.

This was proposed on 2026-09-22 and the operator asked that it be audited
before being recorded rather than accepted on the strength of the proposal.
The audit is in More Information; it changed four things.

## Decision Drivers

- Research 0001: the major AI crawlers parse the initial HTML response only.
- Research 0001: recruiters treat material that reads as too polished and
  too perfectly matched as a reason for suspicion.
- NN/g 2019, and Princeton's guide: readers skim, and 15 to 30 seconds is
  the working assumption for a first pass.
- ADR-0004 line 7: anything that must be read sits in the initial HTML.
- The operator's stated goal, 2026-09-23: a visitor gets what they want
  easily, and likes it.

## Assumptions

- A1. The three reader types above are the ones that matter, and no fourth
  needs its own layer. **Sourced**: research 0001. The Masters admissions
  reader is served by layer 3 with different emphasis rather than a layer of
  their own, and that mapping is **assumed, not evidenced**.
- A2. Content inside a collapsed disclosure element is read the same as
  visible content. **Sourced for crawlers**: they parse the initial HTML
  response, and disclosure content is in it. **Not verified for assistive
  technology or for AI summarisers' weighting.** The check is in
  Confirmation.
- A3. Of the site's items, ten carry a public artefact and three cannot.
  **Measured** from the master CV, read 2026-09-25, plus the operator's
  statement of 2026-09-26: Rahzaan has a repository page and a live app, the
  research project has a live app, all five certificates have credential
  links, and the Research Concierge, the Crypto scanner and WordPy are all
  public repositories. **Their URLs are not in the master CV and were not
  independently verified**, because GitHub disallows automated fetching of
  a profile's repository list, checked 2026-09-25. HubIT, PAC Kamra and the
  degree cannot carry a link.

## Considered Options

- Three layers per item, all in the initial HTML, disclosed not deferred
- Three layers with layer 3 loaded on demand
- Two layers: a fact and everything else
- One depth, written for the middle reader

## Decision Outcome

Chosen option: "Three layers per item, all in the initial HTML, disclosed
not deferred".

We will give every item on the site three layers: a short checkable fact, a
summary for a reader deciding whether to go further, and full depth.
We will place all three in the initial HTML response, using disclosure to
keep the page scannable, and will not defer any layer to a later fetch.
We will write layer 1 to be specific rather than plain, because specificity
is what separates it from generated prose.
We will link layer 1 to a public artefact wherever one exists, and where
none exists we will name the verification route instead of leaving the claim
bare.
We will limit layer 3 to what a reader would question in an interview:
decisions, trade-offs, what failed, and how each was verified.

### Consequences

- Positive: one artefact serves the crawler, the skimmer and the
  interviewer, rather than three versions that can drift apart.
- Positive: the timeline in ADR-0003 is already an instance of this rule,
  an ordered list in HTML with a visual drawn on top, so the two records
  agree by construction rather than by coincidence.
- Positive: layer 3 largely exists already, in the master CV's bullets.
- Negative: every page ships its full depth on first load, so page weight
  is set by the deepest content, not the shallowest. A budget will be needed
  and does not exist yet.
- Negative: **the numbers burden is large.** The master's Rahzaan entry
  alone carries more than twenty distinct figures, and ADR-0004 line 5
  requires each to be reproducible on demand. Layer 3 is where they live, so
  layer 3 is where that obligation lands.
- Negative: three items can never carry a proof link, so the page will show
  two kinds of claim side by side. Naming the verification route is
  honest but visibly different from a link.
- Neutral: this record governs what content exists at what depth. It does
  not govern visual design, and the operator's goal that a reader likes the
  site is only partly addressed here.

### Confirmation

- Fetch the built page with JavaScript disabled. Every layer of every item
  is present. A build where any layer appears only after script execution
  fails.
- Every layer-1 fact appears in the master CV with the same wording or a
  faithful shortening. A fact absent from the master fails.
- Every item either carries a proof link or names its verification route.
  An item with neither fails.
- Open a collapsed disclosure with a screen reader and confirm the content
  is reachable and announced. This settles the unverified half of A2 and
  must be done before the first content page ships.
- Audit layer 3 against its scope: content that is not a decision, a
  trade-off, a failure or a verification does not belong there. A changelog
  in layer 3 fails.

## Pros and Cons of the Options

### Three layers, all in HTML, disclosed not deferred

- Good: satisfies ADR-0004 line 7 without making the page a wall.
- Bad: full weight on first load; no budget exists yet.

### Three layers with layer 3 loaded on demand

- Good: lightest first load.
- Bad: breaches ADR-0004 line 7 directly. The depth is exactly what an
  interviewer needs and exactly what a crawler would never see.

### Two layers: a fact and everything else

- Good: simpler to write and to maintain.
- Bad: collapses the skimmer and the interviewer into one reader. The
  skimmer then has to read interview-depth material to decide whether to
  read it.

### One depth, written for the middle reader

- Good: simplest.
- Bad: it is the CV again, which is the thing the site exists to go beyond.

## More Information

### What the audit changed

1. **"Deliberately unpolished" was wrong, and it was my phrasing.** The
   proposal said layer 1 should read as unpolished because polish invites
   suspicion. Research 0001 says recruiters distrust material that is too
   perfectly matched and reads as vapid, which is about generic prose with
   no substance, not about clear writing. Writing badly on purpose would be
   a misreading of the finding. The rule is **specific, not unpolished**.
   Specificity is the antidote; roughness is not.
2. **Disclosure and deferral were conflated.** "All three in the initial
   HTML" said nothing about whether a skimmer has to scroll past the depth.
   Disclosure, collapsed but present, satisfies both constraints at once.
   The original proposal did not distinguish them.
3. **"Proof one click away" is not achievable for every item**, and the
   proposal asserted it as though it were. A3 has the count. HubIT is
   client work whose two bullets are verbatim or cut with the client
   unnamed; PAC and the degree have no artefact. These verify by reference
   and transcript, not by link, and the site should say so rather than leave
   the claim looking like an oversight.

4. **Layer 3 had no upper bound.** "Full depth" invites a dumping ground.
   Scoping it to what an interviewer would question gives it an edge.

### What the audit did not resolve

- The three repository URLs. The operator confirmed on 2026-09-26 that all
  three are public, but the master CV carries no link for any of them and
  GitHub blocks automated listing. The URLs must be added to the master
  before those items can carry a proof link on the site.
- The Masters reader's mapping to layer 3, per A1.
- Whether a reader likes the site. This record cannot answer that.

- Evidence: `docs/research/0001`, and `docs/research/0003` for why layer 1
  leads with what is checkable.
- Constrained by: ADR-0004 lines 1, 5 and 7.
- Revisit if a page's first load exceeds whatever budget the framework
  decision sets, since that is the pressure that would push layer 3 out of
  the initial HTML.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-09-26 | Assumption A3 revised: ten items carry a public artefact, not seven, and the "could in principle" category is empty. The Research Concierge, the Crypto scanner and WordPy are public repositories. | The operator confirmed it on 2026-09-26. The record was written while that was an open question and said so. No Decision Outcome rule changed: rule 4 already said link where a link exists and name the route where none does. |
| 2026-09-26 | Three internal dates corrected from 2026-09-25 to 2026-09-26. | The session hit its limit mid-write and the turn was retried, so a partial version of this update had already landed with the earlier date on it. The substance was right and the dates were not. Recorded because the chat initially could not account for the discrepancy and said so; the operator supplied the cause. |
