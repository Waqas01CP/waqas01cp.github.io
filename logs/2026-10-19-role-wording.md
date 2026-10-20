---
type: log
description: "Briefs 9 to 11, and the briefs folder taken off the repository. The master CV's role wording of 2026-10-18 carried onto the page by script (the summary, a skills item, the job aggregator's role line and two bullets); the trace passing again against the master; no \"seat\" on the page; the new CV PDF checked and committed; CAPABILITIES.md's build table relabelled by what each role did. Brief 8 confirmed live. Brief 10: this machine's load measured against Lighthouse; the quiet set passes ADR-0009; light, medium and heavy proposed from the measurements."
status: current
---

# 2026-10-19 (UTC): The role wording

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: 809fa14, the
chat's, pushed; origin/main also at 809fa14. The working tree held one
uncommitted change, `cv/Waqas_Sharif_CV.pdf`, the new site CV placed by
the operator. HEAD at end: the commit carrying this log. Mode: mutating.
Brief: 9. Previous log: 2026-10-15-footer-line.md.

The session ran from about 14:00Z on 2026-10-19 (19:00 local). It
continues the conversation that ran Briefs 5 to 8.

## What was asked

Brief 9, which is never committed, so its substance is here. The master
CV changed on 2026-10-18 at 21:33Z to the operator's clarified
description of his role. The chat measured the trace against it on
2026-10-19: 373 traced, 4 not traced, FAIL.

1. Bring `site.json` and `items.json` to the master, with the cut rules
   as before; show the trace passing, and its defeat.
2. The longer summary and the eight-item skills line: layout at 360 and
   1366 px and the standing checks; say what moved.
3. A search of the built page finding no "seat".
4. The new CV PDF: check it as in Brief 6, and its MD5,
   03a9be1dd2a404b482aebd71aebafb15; commit it on its own, after the
   content; both download links still resolving to it.
5. The role rule in the seat's handoff, replaced: no wording may imply
   he cannot code, or that the AI designed the work; the difference from
   other ways of building shown by evidence, never by a stated contrast;
   "seat" kept to records, logs and `CLAUDE.md`, never on the site, the
   CV or public text about him.
6. `CAPABILITIES.md`, this seat's lane: the build table's rows relabelled
   by what each did. The chat rewrites the role section and README's
   "How this project is run" after this commit.

## Live, Brief 8

[VERIFIED] At 2026-10-19T14:04:34Z, 24 live files (the page, everything
under `static/`, the CV PDF and the design-system draft) byte-identical
to HEAD 809fa14 by SHA-256; the footer line and its link on the live
page. Defeat: the same check against a18919d, the commit before the
footer, reports `index.html` and `static/site.css` as different.

## The content

[VERIFIED] The master and the copy of it this seat traced on 2026-10-16
differ in five lines. A script diffed each word by word and replaced the
changed region, with the least context that occurs exactly once in the
content, by the master's new text; the skills line became its group's
list. Nothing was retyped.

| Master line | Where on the page | Change |
|---|---|---|
| Professional summary | The Intro's lede, `site.json` `summary` | "sets the architecture, the engineering trade-offs and the standards, and directs AI seats that implement and audit to them" becomes "designs the architecture and the algorithms, makes the engineering trade-offs, and directs coding agents that implement to written specifications, verifying their work through automated tests, mutation testing and independent audits" |
| AI-Native Development | Skills, `site.json` | An eighth item, "Directing and Reviewing Coding Agents" |
| Job aggregator, italic line | The item's layer 2, `items.json` | "the blueprint, the architecture, ... AI seats wrote the code and the audits" becomes "the design, the algorithms, ... Claude Code writes the code to specifications I approve" |
| Job aggregator, method bullet | Its depth, bullet 05 | "four-seat" to "four-role", "every seat" to "every role", "read-only seat" to "read-only reviewer" |
| Job aggregator, review bullet | Its depth, bullet 06 | "the AI seats missed" to "the coding agents missed" |

