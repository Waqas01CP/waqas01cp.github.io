---
type: reference
description: Where DONE rows from STATE.md move, so the state file holds only what is unsettled. Nothing is ever deleted from here.
status: current
---

# Completed

DONE rows move here from `STATE.md` in the same commit that completes them,
so every session reads only what is still unsettled. Rows are never deleted.

Proof is a commit, a decision record or a log filename. Never a file path.

| Task | Evidence | Date | Proof |
|---|---|---|---|
| Design prototype, moved from STATE.md's Build table | [VERIFIED] | 2026-10-05 | ADR-0011, accepted from it. The export opened and compared section by section by Brief 3's session, logs/2026-10-05-styled-site.md |
| Styled site: the prototype rebuilt in the generator, eight sections, every master item, every word in the first response | [VERIFIED] | 2026-10-05 | 9fbd407; logs/2026-10-05-styled-site.md, checks 1 to 9 |
| Fonts with their OFL texts; LinkedIn and GitHub marks, unmodified | [VERIFIED] | 2026-10-05 | 4fb6a3c; same log, Assets |
| Build refuses shortened text that is not a cut of its source, and a missing proof link outside ADR-0010's three | [VERIFIED] | 2026-10-05 | 9fbd407; same log, 27 generator checks each failing as built |
| Content trace of the built page against the master CV, with its command | [VERIFIED] | 2026-10-05 | 037a50e; same log, check 3, five planted changes each failing |
| Lighthouse, default mobile, medians of five, with and without each heavy element | [VERIFIED] | 2026-10-05 | Same log, check 10. One machine; results comparable only with each other (ADR-0009) |
| Intro paragraph's approval dated in UTC, 2026-10-05, in the content file and its schema note | [VERIFIED] | 2026-10-06 | 06f97c6; logs/2026-10-06-before-push.md |
| content-visibility on the sections measured both ways: Lighthouse, layout time, the accessibility tree at load in both modes, anchors and axe. Removed, failed ADR-0009 here, restored with a comment saying what was measured | [VERIFIED] | 2026-10-06 | e0e876c, 9a2043b; same log. The keep-or-remove decision is a STATE.md row |
| STATE.md's 44 DONE rows moved here, each verbatim | [VERIFIED] | 2026-10-06 | 9d06c61; same log |

## Moved from STATE.md, 2026-10-06

Every row STATE.md still held as DONE, moved together with the
operator's approval of 2026-10-06 (Brief 4). Each row's text is as it
stood in STATE.md at 35d54dd; only the Status column, DONE in every
row, is dropped. Grouped by the STATE.md table each came from.

### Documents

| Task | Evidence | Date | Proof |
|---|---|---|---|
| Decision index and topic list created | [VERIFIED] | 2026-09-23 | docs/decisions/README.md, read back after writing |
| ADR-0001 concluded and written | [VERIFIED] | 2026-09-23 | ADR-0001 |
| ADR-0002 concluded and written | [VERIFIED] | 2026-09-23 | ADR-0002 |
| ADR-0003 concluded and written | [VERIFIED] | 2026-09-23 | ADR-0003 |
| ADR-0004, the scope floor, concluded and written | [VERIFIED] | 2026-09-25 | ADR-0004 |
| Research 0003 written, skill display and writing settled | [VERIFIED] | 2026-09-25 | docs/research/0003-skill-display-and-writing.md |
| Master CV: UC Davis certificate and its credential link added | [VERIFIED] | 2026-09-25 | Diff returned by the edit |
| ADR-0001 annotated with the reversed clause | [VERIFIED] | 2026-09-23 | ADR-0001 Changes table |
| Master CV corrected: degree start, four certificate dates | [VERIFIED] | 2026-09-23 | Diff returned by the edit, reviewed line by line |
| Research 0001 written | [VERIFIED] | 2026-09-23 | docs/research/0001-how-hiring-readers-read-candidate-material.md, read back after writing |
| Research 0002 written, tool findings captured before loss | [VERIFIED] | 2026-09-23 | docs/research/0002-tools-and-libraries.md |
| Deferred entry for the timeline written | [VERIFIED] | 2026-09-23 | docs/deferred/projects-timeline.md, read back after writing |
| Log index created, no logs yet | [VERIFIED] | 2026-09-23 | logs/README.md, read back after writing |
| CLAUDE.md scope floor section | [VERIFIED] | 2026-09-26 | Written before Brief 1; this row was stale and was corrected by that session, evidence in logs/2026-09-26-generator-and-content-model.md |
| CLAUDE.md runtime and conventions sections | [VERIFIED] | 2026-09-26 | ADR-0006; written before Brief 1, row corrected by that session, same log |
| CLAUDE.md commands section | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md. Environment, gates activation, build with and without --as-of, monthly refresh, map and dependency check, each run |
| CLAUDE.md hook blocks section | [VERIFIED] | 2026-09-26 | Same log. Each of the five gates with what it blocks and the case that defeats it |
| MAP.md and its generator, with a check mode against the staged files | [VERIFIED] | 2026-09-26 | Same log. No file needed frontmatter added |
| ADR-0005 concluded and written | [VERIFIED] | 2026-09-25 | ADR-0005 |
| ADR-0007, the repository gates, concluded and written | [VERIFIED] | 2026-09-26 | ADR-0007 |
| ADR-0008, sections, tiers and depth, concluded and written | [VERIFIED] | 2026-09-26 | ADR-0008 |
| Named Working Method paths in this file's header, briefs/README.md and logs/README.md | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 4. Ruled pointers by the chat and removed by it; a scan of the working tree finds none left. They remain in pushed history. The Brief 2 never-commit gate must catch any path segment naming the Working Method or its templates |

