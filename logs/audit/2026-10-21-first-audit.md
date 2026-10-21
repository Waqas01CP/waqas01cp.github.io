---
type: log
description: "The first cold audit, read-only, of the repository at 27013c5 and the live site: wording about Waqas Sharif, content, accessibility, performance, records, documents and a visual pass. Verdict: the live site is sound and traces to the master; the wording fails in places, on the page only in the master's footer line; three other reader-facing faults; and several documents and records are stale against the repository."
status: current
---

# 2026-10-21 (UTC): The first audit

| | |
|---|---|
| Date | 2026-10-21 UTC, about 10:25Z to 11:45Z (15:25 to 16:45 local, the same date) |
| Model | Claude Opus 5.5 (claude-opus-5-5), in Claude Code |
| Commit audited | 27013c5 on `main`, equal to `origin/main`; working tree clean at the start |
| Live site | Serves 27013c5's build: 15 live files fetched at 10:35:13Z byte-identical to HEAD; `index.html` Last-Modified 10:22:11Z |
| Mode | Read-only. This report and its index row are the only files written in the repository; every build, variant and harness ran in scratch space outside it |
| Brief | The audit brief of 2026-10-21, written by the implementing seat (Claude Code) at Waqas Sharif's request through the architecture chat; never committed |
| Previous report | None; this is the first |

Tags: [C] checked in this audit, with the command shown; [I] inferred;
[O] from outside the repository. No subagent was used.

## 1. Verdict

**The live site is sound.** It equals a fresh build of 27013c5 byte for
byte; every one of its 378 blocks of text traces to the master CV and
every master line it must carry is on it; the gates do what `CLAUDE.md`
says, each defeated in a scratch clone; axe finds no violation in 12 of 12
cells; the accessibility tree at load matches the page without layout
skipping in 8 of 8 cells; Lighthouse passes ADR-0009 on the live page at
medium load (LCP 1,725 ms, CLS 0.031, TBT 113 ms); and neither "seat"
nor "operator" appears on the page or in the CV PDF. [C]

**What fails is wording, four things a reader meets, and the documents
around the site.** On the page, only the master's footer line fails the
wording rules: it says the implementation is AI-native without naming
Claude Code (F1, master text). A public research file implies he cannot
write languages the site lists among his skills (F5). "Operator" or
"seat" appears in 21 tracked files outside records, logs and
`CLAUDE.md`, `README.md` among them (F9, F10). A reader also meets a
sleeping Streamlit app behind a "Live app" link (F2), certificate cards
with no visible link cue on a touch screen (F3), and an overlap in the
phone's lead figure (F4). Several documents and two records are stale
against the repository: portfolio-gallery is public but `LICENSE` and
`README.md` still call it planned (F6); ADR-0004's promised gates were
never built (F7). Two checks are weaker than they read: axe leaves most
of the page's contrast as "needs review" (F8), and the tree-at-load
defeat fires only at 360 px (F18).

No finding blocks the site. Two need the master's own chat (F1, and the
judgement in F16).

## 2. A verdict for each item the brief listed

| Item | Verdict | Evidence |
|---|---|---|
| 1. Wording about Waqas, every surface | **Incorrect in places** | Page and CV PDF: no "seat" or "operator" [C]. Footer line, master text: F1. Research 0004 and a log: F5. `README.md`: F9. 21 files: F10. Judgement calls: F16. Commit messages, reported only: F22 |
| 2a. Content against the master | **Correct** | Trace PASS, 378 traced, 0 not; coverage complete; defeat exits 1 (section 4) [C] |
| 2a. Content against the records | **Correct** | ADR-0008's eight sections in order, the CV link in the Intro and footer, tier never a label; ADR-0010's proof links; ADR-0003's lanes (section 4) [C] |
| 2b. Accessibility | **Correct on the page, with weak checks** | axe 0 violations in 12 cells; tree at load 8 of 8; reduced motion requests no frame; the switch is forgotten on reload. But F8 and F18 |
| 2c. Performance, ADR-0009 with the load levels | **Correct at medium load** | Live medians LCP 1,725 ms, CLS 0.031, TBT 113 ms; the 600 ms defeat fails by LCP (F19) [C] |
| 2d. Records against the code | **Incorrect in places** | ADR-0012 commitment unmet (F6); ADR-0004's gates never built (F7); ADR-0002's Confirmation fails as worded (F14) |
| 2d. Records against each other | **Correct** | No two live records found in conflict. The decision index's Pending list is stale (F12) |
| 2e. Documents against the repository | **Incorrect in places** | F9, F11, F12, F13, F15, F20 |
| 2f. CAPABILITIES.md against measurement | **Mostly correct; some stale** | Every size, line and content count re-measured equal; dated counts, open questions and CLS stale (F11) |
| 2g. Anything stale | **Yes** | F6, F9, F11, F12, F13, F15, F20, F21 |
| 3. Visual pass, 360 and 1366 px, light and dark by device and by switch, scripts on and off | **Correct, with three reader-facing faults** | 12 configurations read (section 4); F3, F4, F17 |

