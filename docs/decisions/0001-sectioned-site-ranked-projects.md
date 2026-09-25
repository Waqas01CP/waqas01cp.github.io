---
status: accepted
topic: structure
description: How project work is organised on the site. Sectioned layout, projects ranked by importance, a curated set, no timeline. Read before laying out any page.
date: 2026-09-22
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0001: Sectioned site with projects ranked by importance, no timeline

## Context and Problem Statement

The site exists to carry the evidence a one-page CV cannot hold. Project work can be presented in two ways that pull against each other. A date-ordered timeline shows when work happened and where it overlapped, which a CV flattens. An importance-ordered layout puts the strongest work first but hides chronology.

The master CV's dated items are uneven in both dimensions. Six of eight fall between Sep 2025 and Aug 2026, leaving the earlier span sparse: PAC (Jan 2024), WordPy (Feb 2025), Applied LLM Workflow Research (Sep to Dec 2025), Autonomous Research Concierge (Nov to Dec 2025), Rahzaan (Feb 2026 to present), Crypto Accumulation Scanner (Feb 2026), HubIT (Jun to Jul 2026), KIET (Aug 2026). Counted from the master CV, read 2026-09-23. Several overlap: Rahzaan with both the Crypto scanner and HubIT, and the research project with the Research Concierge.

Entry length is uneven too. Rahzaan carries nine bullets in the master; WordPy carries one. Counted from the master CV, read 2026-09-23. A uniform grid puts a tall card beside a nearly empty one.

The site serves employers first and Masters admissions readers second, from one version.

## Decision Drivers

- Hiring readers rarely read a portfolio word for word and want curated work. NN/g survey of 204 UX hiring managers, 2019.
- Hiring readers rely on signals they can verify quickly. Marlow and Dabbish, CSCW 2013.
- The operator's stated structure: dedicated sections such as projects, certifications and skills; main projects first; a curated set, not every project. Stated 2026-09-22.

## Assumptions

- A1. Readers of this site skim and prefer curated work, as NN/g's surveyed hiring managers do. **Sourced**: NN/g, "5 Steps to Creating a UX-Design Portfolio", 2019, reporting a survey of 204 UX professionals in charge of hiring. The surveyed population was UX hiring managers, not engineering hiring managers, so applying it here extends the source rather than restating it.
- A2. Entry length and date spread in the master CV are as counted above. **Measured**: counted from `Operating Plan\Waqas_Sharif_Master.md`, read 2026-09-23.

## Considered Options

- Chronological timeline as the main projects view
- Ranked project sections with a timeline as a secondary, switchable view
- Dedicated sections with projects ranked by importance, a curated set, and no timeline
- One long page in CV order

## Decision Outcome

Chosen option: "Dedicated sections with projects ranked by importance, a curated set, and no timeline".

We will organise the site into dedicated sections, including projects, certifications and skills.
We will order projects by importance, with main projects first and secondary projects after them.
We will show a curated set of projects, not every project in the master CV.
We will not build a timeline view. **Reversed 2026-09-23 by ADR-0003. See Changes.**

### Consequences

- Positive: the strongest work is the first thing a skimming reader meets.
- Positive: no timeline library to load, test, or give a text equivalent for accessibility.
- Positive: uneven entry length is absorbed by ranking rather than fought inside a uniform grid.
- Negative: the reader loses an at-a-glance view of when work happened and where it overlapped, which is the one thing the CV also fails to show.
- Negative: one importance order must serve both employers and Masters readers, and what counts as a main project may differ between them.
- Neutral: which projects are main, which are secondary and which are omitted is not decided here, nor is the full section list.

### Confirmation

- Inspection of the built site: no timeline component exists in the source, the projects section lists main projects before secondary ones, and every project shown appears in the master CV.
- The failing case for that check: a build that renders a project absent from the master CV, or renders a secondary project above a main one, must fail it.
- Whether readers actually reach the strongest work first cannot be verified before the site has real readers. No check is claimed for it.

## Pros and Cons of the Options

### Chronological timeline as the main projects view

- Good: shows recency and overlap at a glance, which the CV cannot.
- Bad: orders by date, not strength, against both NN/g's curation finding and the operator's stated structure.
- Bad: six of eight dated items crowd a single year, leaving most of a true time axis empty.
- Bad: a complex graphic needs a full text equivalent. W3C WAI, Complex Images.

### Ranked sections with a timeline as a secondary, switchable view

- Good: keeps chronology available without leading with it.
- Bad: a second view to design, build, test and keep accessible, for a reader need that is assumed rather than evidenced.

### Dedicated sections with projects ranked by importance, a curated set, no timeline

- Good: matches both the evidence on curation and the operator's stated structure.
- Bad: chronology is lost unless each entry carries its own date.

### One long page in CV order

- Good: simplest to build; no ordering decision to make.
- Bad: reproduces the CV's structure, which the site exists to go beyond.

## More Information

- Evidence: `docs/research/0001-how-hiring-readers-read-candidate-material.md`.
- Deferred, with its reopen trigger: `docs/deferred/projects-timeline.md`.
- Not decided here, and still open: whether each project entry carries a visible date, which would keep recency without a timeline.
- Revisit if: the project count grows until chronology matters to readers, or evidence shows Masters readers need a different order from employers.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-09-23 | The rule "We will not build a timeline view" is reversed by ADR-0003. The other three rules stay in force and are not carried into ADR-0003, so this is an annotation, not a supersession. | Two facts in this record's Context changed. The degree gained a Sep 2022 start date, and three of four certificate dates in the master CV were wrong by one to two years. Corrected, certificates became spans rather than undated points and Sep to Dec 2025 holds five or six concurrent items. The premise that the material was too thin and too crowded for a timeline no longer held. |
