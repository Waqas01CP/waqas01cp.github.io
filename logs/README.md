---
type: index
description: The session log index. Read this first for what prior sessions did, then chain backwards through the most recent relevant log only as far as needed.
status: current
---

# Session logs

One log per session, newest at the top. This table is the navigation index
for all session history.

## How to use this file

Read this table first. It tells you what prior sessions did.

When you need detail beyond this table, read the most recent relevant log.
That log references the one before it. Chain backwards only as far as you
need, and stop when you have enough. Do not read the directory.

This rule is what keeps the reading cost flat as the log count grows.

## How to maintain it

Append your row in the same commit as your work. A log with no row here is
invisible.

Never delete or modify an existing row. A correction is a new row saying so.

Rows are compressed: no prose, no reasoning, nothing beyond what a future
session needs to decide whether to open the log.

If a log file exists with no row here, read it and add the row before doing
anything else.

One session, one file. A session that continues across several rounds adds
a row per round, each naming the same file.

## Log format

The session-log template in the operator's cross-project Working Method,
which lives in his private vault and is deliberately not linked from here.
File name `logs/YYYY-MM-DD-short-description.md`, dated in UTC. There is no
project-specific log-format record yet.

## Reorganisation

When this directory passes about 80 files at its root, split by lane into
subdirectories and leave this index at the top pointing into them. Decide it
before the root becomes unscannable, not after.

## Index

| Date (UTC) | Log file | Session | What was done | Outcome |
|---|---|---|---|---|
| 2026-10-10 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 8 | Working Method read in full; content trace found failing on the master's new project links and mended; CAPABILITIES.md, the seat's lane; report and handoff written to briefs/ | Trace passes, each defeat fails; the chat's lane and a CLAUDE.md update waiting |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 7 | Research 0004: whether this site goes on itself, and whether to open it for reuse; licences, forks against templates, precedents, fake stars | Evidence only; decisions listed for the operator and the chat |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 6 | Certificate diamond gap and one-month dates fixed on the wide timeline; round 3's pixel check found to cover the top of the page only, redone with every section painted | Fix 7e97c5b passes every check; round 3's result still holds; not pushed |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 5 | eaee932 deployed c97b99e; operator's NVDA 2026.2 run in Chrome passed every step; his text matched the model 45 of 45, 0 joins live | Speech test closed; STATE has no open build rows; ADR rows left to the chat |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 4 | c97b99e pushed but its Pages build never started (no runner); operator's second NVDA text found to be of the old page and a page copy, not speech; NVDA 2026.2 recorded | Fix not live until the next push; NVDA re-run waits on it |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 3 | Operator's NVDA run recorded (checks at load pass); his capture showed words run together; NVDA line model built and checked against it (94 of 94); visually hidden spaces added; LCP shift traced to page size | 0 joins in Chrome and Edge, pixel-identical page, all checks pass; c97b99e committed, not pushed |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5, round 2 | Push of 6812c4f checked on the live site; parity, keyboard and axe in Edge 154 and Chrome 154 on the live site; Lighthouse on the live site; .commitmsg deleted; NVDA steps written into the deferred entry | Live site matches in full mode in both browsers; Lighthouse meets ADR-0009 live with a narrower TBT margin (95 to 138 ms) |
| 2026-10-07 | [2026-10-07-tree-parity.md](2026-10-07-tree-parity.md) | Brief 5 | Everything hidden in the sections made aria-hidden with it; contact marks decorative with a text name; Close moves focus first; standing checks written down; styled site found pushed at 10:25Z, before the speech test | Full-mode tree at load matches the page without the rule in all 32 loads, both widths, themes, scripts on and off; committed, not pushed |
| 2026-10-06 | [2026-10-06-before-push.md](2026-10-06-before-push.md) | Brief 4 | content-visibility removed, failed ADR-0009 here (TBT medians 164, 250, 171, 249 ms), restored with a measured comment; its accessibility cost measured, collapsed panels exposed in full mode; Intro approval dated 2026-10-05 UTC; 44 DONE rows moved to completed.md | Rule kept per ADR-0009 and the brief; accessibility trade put to the chat; committed, not pushed |
| 2026-10-05 | [2026-10-05-styled-site.md](2026-10-05-styled-site.md) | Brief 3 | Prototype rebuilt in the generator; every master item in eight sections; content trace tool; knot in a worker, content-visibility with exact anchors | Ten checks pass, each defeated first; Lighthouse medians meet ADR-0009 with every heavy element; committed, not pushed; speech test open |
| 2026-09-26 | [2026-09-26-gates-map-and-as-of.md](2026-09-26-gates-map-and-as-of.md) | Brief 2 | Five gates from ADR-0007, map generator, build --as-of recorded in the output, tier order enforced; records committed through the live gates | 45 of 45 gate checks and 6 of 6 sabotage proofs pass; brief's commit order swapped; vault root name held as a digest |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 4 | Chat's removal of the last three Working Method paths committed; push authorised; the held commits found already pushed | No vault pointer left in the tree; all Brief 1 commits pushed |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 3 correction | Found the round 2 commits already pushed (20:46Z, not by the seat) and the site live; measured what .nojekyll does | Corrects round 3's "nothing is pushed". Site live at the root, byte-identical to committed output; Jekyll did not run |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 3 | Chat's record and README corrections committed; decisions noted (tier-order check, pre-push state gate, as-of month in Brief 2, no push yet); vault-pointer scan of all history | Committed, not pushed; three named Working Method paths remain, awaiting a ruling |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1, round 2 | Chat's answers applied: MarkupSafe pinned, .gitattributes LF, vault path removed from README.md, draft status dropped; nine commits by concern | Committed; version check confirmed to read requirements.txt; round 1's git diff finding corrected |
| 2026-09-26 | [2026-09-26-generator-and-content-model.md](2026-09-26-generator-and-content-model.md) | Brief 1 | Python generator, JSON content schema, two content gates, Rahzaan rendered unstyled, CLAUDE.md commands | Built and verified, uncommitted pending operator; YAML replaced by JSON; case-study link made root-relative |

The architecture chat's own history is in `CHAT_STATE.md`, not here.
