---
type: explanation
description: "Everything the portfolio site is and does, in one file: how it is built and served end to end, the stack, its engineering qualities and what enforces each, measured numbers with their sources, how it was built, and its limits. For any chat or person who will open nothing else. Kept current."
status: current
---

# Capabilities

**What this file is.** Everything this repository is and does, in one
place, for a reader who will open nothing else. Its readers, as Waqas
Sharif confirmed on 2026-10-10:

- **any chat** that needs to know the project, the resume-tailoring chat
  drafting his CV among them, without exploring the repository;
- **a person** setting the site up or changing it, who reads `README.md`
  to run it and this file for the nuance;
- **an outside reader of this public repository**, such as an interviewer
  who follows the site from his CV, and wants the evidence without reading
  the code. Added by Claude Code on 2026-10-10, under his word
  that readers relevant to this repository may be added.

**Current as of 2026-10-23 UTC**, Claude Code's lane re-measured at the
close of Brief 14. Written by Claude Code, in its lane: what the site
does and how, the stack, the qualities, the numbers, the limits, and the
timeline's rows for what was built. **The architecture chat's sections**
(the problem, where it is going, Waqas Sharif's role, the excluded list
and the timeline's decided rows) **were written 2026-10-10 UTC**, at `main`
fd49b6e, each from a record or the commit history, or marked as his
own account. The role section was brought to the master CV's wording on
2026-10-11.

It decides nothing and is in no role's reading order. Where it disagrees
with the code, the data or a record, it is stale.

---

## In one paragraph

A one-page portfolio site, live at `https://waqas01cp.github.io/`, that
carries the evidence a one-page CV cannot hold. Every claim on it traces
to Waqas Sharif's master CV, and a tool checks that before any content
change. It is built by a small Python generator from two content files
into one HTML page, with every word in the first response, and served free
by GitHub Pages. It sets no cookies, stores nothing and loads nothing from
other sites. On the live site, measured 2026-10-07 in Lighthouse's default
mobile run, the largest paint came at a median of 1.7 seconds and layout
did not shift; a real screen reader (NVDA) read it correctly the same day.
A one-page CV, made from the same master, downloads from the page.

## The problem it solves

A one-page CV cannot hold the evidence behind its lines: what each project
did, in what order, where to see it running, and how the claims were
checked. The site carries that evidence for **employers first and Masters
admissions readers second, from one version** (ADR-0001; `CLAUDE.md`).

Its shape follows how those readers read. Hiring readers rarely read a
portfolio word for word and want curated work (NN/g survey of 204 UX
hiring managers, 2019), and they rely on signals they can verify quickly
(Marlow and Dabbish, CSCW 2013); both in research 0001. So the strongest
work comes first (ADR-0001, ADR-0008), each item opens with one checkable
fact and goes deeper only on request (ADR-0010), and every item that has
public proof links to it.

Before it, his work was carried by his CV and LinkedIn, and the
Rahzaan case study stood alone at `/Rahzaan/`, served from its own
repository (ADR-0002).

## Where it is going

**No version is defined yet** (Working Method 8.10); defining one is
his. The site as built carries every item in the master CV, and
what waits is listed here with its source, as of 2026-10-10, updated 2026-10-21:

- **A CV download: done, 2026-10-11.** `cv/Waqas_Sharif_CV.pdf`, a one-page
  general CV produced from the master CV outside this repository, is live,
  linked from the Intro and the footer (ADR-0008).
- **A template repository, `portfolio-gallery`: done, public since
  2026-10-16,** at https://github.com/Waqas01CP/portfolio-gallery, for
  anyone who wants a site like this one; this repository stays read, not
  reused (ADR-0012). Its licence is MIT, as Waqas Sharif confirmed and
  ADR-0012's Changes record; its own records carry its decisions.
- **Whether this site lists itself as a project: settled, it does not.**
  Waqas Sharif decided not to add it to his master CV as a project
  (`docs/reference/completed.md`; research 0004, decision 1).
- **An open-source lane.** Its section placement is open in the decision
  index's Pending list, to be decided before the brief that brings such
  an item.
- **Listed in emmabostian/developer-portfolios: done,** pull request 4350,
  merged (`docs/reference/completed.md`; research 0004, decision 5).
- **Monthly refresh.** While an item ends "present", the page is rebuilt
  in each new month (`docs/reference/commands.md`).

## What it does, end to end

1. **The source.** His master CV, kept privately and never
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
   12 Jinja2 templates into `index.html` and copies `static/`. When
   `cv/Waqas_Sharif_CV.pdf` exists, the Intro and the footer link to it.
   The footer carries his own one-paragraph account of how the site is
   built, the master's Portfolio Footer word for word, its address a
   link to this repository (ADR-0008 Changes, 2026-10-15).
   On any content failure it writes nothing and exits 1. The output is
   committed.
4. **The content trace.** `tools/check_content.py`, run before any content
   change is committed. Every block of text on the built page, its title,
   description, alt text and labels included, must be a cut of the master
   or approved interface text; and every master bullet, sentence, skills
   line, course, certificate and project link, the summary, the
   Portfolio Intro and the Portfolio Footer must be on the page, the
   footer's address as a link.
5. **The gates.** Seven, in `tools/gates.py`, run by git hooks (ADR-0007):
   nothing private committed; the committed page equal to a fresh build;
   every content string in the page's text without a script; no
   third-party source, cookie, storage or network call, or analytics host
   in the built files; the map current, and every Markdown header one
   GitHub can read; no hook skipping a missing tool; and no push of
   implementation work without the state file moving. What each blocks
   and the case that defeats it: `docs/reference/gates.md`.
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
  committed file holding a path into his private material.
- **The repository is published to be read, not reused.** All rights
  reserved, beyond what GitHub's terms give every user of a public
  repository, to view it and fork it on GitHub (`LICENSE`, 2026-10-10).

## Tech stack

| Area | What is used |
|---|---|
| Build | Python 3.12.10 in a virtual environment; Jinja2 3.1.6 and MarkupSafe 3.0.3, its own requirement; nothing else (ADR-0006, scope floor line 14) |
| Page | HTML, CSS and plain JavaScript; no framework. Three typefaces self-hosted under the SIL Open Font License |
| Hosting | GitHub Pages on the free plan, from a public repository |
| Repository checks | Git hooks running `tools/gates.py`; `tools/generate_map.py`; `tools/check_content.py` |
| Browser checks, outside the repository | Headless Chrome 156 (154 until 2026-10-19, then 155) and Edge 155 through puppeteer-core 25.12.0, axe-core 4.14.0, Lighthouse 13.5.0; not dependencies of the repository (`docs/reference/standing-checks.md`) |
| Design | The visual system Waqas Sharif chose on 2026-10-05, with his changes, from a prototype built in Claude Design from his six reference sites (ADR-0011) |
| AI tooling | Claude Code, to which he delegates implementation, for speed; a Claude chat that works his design into decision records and briefs |

## Engineering qualities, and what enforces each

| Quality | What enforces it |
|---|---|
| Every claim traceable to the master CV | `tools/check_content.py`, page to master and master to page, each check shown able to fail |
| Every word in the first response, readable without scripts and by crawlers | The build renders all content into `index.html`; the page works without `site.js` (ADR-0010, scope floor line 7); gate F refuses a commit whose page lacks any content string in its text without a script |
| A fact is written once | Content files, generated markup (ADR-0006); gate B refuses a hand-edited page |
| Deterministic output | Builds at the recorded month are byte-identical; gate B rebuilds at that month |
| Performance | Core Web Vitals goals (ADR-0009), checked by Lighthouse, median of five, per the standing checks; a fail on any machine is a fail. Each set runs the page, the page before the change and a page with a deliberate 600 ms script that must fail, interleaved run by run, with the machine's CPU, free memory and paging recorded before and after |
| Accessibility | axe at two widths and three theme states; the accessibility tree at load compared with the page without layout skipping; keyboard through every panel; joined-word checks; a recorded NVDA speech test |
| No tracking, no third parties | Scope floor lines 9 to 11; no request leaves the site's origin; gate G refuses an external source, a cookie, storage or network interface, or an analytics host in the built files |
| Reduced motion respected | Every motion stops under `prefers-reduced-motion` (ADR-0011, scope floor line 8) |
| Nothing private published | Gate A |
| The record kept current | Gate C for the map and for headers GitHub can read; gate E for the state file |

## Measured numbers

| What | Value | Date | Source |
|---|---|---|---|
| Hand-written source | `build.py` 784 lines; 3 tools, 1,082 lines; 12 templates, 514 lines; 1 stylesheet, 1,567 lines; 2 scripts, 649 lines; 2 content files, 542 lines | 2026-10-23 | `git ls-files`, `wc -l` |
| Built page | `index.html` 77,163 bytes, 14,941 gzipped; stylesheet 52,193 and 12,248; `site.js` 21,841 and 6,992; `knot.js` 5,638 and 2,215; fonts 78,396 bytes; the CV PDF 58,301 bytes, one A4 page | 2026-10-23 | `wc -c`; Python's gzip, level 6 |
| Live performance | Lighthouse 13.5.0, default mobile, median of five. At light load, Chrome 155, 2026-10-19: LCP 1,670 ms, CLS 0, TBT 63 ms (runs 280, 74, 63, 0, 11); 116,556 bytes transferred. At medium load, Chrome 155, 2026-10-21, the first audit's set: LCP 1,725 ms, CLS 0.031 (above 0 in 3 of 5 runs; the local copy 0 in 5 of 5; cause not tested), TBT 113 ms. ADR-0009 limits: 2,500 ms, 0.1, 200 ms; results compared only within a load level | 2026-10-21 | `logs/2026-10-19-role-wording.md`, Brief 10; `logs/audit/2026-10-21-first-audit.md` |
| Accessibility, automated | axe-core 4.14.0: 0 violations in 12 cells (360 and 1366 px; light, device dark, switched dark; panels closed and open), in Chrome and in Edge | 2026-10-07 | Same log, rounds 1 to 2 |
| Accessibility at load | The full-mode accessibility tree matches the page without layout skipping in 32 of 32 loads locally and 16 of 16 per browser on the live site | 2026-10-07 | Same log |
| Screen reader | NVDA 2026.2 in Chrome: each "In depth" control named and its state spoken, reading into the panel, focus returned; no words run together | 2026-10-07 | Same log, rounds 3 and 5; `docs/deferred/screen-reader-speech-test.md` |
| Keyboard | 60 of 60 checks at 360 and 1366 px | 2026-10-07 | Same log |
| Content | 14 items and 10 skills groups; 378 blocks of text traced to the master, 0 not; every master bullet, italic sentence, skills line, course and certificate, the summary, the Portfolio Intro and the Portfolio Footer on the page; 7 of 7 project links and the footer's link | 2026-10-19 | `tools/check_content.py` |
| Checks on the page, locally | Tree at load in full mode matching the page without layout skipping in 32 of 32 loads, default mode adding no node in 32; keyboard 60 of 60; axe-core 0 violations in 12 cells; measured contrast 0 elements below AA in light and dark at 360 and 1366 px, with 17 and 94 over a gradient unmeasured; the layout check clean at fourteen widths, scripts on and off; no word of a timeline card broken from 1060 to 1920 px; the reading marker never over a label; anchors 132 of 132; no joined words at 360 and 1366 px in Chrome 156 and Edge 155; Lighthouse at light load, median LCP 2,253 ms, CLS 0.0001, TBT 54 ms | 2026-10-23 | `logs/2026-10-19-role-wording.md`, rounds 8 and 9 |
| Decision records | 12, 1 superseded; 51 dated Changes rows | 2026-10-23 | `docs/decisions/` |
| History | 115 commits, the first at 2026-09-25T21:42Z, to `20c8dca`; 9 session logs, 32 rows in their index | 2026-10-23 | `git log`, `logs/` |
| Cost | None | 2026-10-10 | Free plans only |

## How it was built

**Three roles** and a design tool:

| Role | Who | Did |
|---|---|---|
| Architecture and direction | Waqas Sharif | Brought the blueprint and the architecture, made the trade-offs, set the standards, reviewed the design, the logic and the tests and had them corrected (his account, 2026-10-19), and decided every brief and report; see "Waqas Sharif's role" |
| Decisions and briefs: a Claude chat | Claude, in a chat | Refined his design with him into decision records, wrote the briefs, checked each report against the repository |
| Implementation: Claude Code | Claude Code | Built to the briefs he approved: the generator, the templates, the stylesheet and scripts, the checks and gates; logged every session |
| Design prototype: Claude Design | Claude Design | Built a prototype from his six reference sites and the content pack, from which he chose the visual system, with his changes (ADR-0011) |

**Timeline, UTC: what was built.** Rows for what was decided are the
architecture chat's.

| Date | What changed |
|---|---|
| 2026-09-22 to 2026-09-23 | Decided: a sectioned site with projects ranked by importance (ADR-0001); a public user site on GitHub Pages, no custom domain yet (ADR-0002); a hand-built vertical timeline (ADR-0003) |
| 2026-09-25 | First commit: the document skeleton and six accepted records |
| 2026-09-25 | Decided: the scope floor, fourteen lines (ADR-0004); three reading layers (ADR-0005, since superseded by ADR-0010) |
| 2026-09-26 | The generator and content model, and a first, unstyled page carrying the Rahzaan item alone, live at the root; then the five gates, the generated map and the as-of month |
| 2026-09-26 | Decided: a small Python generator (ADR-0006); five repository gates (ADR-0007); eight sections, tiers as order only, no separate project pages (ADR-0008, as amended) |
| 2026-10-02 | Decided: performance as Core Web Vitals goals, not a page-weight figure (ADR-0009) |
| 2026-10-03 | A design-system draft and a 3D prototype |
| 2026-10-03 | Decided: the reading layers consolidated, each item's depth only where the master has material (ADR-0010) |
| 2026-10-05 | Decided: the visual system, from the Claude Design prototype (ADR-0011) |
| 2026-10-06 | The styled site rebuilt in the generator from the approved prototype: one page, eight sections, every master item; the content trace tool |
| 2026-10-06 | Layout skipping measured both ways and kept for speed |
| 2026-10-06 | Decided: a fail on any measuring machine is a fail; layout skipping kept on the condition that a screen reader at load meets the same page (ADR-0009 Changes) |
| 2026-10-07 | The styled site live; everything hidden in the sections also hidden from screen readers, so the tree at load matches; hidden spaces so a screen reader does not run words together; dates shown on one-month timeline entries; the NVDA speech test passed |
| 2026-10-10 | The content trace reads the master's project links and checks them as links; every documented file's frontmatter parses as YAML; a licence notice, all rights reserved, at his instruction |
| 2026-10-10 | Decided: this repository read, not reused; reuse through a separate repository, `portfolio-gallery`, planned (ADR-0012, recorded 2026-10-11) |
| 2026-10-11 | The commands moved to their own reference file; the master's changes on the page (a summary sentence, ten skills groups, the job aggregator's role and method); the trace requires the Portfolio Intro and reads section numbers by markup; the CV PDF checked and added, with its download link |
| 2026-10-12 | Gate C refuses a Markdown header GitHub cannot read; the design-system draft's reserved-name fonts removed; a survey of 200 listed portfolios, research 0005 |
| 2026-10-15 | The footer line on the page, the master's Portfolio Footer word for word, its address a link to this repository; the trace requires both |
| 2026-10-15 | Decided: the footer carries the master CV's Portfolio Footer line, word for word, its address a link to this repository, and the content trace requires it (ADR-0008 Changes) |
| 2026-10-19 | The master's role wording on the page: the summary, a skills item, the job aggregator's role line and two bullets; a new CV PDF, the same wording |
| 2026-10-19 | Decided: his name may appear in `portfolio-gallery`'s showcase, never in what a copy receives (ADR-0012 Changes) |
| 2026-10-20 | Decided: a Lighthouse set counts only on a machine at light or medium load, its level read from free memory and CPU over the minute before; a set at heavy load is void and repeated (ADR-0009 Changes) |
| 2026-10-21 | The master's new role wording on the page and a new CV PDF; the "In depth" button no longer stranded when a card's links wrap; the certificate cards' link cue shown on touch screens; no section marked current without a script; a layout check and a measured contrast check added to the standing checks |
| 2026-10-23 | Gates F and G: a commit is refused when a content string is missing from the page's text without a script, or when the built files carry a third-party source, a cookie, storage or network call, or an analytics host; AGENTS.md, a pointer for other coding agents; CLAUDE.md under 200 lines, five procedures moved to `docs/reference/` |
| 2026-10-22 | The timeline to scale from 1060 px instead of 1180, so a desktop window that narrow gets the desktop timeline, with cards growing to fit their titles; "In depth" starts the next line when a card's actions wrap; the reading marker no longer prints over the axis labels; layout, word-break and marker checks added |
| 2026-10-23 | Decided: floor lines 7, 9 and 10 enforced as pre-commit gates (ADR-0007 Changes); contrast confirmed by a measured check as well as axe (ADR-0011 Changes); the desktop timeline to scale from a 1060 px window (ADR-0003 Changes) |

