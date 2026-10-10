---
type: explanation
description: Everything the portfolio site is and does, in one file: how it is built and served end to end, the stack, its engineering qualities and what enforces each, measured numbers with their sources, how it was built, and its limits. For any chat or person who will open nothing else. Kept current.
status: current
---

# Capabilities

**What this file is.** Everything this repository is and does, in one
place, for a reader who will open nothing else. Its readers are those the
operator's Working Method names as usual: any chat that needs to know the
project, a chat drafting his CV among them, without exploring the
repository; and a person, who reads `README.md` to set it up and this file
for the nuance. *The operator sets the readers; this paragraph awaits his
or the architecture chat's confirmation.*

**Current as of 2026-10-10 UTC**, against `main` at the commit that added
this file. Written by the implementing seat, in its lane: what the site
does and how, the stack, the qualities, the numbers, the limits, and the
timeline's rows for what was built. **The sections marked as the
architecture chat's are not yet written.**

It decides nothing and is in no seat's reading order. Where it disagrees
with the code, the data or a record, it is stale.

---

## In one paragraph

A one-page portfolio site, live at `https://waqas01cp.github.io/`, that
carries the evidence a one-page CV cannot hold. Every claim on it traces
to the operator's master CV, and a tool checks that before any content
change. It is built by a small Python generator from two content files
into one HTML page, with every word in the first response, and served free
by GitHub Pages. It sets no cookies, stores nothing and loads nothing from
other sites. On the live site, measured 2026-10-07 in Lighthouse's default
mobile run, the largest paint came at a median of 1.7 seconds and layout
did not shift; a real screen reader (NVDA) read it correctly the same day.

## The problem it solves

*The architecture chat's section, not yet written:* why it exists, for
whom, and what was done before it.

## Where it is going

*The architecture chat's section, not yet written:* the end state and what
waits. Open questions it will draw on: research 0004 (whether the site
lists itself as a project, and whether its code is opened for reuse).

## What it does, end to end

1. **The source.** The operator's master CV, kept privately and never
   committed. Content reaches this repository through him or a brief
   (`CLAUDE.md`).
2. **The content files.** `src/content/items.json` holds 14 items (6
   projects, 2 roles, 5 certificates, the degree) and `site.json` the
   page-wide text. Each item carries a checkable fact, then a summary and
   full depth where the master has material for them (ADR-0010). Markup is
   never written per item (ADR-0006).
3. **The build.** `python build.py`, in the project's virtual environment
   with the pinned versions, which it checks before running. It refuses
   content with a missing source, a missing proof link (outside the three
   items ADR-0010 names), projects out of tier order (ADR-0008), or
   shortened text that is not a cut of its source. It resolves "present"
   to the month the page is as of and records it in the page. It renders
   12 Jinja2 templates into `index.html` and copies `static/`. On any
   content failure it writes nothing and exits 1. The output is committed.
4. **The content trace.** `tools/check_content.py`, run before any content
   change is committed. Every block of text on the built page, its title,
   description, alt text and labels included, must be a cut of the master
   or approved interface text; and every master bullet, sentence, skills
   line, course, certificate and project link must be on the page.
5. **The gates.** Five, in `tools/gates.py`, run by git hooks (ADR-0007):
   nothing private committed; the committed page equal to a fresh build;
   the map current; no hook skipping a missing tool; and no push of
   implementation work without the state file moving.
6. **Serving.** GitHub Pages serves `main` from the repository root. A
   push was live 17 seconds later on 2026-10-07; one deployment that day
   never started, because GitHub found no machine to run it, and the next
   push deployed it.
7. **In the browser.** The page is complete without scripts: every panel
   open, every word present. `static/site.js` then closes the "In depth"
   panels, runs the timeline's lane filters and cards, the section menu,
   the progress marker and a light or dark switch for the visit. It adds
   four heavy elements, each kept only while the page meets ADR-0009: a 3D
   knot drawn in a web worker, card tilt, a moving availability strip with
   a pause control, and scroll effects. Under reduced motion nothing moves
   (ADR-0004 line 8, ADR-0011). Sections below the Intro skip their layout
   until near the viewport (ADR-0009), and everything they hide is also
   hidden from screen readers, so a screen reader at load meets the same
   page as without the skipping.

## How data is stored, and where it may go

- **No database, no server code.** The content is two JSON files in the
  repository; the page is static.
