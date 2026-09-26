---
type: log
description: Brief 2. Five repository gates from ADR-0007, each proven by its defeating case and by sabotage; the map generator; the as-of month in the output; tier order enforced by the build. Two departures from the brief, both reported.
status: current
---

# 2026-09-26 (UTC): Gates, map, as-of month and tier order

Model: Claude Opus 5.5 (claude-opus-5-5). HEAD at start: 8aa86e2, with the
chat's uncommitted records in the working tree. HEAD at end: the commit
carrying this log, after 611bab2, 1429a5d, a5323ed and cb20f35. Mode:
mutating. Brief: 2. Previous log: 2026-09-26-generator-and-content-model.md.

The session's first `date -u` read 2026-09-26T21:54Z. Every date here is UTC; the local
date (UTC+5) was already 2026-09-27.

## What was asked

Brief 2, which is never committed, so its substance is here.

- **Five gates**, ADR-0007, as committed hooks in `.githooks/` that call
  Python in `.venv`, with the logic in `tools/`, standard library only.
  - **A**, pre-commit: refuse `CHAT_STATE.md` at any path, anything in
    `briefs/` but its README, and staged content holding a filesystem path
    into the operator's private material. Match path forms, never prose,
    and print file, line and matched text.
  - **B**, pre-commit: rebuild the staged tree with the as-of month read
    from the staged `index.html` and compare every generated file byte for
    byte; refuse an `index.html` with no as-of element.
  - **C**, pre-commit: a map generator writing `MAP.md` from every tracked
    Markdown file's frontmatter, with a check mode against the staged
    files. Coverage excludes `MAP.md` and `docs/design/DESIGN.md`.
  - **D**, every gate: a missing tool is a hard failure, never a skip.
  - **E**, pre-push: across the whole pushed range, refuse implementation
    work with no commit touching `STATE.md`, using the brief's
    implementation paths.
- **`build.py --as-of YYYY-MM`**, recorded as `<meta name="as-of">`.
- **Tier order** as a build check that fails, never sorts.
- **Documents**: CLAUDE.md commands and hook blocks, STATE.md corrections,
  this log.
- **Commit order**: gates first, activated after; then the chat's records
  through the live gates; then the build change; bookkeeping last; then
  push, as gate E's first real run.

Sixteen verification checks, each with its defeating case. Stop and hand
back if prose would have to be refused, a gate could not be proven, a
second dependency looked necessary, anything needed `--no-verify`, a
scope floor line would bend, a record and the brief disagreed, or gate E's
range could not be computed for a new branch's first push. **None fired.**

## What was done

**Gates.** [VERIFIED] `tools/gates.py` holds gates A to E. The hooks
`.githooks/pre-commit` and `.githooks/pre-push` are thin, mode 755, and
refuse, naming it, when the venv interpreter or the gate script is
missing. `tools/generate_map.py` exits 0 when current, 1 on a structural
problem and 2 when stale, so a caller never mistakes one for the other.
Activated with `git config core.hooksPath .githooks` after commit 611bab2.

**Proof, in a scratch clone.** [VERIFIED] The clone sat under a path with
spaces, with its own venv and a local bare repository as its only remote.
The real remote was never used for a test. A script drove real `git
commit` and `git push` through every case: **45 of 45 passed.** The script
lives in the session scratchpad, not in the repository.

| Brief check | Result |
|---|---|
| 1 `CHAT_STATE.md` with `-f`, at root and in a subfolder | Refused by gate A alone, with the planted files given frontmatter and the map regenerated so no other gate could object |
| 2 A brief other than the README with `-f` | Refused by gate A alone |
| 3 A planted template path | Refused, naming file, line 2, and the matched text |
| 4 A planted drive-letter path, with back and forward slashes | Refused |
| 5 A trivial edit to `briefs/README.md`, which names the Working Method in prose | Allowed. The control for 3 |
| 6 One character of `index.html` hand-edited | Refused by gate B, naming `index.html`. Also refused when the working tree was correct and only the staged copy was edited |
| 7 `items.json` changed, not rebuilt | Refused |
| 8 Rebuilt and staged | Allowed. The control for 6 and 7 |
| 9 Clock one month ahead | A `sitecustomize` on `PYTHONPATH` moved the clock to 2026-10-15; a plain build under it recorded 2026-10, proving the clock moved. A commit under it was allowed: gate B rebuilt with the recorded 2026-09 and matched. Then `--as-of 2026-10` changed the element and Rahzaan's span from 32 to 36 |
| 10 New Markdown, map not regenerated | Refused by gate C; still refused with the map regenerated but not staged; allowed once staged. A file with no description is a structural failure, reported as such |
| 11 Map generator renamed; venv moved | Each a hard failure naming what is missing. So are the gate script missing and `build.py` missing from the staged tree |
| 12 Push touching `src/` with no `STATE.md` | Refused; the remote did not move |
| 13 Several commits, `STATE.md` only in the last | Allowed |
| 14 Docs-only push, no `STATE.md` | Allowed |
| 15 Tier 3 above Rahzaan, tier 1, in a scratch copy | "item 'synthetic' (tier 3) is above item 'rahzaan' (tier 1) in Projects"; below, it builds |
| 16 Brief 1 checks | 37 of 37, and the no-script check with its defeat and control. The rebuilt output differs from the committed one by the as-of line only |

Beyond the sixteen: a stray file under `static/` is refused; the vault's
root folder name is refused in upper and lower case; the master CV's file
name is refused; a two-level climb from the root is refused while one from
`docs/decisions/` that stays inside passes. For a new branch's first push,
the range is exactly the commits on no remote: one commit, checked with
`git rev-list feature --not --remotes`. Refused without `STATE.md`,
allowed with it last.

