---
type: log
description: Brief 1 in three rounds. Python generator, JSON content schema, two content gates and Rahzaan rendered unstyled, all verified with defeating cases; YAML replaced by JSON, case-study link made root-relative; MarkupSafe pinned, LF forced; committed by concern, not pushed; three Working Method paths await a ruling.
status: current
---

# 2026-09-26 (UTC): Generator, content model, one item end to end

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: fa68814.
HEAD at end: round 1 left everything uncommitted. Round 2 committed eight
commits ending 675652c, then da45bd6 carrying this log. Round 3 committed
f7479f7 and ccee5b1, then the commit carrying this update. Nothing is
pushed. Mode: mutating. Brief: 1. Previous log: none, this is the first.

The first file this session wrote, `.venv/pyvenv.cfg`, is timestamped
2026-09-26T18:45Z. The
local date (UTC+5) passed into 2026-09-27 during the session; `date -u`
read 2026-09-26T19:00Z at that moment. Every date here is UTC.

## What was asked

Brief 1, which is not committed, so its substance is here. Build the Python
generator ADR-0006 settled, with Jinja2 as the one pinned dependency in a
venv at `.venv/`. Define the item schema: `id`, `title`, `tier` (1 to 3,
never a visible label), `lane`, `start`, `end` (`YYYY-MM` or `present`),
optional `stack`, required `source`, exactly one of `proof` (list of
`{label, url}`) or `verification`, and `layer1`, `layer2`, `layer3`. Compute
timeline rows at four units per month from January 2024, where the start
row is `(months since 2024-01) * 4 + 1` and the span is `(months inclusive) * 4`.
A pre-2024 start fails the build except in the band lane. Three templates:
shell, item with layer 3 in `<details>`, and timeline as an ordered list with
inline grid positions. Two build gates: missing source, missing or doubled
proof route. Render Rahzaan only, with layer 3 verbatim from the master CV as
HTML fragments limited to `<strong>` and `<a href>`, rendered with `|safe` on
that field only. Layer 1 and layer 2 were drafted by the architecture chat,
marked draft. No visual design, no JavaScript, no other items, no hooks or
map generator, no enabling Pages. Nine verification checks, each with a
defeating case. Fill the CLAUDE.md Commands section.

Stop conditions: a second dependency, a scope floor line bending, a field
outside the schema, a date or claim disagreeing with the master CV, or the
layout conflicting with how Pages serves a user site. **None fired.**

## What was done

**Environment.** [VERIFIED] `python -m venv .venv` with Python 3.12.10, then
`requirements.txt` containing the one line `Jinja2==3.1.6`, the latest
release per `pip index versions Jinja2`. `pip list` in the venv printed
Jinja2 3.1.6, MarkupSafe 3.0.3 and pip 25.0.1. `pip list --not-required`
printed Jinja2 and pip only. `.venv/` was already in `.gitignore` as an
uncommitted change labelled "Brief 1", made by another seat before this
session; kept as found. `git check-ignore -v .venv/pyvenv.cfg` names
`.gitignore:11`.

**Content file.** [VERIFIED] `src/content/items.json`, not `items.yaml`. The
global Python has no YAML parser (`import yaml` raised ModuleNotFoundError)
and the venv holds only Jinja2, MarkupSafe and pip, so YAML would be a
second dependency. Brief 1 allowed
JSON as the answer. Rahzaan's nine layer 3 blocks, title, dates and stack
were compared with the master CV by a scratch script. The script turned the
master's `**bold**` and `[text](url)` into `<strong>` and `<a href>` and
compared character by character: "block 1: identical (493 chars)" through
"block 9: identical (381 chars)", title, dates and stack true, RESULT PASS.
Defeating case: the same script on a copy with one comma removed from block 3
printed "block 3: DIFFERS at char 465" and RESULT FAIL. The master was read
from the operator's vault; its path is not recorded here, per CLAUDE.md.

**Case-study proof link stored as `/Rahzaan/`.** [VERIFIED] The brief gave
`https://waqas01cp.github.io/Rahzaan/` and said both proof links point at
other origins. That one has this site's own origin, which ADR-0002 forbids,
and check 9 would have failed on it. Followed the record. GitHub's "About
custom domains and GitHub Pages", fetched 2026-09-26, says a project site
with no custom domain of its own is served under the user site's custom
domain as a subpath, so the root-relative link survives a domain move. It
returns 404 when the repository root is served locally, because the case
study is a separate repository.

