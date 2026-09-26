---
type: index
description: The decision record index for the portfolio site, with the fixed topic list and the Pending list of decisions identified but not concluded.
status: current
---

# Decision records

MADR 4.0.0 with an Assumptions section, per the operator's Decision Record
Standard. One choice per record, written at the moment it was concluded.

## How to read this

Records are numbered in the order they were concluded, not by importance.
The status column tells you whether a record is still in force. Follow a
superseded record's pointer to its replacement.

A record's decision is never silently rewritten. An amendment that leaves
it in force goes in its Changes table; a replacement is a new record that
supersedes it. Before superseding, ask whether any rule is still in force
and not carried into the later record.

## Topic list

Fixed. A record's `topic` frontmatter field takes exactly one of these.
Adding a topic is itself a decision.

| Topic | Covers |
|---|---|
| structure | Information architecture, sections, ordering, navigation |
| content | What claims appear, where each traces to, how deep each layer goes |
| design | Visual direction, typography, colour, motion, imagery |
| build | Framework, rendering strategy, components, performance budgets |
| hosting | Where it is served from, domain, analytics, forms |
| process | Repository conventions, gates, workflow between seats |

## Index

| ID | Title | Status |
|---|---|---|
| [0001](0001-sectioned-site-ranked-projects.md) | Sectioned site with projects ranked by importance, no timeline | Accepted, one clause reversed by 0003 |
| [0002](0002-hosting-and-addressing.md) | Public user site at waqas01cp.github.io, no custom domain yet | Accepted |
| [0003](0003-vertical-timeline-section.md) | A hand-built vertical timeline section | Accepted |
| [0004](0004-scope-floor.md) | The scope floor, fourteen lines | Accepted |
| [0005](0005-three-reading-layers.md) | Three reading layers for every item | Accepted |
| [0006](0006-python-generator-build.md) | Build with a small Python generator | Accepted |

## Pending

Decisions identified but not yet concluded.

- The scope floor. **Closed 2026-09-25 by ADR-0004**, at fourteen lines.
- Whether a skill level is shown at all, and in what form. **Closed
  2026-09-25**, research 0003, ADR-0004 line 2. No rating of any kind,
  including years.
- Whether the site carries writing of any kind. **Closed 2026-09-25**,
  research 0003, ADR-0004 line 4.
- Whether a duration or overlap view belongs in the work or projects
  section. **Closed 2026-09-23 by ADR-0003.**
- Whether Professional Skills for the Workplace, UC Davis, Jun to Sep 2025,
  is added to the master CV. **Closed 2026-09-26**: added, with its
  credential link.
- What each `tier` value renders. **Closed 2026-09-27**: tier controls order
  and prominence only, never which layers render. ADR-0005 Changes.
- Section headings for the `work`, `opensource` and `band` lanes. The build
  fails if an item arrives in a lane with no section, so these are decided in
  the brief that brings those items.
- A `.gitattributes` forcing LF line endings, so the rebuild gate cannot fail
  on line endings alone under Windows autocrlf. **Closed 2026-09-26 (UTC)**:
  agreed in the chat's reply to Brief 1's report, added by the Brief 1 seat.
- The pixel size of one timeline layout unit, and the collapse control's
  behaviour at each breakpoint. Left open by ADR-0003.
- What exception the operator wants to line 8 of the floor. **Closed
  2026-09-25**: none. He withdrew the qualifier and the line stands as
  written, now ADR-0004 line 7.
- Whether the Research Concierge, the Crypto scanner and WordPy have public
  repositories. **Closed 2026-09-26**: all three are public. Their URLs are
  still missing from the master CV and must be added before those items can
  carry a proof link.
- The framework and rendering approach. **Closed 2026-09-26 by ADR-0006.**
- The repository layout, the templating library by name, and where the
  structured content file lives. Left to the first implementing brief by
  ADR-0006.
- A page-weight budget. ADR-0005 ships every layer on first load, so the
  budget is set by the deepest page. None exists yet.
- Where the design prototype is built: a dedicated design chat using the
  Design artifact type, or the standalone experience at claude.ai/design.
  Gated on the four-check test in `CHAT_STATE.md` item 4.
- Whether the site carries an AI assistant, and if so how it is prevented
  from stating anything not already on the page.
- Whether the Rahzaan case study is folded into this site or linked to.
  Folding it in imports claims that are not in the master CV.
- Whether each project entry carries a visible date. Left open by ADR-0001.
- Which projects are main, which are secondary, and which are omitted.
- Framework and rendering strategy. Constrained by the evidence in
  research 0001: the major AI crawlers do not run JavaScript.
