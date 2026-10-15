---
type: log
description: "Brief 8. The master CV's Portfolio Footer line on the page, word for word, in the footer, its repository address a link to this repository; the build checks the footer's shape and splits it around the link; the content trace requires the line whole and its address as a link. Every standing check rerun on the new page; the link checked on a GET."
status: current
---

# 2026-10-15 (UTC): The footer line

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: 5f3b84d, the
chat's, pushed; origin/main also at 5f3b84d. The working tree held an
uncommitted Changes row in ADR-0008, with the chat's message in
`.commitmsg/1-adr-0008-footer-line.txt`. HEAD at end: the commit carrying
this log. Mode: mutating. Brief: 8. Previous log:
2026-10-12-fonts-gate-c-survey.md.

The session ran from 22:15Z on 2026-10-15 (03:15 local on 2026-10-16). It
continues the conversation that ran Briefs 5 to 7.

## What was asked

Brief 8, which is never committed, so its substance is here. The chat
verified Report 7 on 2026-10-12: live files matching, the rebuild
identical, the trace passing, the removed fonts answering 404, and gate
C's header check holding on 31 values of its own. It noted that the check
is stricter than "agreeing with PyYAML": it also refuses values PyYAML
would silently reinterpret, such as a " #" that cuts a description short.

The master CV now carries a site-only paragraph, PORTFOLIO FOOTER,
approved by the operator on 2026-10-15. ADR-0008's Changes row of
2026-10-15 decides it: the footer carries the line word for word, its
repository address a link to this repository, and the trace's coverage
requires it. The row was written outside the chat on 2026-10-15 at 14:16Z;
the chat read it and adopted it.

1. **The footer.** The line in `footer.html.j2` from site content, taken
   from the master by script, the master's italic note above it left out;
   the address `github.com/Waqas01CP/waqas01cp.github.io` a link to
   `https://github.com/Waqas01CP/waqas01cp.github.io`, its visible text as
   the master has it; one paragraph a screen reader reads as one run.
   Placement and styling within ADR-0011 are this seat's. If a claim in
   the line is not supported by the repository, stop and report; do not
   reword it.
2. **The trace.** Coverage requires the line whole, beside the Portfolio
   Intro. Defeats: the line removed from the page; one word changed in a
   copy of the master. Each must exit 1.
3. **`CAPABILITIES.md`,** this seat's lane.

Verification: each check on its defeat case first; build twice; gates; the
trace; the full standing checks on the new page, with the footer line
reading with no run-together words; Lighthouse, median of five, against
ADR-0009; the link resolving on a GET, with status and final address.

## A commit this seat did not make

The ADR-0008 row was uncommitted at the start, with the chat's message
file. `CLAUDE.md` lets this seat make the chat's commits only when the
operator hands them over, so it was left unstaged; every commit of this
seat names its files. During the session, at 2026-10-15T22:16:34Z, the
operator committed it as a18919d with the chat's message, that one file
only, pushed it, and removed `.commitmsg/`.

## The line's claims

[VERIFIED] Each checked against the repository this session before the
line went on the page:

- "A small Python generator builds it": `build.py`; `requirements.txt`
  pins Jinja2 3.1.6 and MarkupSafe 3.0.3, Jinja2's own requirement.
- "a tool checks every claim against my CV": `tools/check_content.py`,
  which traces every block of text on the page to the master.
- "its decisions are recorded": 12 records in `docs/decisions/`.
- "it was tested with a screen reader": ADR-0010's Changes row of
  2026-10-07, NVDA 2026.2.
- "in the open", "Source and records": the repository is public; a GET of
  `https://github.com/Waqas01CP/waqas01cp.github.io` at
  2026-10-15T22:19:23Z returned 200, final address the same, no redirect.
  `LICENSE` reads all rights reserved (ADR-0012), which the line does not
  contradict: it offers the source to read.

No claim needed stopping on.

## The change

**Content.** [VERIFIED] A script took the line from the master's
PORTFOLIO FOOTER section (the master last changed 2026-10-15T14:09Z),
leaving out the italic note above it, and found the address by pattern.
`site.json` gains `footer`: the line as `text`, and `link` with the
address as its `text` and `https://` plus the address as its `url`.
`source` names `portfolio-footer`.

**Build.** `build.py` refuses a footer that is not `{text, link: {text,
url}}`, whose link text does not occur exactly once in the line, or whose
URL `url_problem` refuses (ADR-0002); then splits the line around the
link's text. The template renders one paragraph, the text before, the
link, the text after, all inline, so a screen reader reads one run and no
hidden space is needed.