The page changes in exactly these five places. It grew by 179 bytes, 51
gzipped.

**Trace.** [VERIFIED] 378 blocks, 0 not traced; summary 1 of 1, skills
lines 10 of 10, italic-line sentences 17 of 17, bullets 28 of 28; PASS.
Defeats, each exit 1:

- the page before this change: 373 traced, 4 not traced, the chat's
  measurement reproduced;
- "coding agents" made "AI agents" in a copy of the master, the copy
  differing only at line 85: 1 not traced, bullets 27 of 28;
- the new skills item removed from a copy of the page: skills lines 9 of
  10.

Control, the page unchanged: exit 0.

**No "seat".** [VERIFIED] A case-insensitive search of the built page: 0
hits. The page before the change: 6.

**Build twice:** identical across the 14 generated files.

Commit 33bbff9. The PDF follows in its own commit, d053c17.

## What moved

Measured in headless Chrome against the page before, light and dark, under
reduced motion; screenshots of the Intro and Skills at both widths.

- **The summary** grows by one line at 1366 px (304 to 332 px high) and
  three at 360 px (508 to 588 px).
- **The new skills item** wraps to two lines at both widths, as
  "Architecture Decision Records (ADRs)" and the Pandas item already do.
  At 360 px the AI-Native Development card grows by 60 px; at 1366 px its
  row of four cards, which take the tallest card's height, grows by 51
  px.
- **Nothing else changes shape;** what follows shifts down. The page is
  78 px longer at 1366 px and 140 px longer at 360 px. No horizontal
  overflow at either width.

## The standing checks, on the new page

One harness at a time, headless, each defeat first, 14:09Z to 14:40Z.
Chrome 154.0.8037.98, Edge 155.0.4283.62, each read from its file.

| Check | Defeat case, result | The page |
|---|---|---|
| Tree at load, full mode | 0403c68 against its reference: 4 of 4 loads differ | 32 of 32 loads match the page without the rule |
| Tree at load, default mode | The planted Intro paragraph: 1 node added | 32 of 32 loads add no node |
| Keyboard | Close hiding before moving focus: 58 of 60 | 60 of 60 |
| axe-core 4.14.0, 360 and 1366 px, light, device dark, switched dark, as loaded and all open | Planted faint text and an image without alt: violations in 12 of 12 cells | 0 violations in 12 of 12 cells |
| Anchors | The rule without its `:has(:target)` undo: 75 of 132 landed | 132 of 132 |
| Joined words, NVDA model | 6812c4f: 58 at 1366 px, 59 at 360 px, in Chrome and Edge | 0 at both widths, in both |

**The summary and the new skills item, as the NVDA model reads them,**
at 1366 and 360 px: the summary one line, every space present; the item
"Directing and Reviewing Coding Agents" one line, though it wraps on
screen.

**Lighthouse: not passed this session.** Lighthouse 13.5.0, default
mobile, five runs each, interleaved, served locally without compression.
Two sets:

| Set | Variant | LCP median | CLS | TBT median | TBT runs |
|---|---|---|---|---|---|
| 1, ending 14:40Z | This page | 2,286 ms | 0 | 361 ms | 436 613 361 212 236 |
| 1 | The page before it, 809fa14 | 2,352 ms | 0 | 300 ms | 300 200 268 378 509 |
| 1 | Defeat: a 600 ms script | 2,106 ms | 0 | 1,922 ms | fails |
| 2, 14:41Z to 14:48Z | This page | 2,552 ms | 0.031 | 515 ms | 529 515 454 458 730 |
| 2 | The page before it | 2,517 ms | 0.031 | 580 ms | 580 658 512 630 420 |
| 2 | Defeat | 2,282 ms | 0 | 2,249 ms | fails |

