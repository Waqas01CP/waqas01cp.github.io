---
type: log
description: "Brief 7. The design-system draft's IBM Plex Mono and Source Serif 4 subsets removed, with the draft made consistent and its specimen checked over HTTP. Gate C now refuses a Markdown header GitHub would refuse to read, compared case by case with PyYAML outside the repository. Research 0005: a seeded survey of 200 listed portfolios, one load each, and the repositories that already do what portfolio-gallery would. Every live file checked against the build; the standing checks rerun on the unchanged page; Lighthouse on the live site."
status: current
---

# 2026-10-12 (UTC): Fonts out, a header check in, and research 0005

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: 063950b, the
chat's, pushed; origin/main also at 063950b. The working tree held the
chat's two uncommitted Changes rows, in ADR-0007 and ADR-0012, with no
`.commitmsg/`. HEAD at end: the commit carrying this log. Mode: mutating.
Brief: 7. Previous log: 2026-10-11-review-commands-cv.md.

The session ran from 15:41Z on 2026-10-12 (20:41 local, the same date). It
continues the conversation that ran Briefs 5 and 6.

## What was asked

Brief 7, which is never committed, so its substance is here. The chat
verified Report 6 on 2026-10-12: live files byte-identical to a311809, the
CV PDF among them; the rebuild identical; the trace passing, with three
planted changes (592 to 593, 55 to 56, 122 to 12) each exiting 1. Its
answers to Report 6: 6.1 right, and wider; 6.2 recorded in 063950b; 6.3
done in its lane; 6.4 no action; 6.5 the operator keeps the 4, 4 and 2
skills layout; 6.6 the gate C proposal became section 2, and a live
Lighthouse set belongs in this round; 6.7 noted for the gallery's chat.

1. **Remove the draft's reserved-name fonts**, by the operator's choice of
   2026-10-12 over renaming them or shipping the makers' complete files:
   IBM Plex Mono reserves "Plex" (upstream google/fonts OFL.txt), and the
   shipped Source Serif 4 subsets' own name table, ID 0, reads "with
   Reserved Font Name 'Source'" (the chat, with fontTools, 2026-10-12).
   The OFL FAQ, entries 2.6 to 2.8 and 3.1, treats a subset as a Modified
   Version, which may not use a reserved name. Atkinson Hyperlegible Next
   reserves none and stays. Make the draft consistent: `@font-face` rules
   and stacks, the specimen's prose switch, the draft's README, `LICENSE`.
   Do not rewrite history.
2. **Gate C refuses a header GitHub cannot read**, by the operator's
   choice of a standard-library check (ADR-0007 Changes, 2026-10-12): an
   unquoted value holding ": " or " #", or beginning with a character YAML
   reserves, the set taken from the YAML 1.2 specification. Prove it
   against PyYAML in a scratch environment without adding it; report any
   case PyYAML rejects and the check passes; defeat the gate. Apply the
   operator's `CLAUDE.md` update block exactly, or stop if its Find text
   no longer matches. Update `docs/reference/commands.md`'s exit codes.
3. **Research 0005**, carried from Brief 6, Addenda 2 and 4: what most
   listed portfolios do; which of this site's practices are rare,
   measured; ideas within the scope floor; and what already does what
   `portfolio-gallery` would. Bounded and polite, one load per site, the
   home page only; no code or design copied; no personal data beyond the
   listing. Evidence only.

Verification: every check on its defeat case first; the standing checks
on the page, which should not change; the specimen with no failed font
request over HTTP; Lighthouse on the live site, medians of five.

## A commit this seat did not make

The brief says the operator would commit the chat's two Changes rows
before handing it over. At the start they were uncommitted, with no
message file, and `CLAUDE.md` lets this seat make the chat's commits only
when he hands them over. They were left unstaged; every commit of this
seat names its files. During this session, at 15:45:09Z, the operator
committed them as e8da17f, "[chat] ADR-0007: gate C refuses unreadable
headers; ADR-0012: draft fonts removed", those two files only, and pushed
it. Its gate C ran the working tree's `tools/generate_map.py`, which then
held this seat's uncommitted header check; it passed.

## The live site

[VERIFIED] 15 live files (the page, every file under `static/`, the CV
PDF) byte-identical to HEAD, by SHA-256 of each fetched file. The PDF
serves as `application/pdf`, 58,402 bytes. The comparison can fail: the
live page against 6e6b8cd's differs.

## Section 2: gate C refuses a header GitHub cannot read

**Where.** In `tools/generate_map.py`'s frontmatter reader, which already
exits 1 on a structural error; gate C refuses on exit 1 and prints the
message. So the map generator also refuses when writing the map, and the
author meets the error before the gate does. Commit ae42aef.