**Generator, `build.py`.** [VERIFIED] Timeline arithmetic is pure functions:
`month_index` (build.py:83) and `grid_position` (build.py:91). They live in
`build.py` because the brief's layout allowed no other file. Content checks:
`check_item` (build.py:202) with the two gates first (build.py:217, 220,
222), then the schema checks. `_FragmentCheck` (build.py:137) accepts only
`<strong>` and `<a href>`, properly nested. `url_problem` (build.py:184)
rejects this site's own origin. `check_environment` (build.py:326) refuses to
run outside a venv or with a Jinja2 other than the pin. `render`
(build.py:350) sets `autoescape=True` (build.py:359), because
`select_autoescape` keys on the file extension and would leave `.html.j2`
templates unescaped. Every check runs before any write (build.py:390).

**Templates and static.** [VERIFIED] `base.html.j2`: shell, `lang="en-GB"`,
skip link, header, main, one section per lane with items, then the timeline.
`item.html.j2`: title, layer 1, a `dl` of dates, stack and proof, layer 2,
then layer 3 in `<details>` (item.html.j2:26), `|safe` on layer 3 only
(item.html.j2:33). `timeline.html.j2`: an `ol` with inline `grid-row` and
`grid-column` (timeline.html.j2:10). `src/static/timeline.css`: `display:
grid` and named column lines for the lanes, nothing else. No row size is set,
because ADR-0003 leaves the unit size open.

**Output.** [VERIFIED] `python build.py` printed "built index.html: 1
item(s), timeline as of 2026-09 UTC; copied 1 static file(s)", exit 0. The
Rahzaan timeline entry is `grid-row: 101 / span 32; grid-column: builds`,
that is Feb 2026 to Sep 2026, eight months.

**Verification, with the case built to defeat each.** A scratch script ran
every mutation in a throwaway copy of `build.py`, `requirements.txt` and
`src/`, never in the repository: 37 of 37 passed. [VERIFIED]

| Brief check | Result | Defeating case |
|---|---|---|
| 1 Build runs | exit 0, index.html written | the gate cases below exit 1 |
| 2 One dependency | venv top level: Jinja2, pip | same command on the global Python lists `ocrmypdf` and fails |
| 3 Idempotent | two builds, identical SHA-256 for index.html and static/timeline.css | the same comparison differs after a one-month content change |
| 4 Missing source | exit 1, "item 'rahzaan': has no source. Every item must trace to the master CV (ADR-0006)", prior index.html unchanged | the check itself |
| 5 Proof route | neither: exit 1 "has neither proof nor verification"; both: exit 1 "has both proof and verification" | the check itself, both ways |
| 6 Arithmetic | start 2026-02 to 2026-03: (101, 32) to (105, 28); a control item stayed at (85, 12) | a hand-moved control row is detected |
| 7 Pre-2024 | `start: 2023-11` on builds: exit 1 "starts 2023-11, before the timeline opens at 2024-01; only the band may" | the check itself |
| 8 No JavaScript | 0 script elements, 0 `on*` attributes; with page scripts blocked, all 14 layer texts present, all 9 layer 3 blocks inside `<details>` | layer 3 written by a script: 9 blocks missing; same variant with scripts allowed: 14 of 14, so the loss is caused by scripting |
| 9 No self-origin | 0 matches for `waqas01cp.github.io` in index.html and static/ | the same grep finds 1 in a copy with the absolute link put back |

Arithmetic also checked directly: `grid_position` matched a stepped calendar
on all 666 start/end pairs from 2024-01 to 2026-12, gave ADR-0003's own
example (Sep to Dec 2025 spans 16), and placed a band starting 2022-09 at
(1, 128) flagged as starting before the axis. It raised on a pre-2024 builds
start, on end before start, on month 13, on an unpadded month, and on a band
that ends before 2024.

Additional checks this session added, each proven by a failing case: a
self-origin URL in `proof` or inside layer 3 (hostname match is
case-insensitive); `<em>`, `<script>`, `<a onclick>` and an unclosed
`<strong>` in layer 3; an unknown field (`sorce`); a lane with no page
section; a duplicate id; an id the page uses (`timeline`); a pin mismatch
(`requirements.txt` set to 3.1.5); and a build outside the venv. Every one
exited 1 with the prior output unchanged. Autoescape: `<b>` in layer 2 and
`<script>` in the title came out as `&lt;b&gt;` and `&lt;script&gt;`.