## Waqas Sharif's role

Updated 2026-10-19 UTC to his own account of that day and the master CV's
role wording of 2026-10-18, which he approved; reworded 2026-10-21 so that
every line has him as its subject. His Working Method calls
his role "the operator"; the records and logs keep that term. Each line
below comes from a record or the commit history, or is marked as his own
account.

- **Designs the architecture, and the algorithms with it.** He defined
  what the site is for and whom it serves: the evidence a CV cannot hold,
  employers first and Masters readers second, in dedicated sections with
  the main projects first and a curated set (ADR-0001, stated
  2026-09-22). The rules the site is built by are his records'
  (`docs/decisions/`); the architecture chat refines his design into them
  rather than starting from nothing (his own account, through the master
  CV, 2026-10-11).
- **Sets the look.** He found the reference sites and proposed the look
  (his own account, 2026-10-19; the sites were reviewed 2026-10-03).
  - He found the first design-system draft basic and restrictive, and the
    visual system was then chosen from the prototype (ADR-0011,
    2026-10-05).
  - He designed the timeline: a vertical spine with lanes either side,
    lane headers travelling down the page, collapse controls and a fixed
    scale per month (ADR-0003, stated 2026-09-23). He reopened it from its
    deferral the same day and shaped it: newest at the top, decided on seeing the design-system
    specimen, so that the latest work is what a reader meets first
    (2026-10-03); and on a phone, one spine with every lane, chosen from
    the prototype's two versions after viewing both on his phone
    (2026-10-05; ADR-0003 Changes).