Both pages fail ADR-0009's 200 ms blocking-time limit in both sets, and
in the second its 2,500 ms paint limit. The page before it is the same
bytes that measured LCP 2,258 ms and TBT 29 ms on 2026-10-15. Measured,
not a cause: before the second set, with no harness of this seat
running, the machine's CPU load read 62%, with the operator's Chrome (21
processes), VS Code and Notepad among the busiest. During the second set
it read 10 to 71%, median 42%, in 30 samples, but those samples include
Lighthouse's own browser, so they do not measure other programs; the
first draft of these records said they did.

**A third set, 2026-10-19T19:46Z to 19:51Z (2026-10-20 local),** after the
operator closed his programs; his Chrome's main process and Notepad
still ran but used 0.3% and 1.0% of the machine over 20 s. This page:
LCP 2,451 ms, CLS 0, TBT 427 ms (runs 908 280 429 427 224); the page
before it: 2,366 ms, 0, 317 ms (243 377 675 317 46); the defeat 2,008
ms. Both fail again.

What was ruled out, measured: the laptop was plugged in, on the Balanced
plan with no power-saving overlay. Lighthouse's own speed index for the
machine (`benchmarkIndex`, median per variant) was 1,741 to 1,859 in the
third set against 1,631 to 2,032 on 2026-10-15, so the machine was not
slower on its short benchmark; yet on the same bytes, every main-thread
category took 2.5 to 4 times as long (style and layout 199 to 485 ms,
script evaluation 45 to 205 ms, long tasks 1 to 3 per run against 2 to
7). A slowdown even across every category points at contention during
the page's work, not at the page.

