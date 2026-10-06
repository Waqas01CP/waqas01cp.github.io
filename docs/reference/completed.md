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
