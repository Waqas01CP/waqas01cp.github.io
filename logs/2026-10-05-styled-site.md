---
type: log
description: Brief 3. The approved Claude Design prototype rebuilt in the generator with every item from the master CV in eight sections; content traced to the master; ten verification checks, each shown able to fail; Lighthouse with and without each heavy element. Committed in series, not pushed.
status: current
---

# 2026-10-05 (UTC): The styled site, with all content

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: ca5e461, working
tree clean apart from the untracked `assets/`. HEAD at end: the commit
carrying this log, after 4fb6a3c, 9fbd407 and 037a50e. Mode: mutating.
Brief: 3. Previous log: 2026-09-26-gates-map-and-as-of.md.

The session began after 22:07Z on 2026-10-05 and its commits were made just
after 00:00Z on 2026-10-06. The local date (UTC+5) was 2026-10-06
throughout.

## What was asked

Brief 3, which is never committed, so its substance is here.

- **Rebuild the approved prototype** (`docs/design/prototype/`, gitignored,
  rendered by a design framework that loads React and Babel from a CDN)
  inside the existing generator as plain generated HTML, hand-written CSS
  and a little vanilla script. The framework never ships.
- **Every item from the master CV**: six projects in ADR-0008's tier order,
  two work entries, the degree with its coursework, five certificates,
  eight skill groups and contact, in the eight sections Intro, Projects,
  Timeline, Work, Education, Certifications, Skills, Contact. Text word for
  word or shortened by cutting words, never by changing a fact. Data shape
  free, each fact written once, the build still failing on a missing source
  and a tier contradiction.
- **Every word in the first response**; scripts only reveal, animate or
  filter. Interactions as enhancement: the section menu with active state
  and progress marker, the phone's floating bar, the theme switch, "In
  depth" panels as a full-width panel under the card's row, timeline detail
  cards with a link to the full entry, phone filter chips, the availability
  strip with a pause control, card tilt and lift, the torus knot on a canvas
  with no library. Hover also by touch and keyboard; all motion stops under
  reduced motion.
- **Contact marks**: LinkedIn's official files from `assets/`, moved;
  GitHub's official mark from github.com/logos, unmodified, or no mark and a
  report. **Fonts**: the three woff2 files with their SIL Open Font
  License texts. **Head**: `lang`, the as-of meta, a title, a description
  from the master's headline; no analytics, no external request.
- **The CV link** in the Intro and the footer only when the PDF exists in
  the tree being built.
- **Content rules**: Rahzaan agentic, never multi-agent; no OCR for
  Rahzaan; no model provider in a stack line; HubIT's bullets word for word
  or cut; never "sole engineer"; the Coursework labels kept; no em-dashes.
- **Ten checks**, each made to fail first: build and gates on every commit
  and a byte-identical rebuild; every master bullet present with scripts
  off; a content trace with a planted number failing; no request off the
  origin and storage empty after every control; device-dark, switch,
  reload; no animation frame in three seconds under reduced motion; axe at
  1366 and 360 px in both themes and distinct "In depth" names; no
  horizontal scroll at 360 px; the timeline to scale and newest first;
  Lighthouse with and without each heavy element.
- **Commit in series, do not push**; bookkeeping last; report in the
  seat-report format.

## What was done

Commits, each through gates A, B and C ("gates A, B, C passed" on each):
4fb6a3c fonts, licences and marks; 9fbd407 the styled site; 037a50e the
content trace and its command; then this bookkeeping. [VERIFIED]

**Content model.** [VERIFIED] `items.json` holds the fourteen dated items
with per-lane fields; `site.json` holds the Intro, the opening figures, the
skills and the contact labels. Bullets, skills lines, coursework and
certificate links were extracted from the master by a script, not retyped;
Rahzaan's nine extracted bullets were byte-identical to those already
committed. The build now refuses any shortened text that is not a cut of
its own source (`layer1`, `detail`, `org_short`, the highlights and the
feature), and a one-bullet project whose `layer2` then `layer1` do not
carry the whole bullet. ADR-0010's three items carry `no_proof`; any other
item without a proof link fails. Schema in `src/content/README.md`.