What was found, not tested as the cause: another Claude Code session, in
the operator's job-aggregator repository, was running mutation testing
(`tools/mutate.py`, which reruns that project's test suite repeatedly)
from 2026-10-19T17:53Z, through the third set. This seat did not touch
it. Whether anything like it ran during the first two sets is not known.

Within each set the two pages overlap run for run, so no set shows a
cost of the change; but ADR-0009 counts a fail on any machine, so
Lighthouse stays open until a set passes with no other sustained load.

## The CV PDF

[VERIFIED] The operator placed it; the CV chat built it. 58,639 bytes,
MD5 03a9be1dd2a404b482aebd71aebafb15, as the brief states; SHA-256
be4f9102...0ad2be.

**Its name on disk was lower case,** `waqas_sharif_cv.pdf`, where git
tracks `cv/Waqas_Sharif_CV.pdf`. On this Windows checkout git matches
names without case, so a commit would still have stored the tracked name,
but Brief 6's check exists because the host matches with case: the live
site answers 404 for the lower-case name. The file was renamed on disk to
the tracked name, its content unchanged (MD5 rechecked).

Brief 6's 15 checks, pypdf 6.20.0 and xpdf's pdftotext 4.00, after the
rename: 14 pass. One A4 page (595 by 842 pt); Title "Waqas Sharif CV",
Author "Waqas Sharif", no other properties, no XMP block; 4 fonts, all
embedded (Carlito Bold, Regular, Italic; OpenSymbol); 3 links, each to an
address in the master's header, each answering 200 on a GET at
2026-10-19T14:11:28Z with no redirect; tagged; text extractable, 608
words; no em or en dash; no UC Davis certificate; no phone number; 41
numbers, every one in the master. The one fail is the probe for this
machine's user name, which is "waqas", as in Brief 6: 5 occurrences, all
required fields (Author, Title and the three link addresses), none a
path form.

Defeat: the doctored copy, rebuilt from this PDF, fails 13 of the 15,
each on its planted fault, as in Brief 6.

The new wording, searched in the text joined across line breaks: the
summary's "designs the architecture and the algorithms, makes the
engineering trade-offs, and directs coding agents", the skills item, and
"Claude Code writes the code to specifications I approve" present; "AI
seats", "four-seat" and the old summary wording absent; no "seat",
"vibe", "operator" or "routing". Defeat: the PDF before it fails 8 of
these checks. One check, the old italic line's "the blueprint, the
architecture, the trade-offs and the decisions are mine", is absent from
both, so it has no defeat; the earlier CV never carried that sentence.

Both download links on the built page, the Intro's and the footer's,
point to `/cv/Waqas_Sharif_CV.pdf`, the path git tracks; served locally,
it returns the new file's MD5.

## The brief's claim about gate B

"Until this is fixed, gate B refuses every commit, the chat's included."
[VERIFIED] It does not. Gate B rebuilds the staged source and compares
the staged output; it never reads the master. Run on the index as it
stood, 809fa14's content with the master already changed: gates A, B and
C passed, exit 0. The trace runs by procedure before a content commit,
not as a gate.

## CAPABILITIES.md

This seat's lane. The build table: "Seat" becomes "Role"; rows labelled
"Architecture and direction", "Decisions and briefs: a Claude chat",
"Implementation: Claude Code", "Design prototype: Claude Design". His
row's "corrected the seats" becomes his account of 2026-10-19: he
reviewed the design, the logic and the tests and had them corrected. The
design row now says Claude Design built the prototype from his six
reference sites and the content pack, and he reviewed it (ADR-0011). The
stack's AI tooling row, the file's header lines and the Highlights label
no longer say "seat". Left for the chat: its role section, its Highlights
line on "a second seat", and README's "How this project is run".

## Decisions this seat took, and why

- **The master's changes applied by a word diff against the last traced
  copy,** not retyped, and each replacement required to occur exactly
  once, so a wrong match fails rather than edits two places.
- **The CV's on-disk name restored to the tracked case,** a rename only,
  since a later `git add` from a case-sensitive tool could otherwise
  carry the lower-case name.
- **"Seat" removed from the rest of this seat's lane in
  `CAPABILITIES.md`,** beyond the table the brief names, because the
  rule covers public text about him and interviewers read that file.

## Errors this seat made

- A wording-check script crashed printing a bullet character to the
  console; rerun with the environment's encoding setting, which `-I`
  ignores, it crashed again. The checks it had already printed stood;
  the lines it was printing were read from the text file instead.

- The first draft of these records said the CPU was "10 to 71% busy
  with other programs" during the second Lighthouse set; those samples
  include Lighthouse's own browser. Corrected above and in
  `CAPABILITIES.md` and `STATE.md` before the push.

## What is next

- Lighthouse, five each, with no other sustained load (the job
  aggregator's mutation run finished): this page against the page
  before it. Until then, ADR-0009 is not shown met for this round.
- The operator's push; then the live check of this round.
- The chat: the role section and README, after this commit.
- For him: listing the site in emmabostian/developer-portfolios.

# Round 2, 2026-10-19 (UTC): Brief 10, the machine's load against Lighthouse

The session continued into Brief 10, pasted by the operator. HEAD at the
round's start: 12084bc, the chat's, pushed.

## Brief 9 live

[VERIFIED] At 2026-10-19T19:57:34Z, after the operator's push of
33bbff9 to bec7623: 24 live files byte-identical to HEAD by SHA-256; the
live page has the new summary, the new skills item and the review
bullet, and 0 hits for "seat"; the live CV PDF's MD5 is
03a9be1dd2a404b482aebd71aebafb15. The check's defeat, an older commit,
was shown earlier this session.

## What was asked

Brief 10, which is never committed. The operator's decision of
2026-10-19: a Lighthouse set counts only at light or medium load on this
machine; a set at heavy load is void and repeated once the load falls;
at medium the set is run, not deferred; every result is reported with
its level and compared only within it; a fail at light or medium is a
fail. Where the levels begin and end is not decided: the operator chose
to set them from measurement. Measure under the job aggregator's
mutation run (another Claude session, not to be stopped, slowed or
changed), then quiet, then optionally at controlled loads between; report
raw numbers, the quiet set against ADR-0009, and proposed levels with
their basis. The chat writes the ADR-0009 row; the operator decides.

## How it was measured

`cpu10.ps1` (scratchpad): Windows' counters once a second for 60 s,
`\Processor(_Total)\% Processor Time`, `\Memory\Available MBytes` and
`\Memory\Pages/sec`; then committed memory, and the processes using most
CPU over 5 s and most private memory. Memory was added after the first
phase showed it mattered; the first phase has CPU only. A Lighthouse set:
13.5.0, default mobile, five runs each, interleaved: the live page, the
same bytes served locally without compression, and the 600 ms defeat.
Each run's TBT, LCP, CLS and `environment.benchmarkIndex` were kept. A
reading during each set includes Lighthouse's own browser and is
reported only as that.

## The machine

7.7 GB of RAM, a commit limit of 31.7 GB, 12 logical processors, plugged
in, Balanced power plan. Microsoft Defender's scanner (`MsMpEng`) used
6 to 10% of the machine in most readings; Windows Update's background
download and Disk Cleanup appeared from 21:48Z, at up to 8% and 6%.

## The sets

Medians over the 60 s before each set.

| Set, UTC | Chrome | CPU | Available memory | Pages/s | Committed | Live TBT, LCP | Local TBT, LCP | Defeat TBT | ADR-0009 |
|---|---|---|---|---|---|---|---|---|---|
| Under the mutation run, 21:14 to 21:19 | 154 | 38% (mean 42.7) | not recorded; 235 MB at 21:22 to 21:23, 139 MB at 21:28 to 21:29 | not recorded; 13,539 and 13,833 then | 30.9 and 31.0 of 31.7 GB then | 516, 2,143 | 350, 2,455 | 2,117 | fails |
| Quiet, 21:58 to 22:02 | 155 | 34.9% | 850 MB | 5,969 | 22.9 GB | 63, 1,670 | 42, 2,255 | 1,854 | passes |
| Controlled: 6 of 12 cores busy, 22:09 to 22:13 | 155 | 77% | 444 MB | 7,581 | 22.7 GB | 25, 1,607 | 73, 2,256 | 1,826 | passes |
| Controlled: 600 MB held, with the 6 cores still busy until 22:22:44, 22:19 to 22:23 | 155 | 51.3% | 716 MB | 16 | 22.7 GB | 45, 1,667 | 33, 2,255 | 1,790 | passes |
| Controlled: 850 MB held, 22:30 to 22:34 | 155 | 32.7% | 994 MB | 6,834 | 23.1 GB | 36, 1,654 | 39, 2,257 | 1,850 | passes |

Runs, TBT in ms, in order:

- Under the mutation run: live 784 628 312 516 305; local 246 483 350 414 331; defeat 1949 1933 2117 2167 2148. benchmarkIndex 1,077 to 2,062.
- Quiet: live 280 74 63 0 11; local 36 64 42 25 43; defeat 1814 1888 1859 1852 1854. benchmarkIndex 1,703 to 2,313.
- 6 cores: live 80 0 25 22 36; local 85 57 73 13 92; defeat 1852 1905 1762 1769 1826. Local benchmarkIndex 1,598 to 2,068.
- 600 MB: live 156 76 45 20 38; local 94 33 59 13 26; defeat 1790 1766 1795 1760 1823.
- 850 MB: live 36 12 47 44 15; local 53 36 39 37 60; defeat 1893 1907 1850 1761 1764.

Every JSON report and every reading is kept in the scratchpad,
`load10/`.

**The quiet set passes ADR-0009** for the live page (LCP 1,670 ms, CLS 0,
TBT 63 ms) and the local copy (2,255 ms, 0, 42 ms); the defeat fails in
every set. That answers Brief 9's open Lighthouse check. The local
figures match 2026-10-15's (2,255 ms, 49 ms) on Chrome 154.

## What the numbers show

- **Memory, not CPU, separates the failing set from the passing ones.**
  CPU before the failing set (median 38%) was within the range of the
  passing ones (33 to 77%); the controlled load at 77% CPU passed.
  Available memory near the failing set was 139 to 235 MB with
  committed memory at 97 to 98% of its limit; every passing set had 444
  MB or more and 72 to 73%. In the failing set every main-thread
  category took 2.5 to 4 times as long as on 2026-10-15 (Brief 9's
  third set), as paging to disk would cause.
- **What was holding memory under the mutation run,** private memory at
  21:22Z: VS Code 8.1 GB over 42 processes, Claude 4.3 GB over 17,
  `vmmem` 3.0 GB (the virtual machine behind Claude Cowork, in the
  operator's account), Chrome 2.9 GB over 28. The mutation run's own
  processes held about 0.05 GB. With Cowork's machine and Chrome closed,
  committed memory fell from 31 to 22.3 GB.
- **`benchmarkIndex` does not separate them:** 1,077 to 2,062 in the
  failing set against 1,598 to 2,313 in the passing ones.
- **Not reproduced:** holding 600 or 850 MB did not bring available
  memory near the failing level; Windows paged other programs out and
  kept 556 to 1,032 MB available. A larger hold was not run: it would
  have pushed the whole machine into paging and slowed the job
  aggregator's session, which the brief forbids.
- **Paging per second is too noisy to place a boundary:** a median of
  16 in one passing set and 7,581 in another.
- **Chrome changed version mid-round:** it updated from 154 to
  155.0.8059.85 when the operator closed it, 21:48Z; the failing set ran
  on 154, the passing ones on 155. The 154 passes of 2026-10-15 give the
  same local figures as the 155 quiet set.

## Proposed levels, for the operator and the chat

Read over the 60 s before a set, with `cpu10.ps1`'s counters; available
memory first, because it is what separated the results.

- **Light:** available memory 800 MB or more, CPU median 40% or less.
  Basis: the quiet set (850 MB, 34.9%) and the 850 MB set (994 MB,
  32.7%), both passing.
- **Medium:** available memory 440 to 800 MB, or CPU median 40 to 77%.
  Basis: the 6-core set (444 MB, 77%) and the 600 MB set (716 MB, 51%),
  both passing. 77% is the highest CPU measured.
- **Heavy, void:** available memory under 440 MB, or committed memory
  over 90% of its limit, or CPU over 77%. Basis: the failing set (139 to
  235 MB, 97 to 98% committed). The 440 MB edge is the lowest passing
  reading; the true edge lies somewhere between 235 and 444 MB and is
  not measured. The 90% edge lies between 73% (passing) and 97% (failing)
  and is not measured. Above 77% CPU nothing was measured, so it is
  heavy until measured.

Each edge can be refined by any set run near it, since every set now
records the reading.

## Errors this seat made, Brief 10

- The first local server was started with a name that is not a variant
  directory and answered 404; caught by a request before any set ran.
- The first quiet attempt filtered out Lighthouse's error and left two
  headless Chrome processes; found, stopped by their Lighthouse profile,
  and the cause (Chrome's first launch after its update) found by a
  probe run.
- The CPU load's worker processes do not carry the script's name, so
  the stop script stopped only their parent and reported "0 left", a
  check that could not fail. The workers ran on until their own
  deadline, 22:22:44Z, into the 600 MB set, which is reported as a
  combined point.
- A first draft of the CAPABILITIES.md limit said the four failing sets
  ran at 139 to 235 MB available; only the last was followed by a
  memory reading, minutes after it. A first draft of the highlight said
  the cause was found; it is indicated, not reproduced. Both corrected
  before the commit.

## What is next

- The chat: Report 10; the ADR-0009 row on the levels, from it.
- The operator: deciding the levels.
- For him: listing the site in emmabostian/developer-portfolios.

# Round 3, 2026-10-20 (UTC): Brief 11, Report 10's close-out

The session continued into Brief 11, pasted by the operator, after the
Claude Code process exited with code 3221226505 (0xC0000409, a fail-fast)
partway through the first attempt; nothing had been written. Its log
showed event-loop stalls of about half a second with thousands of major
page faults each, which fits the memory pressure of round 2; the cause of
the exit is not tested. HEAD at the round's start: 750faec, the chat's,
pushed. It adds ADR-0009's Changes row of 2026-10-20, read this round:
the level is the worse of the memory and CPU readings over the minute
before a set; committed memory and the Chrome version are recorded but
set no level.

## What was asked

1. `CAPABILITIES.md`: beside the memory finding, the Chrome versions;
   and the highlight's "battery and machine speed were ruled out by
   measurement" kept only where a measurement supports each part.
2. The handoff: next actions to ADR-0009's levels; the portfolio-gallery
   review no longer this seat's (the gallery is public; reviews come
   through the chat); the listing merged (pull request 4350); the site
   not to go on his master CV.
3. Records only; the standing checks a records-only change needs.

## What was done

- **Chrome versions.** Added to the limit and the highlight: the four
  failing sets of 2026-10-19 ran on Chrome 154, the passing ones on 155
  after it updated itself at 21:48Z; against that, 154 passed on
  2026-10-15 (local LCP 2,255 ms, TBT 49 ms; 155 quiet: 2,255 ms, 42 ms).
- **The highlight's claim, checked part by part.** Battery: read once,
  at about 19:53Z on 2026-10-19, plugged in, between the third and
  fourth failing sets; nothing was read for the first two, so "ruled
  out" became "plugged in when checked". Machine speed: Lighthouse's
  `benchmarkIndex` read 1,077 to 2,062 in failing runs and 1,598 to
  2,313 in passing ones, so the measurement shows the short speed test
  did not separate them, not that speed was ruled out; reworded to that.
- **The limit** also notes that since 2026-10-20 a set counts only at
  light or medium load.
- **STATE and the completed list.** The levels row closed into
  completed, with the listing (his account, through the chat) and the
  master-CV answer; the blocked rows they cleared removed.

## Checks

[VERIFIED] The page did not change: two builds as of 2026-10 left
`index.html` and `static/` byte-identical to the committed files; the
content trace against the master passes. No page check applies to a
change that leaves the built page as it was (`docs/reference/standing-checks.md`
covers changes to the built page). Gates on the commit.

## Errors this seat made, Brief 11

- None found this round.

# Round 4, 2026-10-21 (UTC): the briefs folder off the repository

Waqas Sharif's instruction in this session: the briefs folder must not
appear on GitHub. It still did, because `briefs/README.md` was tracked
and `.gitignore` ignored the folder's contents (`briefs/*`) with that one
file excepted. Git cannot re-include a file whose parent folder is
ignored, which is why the earlier rule was written that way.

## What was done

- `briefs/README.md` untracked with `git rm --cached`; the file stays on
  disk, outside the repository.
- `.gitignore`: `briefs/`, the whole folder, with a comment naming his
  instruction.
- `README.md`: the pointer "Why briefs are not committed" moved from
  `briefs/README.md` to `CLAUDE.md`, Briefs, which says the folder is
  gitignored.
- `MAP.md` regenerated: 40 documented files, the briefs README gone.

[VERIFIED] `git ls-files briefs` lists nothing; `git check-ignore`
reports `briefs/README.md` and `briefs/architecture.md` ignored by the
new rule.

## Left as it was, and why

- **Gate A** still refuses anything under `briefs/` except a README
  (`tools/gates.py`). With the README untracked the exception never
  applies; changing what the gate blocks is ADR-0007's, so it is left
  for the architecture chat. ADR-0007 says only that the briefs are never
  committed, which the change keeps.
- **`CLAUDE.md`'s gate table** ("anything in `briefs/` but its README")
  still describes gate A as it is.
- **History:** the README remains in commits before this one; removing
  it would rewrite pushed history, which this seat does not do.

