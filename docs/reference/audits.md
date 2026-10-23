---
type: reference
description: Where audit reports live, who writes a report and its index row, and who checks and commits them. Moved word for word from CLAUDE.md.
status: current
---

# Audits

Moved word for word from `CLAUDE.md`'s section "Audits" on
2026-10-23 (UTC), which the operator approved that day (Brief 14,
Part 3). `CLAUDE.md` points here. A section named in the text, such as
Commands, is one of `CLAUDE.md`'s.

Audit reports live in logs/audit/, indexed in its README, which gives
their format. The audit seat writes its report and the report's index
row, and nothing else; this seat checks the report for anything the
public repository must not carry, then commits both unchanged.