**The set, from the specification itself.** [VERIFIED] Read from the YAML
1.2.2 source, yaml/yaml-spec `spec/1.2.2/spec.md` (latest commit
1b1a1be, 2023-05-23): production c-indicator, `- ? : , [ ] { } # & * ! |
> ' " % @` and the backtick; ns-plain-first, which lets "-", "?" and ":"
begin a plain scalar only before a non-space "safe" character; and
ns-plain-char, under which ":" must be followed by a safe character and
"#" preceded by a non-space one, the spec's "Plain scalars must never
contain the ": " and " #" character combinations". A fetch tool's summary
of the spec page dropped "-" from ns-plain-first and garbled ns-plain-char,
so the source text was used instead.

The check, on every unquoted value: refuse a first character in
c-indicator, unless it is "-", "?" or ":" before a non-space; refuse ":"
before a space, a tab or the value's end; refuse "#" after a space or tab.
The refusal names the file, the line and the reason, and says to quote
the value. Quoted values are not checked, and the generator's docstring
says so, with "known patterns, not every YAML rule".

**Against PyYAML 6.0.3**, in the scratch environment outside the
repository. A case "fails in PyYAML" when it raises, or parses to a value
other than the text as written (a comment cutting it short, a list, a
mapping, a null):

- every tracked header, 37: PyYAML accepts all, the check refuses none;
- a planted corpus of 47 values: 37 inside the check's claim, agreeing on
  every one, 0 disagreements. They include each indicator as a first
  character, "-", "?" and ":" before a space and before a letter, ": "
  mid-value, a trailing ":", ":" before a tab, " #" and a tab before "#",
  and the allowed forms "https://example.com/a:b", "10:30", "C# and F#",
  "item#1" and "--- three dashes";
- outside the claim, 10: quoted values and types. **The limit:** PyYAML
  rejects three badly quoted values the check passes, an unterminated
  quote, text after a closing quote, and an unescaped apostrophe in single
  quotes. Also outside: "null" parses to nothing, and "yes", a date and
  "1.0" parse as other types; not errors.

PyYAML reads YAML 1.1, and which parser GitHub's renderer uses was not
established this session. Not checked against GitHub's own renderer
beyond the four real cases below.

**The real cases.** [VERIFIED] The check refuses each of the four headers
GitHub showed as "Error in user YAML" in October: `CAPABILITIES.md` at
502b6a5, and ADR-0011, research 0004 and the Brief 5 log before 73f2ab3.
Each fixed version passes.

**The gate's defeat.** [VERIFIED] A description in
`docs/reference/completed.md` given an unquoted ": " and committed through
the hook: "COMMIT REFUSED by the repository gates (ADR-0007): C the map
check failed (exit 1) ... docs/reference/completed.md, line 3: GitHub would
not read the description value as written: it holds a colon followed by a
space or ending the value". With the same value in double quotes, gates A,
B and C passed (run directly, nothing committed). The file was restored
from HEAD; its diff had been that one line.

**`CLAUDE.md`.** The update block's Find text matched exactly once; the
replacement was applied word for word. `docs/reference/commands.md`'s exit
1 now names the new cause.

## Section 1: the draft's fonts

[VERIFIED] Commit d7dc216. Removed with `git rm`: the three subsets and
their two licence texts. The draft made consistent with what remains:
`tokens.css` and `tokens.json` lose the five font entries and
`@font-face` rules for the two families; direction A's prose stack is
now `Georgia, "Times New Roman", serif` and mono is `ui-monospace,
Consolas, "Courier New", monospace`. The metric-matched fallbacks in
`components.css` that were computed against the removed files go with
them; Atkinson's stay. The specimen's preload goes, and its captions say
what loads. The README gets its files table, the prose-face note and a
dated section on the removal. `LICENSE`'s bullet names Atkinson.
`tokens.json` was not in the brief's list but named the removed files.

**Choice: fallback stacks, not a substitute face.** The draft is history
since ADR-0011, nothing on the live site uses it, and any substitute would
be a new font decision.

**Nothing references a removed file.** `git grep` for the five file names
finds only the Brief 6 log, which is history; at HEAD before the change
the same search found 9.

**The specimen over HTTP.** Defeat first: a copy of the draft at HEAD
with the three font files deleted and the references kept had 3 font
requests answered 404 and 3 faces in error. The edited draft: 2 font
requests, both 200 (Atkinson upright and italic, with direction B
switched on so its face loads), no face in error. One request failed in
both: `/favicon.ico`, which Chrome asks for when a page declares no icon;
the specimen declares none, before or after.

## Section 3: research 0005

Written as `docs/research/0005-listed-portfolios-and-reusable-templates.md`.
Its method, measures, numbers and limits are there; what follows is how
the session ran it.

- **The draw.** The list at be7238e, `README.md` SHA-256 67a6ecdc...0769;
  2,035 well-formed entries; 200 drawn with `random.Random(20261012)`,
  sample SHA-256 00c3e19e...c030, drawn twice to show it repeats.
- **The harness.** puppeteer-core driving headless Chrome 154 with its
  own temporary profile; one load per listed address, sequential; axe-core
  4.14.0 injected from the local npx cache. 200 loads from 15:45Z to
  16:09Z: 197 pages, one timeout, one expired certificate, one 403.
