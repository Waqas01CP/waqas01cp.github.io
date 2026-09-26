---
status: accepted
topic: build
description: A small Python generator, no site framework, built locally with its output committed. Turns two of ADR-0005's review checks into build gates. Read before writing any build code.
date: 2026-09-26
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0006: Build with a small Python generator

## Context and Problem Statement

The accepted records leave the site with exactly three things to generate.
The timeline's grid positions, computed from fourteen items' dates at four
layout units per month from Jan 2024 (ADR-0003). The same three-layer markup
repeated for roughly twelve items (ADR-0005). Nothing else: no routing, no
client state, no data fetching.

Every option can do that. The question is how much dependency and how much
toolchain to accept for it, against a standing constraint that a dependency
is added by decision and not by import (ADR-0004 line 14), and against
output that must carry all content in the initial HTML (ADR-0004 line 7).

Writing the HTML by hand is the zero-dependency answer, but it means
calculating each timeline item's grid row and span by hand, fourteen times,
and recalculating whenever a date moves. That failure is silent: a bar in
the wrong month looks entirely normal.

## Decision Drivers

- ADR-0003: timeline positions are a function of dates and must stay in
  sync with the master CV.
- ADR-0005: repeated markup per item, and two confirmation checks that are
  review-only unless something enforces them.
- ADR-0004 lines 7 and 14: content in the initial HTML; no dependency by
  import.
- ADR-0002: GitHub Pages, served at the domain root, root-relative links.
- Free by default, minimum spend, discussed before committed.
- Python is the operator's primary language.

## Assumptions

- A1. The operator can maintain and audit the generator himself. **Stated**:
  the master CV lists Python as his primary language, read 2026-09-25.
- A2. The content stays small enough that the generator does not grow into a
  framework. **Measured**: fourteen dated items, about twelve content items,
  a handful of sections, counted 2026-09-25. If the item count multiplies,
  this assumption fails and the decision should be revisited.
- A3. A committed build output can be served by GitHub Pages from the
  repository root with no build service involved. **Measured** 2026-09-26 by
  the implementing seat: the site returns 200 at the root and its body is
  byte-identical to the committed `index.html`, as is the stylesheet. Jekyll
  did not process the site: Markdown files serve raw with their front matter
  and `/README.html` is 404. **The cause is `.nojekyll`.** The operator read
  the Pages configuration on 2026-09-27 local and Source is "Deploy from a
  branch", which runs Jekyll by default. Jekyll did not run, and the only
  thing in the repository that suppresses it is `.nojekyll`. That is an
  inference from two observations rather than a direct test; a direct test
  would mean removing the file from a live site, which is not worth doing.

## Considered Options

- A small generator written in Python
- Hand-written HTML and CSS, no build step
- Astro
- A JavaScript static site generator such as Eleventy

## Decision Outcome

Chosen option: "A small generator written in Python".

We will build the site with a small generator written in Python and will not
adopt a site framework.
We will keep its templating to one library, added by this record rather than
by import, and will add no further dependency without a record.
We will hold every item's content as structured data in one place and
generate all markup from it, so that a date or a fact is written once.
We will make the generator fail the build when an item lacks a source
reference to the master CV or lacks either a proof link or a named
verification route.
We will run the build locally and commit its output, rather than building in
a continuous integration service.
We will add a gate that rebuilds from source and fails if the committed
output differs from a fresh build.

### Consequences

- Positive: timeline positions are computed, so they cannot drift from the
  dates silently.
- Positive: two of ADR-0005's confirmation checks stop being review-only and
  become build failures. That is the single largest gain here.
- Positive: the whole build is one language the operator already uses, short
  enough to read end to end, with no node toolchain to rot.
- Positive: building locally sidesteps continuous integration entirely. No
  minutes consumed, no workflow to maintain, and the unverified question in
  A3 about build services never arises.
- Positive: generated output lands in the commit diff, so a change to the
  site is visible as a change, not as a build log.
- Negative: the templating layer is the operator's to write and maintain.
  There is no ecosystem and no community answer when something is awkward.
- Negative: committed output makes diffs noisy, and source and output can
  drift if anyone edits the output directly. The rebuild gate is the answer
  and it must exist before the output is trusted.