**Where, and how it looks.** The last child of the footer, a row of its
own (`flex-basis: 100%`) under the name, place and links, at 72ch, 14 px,
line height 1.65, in the muted ink the footer's place line uses. The link
keeps the site's base link style, the accent ink, underlined, so it is not
marked by colour alone; it may break anywhere on a narrow screen. Reason:
the footer is a wrapping flex row, and a long paragraph as one more item
would have pushed the links aside. Screenshots at 360 and 1366 px, light
and dark: the line wraps to 139 by 320 px and 69 by 615 px, no horizontal
overflow at either width.

**Trace.** Coverage takes PORTFOLIO FOOTER beside PORTFOLIO INTRO: the
line whole, and any address in it as a link (`https://` plus the address
among the page's links), the second because ADR-0008's row makes the
address a link. `docs/reference/commands.md` and
`docs/reference/standing-checks.md` describe the new coverage.

[VERIFIED] Trace: 377 blocks, 0 not traced; portfolio footer 1 of 1,
portfolio footer links 1 of 1; PASS. Defeats, each exit 1:

- the line removed from a copy of the page: portfolio footer 0 of 1, its
  link 0 of 1;
- "small" made "tiny" in a copy of the master: the page's line no longer
  traces, and portfolio footer 0 of 1;
- the address left as text, not a link: portfolio footer links 0 of 1.

The control, the page unchanged: exit 0. The build, in a scratch copy of
the tree, refuses a link text not in the line and a link to this site's
own origin, each by name, exit 1.

**Build twice:** identical across the 14 generated files; a build as of
2026-09 differs. The page changes by one line, the footer paragraph, and
`site.css` by four.

Commit 327f2c1.

## Live, Brief 7

[VERIFIED] Before this round's change: 24 live files (the page,
everything under `static/`, the CV PDF and the design-system draft)
byte-identical to HEAD by SHA-256, and the three removed font and licence
files answer 404.

## The standing checks, on the new page

One harness at a time, headless, each defeat first. Chrome 154.0.8037.98,
Edge 155.0.4283.45.

| Check | Defeat case, result | The page |
|---|---|---|
| Tree at load, full mode | 0403c68 against its reference: 4 of 4 loads differ | 32 of 32 loads match the page without the rule |
| Tree at load, default mode | The planted Intro paragraph: 1 node added | 32 of 32 loads add no node |
| Keyboard | Close hiding before moving focus: 58 of 60 | 60 of 60 |
| axe-core 4.14.0, 360 and 1366 px, light, device dark, switched dark, as loaded and all open | Planted faint text and an image without alt: violations in 12 of 12 cells | 0 violations in 12 of 12 cells |
| Anchors | The rule without its `:has(:target)` undo: 74 of 132 landed | 132 of 132 |
| Joined words, NVDA model | 6812c4f: 58 at 1366 px, 59 at 360 px, in Chrome and Edge | 0 at both widths, in both |

**The footer line, as the NVDA model reads it,** at 1366 and 360 px: one
line, "I architected this site; ... Source and records:
github.com/Waqas01CP/waqas01cp.github.io", every space present.

**Lighthouse** 13.5.0, default mobile, five runs each, interleaved,
served locally without compression:

| Variant | LCP median | CLS | TBT median | TBT runs |
|---|---|---|---|---|
| This page | 2,255 ms | 0 | 49 ms | 58 49 53 41 34 |
| The page before it (HEAD before 327f2c1) | 2,258 ms | 0 | 29 ms | 0 27 31 34 29 |
| Defeat: a 600 ms synchronous script | 2,105 ms | 0 | 1,778 ms | fails ADR-0009 |

Both pages meet ADR-0009. This page's TBT runs sit above the other's, 34
to 58 against 0 to 34; the cause is not tested. The page grew by 368
bytes, 164 gzipped.

## Decisions this seat took, and why

- **The line stored once, split by the build around its link's text,**
  rather than stored as three pieces, so the content file holds the
  master's sentence whole and the trace reads it whole.
- **The address made a link by its own text,** checked to occur exactly
  once, so the link cannot be built from a different string.
- **Its own full-width row at the footer's end,** for the reason above.
- **The trace also requires the address as a link,** not only the words,
  because ADR-0008's row decides the link; the brief asked for the words.

## Errors this seat made

- A first draft of the records script recorded Brief 7's work as live
  before this session had checked it; caught, and the live check run
  before the script was.
- A first draft of Report 8 said the footer's paragraph was the only
  muted 14 px text on the page, which was not checked; cut.
- Brief 6 left one overlong line in `docs/reference/commands.md`'s
  content trace paragraph; rewrapped with this round's edit.

## What is next

- The operator's push of 327f2c1 and this commit; then the live check.
- Report 8 to the chat.
- For him, not for the brief: listing the site in
  emmabostian/developer-portfolios, once the line is live.