## 3. Findings, most severe first

Severities, from `logs/audit/README.md`: wrong on the live site; defect;
stale or wrong document; nit.

### F1. Wrong on the live site, master text: the footer says the implementation is AI-native and names no author

- **Where:** the footer at every width, theme and script state;
  `index.html` line 887; `src/content/site.json` line 14.
- **Claim on the page:** "I architected this site; its implementation is
  AI-native and in the open."
- **Evidence:** the footer names no author of the code. The repository's
  own account of the same fact names Claude Code and frames it as his
  choice: "Implementation is delegated, for speed, to Claude Code"
  (`README.md` line 35, `CAPABILITIES.md` line 300). This fails the audit
  brief's wording rule on naming Claude Code where the code's author is
  said (Waqas holds the brief). [C]
- **Route:** this is the master's Portfolio Footer, word for word (ADR-0008
  Changes, 2026-10-15), and the trace requires it whole. A fix goes to the
  master's chat through Waqas; the site follows the master.
- **Command and output:**

```
$ grep -n -o 'I architected[^;]*;[^.]*\.' index.html src/content/site.json
index.html:887:I architected this site; its implementation is AI-native and in the open.
src/content/site.json:14:I architected this site; its implementation is AI-native and in the open.
$ sed -n '/<footer/,/<\/footer>/p' index.html | grep -c "Claude Code"
0
```

### F2. Wrong on the live site, outside the repository: the research project's "Live app" link opens a sleeping app

- **Where:** Projects, the Applied LLM Workflow Research card, its "In
  depth" panel and bullet 03's "(live)" link: three links on the page.
- **Claim:** "Live app", a proof link (ADR-0010).
- **Evidence:** in headless Chrome 155 at about 11:40Z the address showed
  Streamlit's page "This app has gone to sleep due to inactivity. Would
  you like to wake it back up?", with a button to wake it. Not clicked.
  [O] Every other external link on the page answered 200 to curl,
  following redirects. [C]
- **Command and output:**

```
$ node -e '<open the URL in headless Chrome, wait 8 s, print the body text>'
status 200 url https://applied-llm-workflow-research.streamlit.app/
text: Zzzz This app has gone to sleep due to inactivity. Would you like to wake it back up? Yes, get this app back up! ...
$ curl -s -o /dev/null -L --max-time 20 -A 'Mozilla/5.0' -w '%{http_code}' <each https link on the page>
200 for the 14 others; 303 for the Streamlit app (an authentication redirect loop without cookies)
```

### F3. Wrong on the live site: on a touch screen the certificate cards show no sign that they are links

- **Where:** Certifications, all five cards; seen at 360 px, light and
  dark, scripts on and off.
- **Evidence:** each card is a link to its credential, and its only
  visible cue, "View credential" with an arrow, has `opacity: 0` until
  `:hover` or `:focus-visible` (`src/static/site.css` lines 1436 to
  1447). A phone has no hover, so a reader sees a date, a title, an
  issuer and a small square, and nothing that says "tap". The timeline
  card's "Credential" link still reaches each one. ADR-0011 asks the
  heavy elements to "work by touch as well as hover"; this card is not
  one of them, so this is a reader-facing fault, not a breach of a
  record. [C] for the CSS and the screenshots; that readers miss the link
  is [I].
- **Command and output:**

```
$ sed -n 1436,1447p src/static/site.css   (abridged)
.cert-view {
  ...
  opacity: 0;
  ...
.cert:hover .cert-view, .cert:focus-visible .cert-view { opacity: 1; transform: none; }
$ grep -n "hover: none\|any-hover\|pointer: coarse" src/static/site.css
(no output)
```

### F4. Wrong on the live site, visual: at 360 px the figure card covers part of "592" and splits it from its label

- **Where:** Projects, the Rahzaan feature card, 360 px, every theme and
  script state (the screen at about 15% of the page).
- **Evidence:** the white card holding "19 behavioural probes" and "60
  per-turn traces" overlaps the lower edge of the large "592" and sits
  between it and its label "automated tests", so the eye reads "60
  per-turn traces" then "automated tests". At 1366 px the card sits to
  the top right and nothing overlaps. Screenshot read: 360 by 780,
  light, scripts on, scrolled one viewport at a time. [C]

### F5. Defect: a public research file implies he cannot write languages the site lists among his skills

- **Where:** `docs/research/0004-this-site-as-a-project-and-as-a-template.md`
  lines 57 to 62.
- **Claim:** "The code here was written by AI seats under the operator's
  direction ... Listing HTML, CSS, JavaScript or Jinja2 as skills is a
  claim an interviewer can test by asking him to write some. The rule
  that governs is the operator's own: a claim he cannot stand behind in
  an interview does not go on the site."