- **Makes the engineering trade-offs.** He is the decision-maker on all 12
  records, 2026-09-22 to 2026-10-10 (`docs/decisions/`). They include the
  scope floor (ADR-0004), free hosting on GitHub Pages (ADR-0002), speed
  goals set in readers' terms rather than bytes (ADR-0009) and how the
  code may be reused (ADR-0012).
- **He started `portfolio-gallery`.** He asked whether the site should be
  opened for others to reuse, set its priority, credibility through stars,
  forks and pull requests over preventing sale, and confirmed its MIT
  licence (`logs/2026-10-07-tree-parity.md`, rounds 7 and 10; ADR-0012
  Changes, 2026-10-10).
- **Sets the standards the work follows.** Every claim traces to his
  master CV, which he keeps outside the repository (scope floor line 1;
  `tools/check_content.py`). Free services by default (scope floor line
  13). No em-dashes, and dates in UTC (`CLAUDE.md`, Writing). His Working
  Method sets how the work is briefed, built, logged and checked.
- **Reviews the logic and the tests, and has them corrected** (his own
  account, 2026-10-19).
  - He asked that the reading-layers proposal be audited before it was
    recorded rather than accepted on the strength of the proposal; the
    audit changed four things (ADR-0005, 2026-09-22).
  - His screen-reader run found words read as one, which every automated
    check had passed; they were fixed, and his second run passed
    (ADR-0010 Changes, 2026-10-07).
  - He found two inconsistencies on the wide timeline (7e97c5b,
    2026-10-07) and frontmatter a YAML parser rejected (73f2ab3,
    2026-10-10).