Check 8 method. Edge's headless `--dump-dom` and `--screenshot` both produce
nothing under `--blink-settings=scriptEnabled=false`: 0 characters in both
headless modes, against 6770 with scripts on. So page scripts were blocked
with a `script-src 'none'` Content Security Policy in a copy of the page
instead. A screenshot of that copy with `<details open>`, which is what a
click does natively, shows every layer readable and unstyled.

**Served from the root.** [VERIFIED] `python -m http.server` at the
repository root returned 200 for `/` and `/static/timeline.css`.

**Commands.** [VERIFIED] Every command in CLAUDE.md's Commands section was
run in PowerShell exactly as written. Install: "Requirement already
satisfied", exit 0. Activate and build: exit 0. `pip list --not-required`:
Jinja2 and pip. Build after `deactivate`: exit 1, "not running inside a
virtual environment". Git Bash activation was also run: exit 0.

**Documents.** CLAUDE.md: Commands filled; the intro sentence saying the
build does not exist was corrected. `src/content/README.md` documents the
schema and every enforced rule. STATE.md: verified-against line, new rows,
and stale rows corrected (below). `.nojekyll` created, empty.

**Stale rows in STATE.md, corrected.** [VERIFIED] The header said no
`git init` had run; `git log` shows b0c4a2d as the first commit,
2026-09-25T21:42Z. The scope floor, runtime and conventions rows said
PENDING; `git log -S` shows the fourteen floor lines and the conventions
entered CLAUDE.md in eb024c2. The framework row said PENDING; ADR-0006
accepted it. The Blocked row for CLAUDE.md and the first commit had cleared.

## Rejected alternatives

- **YAML via PyYAML.** A second dependency, scope floor line 14. A stop
  condition, not a choice.
- **TOML via the standard library's `tomllib`.** Reads better than JSON for
  long prose and needs no dependency on Python 3.11 or later, but the brief
  offered only JSON as the fallback. Raised as a question, not adopted.
- **Keeping the absolute case-study URL.** Breaches ADR-0002 and check 9.
- **A separate `timeline.py` module.** Cleaner, but the brief's layout says
  "exactly this, nothing else". The arithmetic is importable from `build.py`.
- **Row sizes in CSS.** The size of one layout unit is ADR-0003's open
  question and a design decision. Without it empty rows collapse, so the
  visual scale is not yet true; the row numbers are.
- **Guessed section headings for work, opensource and band.** ADR-0001
  names projects and certifications only. The build fails instead.
- **Verifying check 8 with the browser's own script switch.** Produces no
  output at all in headless Edge, so it cannot be a check.

## Checked and found already correct

- The brief's Rahzaan title, dates (Feb 2026 to Present), stack and both
  proof URLs match the master CV.
- Layer 1 and layer 2 drafts assert nothing absent from the master.
  Layer 1's "agentic career guidance platform" joins the master's "agentic
  counselling platform" with its "AI career guidance platform". Layer 2
  drops the master's parenthetical minima (PEC at 60% for BE, HEC at 50% for
  BS, 45% elsewhere).
- ADR-0003's "Sep to Dec 2025 is a span of sixteen" and "33 months, 132 rows"
  agree with the brief's formula. Rahzaan ending at the build month, Sep
  2026, ends at row 132.
- The committed brief matches the one the operator pasted.
- `.nojekyll` does not conflict with serving from the root. Jekyll's
  underscore and dot rule does not touch `src/` or `docs/`.

## Not done

- **No commit.** Committing puts the draft layer 1 and layer 2 into public
  history permanently once pushed; `briefs/README.md` keeps briefs out of
  the repository for exactly that reason. The operator decides.
- **`.nojekyll` behaviour.** Pages is not enabled; out of scope.
- **Screen reader check of the collapsed layer 3.** ADR-0005 requires it
  before the first content page ships. Not run.
- **Map generator, rebuild gate, hook gates.** Brief 2.
- **Tier behaviour.** Validated, not used. The brief does not say what each
  tier renders.

## Findings and recommendations