- **Evidence:** the page's Skills section lists JavaScript under
  Languages, from the master. Read together, the passage says he could
  not stand behind JavaScript in an interview. That is wording that
  implies he cannot code, which the repository's own rule forbids ("no
  wording may imply he cannot code", `logs/2026-10-19-role-wording.md`
  lines 33 to 34). It also uses "seats" and "operator" in public text
  about him (F10). The same claim is in `logs/2026-10-07-tree-parity.md`
  line 626 ("Languages written by AI seats are not defensible as
  skills"). Logs are never modified, so a correction there is a new row
  or note. Research is evidence, never a decision, and can carry a dated
  annotation. [C]
- **Command and output:**

```
$ git grep -n -I -i -E "AI seats?|ask(ing)? him to write|cannot stand behind" -- . ':!index.html'
docs/research/0004-...md:57:- **Languages and frameworks as skills.** The code here was written by AI
docs/research/0004-...md:60:  claim an interviewer can test by asking him to write some. The rule
docs/research/0004-...md:61:  that governs is the operator's own: a claim he cannot stand behind in
logs/2026-10-07-tree-parity.md:626:  trace, measured performance, an NVDA test). Languages written by AI
(and others: CLAUDE.md line 69, ADR-0012 lines 54 and 101, which do not imply it)
```

### F6. Defect, a record against the repository: portfolio-gallery is public, but LICENSE and README still call it planned

- **Where:** `LICENSE` lines 15 to 16; `README.md` lines 77 to 78;
  `CAPABILITIES.md` line 78.
- **Claim in the record:** ADR-0012, Decision Outcome: "`LICENSE` and
  `README.md` will name its address once it is published" (line 79).
- **Evidence:** `github.com/Waqas01CP/portfolio-gallery` is public,
  created 2026-10-16T19:45:23Z [O, GitHub's API].
  `docs/reference/completed.md` records "portfolio-gallery published",
  2026-10-20. `LICENSE` still reads "is planned for that purpose. When it
  is published, its address will be given here and in README.md." ADR-0012
  also bars listing it on the site before it is in the master; `LICENSE`
  and `README.md` are not the site. [C]
- **Command and output:**

```
$ curl -s https://api.github.com/repos/Waqas01CP/portfolio-gallery | grep -E '"(private|visibility|created_at)"'
  "private": false,
  "created_at": "2026-10-16T19:45:23Z",
  "visibility": "public",
$ grep -n -E "planned|When it is published" README.md LICENSE
README.md:78:planned for anyone who wants a site like this one.
LICENSE:15:template repository, with its own licence, is planned for that purpose.
LICENSE:16:When it is published, its address will be given here and in README.md.
```

### F7. Defect, a record against the code: ADR-0004's gateable lines were never built as gates

- **Where:** `docs/decisions/0004-scope-floor.md` lines 125 to 136;
  `tools/gates.py`.
- **Claim in the record:** "Gateable, and to be built as gates before the
  first feature": line 7 (fetch the page without scripts, every claim
  present), line 10 (grep the output for cookie APIs and analytics
  hosts), line 9 (grep for external script and iframe sources outside an
  allowlist), line 14 (a dependency without a record fails review).
- **Evidence:** the five gates of ADR-0007 cover none of lines 7, 9 and
  10; ADR-0004 has no Changes row, and no record says the plan changed.
  The page meets lines 9 and 10 today: it loads nothing from another
  origin, and the shipped scripts use no storage, cookie or network API
  (below). Line 7 holds in practice, since the build renders every word
  into `index.html` and the trace reads it. Line 14 is the one-dependency
  check, run by hand (it passes). This is a record whose Confirmation is
  unmet, not a page fault. Whether to build the gates or amend the record
  is the chat's and Waqas's. [C]
- **Command and output:**

```
$ grep -o -E '(src|href)="[^"]*"' index.html | grep -v -E '"(/|#|mailto:)' | grep -c src=
0
$ grep -n -E 'localStorage|sessionStorage|document\.cookie|fetch\(|XMLHttpRequest|sendBeacon|navigator\.' static/site.js static/knot.js
(no output)
$ grep -n -i -E "cookie|analytics|iframe" tools/gates.py
(no output)
```

### F8. Defect, in a check: axe leaves most of the page's contrast as "needs review", so "0 violations" covers little of it

- **Where:** `docs/reference/standing-checks.md`, the axe row; ADR-0011
  Confirmation ("axe-core reports no contrast violation in either
  theme"); `CAPABILITIES.md` lines 191 and 195.
- **Evidence:** on the live page, axe-core 4.14.0's `color-contrast` rule
  passed 30 text nodes and left 349 as "needs review" (incomplete) at
  360 px, and passed 218 and left 194 at 1366 px. The reasons it gave:
  an element overlapping the text (241 at 360 px), a gradient background
  (25, and 89 at 1366 px), pseudo-element content (74). The standing
  check counts violations only, so a contrast regression in most of the
  page's text would pass it. [C]
- **What holds:** axe does catch a fault it can measure, in every
  section, as loaded: faint text (#eee on #fff) appended in the Intro,
  in Projects, inside a project card, in Skills and at the end of
  Contact was a violation each time [C]. My first plant, at the very
  top of Projects, was not: it sat under the section's faded heading
  word, and axe answered "needs review". That was my mistake, and it
  disproved my first guess that layout skipping blinds axe. My own
  estimate covered the rest: each text element's colour, with alpha and
  ancestor opacity applied, against the nearest solid background,
  gradients ignored, on the live page with every section rendered, at
  1366 and 360 px, light and dark. It found nothing below WCAG AA except
  its own artefacts: the "View credential" labels, which are hidden by
  design (F3), and the nav over a translucent background. Its defeat, a
  #c8c8c8 span planted in a Skills heading, was caught at 1.67. [C] for
  the counts; that the page passes AA is [I], an estimate.
- **Command and output:**

```
$ node axe-inc.js     (axe.run with runOnly color-contrast; counts passes, violations, incomplete)
1366 light {"pass":218,"viol":0,"inc":194,"why":{"bgGradient":89,"bgOverlap":84,"pseudoContent":15,...}}
360 light {"pass":30,"viol":0,"inc":349,"why":{"pseudoContent":74,"bgGradient":25,"bgOverlap":241,...}}
$ node axe-probe.js   (faint text appended at five places; violation / needs review)
as loaded | intro .wrap | violation 1 ... | contact .wrap (end) | violation 1   (5 of 5)
```

### F9. Stale or wrong document: README.md uses "operator" and two of its statements are stale

- **Where:** `README.md` line 63; lines 22 to 24; lines 77 to 78 (F6).
- **Evidence:** line 63 reads "The operator's master CV is the only source
  of truth". `README.md` is the repository's public entry point. The
  repository's rule keeps "seat" to records, logs and `CLAUDE.md`
  (`logs/2026-10-19-role-wording.md` lines 36 to 38), and
  `CAPABILITIES.md` line 243 says of "the operator" that "the records and
  logs keep that term". Lines 22 to 24 say `CHAT_STATE.md` "is the one
  file that is never committed ... and will also be blocked by a gate".
  Gate A has blocked it since 2026-09-26 (proven below), and `briefs/`,
  `.commitmsg` and `cv/UPDATING.md` are never committed either. [C]
- **Command and output:**

```
$ grep -n -E "is the one file|blocked by a gate|operator's master CV" README.md
22:The repository is public, per ADR-0002. `CHAT_STATE.md` is the one file that
24:`.gitignore` and will also be blocked by a gate.
63:The operator's master CV is the only source of truth for anything this site
```

### F10. Stale or wrong document: "seat" or "operator" in 21 tracked files outside records, logs and CLAUDE.md

- **Evidence:** 91 lines in 21 files. By count:
  `docs/reference/completed.md` 18, research 0004 15, `STATE.md` 12,
  `MAP.md` 7 (generated from other files' descriptions), research 0003 5,
  `docs/deferred/multi-page-site.md` 5, `docs/reference/commands.md` 4,
  `docs/deferred/projects-timeline.md` 4, research 0005 3,
  `docs/deferred/screen-reader-speech-test.md` 3, `tools/check_content.py`
  2, `src/content/README.md` 2, research 0002 2, `.gitignore` 2,
  `tools/gates.py` 1, `src/templates/projects.html.j2` 1 (a template
  comment, not rendered), `docs/reference/standing-checks.md` 1,
  `docs/design/system/README.md` 1, `README.md` 1 (F9),
  `CAPABILITIES.md` 1 (line 243, naming the term to say where it is kept:
  a mention, not a use), `.gitattributes` 1. [C]
- **Scope, for Waqas:** the rule names "records, logs and `CLAUDE.md`".
  Whether `STATE.md`, `docs/reference/` and `docs/deferred/` count as
  records is not written anywhere. `README.md`, `src/content/README.md`,
  the research files, the design-system README and code comments do not
  count as records on any reading. Not decided here.
- **Command and output:**

```
$ git ls-files | grep -v -E '^(docs/decisions/|logs/|CLAUDE.md)' | grep -v -E '\.(woff2|png|pdf|svg)$' \
    | xargs -d '\n' grep -c -i -E '\b(seats?|operators?)\b' | grep -v ':0$'
docs/reference/completed.md:18 docs/research/0004-...:15 STATE.md:12 MAP.md:7 ... .gitattributes:1   (21 files)
$ grep -c -i -E '\b(seats?|operators?)\b' index.html; pdftotext cv/Waqas_Sharif_CV.pdf - | grep -c -i -E '\b(seats?|operators?)\b'
0
0
```

### F11. Stale or wrong document: CAPABILITIES.md is behind the repository in five places

- **Open questions already decided.** Lines 78, 82 and 87 call
  portfolio-gallery "planned", say whether the site lists itself "waits
  on the master CV first", and call the emmabostian listing "Open".
  `docs/reference/completed.md` records all three as settled on
  2026-10-20: "portfolio-gallery published"; "Decided: no" on listing
  itself; the listing "pull request 4350, merged" (his account). These
  rows are the architecture chat's lane. [C]
- **The date line.** Line 22 says "Current as of 2026-10-19 UTC". The
  file last changed in 5242831 at 2026-10-20T11:05:13Z. [C]
- **Layout shift.** Lines 46 to 47 say layout "did not shift", and the
  2026-10-19 row reads CLS 0. Today's live set, at medium load, had CLS
  above 0 in 3 of 5 runs (0.031, 0.044, 0.031; median 0.031), still under
  ADR-0009's 0.1. The local copy in the same set: 0 in 5 of 5. The cause
  is not tested. [C]
- **Dated counts left behind.** "42 dated Changes rows" (2026-10-12) is
  now 47; "93 commits ... 24 rows" (2026-10-19) is now 98 commits and 27
  rows. Each was true on its date; the file's own rule is to re-measure.
  [C]
- **Order.** The timeline table runs 2026-10-15, 2026-10-19, 2026-10-15,
  2026-10-19 (lines 233 to 236). [C]
- **Command and output:**

```
$ for f in docs/decisions/0*.md; do <count Changes rows dated 20xx>; done   -> total changes rows 47
$ git rev-list --count HEAD   -> 98;   grep -c '^| 20' logs/README.md   -> 27
$ TZ=UTC git log -1 --format='%h %cd' --date=iso-local -- CAPABILITIES.md
5242831 2026-10-20 11:05:13 +0000
```

### F12. Stale or wrong document: the decision index's Pending list holds closed and outdated items

- **Where:** `docs/decisions/README.md` lines 72, 79 to 80 and 86.
- **Evidence:** line 79 lists "the collapse control's behaviour at each
  breakpoint. Left open by ADR-0003" as pending, but ADR-0003's Changes
  row of 2026-10-05 says it "Closes the collapse-behaviour question this
  record left open". Line 86 says three projects' URLs are "still missing
  from the master CV"; all three carry proof links on the page, which the
  build refuses without. Line 72 describes the degree as "a line in the
  Intro plus the timeline band"; since ADR-0008 Changes 2026-10-02 it
  also has the Education section. [C]

### F13. Stale or wrong document: a local date written as UTC

- **Where:** `logs/2026-10-19-role-wording.md` line 479, "Round 4,
  2026-10-21 (UTC)"; `logs/README.md` line 57, the row dated 2026-10-21;
  `.gitignore` line 6, "instruction of 2026-10-21".
- **Evidence:** the round's commit, 2bf8e41, was made at
  2026-10-20T22:38:01Z, which was 2026-10-21 03:38 local. The work and
  the instruction it carries came before that commit, so on 2026-10-20
  UTC. `CLAUDE.md`, Writing: "Dates are UTC". [C]
- **Command and output:**

```
$ TZ=UTC git log -1 --format='%h %cd %s' --date=iso-local 2bf8e41
2bf8e41 2026-10-20 22:38:01 +0000 The briefs folder off the repository, its README included
```

### F14. Stale or wrong document: ADR-0002's Confirmation fails as worded, and "anywhere" is not quite true

- **Where:** `docs/decisions/0002-hosting-and-addressing.md` line 118;
  `CLAUDE.md`, Conventions.
- **Evidence:** the Confirmation reads "A grep of the built output finds
  no occurrence of `waqas01cp.github.io` ...". Since 2026-10-15 the
  footer links to the repository, `github.com/Waqas01CP/waqas01cp.github.io`,
  so that grep finds it twice in `index.html`. That link is not the
  site's own origin, and the intent holds. Separately, `CLAUDE.md` says
  no absolute URL to this site's origin "appears anywhere". It appears in
  `CAPABILITIES.md` line 39 and `docs/deferred/screen-reader-speech-test.md`
  line 114 as prose, and in the CV PDF as a link, where a PDF read off the
  site needs it. [C]
- **Command and output:**

```
$ grep -o -n -E '.{0,40}waqas01cp\.github\.io.{0,20}' index.html
887:: <a href="https://github.com/Waqas01CP/waqas01cp.github.io">github.com/Waqas01
887:CP/waqas01cp.github.io</a></p>
```

### F15. Stale or wrong document: STATE.md lists as blocked a push that has happened

- **Where:** `STATE.md` line 138: "The push of Brief 12's commit | The
  operator".
- **Evidence:** `origin/main` is 27013c5, and the live page is its build.
  A commit cannot record its own push, so this lag is built in. It is
  listed so the next session clears it. [C]

```
$ git ls-remote origin refs/heads/main
27013c53812cf3020e89e54c77c11f9eb5017b9b	refs/heads/main
```

### F16. Nit, a judgement for Waqas, master text: how the agent's part is phrased

These do not clearly breach a rule; they are listed because the brief's
rules turn on tone. [I]

- **The job aggregator's role line** (Projects, its card; `items.json`):
  "Architect and director: the design, the algorithms, the trade-offs and
  the decisions are mine; Claude Code writes the code to specifications I
  approve, under a working method I designed." It names Claude Code. It
  does not phrase the delegation as his choice, as `README.md` line 35
  does. And it sets his part against the agent's in one sentence, which
  may read as the defence the rules warn of. The repository's rule of
  2026-10-11 is narrower ("never contrast him with other ways of
  building", `logs/2026-10-11-review-commands-cv.md` lines 46 to 48),
  and this is not that. The CV PDF's job-aggregator line divides the
  work the same way.
- **The summary** (Intro): "directs coding agents that implement to
  written specifications". It says who writes code without naming Claude
  Code. Which agents built which projects is not in this repository, so
  whether Claude Code should be named here cannot be verified.
- **CAPABILITIES.md** line 166: "Claude Code writes the code to the
  briefs" is not phrased as his choice. Lines 297 to 298: "He makes every
  commit of the architecture chat's work and every push" may read as
  operating, against "never describe him as routing or operating" (log
  of 2026-10-11, line 47). Lines 294 to 295 ("The code itself is checked
  by the repository's gates, and against the repository by the
  architecture chat") say who checks the code; they do not say he could
  not.

### F17. Nit, live, scripts off: the menu stays on "01 Intro" all the way down

- **Where:** the phone's floating menu and the desktop bar, scripts off,
  both themes.
- **Evidence:** without the script, the phone menu's label reads "01
  Intro" on every screen, and the desktop bar keeps "Intro" highlighted.
  `nav.html.j2` sets `aria-current="location"` on Intro statically. The
  page is complete and readable; only the "you are here" state is wrong
  once the reader scrolls. Screenshots: 360 and 1366 px, light, scripts
  off, every screen. [C]

### F18. Nit, in a check: the tree-at-load defeat I could build fires at 360 px only

- **Evidence:** I built a defeat with `setShown` no longer setting
  `aria-hidden` on what it hides. It differed from the reference at
  360 px with scripts on, light and dark: the hidden "In depth: Rahzaan"
  heading was exposed. It matched the reference in the other 6 cells. So
  in my run the parity check is proven at 360 px with scripts on, and
  unproven elsewhere by this defeat. Scripts off cannot differ by
  construction: the script is what hides things. The standing check's
  own defeat, the page at 0403c68, was not run. [C]

### F19. Nit, in a check: the 600 ms defeat fails by LCP, not by TBT

- **Evidence:** in today's set the page with a 600 ms synchronous script
  at the top of its head had TBT medians of 48 ms (runs 83, 48, 0, 4,
  413), under the limit, and LCP medians of 3,855 ms, over it. A script
  that blocks before first paint delays paint; it is not counted as
  blocking time. The defeat still fails ADR-0009 as a whole. It shows the
  LCP check can fail, not the TBT check. The record's own TBT defeat
  (ADR-0009 Changes, 2026-10-03, 1,183 to 1,254 ms) was on a different
  page and machine. [C]

### F20. Nit: two small document drifts

- `tools/gates.py` line 75: "Gate E. This scope is Brief 2's, not a
  record's." ADR-0007 Changes, 2026-09-26, records the scope, and
  `CLAUDE.md` says so. [C]
- `docs/reference/commands.md` lists `tools/check_content.py --master`
  only. The tool also takes `--page`, used in this audit to trace the
  live copy and the defeat copy. [C]

### F21. Nit, local only, not public: leftover chat commit messages

- `.commitmsg/` (gitignored) holds `1-role-and-records.txt` and
  `2-measuring-load.txt`, whose commits exist (12084bc, 750faec), and
  `held-0009-row.md`, a superseded draft of ADR-0009's row.
  `docs/reference/commands.md` says to delete the files and the folder
  once the commits are made and pushed. Its `.gitignore` comment says
  "The implementing seat commits with it"; `commands.md` says Waqas runs
  these commits. [C]

### F22. Reported only: commit messages

75 of 98 commit messages hold "seat" or "operator", for example 502b6a5
"CAPABILITIES.md: the implementing seat's lane". History is not
rewritten. No message implies he cannot code; the two "line by line"
hits describe checks of text. [C]

```
$ git log --format='%H' | while read h; do git log -1 --format='%B' $h | grep -q -i -E '\b(seats?|operators?)\b' && echo $h; done | wc -l
75
```

## 4. What was checked and found correct

Each with what would have shown it failing.

- **The live site equals the commit.** [C] Fifteen files (`index.html`,
  `static/` stylesheet, scripts, three fonts, four marks, three OFL
  texts, and the CV PDF), fetched at 10:35:13Z, byte-identical to HEAD
  by `cmp`. Failing case: any differing byte; the build as of 2026-11
  below differs from the commit at byte 244.
- **Build twice.** [C] Two builds in scratch copies of 27013c5
  (`git archive HEAD`), `--as-of 2026-10`: `index.html`, `site.css`,
  `site.js` and `knot.js` hash the same as each other and as the commit;
  `static/` identical by `diff -r`. Defeat: `--as-of 2026-11` changes
  `index.html` (5a2535... becomes 9025b1...).
- **Content trace.** [C] `python tools/check_content.py --master <path
  to the master CV>`: 378 blocks traced, 0 not; summary, Portfolio Intro
  and Portfolio Footer 1 of 1 each, footer link 1 of 1, skills lines 10
  of 10, headings 9 of 9, heading dates 9 of 9, project links 7 of 7,
  italic-line sentences 17 of 17, bullets 28 of 28, courses 26 of 26,
  certificates 5 of 5; PASS, exit 0. The same on the live copy (`--page`).
  Defeat: a copy with "592 automated tests" made "593": 3 not traced, 2
  missing, FAIL, exit 1.
- **Gates, in a scratch clone** with a copy of the venv and
  `core.hooksPath` set. [C] Gate A refused `CHAT_STATE.md` and
  `briefs/README.md` staged with `-f`, and a planted drive-letter path
  (named with file, line and match); control, prose naming the Working
  Method: committed. B refused a one-character edit to `index.html`, and
  `items.json` changed without a rebuild. C refused a new Markdown file
  without a regenerated map, and an unquoted ": " in a description. D
  refused with the map generator renamed. E refused a push range with a
  `src/` change and no `STATE.md`; control, `STATE.md` in the last commit
  only: passed. The repository itself was not touched.
- **Gate A's patterns over every tracked file.** [C] Its own
  `pointers_in` over all 92 tracked text files: 0 hits. Failing case:
  the planted path above. No tracked path is a never-commit path.
- **Map and dependencies.** [C] `generate_map.py --check` exit 0;
  `pip list --not-required`: Jinja2 3.1.6 and pip only.
- **Scope floor on the page.** [C] Line 9: no external `src`; every
  external URL is a plain link. Line 10 and 11: no storage, cookie or
  network API in the shipped scripts; after using the switch and
  reloading, `localStorage` 0, `sessionStorage` 0, cookies 0. Line 2: the
  Skills section shows names only, no levels (screens read). Lines 4, 6,
  12: no blog, login or prices (screens read). Line 8: under reduced
  motion, 0 animation frames requested in 3.5 s after load with one
  scroll; 54 without it, the defeat.
- **ADR-0008.** [C] Eight sections in the record's order (`build.py`
  SECTIONS and the screens); "Download CV (PDF)" in the Intro and the
  footer; "tier" appears 5 times on the page, all in master text
  ("two-tier", "merit-tier" and the like), never as a label; the job
  aggregator carries "In development".
- **ADR-0010.** [C] Every item but HubIT, PAC Kamra and the degree
  carries a proof link (the build refuses otherwise); WordPy, with one
  bullet, has no disclosure; each control's name carries its item.
- **ADR-0011.** [C] Only the three typefaces, served from `static/fonts/`;
  the Intro dark in light mode; the switch overrides for the visit and a
  reload discards it; reduced motion as above.
- **axe-core 4.14.0, default rules, live page.** [C] 0 violations in 12
  of 12 cells: 360 and 1366 px; light, dark by the device, dark by the
  switch read 3 s after; as loaded, and with every "In depth" panel open
  and each of the 13 timeline cards opened in turn. Repeated with every
  section rendered: 0 in 12. Defeat: an image without alt and faint text
  planted, violations in 12 of 12 (but see F8 on what the contrast part
  showed).
- **Tree at load, full mode, live page.** [C] Matches the page without
  the rule, served locally, in 8 of 8 cells: 360 and 1366 px, light and
  dark, scripts on and off, one load per cell, a fresh headless Chrome
  155 each, CDP `Accessibility.getFullAXTree` 1.5 s after load. Defeat:
  F18.
- **Opened states.** [C] At 1366 and 360 px, an "In depth" control
  opened by click sets `aria-expanded="true"`, shows its panel and keeps
  focus. Three timeline cards opened (the rightmost certificate, a
  certificate and a build) place their popovers inside the viewport.
- **Lighthouse, ADR-0009, at medium load.** [C] Readings over the 60 s
  before, with no Lighthouse browser running, 11:25:17Z to 11:26:18Z:
  available memory median 668 MB (medium), CPU median 26.1% (light); the
  level is medium. Committed memory 26.4 of 31.7 GB. Most memory: claude
  644 MB, Code 277 MB, MsMpEng 217 MB. Chrome 155.0.8059.85, read from
  its file. Claude Cowork's VM was down (vmmem 8 MB). **Waqas's own
  Chrome was still running when the readings began** (one browser
  process, Default profile, started 2026-10-20T20:30:57Z, 13 processes,
  about 352 MB). It was gone by 11:44:55Z; he closed it from Task
  Manager. When it closed was not measured, so it may have run through
  some or all of the set; its memory is inside the readings above. At
  11:32:58Z two headless Chrome processes were running and gone moments
  later. I took them for Lighthouse's own, exiting. From 11:38Z, a script
  for portfolio-gallery in another session was also launching headless
  Chrome, so they may have been that. Not verified.
  Lighthouse 13.5.0, default mobile, simulated throttling, 15 runs
  interleaved, 11:26:53Z to 11:31:42Z:

| Page | LCP runs (ms) | LCP median | CLS median | TBT runs (ms) | TBT median | Verdict |
|---|---|---|---|---|---|---|
| Live | 2240, 2181, 1725, 1625, 1513 | 1,725 | 0.031 | 488, 377, 113, 10, 16 | 113 | Pass |
| The same build, local, uncompressed | 2279, 2290, 2257, 2263, 2297 | 2,279 | 0 | 89, 0, 63, 4, 131 | 63 | Pass |
| 600 ms script in the head, local | 3952, 3855, 3674, 3692, 4601 | 3,855 | 0 | 83, 48, 0, 4, 413 | 48 | Fail (LCP) |

  Readings over the 60 s after, 11:31:57Z to 11:32:58Z: memory median
  348 MB (heavy), CPU median 43.2% (medium), committed 27.5 of 31.7 GB.
  ADR-0009 sets the level from the minute before, so the set counts at
  medium. The heavier readings after are recorded, not used. Two live
  runs exceeded 200 ms TBT, as the record's 2026-10-07 and 2026-10-12
  rows also saw. Results at medium are comparable only with medium
  results.
- **The CV PDF.** [C] One A4 page (595.3 by 841.9 pt), PDF 1.7, title
  "Waqas Sharif CV", author "Waqas Sharif"; links to his LinkedIn, the
  site and his GitHub; no private path in its bytes or decompressed
  streams; no "seat" or "operator"; all 25 distinct numbers in it are on
  the page (defeat: 593 is not). It is a reworded one-page CV, not cuts:
  65 of its 90 sentences and pieces are cuts of one master paragraph by
  the trace's rules, and 25 are rewordings or line-wrap joins, which the
  trace was not built for. No claim in it contradicts the page.
- **CAPABILITIES.md's numbers.** [C] Equal today: `build.py` 784 lines;
  3 tools, 867; 12 templates, 507; stylesheet 1,558; 2 scripts, 643;
  content 542; `index.html` 76,925 bytes, 14,864 gzipped; stylesheet
  51,550 and 11,981; `site.js` 21,323 and 6,823; `knot.js` 5,638 and
  2,215; fonts 78,396; PDF 58,639; 14 items (6 projects, 2 roles, 5
  certificates, the degree); 10 skills groups; 378 blocks; 12 records, 1
  superseded; the first commit at 2026-09-25T21:42:07Z; 93 commits to
  12084bc. Stale ones: F11.
- **Records against each other.** [C, by reading] All twelve records
  read. ADR-0001's timeline clause is reversed by ADR-0003, with rows
  both ways; ADR-0005 is superseded by ADR-0010, with both directions
  linked; ADR-0009's load levels match the brief's. No two live records
  conflict.
- **Visual pass.** [C] Headless Chrome 155, its own temporary profile.
  The live page scrolled one viewport at a time, as a reader scrolls, so
  `content-visibility` rendered each section as it neared; no full-page
  capture, no override. Screens tiled into composites and read: 360 by
  780 and 1366 by 900; light and dark by the device; dark and light by
  the page's switch; scripts off in light and dark. 24 screens per
  configuration at 360 px and 14 at 1366 px with scripts on; 39 and 19
  with scripts off. The switched themes matched the device themes pixel
  for pixel on every screen except those holding the moving knot and
  strip (at most 2 per configuration, and 1 stray pixel at 1366 px).
  Device light against device dark differed on every screen, the defeat.
  No horizontal overflow at either width, in any configuration. Seen and
  correct: the dark Intro; the timeline to scale at 1366 px, entries on
  their months (the Nov to Dec 2025 cards on the Dec and Nov rows, the
  Sep 2025 entries on the Sep row); the phone timeline newest first; the
  contact marks switching with the theme; panels open and complete with
  scripts off; the footer line and its link.
- **Links.** [C] 14 of 15 distinct external links on the page answered
  200; the fifteenth is F2.

## 5. What was not checked, and why

- **NVDA or any screen reader by ear.** Waqas's to run; not asked for in
  this audit.
- **The keyboard walk (60 checks), the anchors (132) and the
  joined-words model.** Not rebuilt; time went to the visual pass,
  contrast and Lighthouse. The opened-state check above covers part of
  the keyboard path.
- **The tree at load at four loads per cell, in default mode, and in
  Edge.** One load per cell, full mode, Chrome only.
- **Firefox, Safari, real phones.** Not available here.
- **The Rahzaan case study at `/Rahzaan/`.** A separate repository,
  outside this audit, though the site links to it. ADR-0008's Consequences
  record three rule breaks there as of 2026-09-26; not re-checked.
- **The CV PDF's rewordings against the master, line by line.** Only its
  numbers and its cuts were checked; its own 15-check routine is the
  implementing seat's.
- **History before HEAD for private paths.** The records say earlier
  pointers remain in pushed history, accepted; not re-scanned.
- **`CHAT_STATE.md` and `briefs/`.** Deliberately not read, beyond the
  audit brief itself.

## 6. Anything a subagent reported that was not re-checked

None. No subagent was used.

## Housekeeping for the implementing seat

- The index row below the new one still reads "No audit yet.". This
  audit may add one row and nothing else, so it is left for you.
- Committing this file needs `MAP.md` regenerated (gate C).
- No process started by this audit is still running: no headless Chrome,
  no Lighthouse node, no local server, checked at the end. The scratch
  clone, builds and screenshots are outside the repository.