- **Decides every brief and report.** A brief is executed and a change
  goes live only on his word. In his words, 2026-10-10: "nothing bypasses
  me".
- **Delegates implementation, for speed, to Claude Code,** which builds
  to specifications he approves, writes the tests, runs the checks and
  logs every session (commit history; `logs/`).

## What it does not do, and its limits

**Excluded by decision:** the scope floor, fourteen lines, from ADR-0004,
restated in `CLAUDE.md`, which governs. In short: no claim outside the
master CV; no skill levels of any kind; no testimonials; no blog or
currently block; no number that cannot be reproduced; no login, CMS or
database; no feature holding the only copy of a fact; no motion that
ignores reduced motion; no embeds that phone home; no cookies or
tracking; no visitor data beyond the host's logs; no prices or payments;
no paid service without prior discussion; no dependency added by import.
Also by decision: no separate project pages, with the Rahzaan case study
the only deeper destination (ADR-0008), and no reuse of this repository
(ADR-0012).

**Limits, as measured:**

- **Live blocking time** was 95 to 138 ms (medians, 2026-10-07) and 58 ms
  (median, 2026-10-12, its first run 481 ms) against about 30 ms for the
  same bytes served locally and compressed; under the 200 ms limit as a
  median, with single runs above it. The cause of the spread is not
  known.