Findings:

1. **Brief contradicted ADR-0002**, as above: the case-study URL is
   same-origin.
2. **Brief contradicted ADR-0003**: its lane list omitted Open source, which
   ADR-0003 keeps in the data model. `opensource` was added as a lane value.
3. **Brief dated the certificate correction 2026-09-25.** ADR-0001's Changes
   table and STATE.md date it 2026-09-23.
4. **The CLAUDE.md commands section is not fully closed** by this brief. The
   section's own contract includes a map generator and a rebuild gate. Its
   STATE row is PARTIAL, not DONE.
5. **`present` makes the output depend on the build month.** Idempotence
   holds within a UTC month. From 2026-10-01 a fresh build differs from the
   committed one, so the rebuild gate will flag stale output monthly.
6. **ADR-0001 assumption A2 names the master CV's vault path**, in a public
   committed record, while CLAUDE.md says the path is deliberately not
   recorded. It is in pushed history already.
7. **STATE.md held 16 DONE rows before this session** that its own rule says belong in
   `docs/reference/completed.md`. The new rows sit beside them, as the brief
   asked.
8. **Every committed file is served by Pages.** With `.nojekyll`, `/src/`,
   `/docs/` and `/logs/` are URL-addressable. Measured locally:
   `/src/static/timeline.css` returned 200. The repository is public, so
   nothing new is exposed.