### Repository

| Task | Evidence | Date | Proof |
|---|---|---|---|
| Repository name chosen | [VERIFIED] | 2026-09-23 | ADR-0002; folder renamed to waqas01cp.github.io |
| Public or private decided | [VERIFIED] | 2026-09-23 | ADR-0002; public, with CHAT_STATE.md never committed |
| .gitignore excluding CHAT_STATE.md written | [VERIFIED] | 2026-09-23 | ADR-0002 |
| git init and first commit | [VERIFIED] | 2026-09-25 | Done before Brief 1; this row was stale and was corrected by that session, evidence in logs/2026-09-26-generator-and-content-model.md |
| Project venv at .venv/, requirements.txt pinning Jinja2 as the one top-level dependency and MarkupSafe as its requirement | [VERIFIED] | 2026-09-26 | ADR-0006 Changes; logs/2026-09-26-generator-and-content-model.md |
| .gitattributes forcing LF, so a checkout under autocrlf matches a fresh build | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 2, fresh clones with and without it; logs/2026-09-26-gates-map-and-as-of.md, a fresh clone under the machine's system-level autocrlf checks out every text file as LF |
| Gate A, never-commit paths and private paths in content, pre-commit | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md; ADR-0007. Defeated by CHAT_STATE.md staged with -f and by a planted template path; control: prose naming the Working Method passes |
| Gate B, rebuild against the recorded as-of month, pre-commit | [VERIFIED] | 2026-09-26 | Same log. Defeated by a one-character edit to index.html and by items.json changed without rebuilding; control: rebuilt and staged passes |
| Gate C, map current against the staged files, pre-commit | [VERIFIED] | 2026-09-26 | Same log. Defeated by a new Markdown file without a regenerated map |
| Gate D, a missing tool is a hard failure, every hook | [VERIFIED] | 2026-09-26 | Same log. Defeated by renaming the map generator and by moving the venv |
| Gate E, STATE.md moved across the pushed range, pre-push | [VERIFIED] | 2026-09-26 | Same log. Defeated by pushing a src/ change with no STATE.md change; control: a series with STATE.md only in its last commit passes. Its implementation-path list is Brief 2's, not yet a record's |
| First push of the Brief 1 commits | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md, round 3 correction. Pushed from this clone at 20:46:30Z through the end of round 2, per the local reflog and git ls-remote, and not by the seat. It happened before the chat's instruction to hold the first push for Brief 2. Round 3's four commits were then pushed from this clone at 20:59:48Z, also not by the seat. The chat has since withdrawn the hold and authorised pushing |

### Build

| Task | Evidence | Date | Proof |
|---|---|---|---|
| Framework and rendering strategy decided | [VERIFIED] | 2026-09-26 | ADR-0006; row corrected by the Brief 1 session |
| Generator: reads content, computes timeline rows, renders, copies static files, byte-identical on rebuild | [VERIFIED] | 2026-09-26 | logs/2026-09-26-generator-and-content-model.md |
| Content schema, JSON, documented beside the content file | [VERIFIED] | 2026-09-26 | Same log |
| Gate: an item with no source fails the build, naming it | [VERIFIED] | 2026-09-26 | Same log; proven by deleting Rahzaan's source |
| Gate: an item with neither or both of proof and verification fails the build, naming it | [VERIFIED] | 2026-09-26 | Same log; proven both ways |
| Rahzaan rendered end to end, unstyled, every layer readable without scripts | [VERIFIED] | 2026-09-26 | Same log |
| Rahzaan layer 1 and layer 2 wording approved by the operator | [BELIEVED] | 2026-09-26 | Same log, round 2. Approved before Brief 1 was written; the brief's draft marker was left in by mistake. Stated by the architecture chat, not seen first-hand by the seat. Not in the master CV word for word; that is expected of layers 1 and 2. **Superseded 2026-10-05 by Brief 3**: Rahzaan's layer 1 is now the content pack's cut of its first bullet and its layer 2 the master's italic line, both checked against the master; logs/2026-10-05-styled-site.md |
| Tier order: the build fails when the content file's order contradicts tier | [VERIFIED] | 2026-09-26 | logs/2026-09-26-gates-map-and-as-of.md; ADR-0005 Changes, ADR-0008. Defeated by a synthetic tier 3 item above Rahzaan in a scratch copy; control: the same item below builds |
| As-of month: build.py --as-of, recorded in the output as a meta element | [VERIFIED] | 2026-09-26 | Same log; ADR-0006 Changes. With the clock a month ahead, the gate's rebuild is unchanged; --as-of with the next month changes the element and Rahzaan's span |
| What .nojekyll actually does when Pages is enabled | [VERIFIED] | 2026-09-26 | Same log, round 3 correction. Jekyll did not process the site: Markdown files are served raw with their front matter, /README.html is 404, and /.nojekyll itself is served. The live index.html and stylesheet are byte-identical to the committed ones. The cause is .nojekyll, settled by inference in ADR-0006 A3: the Pages source is "Deploy from a branch", which runs Jekyll by default, and Jekyll did not run |