- **Lighthouse on this machine appears to depend on its free memory.**
  The machine has 7.7 GB of RAM. On 2026-10-19 four sets failed ADR-0009
  for this page and the page before it alike (blocking time medians 300
  to 580 ms); minutes after the last of them, available memory read 139
  to 235 MB and committed memory 31 of 31.7 GB. Four sets passed with
  444 to 994 MB available (medians over the minute before each), one of
  them with CPU at 77% from a controlled load. The Chrome version
  changed too: the failing sets ran on Chrome 154, the passing ones on
  155, after it updated itself at 21:48Z; against that, Chrome 154
  passed on 2026-10-15 at nearly the same figures (LCP 2,255 ms, TBT
  49 ms, against 2,255 ms and 42 ms on 155).
  No controlled run reproduced the failure by taking memory away, and
  where between 235 and 444 MB results begin to fail is not measured
  (`logs/2026-10-19-role-wording.md`, Brief 10). Since 2026-10-20 a set
  counts only at light or medium load (ADR-0009 Changes).
- **Gates F and G check known patterns, not every route.** F reads the
  page's markup, not its stylesheet, so text a stylesheet hides passes it
  (the accessibility tree and scripts-off checks cover that); G knows 33
  analytics hosts, not every one, and cannot follow an address a script
  builds in pieces (ADR-0007 Changes, 2026-10-23).