- Negative: a later need for client-side interactivity, such as the AI
  assistant, has no framework to fall back on. Against that, the assistant
  as the operator described it, matching what a visitor needs against what
  he offers, may need no client-side code at all.
- Neutral: the repository will hold source and output side by side. The
  layout is left to the implementing brief.

### Confirmation

- `pip list` inside the project environment shows exactly one templating
  dependency. A second dependency without a record fails the review.
- Remove an item's source reference and run the build. It must fail. A build
  that succeeds fails this check.
- Remove an item's proof link and verification route and run the build. It
  must fail.
- Change one item's end date by one month, rebuild, and confirm its grid
  span changes by four units and no other item moves.
- Run the rebuild gate against a deliberately hand-edited output file. It
  must fail.
- Fetch the built page with JavaScript disabled and confirm every layer of
  every item is present, per ADR-0005.

## Pros and Cons of the Options

### A small generator written in Python

- Good: one language, one dependency, fully auditable, and it can enforce
  the content rules rather than merely rendering them.
- Bad: the templating is hand-rolled and unsupported by anyone else.

### Hand-written HTML and CSS

- Good: no dependency, no build, nothing between source and served output.
- Bad: fourteen timeline positions calculated by hand and kept in sync
  manually, with silent failure when they drift.
- Bad: the three-layer markup copy-pasted roughly twelve times, so a change
  to the pattern is twelve edits.
- Bad: no mechanism can enforce that a claim traces to the master CV.

### Astro

- Good: static HTML with no client JavaScript by default, which matches
  ADR-0004 line 7 by construction; islands available if ever needed; a
  GitHub Pages deployment guide exists (research 0002).
- Bad: a framework and a node dependency tree for a site whose entire
  dynamic requirement is arithmetic on fourteen dates.
- Bad: toolchain rot on a site expected to sit unchanged for long periods.

### A JavaScript static site generator such as Eleventy

- Good: lighter than Astro, well established.
- Bad: same node toolchain cost, in a language that is not the operator's
  primary one, with no compensating gain over the Python option.

## More Information

- The deciding comparison was not framework against framework. It was
  whether the build can enforce ADR-0005's rules or only render them. Only a
  generator the operator controls can fail a build on a missing source
  reference, and that is what turns the scope floor from documentation into
  enforcement.
- Not decided here: the repository layout, the templating library by name,
  and where the structured content file lives. Those belong in the first
  implementing brief.
- Left open by ADR-0005 and unaffected by this record: a page-weight budget.
- Revisit if A2 fails, if a genuine need for client-side interactivity
  appears that cannot be met without a framework, or if the rebuild gate
  proves unable to catch hand-edited output.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-09-26 | The three items this record deferred to the first implementing brief are now settled and recorded here: **repository layout** is `build.py` and `requirements.txt` at the root, `src/content/`, `src/templates/`, `src/static/`, `.venv/`, with generated `index.html` and `static/` committed at the root; **the content file** is `src/content/items.json`; **the templating dependency** is `Jinja2==3.1.6`, with MarkupSafe pinned alongside it. | Brief 1 decided all three and the brief is working space that is overwritten and never committed, so the choices would otherwise have survived nowhere. That is exactly the gap `briefs/README.md` warns about. JSON replaced the brief's proposed YAML because the standard library has no YAML parser and a parser would be a second dependency, which scope floor line 14 forbids. |
| 2026-09-26 | The rebuild gate in rule 6 reads an as-of month recorded in the generated output rather than the build date. | Rule 5 commits the output to the repository and rule 6's gate fails when a fresh build differs from it. An item with `end: present` resolves to the build's month, so from 2026-10-01 the gate would have failed on every repository without any content having changed. Recording the as-of month keeps the gate deterministic and makes a monthly refresh a deliberate commit. Raised by the implementing seat, which also corrected the chat's misattribution of the gate to rule 5. |
| 2026-09-26 | Assumption A3 moved from sourced to **measured**. A committed build output is served from the repository root, byte for byte, with no build service. | The site went live on 2026-09-26 and the implementing seat compared the served bytes against the committed output and found them identical. What was an inference from the user-site rule is now an observation. One part stays unverified and is named in A3: whether `.nojekyll` is the cause or the publishing source is a workflow. |