**Generator.** [VERIFIED] Eight sections; the timeline newest first from
the as-of month to January 2024 at four rows a month (66 px a month on a
wide screen); overlapping entries in one lane set side by side; the degree
band running past the bottom edge; the project grid's spans computed per
width. Output byte-identical on rebuild.

**Speed work, in the order found.** [VERIFIED] A first Lighthouse trial
gave TBT 169 ms. Traces showed: forced layouts in the script's start, then
the knot's first canvas draw (53 ms in a fresh browser, 3 to 6 ms after),
then two full-page layouts of 50 to 90 ms each, the second when the web
fonts swap in. Fixed by moving measurements to the idle start, by drawing
the knot in a worker on a transferred OffscreenCanvas, by
`content-visibility: auto` on the sections below the Intro, and by
preloading all three faces (which removed a 0.03 to 0.04 layout shift).
`content-visibility` broke anchor jumps (targets landed 750 to 15,000 px
off); `html:has(:target) .page > .sec { content-visibility: visible }`
fixed them without a script, and keeping the strip's height when it starts
moving fixed the last 46 px on a phone. Final anchor landings: 96 and 0 px
on desktop, 19 and -1 px on a phone, against margins of 96, 20 and 0.

**Verification.** Every check was first run against a variant built to
defeat it; variants were made in scratch copies or by rewriting responses
in flight, never in the repository.

| Check | Defeated by | Result |
|---|---|---|
| 1 Build, gates, rebuild | (gate proofs: Brief 2) | Gates passed on all four commits; a second build byte-identical; scratch build equals the committed 73,296-byte `index.html` [VERIFIED] |
| 2 Bullets with scripts off | Rahzaan's panel hidden: 19 of 28 | 28 of 28 visible, read one viewport at a time [VERIFIED] |
| 3 Content trace | 592 made 593; 60 made 61; 22 made 11; agentic made multi-agent; a bullet removed: each failed | 396 blocks traced, 0 untraced; 28 of 28 bullets, 17 of 17 italic-line sentences, 8 of 8 skills lines, 26 of 26 courses, 5 of 5 certificates, 9 of 9 headings and dates [VERIFIED] |
| 4 Requests and storage | An image from another site; a script storing and setting a cookie | 0 off-origin requests and empty local, session, IndexedDB, Cache Storage and cookies after 39 control uses at 1366 px and 40 at 360 px [VERIFIED] |
| 5 Device dark, switch, reload | Stylesheet without the device rule; a remembered choice | Below the opening rgb(10, 11, 14); after the switch rgb(243, 241, 236); after reload rgb(10, 11, 14), no `data-theme`, storage empty [VERIFIED] |
| 6 Reduced motion | Script ignoring reduced motion: 470 worker frames in 3 s | 0 frames on the main thread and 0 in the worker, 0 running animations, identical screenshots 3 s apart; control without reduced motion: 472 worker frames [VERIFIED] |
| 7 axe and names | Faint text and an image without alt; two controls with one name | 0 violations at 1366 and 360 px, light and dark; five "In depth" controls, all distinct [VERIFIED] |
| 8 No horizontal scroll at 360 px | A 400 px block: scrollWidth 400 | scrollWidth 360 with scripts on, off, and with every panel and card open [VERIFIED] |
| 9 Timeline | One span altered; the list reordered | 13 entries, every height months x 66 px, every place from its end month, 33 month gaps all 66 px, newest first; the wheel over it scrolls the page [VERIFIED] |
| 10 Lighthouse | A 600 ms script in the head: TBT 1760 ms, fails | See below [VERIFIED] |

Lighthouse 13.5.0, default mobile, Chrome 154, served locally without
compression from this machine; medians of five runs. Results from this
machine are comparable only with each other (ADR-0009).