- **A defect, found and reported, not fixed:** the cookie measure read
  every cookie in the one shared browser, so it accumulated across sites
  (60 of the first 60 "set a cookie"). Fixing it needs a second load of
  each site, which the survey's rule forbids, so cookies are reported
  nowhere.
- **Two measures narrowed after reading the data:** reduced-motion
  handling counts the site's own CSS only, since animation libraries
  carry the string; "complete without scripts" uses only the 182 pages
  showing 20 words or more, since 15 show an intro or splash screen.
- **The "template source" links checked:** all seven linked the site
  owner's own repository, so none credits a template.
- **The control:** one load of this site, live: complete without scripts,
  no other site, 0 axe violations, a skip link, CV links, a theme control,
  reduced-motion CSS. It also matched "decision records" in its CV text,
  which is why the text measures are reported as words, not practices.
- **Question 4,** from GitHub's REST API, unauthenticated, 49 calls of
  the hour's 60, and raw files: nine repositories profiled, and
  csszengarden.com's Participation text read.
- **Personal data:** none kept beyond the list's own addresses; no site
  from the sample is named in the document.

## The page, unchanged, and its checks

Nothing on the page changed in this round. [VERIFIED] Built twice at
2026-10: identical across the 14 generated files, equal to the committed
output, and equal to a311809's; a build as of 2026-09 differs. The content
trace against the master (unchanged since 2026-10-11 08:10Z): 376 blocks,
0 not traced, every coverage group complete, PASS. Its defeat, the
feature's "592 automated tests" made 593: three blocks not traced, exit 1.

The standing checks on the page, one harness at a time, headless, each
defeat first. Chrome 154.0.8037.98, Edge 155.0.4283.45.

| Check | Defeat case, result | The page |
|---|---|---|
| Tree at load, full mode | 0403c68 against its reference: 4 of 4 loads differ | 32 of 32 loads match the page without the rule |
| Tree at load, default mode | The planted Intro paragraph: 1 node added | 32 of 32 loads add no node |
| Keyboard | Close hiding before moving focus: 58 of 60 | 60 of 60 |
| axe-core 4.14.0 | Planted faint text and an image without alt: violations in 12 of 12 cells | 0 violations in 12 of 12 cells |
| Anchors | The rule without its `:has(:target)` undo: 74 of 132 landed | 132 of 132 |
| Joined words, NVDA model | 6812c4f: 58 at 1366 px, 59 at 360 px, in Chrome and Edge alike | 0 at both widths, in both |

**Lighthouse on the live site,** for Report 6's 6.6: Lighthouse 13.5.0,
default mobile, five runs, 2026-10-12, the operator's Chrome open: median
LCP 1,685 ms, CLS 0, TBT 58 ms, 116,128 bytes transferred; meets ADR-0009
(2,500 ms, 0.1, 200 ms). TBT runs 481, 58, 0, 57, 104; LCP runs 2,324,
1,616, 1,569, 1,685, 1,729. The first run was the slowest on both. Against
2026-10-07's live medians of 138 and 95 ms, today's TBT is lower; one set
does not say why. Defeat, locally the same day: the page with a 600 ms
synchronous script, TBT median 1,917 ms, failing.

## Decisions this seat took, and why

- **The header check in the map generator, not a new gate script:** the
  reader already exits 1 on a structural error and gate C already refuses
  on it, and the author meets the error when regenerating the map.
- **A trailing ":" and a tab count as ": "**, because the spec's
  ns-plain-char allows ":" only before a safe character; PyYAML agreed on
  both.
- **Quoted values not checked:** the brief scoped the check to unquoted
  values, and the record names known patterns; the three badly quoted
  cases are the stated limit.
- **Fallback stacks for the draft,** not a substitute face (section 1).
- **200 portfolios, one load each,** for intervals of at most about 7
  points; the 15 near-wordless pages kept in, excluded only from the word
  ratio; cookies dropped rather than measured with a second load.
- **The chat's uncommitted rows left alone** until the operator committed
  them.

## Errors this seat made

- The survey's cookie measure accumulated across sites in one browser;
  found in the data, reported, not used.
- A content-trace defeat planted ">592 automated" matched nothing,
  because the markup splits the figure, and the trace exited 0 on an
  unchanged page. Caught by its exit code; replanted, it exited 1.
- A backup for the gate C defeat went to /tmp, not the scratchpad; the
  file was restored from HEAD instead, its diff having been one line.
- A sentence in this log about GitHub's documentation that I had not read,
  and "about one percent each" for a framework at 2% in research 0005;
  both corrected before commit.
- A first records script would have put this round's timeline row out of
  date order and broken on its own earlier edit; fixed before it ran.

## What is next

- The operator's push of ae42aef, d7dc216, 2cf9df2 and this commit; then
  the live check (the page is unchanged; the draft's files changed).
- The chat's reply to Report 7.
- portfolio-gallery: built by its own session; this seat reviews it
  before anything is published.