- **Nothing about a visitor is kept.** No cookies, no storage, no
  tracking, no third-party requests; fonts and images are served from the
  site (ADR-0004 lines 9 to 11).
- **The master CV never enters the repository.** Gate A blocks any
  committed file holding a path into the operator's private material.

## Tech stack

| Area | What is used |
|---|---|
| Build | Python 3.12.10 in a virtual environment; Jinja2 3.1.6 and MarkupSafe 3.0.3, its own requirement; nothing else (ADR-0006, scope floor line 14) |
| Page | HTML, CSS and plain JavaScript; no framework. Three typefaces self-hosted under the SIL Open Font License |
| Hosting | GitHub Pages on the free plan, from a public repository |
| Repository checks | Git hooks running `tools/gates.py`; `tools/generate_map.py`; `tools/check_content.py` |
| Browser checks, outside the repository | Headless Chrome 154 and Edge 154 through puppeteer-core 25.12.0, axe-core 4.14.0, Lighthouse 13.5.0; not dependencies of the repository (`docs/reference/standing-checks.md`) |
| Design | A prototype built in Claude Design and reviewed by the operator on 2026-10-05 (ADR-0011) |
| AI tooling | Claude Code as the implementing seat; a Claude chat as the architecture seat |

## Engineering qualities, and what enforces each

| Quality | What enforces it |
|---|---|
| Every claim traceable to the master CV | `tools/check_content.py`, page to master and master to page, each check shown able to fail |
| Every word in the first response, readable without scripts and by crawlers | The build renders all content into `index.html`; the page works without `site.js` (ADR-0010, scope floor line 7) |
| A fact is written once | Content files, generated markup (ADR-0006); gate B refuses a hand-edited page |
| Deterministic output | Builds at the recorded month are byte-identical; gate B rebuilds at that month |
| Performance | Core Web Vitals goals (ADR-0009), checked by Lighthouse, median of five, per the standing checks; a fail on any machine is a fail |
| Accessibility | axe at two widths and three theme states; the accessibility tree at load compared with the page without layout skipping; keyboard through every panel; joined-word checks; a recorded NVDA speech test |
| No tracking, no third parties | Scope floor lines 9 to 11; no request leaves the site's origin |
| Reduced motion respected | Every motion stops under `prefers-reduced-motion` (ADR-0011, scope floor line 8) |
| Nothing private published | Gate A |
| The record kept current | Gate C for the map; gate E for the state file |

## Measured numbers

| What | Value | Date | Source |
|---|---|---|---|
| Hand-written source | `build.py` 770 lines; 3 tools, 784 lines; 12 templates, 501 lines; 1 stylesheet, 1,554 lines; 2 scripts, 643 lines; 2 content files, 518 lines | 2026-10-10 | `git ls-files`, `wc -l` |
| Built page | `index.html` 75,222 bytes, 14,341 gzipped; stylesheet 51,253 and 11,888; `site.js` 21,323 and 6,823; `knot.js` 5,638 and 2,215; fonts 78,396 bytes | 2026-10-10 | `wc -c`; gzip level 6 |
| Live performance | Lighthouse 13.5.0, default mobile, two medians of five: LCP 1,721 and 1,739 ms, CLS 0, TBT 138 and 95 ms; 113,387 and 115,692 bytes transferred. ADR-0009 limits: 2,500 ms, 0.1, 200 ms | 2026-10-07 | `logs/2026-10-07-tree-parity.md`, round 2 |
| Accessibility, automated | axe-core 4.14.0: 0 violations in 12 cells (360 and 1366 px; light, device dark, switched dark; panels closed and open), in Chrome and in Edge | 2026-10-07 | Same log, rounds 1 to 2 |
| Accessibility at load | The full-mode accessibility tree matches the page without layout skipping in 32 of 32 loads locally and 16 of 16 per browser on the live site | 2026-10-07 | Same log |
| Screen reader | NVDA 2026.2 in Chrome: each "In depth" control named and its state spoken, reading into the panel, focus returned; no words run together | 2026-10-07 | Same log, rounds 3 and 5; `docs/deferred/screen-reader-speech-test.md` |
| Keyboard | 60 of 60 checks at 360 and 1366 px | 2026-10-07 | Same log |
| Content | 14 items; 394 blocks of text traced to the master, 0 not; 7 of 7 project links on the page | 2026-10-10 | `tools/check_content.py` |
| Decision records | 11, 1 superseded; 34 dated Changes rows | 2026-10-10 | `docs/decisions/` |
| History | 58 commits, the first at 2026-09-25T21:42Z, to `c186714`; 5 session logs, 15 rows in their index | 2026-10-10 | `git log`, `logs/` |
| Cost | None | 2026-10-10 | Free plans only |

