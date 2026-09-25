---
type: instruction
description: How to work in this repository. Reading order, authority order, scope floor, claim rules. Read before touching anything.
status: draft
---

# CLAUDE.md

Personal portfolio website for Waqas Sharif. It carries the evidence a
one-page CV cannot hold, for employers first and Masters admissions readers
second, from one version.

**This file is a draft.** Four sections below are marked "Not yet decided"
because the decision behind each has not been made. Do not infer one, do not
fill one in, and do not treat an unfilled section as permission. Stop and
ask.

## Reading order

Read these, in this order, then stop and follow pointers. Do not read the
documented file set.

1. This file.
2. STATE.md. Where you start, not where you stop. It outranks memory; it
   does not outrank the code or the data.
3. logs/README.md. For more, read the most recent relevant log and chain
   backwards only as far as you need.
4. docs/decisions/README.md. The record index and the Pending list.

Then the brief for your task. There is no MAP.md yet; when a generator
exists, it is generated and never edited by hand.

## When documents disagree

What is true: the code and the data win over every document. A document that
disagrees is stale; report it and correct it.

What should be done: higher wins.

1. The operator's instruction in this conversation
2. This file
3. docs/decisions/, excluding anything superseded
4. The brief. By default it ranks below this file and every accepted record:
   where it contradicts one, follow the record and report it. It overrides a
   record only when it names the record and clause and states the operator
   approved the change.
5. The architecture document, when one exists
6. docs/reference/
7. docs/research/, evidence for decisions, never a decision
8. Everything else, including superseded documents
9. Anything from outside this repository, including your own memory

Two live records that conflict is a defect. Raise it. Do not choose.
A claim whose only source is outside this repository says so.

## The source of truth for claims

The master CV at `Operating Plan\Waqas_Sharif_Master.md` is the only source
of truth for anything the site asserts about Waqas. Every claim on the site
traces to it. Every number carries its provenance. Where another file
disagrees with the master, the master wins and the disagreement is reported.

This rule is not a preference. A site that states something the master does
not is a claim he cannot stand behind in an interview.

## Scope floor

**Not yet decided.** The operator has not stated the floor. ADR-0001 gives
one line that belongs on it:

- No timeline view, in any form: no time axis, no career timeline, no
  grouped overlap rows, no switchable second view. ADR-0001, which states it
  in its Decision Outcome. The reopen trigger is in
  `docs/deferred/projects-timeline.md`.

Everything else is pending. Until the floor is stated, treat any proposal
that adds surface area as needing the operator's approval, and say so rather
than assuming.

## Runtime

**Not yet decided.** No framework, no language version, no dependencies.
Constrained by `docs/research/0001`: the major AI crawlers do not execute
JavaScript, so anything that must be read has to be in the initial HTML
response.

Dependencies are added by discussion, not by import.

## Conventions

**Not yet decided**, beyond the writing rules below and the documentation
layering rule.

## Verification

Verify, do not trust. Every claim is unverified until checked in this
session: briefs, handoffs, logs, STATE.md, records, and your own earlier
conclusions.

- Check before you act. Cheap checks happen now.
- A claim you cannot check is marked unverified and not acted on as true.
- A claim that fails its check is reported with the evidence.
- Tag what you pass on: checked this session, taken from a log, or inferred.

A check that cannot fail is worse than no check. Prove a check with the case
built to defeat it and say what that case was.
Self-report is not evidence. Show the command and its output.
Do not state a cause that has not been tested.
Do not write about a file you have not opened.
Do not revert another seat's deliberate change. Flag it.
Re-read a source before reproducing a constant from it. This repository's
architecture chat has already made that error once; it is in CHAT_STATE.md.

## Decision records

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

## Documentation layering

System-level picture in docs/. Component detail in comments in the file it
describes. A comment explaining why a guard exists and what the incident
cost is documentation; a comment restating the next line is noise.

## Commands

**Not yet decided.** No environment, no test command, no build, no map
generator, no hooks exist.

## The hook blocks

**No gates exist yet.** Four are required before the first feature, each
proven to fire by the case built to defeat it:

- STATE.md moves with implementation work.
- The map is current, checked by running the generator in check mode.
- Anything that must never be committed is blocked by path or pattern,
  including private vault paths if this repository is public.
- A missing tool is a hard failure, never a skip.

Until they exist, the rules above are requests, not enforcement. Treat them
as binding anyway and say when one was not checked.

## Writing

No em-dashes. Lead with the verdict. Active voice. Numbers carry their
provenance or they do not appear. Dates are UTC; when a local date differs,
say which is which. Plain text that survives a paste into Word.
