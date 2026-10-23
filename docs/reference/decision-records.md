---
type: reference
description: How decision records are written and amended, and what a seat may and may not change in one. Moved word for word from CLAUDE.md. Read before writing or touching a record.
status: current
---

# Decision records

Moved word for word from `CLAUDE.md`'s section "Decision records" on
2026-10-23 (UTC), which the operator approved that day (Brief 14,
Part 3). `CLAUDE.md` points here. A section named in the text, such as
Commands, is one of `CLAUDE.md`'s.

docs/decisions/, MADR 4.0.0 with an Assumptions section, per the Decision
Record Standard. The `topic` field takes one value from the fixed list in
docs/decisions/README.md.

Write the record when the decision concludes, not afterwards.
A record's decision is never silently rewritten: an amendment that leaves it
in force goes in its Changes table; a replacement is a new record that
supersedes it, with both directions linked.
Every assumption carries its basis: measured, sourced, or stated by the
operator.

A seat may annotate a factual error with its date and evidence, correct a
wrong reference, and report a record as stale. It may not change a decision,
retire a record, or resolve a conflict between two records.