- **A browser that turns accessibility on only after load** meets the
  lower sections when they render, a residual ADR-0009 accepts.
- **Tested only in Chrome 154 to 156 and Edge 154 and 155**, and with one screen
  reader,
  NVDA 2026.2. Firefox, Safari with VoiceOver, phones' screen readers and
  find-in-page are not tested.
- **The 3D knot needs a canvas handed to a worker;** a browser without that
  shows no knot. Not run on Safari.
- **Not licensed for reuse** (`LICENSE`); a template repository with its
  own licence is planned for anyone who wants a site like this one.

## Highlights

*Claude Code's, then the architecture chat's.* Each true as written and
dated.

- A portfolio where every claim traces to a single source document, checked
  by a tool in both directions before any content change (2026-10-10).
- Every word in the first response, readable without scripts, with no
  cookies, tracking or third-party requests; since 2026-10-23 a commit
  that breaks any of the three is refused by a gate.
- Built by a small Python generator with one templating library and no
  framework; 12 decision records and 7 repository gates (2026-10-23).
- Verified with a real screen reader: NVDA found words read as one, such as
  "Dec 20255-Day"; fixed with hidden spaces and confirmed by ear the same
  day (2026-10-07).
- On the live site, Lighthouse medians of 1.7 s largest paint and zero
  layout shift on its default mobile run (2026-10-07).
- Performance measured so a slow machine is not mistaken for a slow
  page: every Lighthouse set runs the page, the page before the change,
  and a page with a deliberate 600 ms script that must fail, five runs
  each, interleaved. On 2026-10-19 both pages failed alike where the
  earlier one had passed four days before, so the change was not
  blamed. The laptop was plugged in when checked, and Lighthouse's own
  speed test of the machine read about the same in failing and passing
  runs. The evidence points to the machine's free memory: with memory
  freed, the page passed (live, LCP 1.7 s, TBT 63 ms), and a controlled
  CPU load of 77% did not make it fail. The failing sets also ran on
  Chrome 154 and the passing ones on 155, though 154 had passed four
  days earlier.
- Every non-obvious choice written as a decision record when it was made,
  each assumption carrying its basis, measured, sourced or stated: 12
  records, 2026-09-22 to 2026-10-10 (the architecture chat's).
- Every implementation report checked against the repository by the
  architecture chat before anything was acted on, and each role's own
  errors logged with what they cost (`logs/`, the chat's briefs; the
  architecture chat's).

## Where the evidence lives

| Question | File |
|---|---|
| How to build it | `docs/reference/commands.md` |
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