| Variant | LCP | CLS | TBT | Bytes |
|---|---|---|---|---|
| All four heavy elements | 2108 ms | 0 | 17 ms | 224,000 |
| Without the knot | 2116 ms | 0 | 24 ms | 223,807 |
| Without tilt | 2107 ms | 0 | 0 ms | 224,001 |
| Without the strip | 2115 ms | 0 | 0 ms | 224,001 |
| Without scroll effects | 2113 ms | 0 | 0 ms | 224,001 |
| Without any | 2108 ms | 0 | 0 ms | 223,810 |
| Defeat: 600 ms script | 2113 ms | 0 | 1760 ms | 224,076 |

Every variant meets ADR-0009, so all four heavy elements stay. The knot
costs the main thread nothing measurable because it runs in a worker;
Lighthouse does not see the worker's own cost.

Beyond the ten: the generator's checks, 27 of 27, each failing as built
(missing source, no proof route, two routes, `no_proof` outside ADR-0010's
three, tier contradiction naming both, a changed number in a cut and in a
bullet, a one-bullet project dropping words, a detail and an `org_short`
that are not cuts, an open-source item, a self-origin link, an unknown
field, a highlight that is not a cut; HubIT's end moved a month grows its
span by exactly 4 and moves nothing else; the CV link 0 without the PDF and
2 with it, in the Intro and the footer). Keyboard and accessibility tree,
10 of 10: Tab reaches the first "In depth" control in 17 presses; it is a
button named for its item, collapsed, its layer 3 absent from the tree;
Enter expands it and layer 3 enters the tree; timeline cards open with
Enter and close with Escape returning focus; certificate flood and card
lift on keyboard focus; the phone menu opens and closes from the keyboard.
A gate-A-style scan of the 49 changed paths found nothing; `pip list
--not-required` shows Jinja2 and pip; no em-dash anywhere in the tree.
[VERIFIED]

**Choices the brief left open, and why.**

- Two content files rather than one, because the page's own text (Intro,
  skills, contact) belongs to no dated item. Shortened text stored as
  written and checked as a cut at build time, because a cut cannot be
  derived from its source and a stored copy must not drift from it.
- Timeline: four rows a month at 16.5 px, 66 px a month, the prototype's
  scale on ADR-0003's four units. Ties in the newest-first order: start
  month, then end month, then the content file's order.
- Widths: the prototype's 760, 1040 and 1180 px.
- Work entries show their bullets in full with no disclosure, as the
  prototype does; the master holds nothing beyond them.
- HubIT's dates read "June 2026 to July 2026" in Work and PAC Kamra's and
  the degree's keep both years, the master's own forms; the timeline uses
  the compact form throughout.
- Without a script every "In depth" panel is open under its card, in one
  column, so nothing waits on the script.
- The content trace is committed as a tool with its command in CLAUDE.md,
  which records every command that exists, so the chat can rerun it.
- The operator-approved Intro paragraph is included, as the brief names it,
  and reported.
- The LinkedIn mark in blue on the light page and white on the dark; the
  GitHub Invertocat in white or black against its card's colour.
- The CV link's label "Download CV (PDF)".

**Changes from the prototype, and why.**

- The timeline axis ends at January 2024 with the band running past it
  (ADR-0003); the prototype drew 16 empty months down to September 2022.
- A timeline detail card opens under its entry's title instead of covering
  it, and drops the repeated title, so it can be closed without a script.
  Timeline cards do not tilt, since each holds a disclosure.
- An open "In depth" control keeps its label and turns its + to a minus;
  the prototype relabelled it "Close", which would have given two controls
  one name (ADR-0010).
- Links open in the same tab; the prototype opened new ones.
- The Rahzaan case-study link is root-relative, `/Rahzaan/` (ADR-0002); the
  prototype used the full URL.
- The figure at the head of Projects keeps "592 automated tests" together
  in the reading order; on a wide screen its label sits at the top left.
- The knot runs in a worker, and browsers that cannot hand a canvas to one
  get no knot. The strip keeps its height when it starts moving.
- Real LinkedIn and GitHub marks replace the prototype's placeholders. The
  phone's theme switch sits inside the menu's landmark (axe `region`).
- Live-app links read "Live app"; the prototype said "Live".

