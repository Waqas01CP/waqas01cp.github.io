---
type: reference
description: "The audit reports of this repository, one per audit, written by the audit seat in its own words, newest first, and how a report is written and committed."
status: current
---

# Audit reports

One report per audit, newest at the top, written by the audit seat in its
own words. This table is the navigation index for every audit of this
repository.

## Why this folder exists

An audit's own words, including what it checked and found correct, are
lost if only the implementing seat's summary of them survives, and the
audit itself could then never be checked. So the audit seat saves its
report here, chained like the session logs. This follows the operator's
decision of 2026-09-30 for the job-aggregator project, carried in his
Working Method: a trail of the order of the work, an audit that is itself
open to checking, and a later audit that reads this index first.

## How to use this file

Read the table first. When you need more, read the most recent relevant
report; each names the one before it.

An auditor starting a new audit reads the previous report and checks
whether each of its findings was closed. A finding closed in name only is
a finding again.

## How the audit seat writes a report

- **The file:** `logs/audit/YYYY-MM-DD-<which>-audit.md`, dated in UTC by
  the day the audit ran.
- **Frontmatter:** `type: log`; `description`, one sentence naming the
  scope and the verdict, in double quotes (gate C refuses an unquoted
  value holding ": "); `status: current`.
- **A header table:** the date in UTC; the model; the commit audited and
  the live site's state; "read-only"; the brief it answered; the previous
  report, by file name, or "none".
- **The body, in this order:**
  1. The verdict.
  2. A verdict for each item the brief listed: correct, incorrect, or
     cannot verify, with the evidence.
  3. Findings, most severe first. Each with a severity (wrong on the live
     site / defect / stale or wrong document / nit), its file and line or
     its place on the page, the claim, the evidence, and the command with
     its output.
  4. What was checked and found correct.
  5. What was not checked, and why.
  6. Anything a subagent reported that was not re-checked, tagged as such.
- **One row in the index below**, added at the top.

**What a report may never contain.** This repository is public.

- **No path into the operator's private material:** not the master CV's
  path or file name, not his vault's folders. Gate A refuses a file that
  holds one.
- **No text from the master CV that is not already on the live page.**
  Quote the page, not the master.
- **Nothing from the architecture chat's ledger or a brief that is not
  already in the repository.** Briefs are never committed.
- No em-dashes; dates in UTC.

**The audit seat writes the report and its index row, and nothing else.**
It never commits or pushes.

**The implementing seat then** reads the report, checks it for anything
the public repository must not carry, commits it unchanged with
`STATE.md`, and records what it did with each finding in its own session
log, which names the report. A committed report is never modified; a
correction is a note in the next report.

## Index

| Date | Audit | Scope | Verdict | Report |
|---|---|---|---|---|
| 2026-10-21 | First, cold, read-only | The repository at 27013c5 and the live site: wording about Waqas on every surface, content, accessibility, performance, records, documents, a visual pass at 360 and 1366 px | Live site sound and traced to the master; the footer line names no author of the code; three other reader-facing faults; stale documents and two records behind the repository; 22 findings, none blocking | [2026-10-21-first-audit.md](2026-10-21-first-audit.md) |