**Every test can fail.** [VERIFIED] A second script neutered each gate in
the scratch clone and replayed its defeating case. Six of six got through:
A, B, C, D (the hook turned into a skip), E, and the tier check. The first
run reported one false failure. A sabotaged commit left a hand-edited
`index.html` at HEAD, and gate B then refused the next case. The script
now drops each commit a neutered gate lets in.

**Gate A cannot match itself.** [VERIFIED] It avoids that by construction:
every pattern is written so the source never contains the text it
matches. A scan of every file in the repository, the gate included, found
nothing. The first scan found one hit, a comment in `gates.py` giving a
two-level climb as an example; the comment now says it in prose.

**Gate results on the real commits.** [VERIFIED]

- 611bab2 (gates, tooling, map): committed before activation, as the brief
  orders. `--check` was run by hand against the staged files (exit 0), and
  gate A's scan by hand on the five staged files (no refusals).
- The records, attempted first in the brief's order: **refused by gate B
  alone**, "the staged index.html records no as-of month". Gates A and C
  raised nothing on any record.
- 1429a5d (build change): "gates A, B, C passed".
- a5323ed (records, second): "gates A, B, C passed".
- cb20f35 (CLAUDE.md): "gates A, B, C passed". The new hook-blocks text
  describes every pattern in prose and passed gate A.

**Map.** [VERIFIED] 19 files at 611bab2, 21 with ADR-0007 and ADR-0008.
**No file needed frontmatter added**: every covered file already had a
`description`. Record frontmatter's commented lines are skipped; any
other unreadable line is a structural failure, not a guess.

**Line endings.** [VERIFIED] `core.autocrlf` is true in the system Git
configuration on this machine. A fresh clone of cb20f35, made under that
setting, checked out 38 of 39 tracked files as LF in the working tree; the
39th is the empty `.nojekyll`, which has no line endings. Gate B compares
staged blobs, not working files, so working-tree line endings cannot fail
it.

**Documents.** CLAUDE.md: the gates, `--as-of`, the monthly refresh, the
map, and a rewritten hook-blocks table. STATE.md: every correction the
brief listed. The headline is rewritten as the current picture, the Pages
source is removed from Known unverified, the `.nojekyll` cause is settled
by ADR-0006 A3, the tier row is done, ADR-0005, 0007 and 0008 have rows,
and the design prototype is no longer blocked. Each gate has its own row.
`src/content/README.md`: tier enforced, as-of month, and a stale date
reference corrected.

## Rejected alternatives

- **The vault root folder name as a literal pattern**, as the brief listed
  it. `git log -S` finds it in no commit, so a committed pattern would
  publish it for the first time. The brief's reassurance that the pattern
  names already appear in pushed history is true of the other three and
  false of this one. It is held as a SHA-256 digest and matched by hashing
  every window of its length.
- **Any two-level climb refused.** That would refuse a legitimate link two
  levels up from `docs/decisions/`. A climb is refused only when it rises
  above the root from the file's own folder.
- **Exempting `gates.py` from gate A.** One named exemption would hide the
  gate's own file from the gate. Construction covers it instead.
- **The brief's literal commit order.** Records before the build change
  cannot pass gate B, which the brief also specifies. Scoping gate B to
  build paths would have let docs commits through unchecked on an
  inconsistent HEAD. Swapping the two steps kept the gate unconditional.
- **Gate B only on build-relevant commits.** Rejected for the same reason.
  It runs on every commit.
- **Reading the working tree for gate C.** A working-tree check passes a
  commit whose staged content differs. The generator writes from the
  working tree for convenience, and the check reads the index.

## Checked and found already correct

- Every covered Markdown file already carries a `description`.
- Four tracked files use the phrase "the operator's cross-project Working
  Method" in prose, as the brief said, and gate A passes all of them.
- ADR-0001's corrected count, seven pointers in six files, matches round 3
  of the previous log's scan.

## Not done

- ADR-0008's seven sections, which are out of scope and arrive with their
  content.
- Anything on GitHub's side, and any change to `items.json`'s content.

## Findings and recommendations

In the records, reported and not changed:

1. **ADR-0006 contradicts itself on `.nojekyll`.** A3 now says the cause
   is `.nojekyll`, settled by inference. Its new Changes row, dated the same
   day, says the cause "stays unverified and is named in A3". The row
   describes an earlier draft of A3. A3 also dates the operator's reading
   of the Pages settings as "2026-09-27 local" without its UTC date.
2. **ADR-0008 names a Work section,** yet its Consequences and More
   Information say the section headings for the `work`, `opensource` and
   `band` lanes are undecided. And none of its seven sections holds the
   degree, which ADR-0005 A3 counts as an item.
3. **ADR-0008 More Information still lists the visible date as open,**
   which its own Changes row closes. Kept as history, but it reads as
   open.
4. **ADR-0007's clock case** says "set the clock forward one month and
   rebuild; output unchanged". Read as a plain `python build.py`, that is
   false by design: the default as-of month is the clock's. Only the
   gate's rebuild is unchanged. The brief's wording, "gate B's rebuild",
   is the precise one.
5. **ADR-0007's "seven times in four days"** cannot be checked from the
   repository, whose first commit is 2026-09-25T21:42Z. Unverified, not
   shown wrong.

About the build, for when sections arrive: it renders every item section
before the timeline. ADR-0008 puts Timeline between Projects and Work, so
a Certifications item would render in the wrong place. Not reachable today.

Recommendations, not decisions:

- R1. Record gate E's implementation paths. They are the brief's.
- R2. Correct ADR-0006's Changes row to match A3.
- R3. Settle whether "Work" in ADR-0008 decides the `work` lane's heading.

## Noticed and not investigated

Nothing.