**Assets.** [VERIFIED] The fonts are byte-identical to the export (MD5).
Their embedded name tables were read: Instrument Serif 1.000, JetBrains
Mono 2.211, Manrope 4.504, each naming the OFL. GitHub's mark is from the
logo archive at brand.github.com, where github.com/logos now redirects;
its terms permit the Invertocat as a social button linking to a profile.

## Rejected alternatives

- **The knot on the main thread, made cheaper.** Its frames were already
  1 to 3 ms; the cost was the first draw in a fresh browser, which no
  simplification removes. A worker removes it from the main thread.
- **Starting the knot later**, outside Lighthouse's window. It would have
  hidden the cost from the measurement without removing it from a reader.
- **Keeping `content-visibility` and correcting anchors with a script.**
  Readers without scripts, and shared links, would still have landed wrong.
  The `:has(:target)` rule works in CSS alone.
- **Dropping `content-visibility`.** Trials without it gave TBT 95, 193 and
  165 ms: under the limit, but by little.
- **`text-wrap: pretty` removed** to cut layout time: no measurable change.
- **`font-display: optional`**: would remove the swap at the price of system
  fonts on a slow first visit, against the approved look. Preloading fixed
  the shift instead.
- **A free re-split of a block into fragments** in the content trace: it
  let "01 Agentic AI and LLM" pass on one-word fragments of the header.
  Splits now come only from the page's own markup.
- **The timeline detail card covering its entry**, as in the prototype:
  without a script it could not be closed. It opens under the entry's
  title, which stays visible and clickable.

## Checked and found already correct

- The brief's starting state: `main` at ca5e461, only `assets/` untracked,
  hooks active (`core.hooksPath` is `.githooks`).
- Every contact URL, credential link and date on the page against the
  master; the certificate links differ only by the tracking parameters the
  content pack removed.
- The master holds no em-dash or en-dash.

## Not done

- **Push.** Not asked, and the brief places two checks before it.
- **The screen-reader speech test** (`docs/deferred/screen-reader-speech-test.md`):
  needs NVDA and a person; its accessibility-tree half was run, above. Its
  trigger is before the styled site replaces the live one, so it blocks the
  push.
- **The CV PDF**: out of scope.

## Findings and recommendations

1. The Intro's second paragraph is not in the master CV; the content pack
   records the operator's approval of 2026-10-06. Every number in it is in
   the master with the same following word, and the trace reports it on
   every run. Recommendation: add it to the master, so scope floor line 1
   holds without a named exception.
   *Annotated 2026-10-06 by the Brief 4 session: the approval was
   2026-10-05 UTC. The pack carried the chat's local date; this session
   wrote the paragraph into a scratch file at 22:43Z on 2026-10-05.
   Corrected in the content files; logs/2026-10-06-before-push.md.*
2. ADR-0008's Changes row of 2026-10-02 counts 17 courses; the master now
   lists 26, all on the page.
3. ADR-0008's Confirmation says no tier word appears in the rendered text.
   The master's own bullets say "two-tier", "merit-tier", "market-cap
   tier", "reasoning tier" and "tier validation". No tier label or number
   appears. Recommendation: reword the confirmation as "no tier label".
4. ADR-0003's inventory names "Python 3 Specialization, Michigan"; the
   master says "Python 3 Programming Specialization, Michigan".
5. The master's three Coursera links carry `utm_` tracking parameters; the
   pack and the page drop them. Recommendation: drop them in the master.
6. Manrope's licence file from google/fonts gives "Copyright 2018 ...
   googlefonts/manrope"; the font file's own name table gives "Copyright
   2019 ... sharanda/manrope". The licence terms are the same OFL 1.1.
7. The brief names three approved woff2 files; the export holds four. The
   fourth, upright Instrument Serif, is unused and not shipped.
8. STATE.md holds about forty DONE rows that its own rule says belong in
   `docs/reference/completed.md`, which had no rows. This session moved
   only its own rows; the rest is left for a decision.
9. ADR-0011 A1 asked the build brief to check each licence: done, see
   Assets. ADR-0011 A3's unknown knot cost is now measured, above.

## Noticed and not investigated

- Headless Chrome on this machine reported the device as dark when no
  colour scheme was emulated, presumably from the Windows setting.