## How it was built

**Three seats** and a design tool:

| Seat | Who | Did |
|---|---|---|
| Operator | Waqas Sharif | *The architecture chat's to write, from the records and the operator's account* |
| Architecture chat | Claude, in a chat | Concluded the decisions, wrote the records and the briefs, checked each report against the repository |
| Implementing seat | Claude Code | Built to the briefs: the generator, the templates, the stylesheet and scripts, the checks and gates; logged every session |
| Design | Claude Design | Built the prototype the visual system was settled from (ADR-0011) |

**Timeline, UTC: what was built.** Rows for what was decided are the
architecture chat's.

| Date | What changed |
|---|---|
| 2026-09-25 | First commit: the document skeleton and six accepted records |
| 2026-09-26 | The generator and content model, and a first, unstyled page carrying the Rahzaan item alone, live at the root; then the five gates, the generated map and the as-of month |
| 2026-10-03 | A design-system draft and a 3D prototype |
| 2026-10-06 | The styled site rebuilt in the generator from the approved prototype: one page, eight sections, every master item; the content trace tool |
| 2026-10-06 | Layout skipping measured both ways and kept for speed |
| 2026-10-07 | The styled site live; everything hidden in the sections also hidden from screen readers, so the tree at load matches; hidden spaces so a screen reader does not run words together; dates shown on one-month timeline entries; the NVDA speech test passed |
| 2026-10-10 | The content trace reads the master's project links and checks them as links |

## The operator's role

*The architecture chat's section, not yet written:* what he defined,
designed, decided, caught and did that only he could, each from a record or
the commit history, or marked as his own account.

## What it does not do, and its limits

**Excluded by decision:** the scope floor, fourteen lines, ADR-0004 and
`CLAUDE.md`. *The architecture chat restates them here.*

**Limits, as measured:**

- **Live blocking time** was 95 to 138 ms (medians, 2026-10-07) against
  about 30 ms for the same bytes served locally and compressed; under the
  200 ms limit, with one live run of ten at 208 ms. The cause is not
  known.
- **A browser that turns accessibility on only after load** meets the
  lower sections when they render, a residual ADR-0009 accepts.
- **Tested only in Chrome and Edge 154**, and with one screen reader,
  NVDA 2026.2. Firefox, Safari with VoiceOver, phones' screen readers and
  find-in-page are not tested.
- **The 3D knot needs a canvas handed to a worker;** a browser without that
  shows no knot. Not run on Safari.

## Highlights

*The seat's; the architecture chat adds its own.* Each true as written and
dated.

- A portfolio where every claim traces to a single source document, checked
  by a tool in both directions before any content change (2026-10-10).
- Every word in the first response, readable without scripts, with no
  cookies, tracking or third-party requests.
- Built by a small Python generator with one templating library and no
  framework; 11 decision records and 5 repository gates (2026-10-10).
- Verified with a real screen reader: NVDA found words read as one, such as
  "Dec 20255-Day"; fixed with hidden spaces and confirmed by ear the same
  day (2026-10-07).
- On the live site, Lighthouse medians of 1.7 s largest paint and zero
  layout shift on its default mobile run (2026-10-07).

## Where the evidence lives

| Question | File |
|---|---|
| How to build it | `CLAUDE.md`, Commands |
| What exists now, and what is blocked | `STATE.md` |
| What was finished, with proof | `docs/reference/completed.md` |
| Why it is shaped as it is | `docs/decisions/`, indexed in its README |
| The checks every change runs | `docs/reference/standing-checks.md` |
| What each session did | `logs/README.md`, then the log it names |
| What was deliberately not done | `docs/deferred/` |
| Every documented file | `MAP.md` |

## Keeping this file current

At the close of any session that changes a capability or a measured number:
update the section it belongs to and the date at the top; re-measure a
number rather than carrying it forward, with its new date and source;
remove a number that can no longer be measured; record a removed limit
where it was listed, with the date.