9. **Git converts line endings here** (`core.autocrlf` warned "LF will be
   replaced by CRLF"). The build writes LF. A byte-level rebuild gate on a
   fresh Windows checkout would see CRLF; a `git diff` would not.

Recommendations, not decisions:

- R1. Confirm or replace the layer 1 and layer 2 drafts before the first
  commit of `items.json` and `index.html`.
- R2. Pin the build month for the rebuild gate, for example with an
  as-of argument or `SOURCE_DATE_EPOCH`, so the gate tests the build rather
  than the calendar.
- R3. Decide whether the layout, JSON and Jinja2 choices need a record,
  since the brief that made them is not committed and ADR-0006 left them to
  it.
- R4. Pin MarkupSafe too, or accept that it floats within Jinja2's range.
- R5. Pick section headings for work, opensource and band before their
  content arrives.
- R6. Add a `.gitattributes` forcing LF on generated output before the
  rebuild gate is written.

## Noticed and not investigated

- The master CV writes HubIT's dates as "June 2026 to July 2026", the only
  entry with full month names. The build renders every item in the short
  form.
- `docs/decisions/README.md` Pending still lists the UC Davis certificate as
  not in the master, while STATE.md records it added 2026-09-25.
- The session-start git snapshot showed the brief staged and
  `briefs/README.md` modified. The actual tree showed neither.

## Round 2, 2026-09-26 (UTC)

### What was asked

The architecture chat verified report 1 against the repository, accepted
every check added beyond the brief, and answered the questions:

- Commit. The layer 1 and layer 2 wording was approved by the operator
  before the brief was written; the draft marker was a mistake.
- Tier controls order and prominence, never which layers render. Tier 1
  also links to a standalone case study (ADR-0005 Changes).
- Headings for work, opensource and band come with those items. The build
  keeps failing on a lane with no section.
- The rebuild gate reads an as-of month recorded in the output, not the
  build date (ADR-0006 Changes).
- ADR-0006 Changes now records the layout, `items.json` and
  `Jinja2==3.1.6`.
- Pin MarkupSafe, and add `.gitattributes` forcing LF.
- ADR-0001 A2 no longer names the vault path.

It asked whether the build's expected Jinja2 version is read from
`requirements.txt` or written into `build.py`, without changing it. It asked
for commits by concern with detailed messages, with CHAT_STATE.md in none
of them.

### What was done

- **Records read before committing.** [VERIFIED] The four diffs say what the
  chat described. A search of every file git sees for the vault path then
  found one more: `README.md` line 59, present since the first commit.
  Removed in its own commit.
- **MarkupSafe pinned.** [VERIFIED] `requirements.txt` now pins
  `MarkupSafe==3.0.3` under Jinja2, with a comment. `pip install -r` was a
  no-op, exit 0. `pip list --not-required` still shows Jinja2 and pip.
  Defeating case: a copy with `MarkupSafe==3.0.2` and a `build.py`
  byte-identical to the repository's failed with "MarkupSafe 3.0.3 is
  installed but requirements.txt pins 3.0.2", exit 1.
- **`.gitattributes`, `* text=auto eol=lf`.** [VERIFIED] Committed first.
  Afterwards `git ls-files --eol` showed all 20 tracked files `i/lf w/lf`,
  with no spurious changes. A fresh clone at 675652c with `core.autocrlf`
  true checked out `index.html` as LF, a fresh build was byte-identical to
  it, and `git status` was clean. Defeating case: the same clone with
  `.gitattributes` removed by a scratch commit checked `index.html` out as
  CRLF, and a fresh build differed from it byte for byte.
- **Re-verified after the changes.** [VERIFIED] The suite passed 37 of 37,
  check 8 passed with its defeat and control, and the output hashes were
  unchanged: `index.html` 759dc7dd, `static/timeline.css` c9333e93.
- **Documents.** CLAUDE.md's environment paragraph names both pins and says
  `build.py` reads them from `requirements.txt`. `src/content/README.md`
  documents tier per ADR-0005 Changes. The `.gitattributes` item in
  `docs/decisions/README.md` Pending is marked closed. STATE.md: draft
  status dropped, Blocked row cleared, new rows added, verified-against
  line updated.
- **CHAT_STATE guard.** [VERIFIED] Before each commit the staged list was
  searched for CHAT_STATE, and the commit was refused on a match. Proven
  able to fire: `git add --dry-run -f CHAT_STATE.md` prints "add
  'CHAT_STATE.md'", which the same test refuses. The index stayed empty.
  Every commit printed "CHAT_STATE check: not staged".
- **Commits, in order.**
  - 89de898: `.gitattributes`.
  - 20e1ef8: the chat's record changes.
  - ad6c28f: `.gitignore` and `requirements.txt`.
  - 5c259ae: generator, templates, CSS.
  - 7f2cbd2: `items.json` and the schema README.
  - bbd62ce: generated output and `.nojekyll`.
  - 1da6581: CLAUDE.md.
  - 675652c: README.md.
  - Then this log, its index row and STATE.md.

### The question back: where the expected version comes from

It is read from `requirements.txt`, at build.py:334, and not written into
`build.py`. [VERIFIED] A search of `build.py` for `3.1.6` or `3.0.3` finds
nothing. Both mismatch cases changed only `requirements.txt` in a copy,
with `build.py` untouched, and each build failed quoting the version from
that file. So the pin has one live home and the check cannot drift from it.

Would not change it. What the check does not cover: it verifies only the
pinned packages, so an extra unpinned package in the venv is caught by the
`pip list --not-required` check, not by the build. ADR-0006 Changes names
`Jinja2==3.1.6` as a dated decision that nothing reads, so a version bump
needs its own Changes row. The line parser fails closed: extras, markers,
or a specifier other than `==` stop the build rather than pass.

### Findings

1. **Correction to round 1, finding 9.** Round 1 inferred that a `git diff`
   would not see a CRLF checkout. Measured this round, without
   `.gitattributes`: `git diff` shows no content change, but `git status`
   lists `index.html` as modified even after `git update-index --refresh`,
   and a byte comparison differs. With `.gitattributes`, all three are
   clean.
2. The vault path was in three files, not two: `README.md` as well.
3. The chat's new record rows are dated 2026-09-27, the local date. UTC was
   2026-09-26 (`date -u` read 20:39Z). CLAUDE.md says dates are UTC. The
   seat's annotation in the Pending list uses 2026-09-26 (UTC), so that
   list now carries both dates.
4. ADR-0006's second new Changes row cites "Rule 5" for the gate. In its
   Decision Outcome the fifth rule commits the output; the gate is the
   sixth.
5. The Pending list closes the UC Davis item on 2026-09-26. STATE.md's row
   records the master gaining it on 2026-09-25.
6. The build validates tier but does not order by it, while ADR-0005 now
   says tier controls order. With one item this has no visible effect.
7. The as-of month is not recorded in the output yet. Its format and the
   build's as-of input are the gate's interface, so they belong with the
   gate in Brief 2.
8. Commits by concern put STATE.md and this log in the last commit rather
   than with each piece of work. The planned "STATE.md moves with
   implementation work" gate has to allow for that.

Recommendations, not decisions:

- R7. In Brief 2, have `build.py` take an as-of month, defaulting to the
  current UTC month, and write it into the output. The gate reads it back
  and rebuilds with it.
- R8. When a second item arrives, have the build fail when the content
  file's order contradicts tier, rather than sort by tier. That keeps one
  source of order and makes a contradiction visible.

## Round 3, 2026-09-26 (UTC)

### What was asked

The chat verified round 2 and accepted the answer on version pins,
including where its coverage stops; it is not to change. The chat
corrected the three errors round 2 raised in its records: local-date
stamps, the gate attributed to rule 5 instead of rule 6, and the UC Davis
date. It also updated README.md itself, reporting a fourth vault pointer
there and six in total across four files. The corrected files were to go
into the next commit.

Decisions, in the chat's message and not yet in a record:

- **Tier order.** The build fails when the content file's order
  contradicts tier, rather than sorting by tier.
- **As-of month.** Accepted for Brief 2, with the format and the build's
  as-of input landing together.
- **State-file gate.** A pre-push hook checking the whole range being
  pushed, not a pre-commit hook.
- **Commits by concern with bookkeeping last** is the correct shape. It is
  recorded here as such, not as a defect; round 2's finding 8 and that
  bookkeeping commit's "departs from" note are superseded by this ruling.
- **No push.** Brief 2 covers the four gates, the map generator,
  `.gitattributes` verification and the as-of month. The first push
  follows it.

### What was done

- **Chat's changes read, then committed by concern.** [VERIFIED] Record
  dates are now UTC, ADR-0006 attributes the gate to rule 6, and UC Davis
  closes 2026-09-25, matching STATE.md. README.md: six accepted records,
  every path in its table exists, no stale phrasing, no em-dashes.
  Commits: f7479f7 (records), ccee5b1 (README.md), then this log with its
  index row and STATE.md.
- **Vault-pointer scan over all history.** [VERIFIED] A scratch script
  scanned every commit up to ccee5b1, and the working tree, for file paths
  under either of the two vault folders this repository has named, with
  or without leading parent-directory segments. It found 7 distinct
  pointers in 6 files. This log names them by what they point at, not by
  their text, so that it does not become an eighth. Four are gone from the
  tree: the master CV's path in CLAUDE.md, ADR-0001 and README.md, and
  README.md's relative path to the Working Method document. Three remain,
  each present since the first or second commit:
  - STATE.md's header: the Working Method's new-project setup procedure.
  - `briefs/README.md`: the Working Method's brief template.
  - `logs/README.md`: the Working Method's session-log template.

  The script's pattern found a planted pointer and ignored the prose
  phrase "cross-project Working Method". Not edited: whether a named
  template path counts is the chat's ruling, and the never-commit gate's
  pattern depends on it.
- **STATE.md.** [VERIFIED] Rows now carry the tier-order decision, the
  pre-push shape of the state-file gate, the as-of month for Brief 2, the
  held first push, and the three remaining paths awaiting a ruling.

### Errors this round found in the seat's own work

1. **The vault-path checks in rounds 1 and 2 could not fail on this class
   of pointer.** They searched only for the master CV's folder and file
   names and the vault's top-level folder name, so a path under the
   Working Method folder passed unseen. Round 2's "a search of every file
   git sees for the vault path" was true only for the master CV's path.
   The first attempt this round also failed silently: the backslash pattern
   was mangled on its way through the shell and matched nothing. Caught by
   comparing it with the Grep tool's result on text already known to be
   there. The scan was then rewritten as a file and given the self-test
   above.
2. **Round 1 carried a pointer forward.** Rewriting STATE.md's header, the
   seat kept the Working Method path in it without treating it as a vault
   pointer.
3. **This round's first draft of this log quoted all four Working Method
   paths while reporting them.** Re-running the scan before committing
   caught it: 4 new pointers, found only in the working tree and all in
   this file. The passages were rewritten to name each pointer by its
   target. The scan was run again afterwards.

### Findings

1. The chat's count, six pointers in four files, differs from the scan's
   seven in six. The difference is the three named template paths still in
   the tree.
2. The tier-order and state-gate decisions exist only in the chat's message
   and this log. Recommendation, not a decision: record them. The tier
   check could go in ADR-0005 Changes, and the pre-push shape wherever the
   gates are recorded.
