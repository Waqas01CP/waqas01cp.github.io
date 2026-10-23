---
type: instruction
description: How to work in this repository. Reading order, authority order, the fourteen-line scope floor, runtime and claim rules. Read before touching anything.
status: current
---

# CLAUDE.md

Personal portfolio website for Waqas Sharif. It carries the evidence a
one-page CV cannot hold, for employers first and Masters admissions readers
second, from one version.

The scope floor, runtime and conventions below are settled. **Commands
records every command that exists: the environment, the build, the gates
and the map.** Do not infer a command that is not there, and do not treat
its absence as permission. Stop and ask.

## Reading order

Read these, in this order, then stop and follow pointers. Do not read the
documented file set.

1. This file.
2. STATE.md. Where you start, not where you stop. It outranks memory; it
   does not outrank the code or the data.
3. logs/README.md. For more, read the most recent relevant log and chain
   backwards only as far as you need.
4. docs/decisions/README.md. The record index and the Pending list.

Then the brief for your task. MAP.md lists every documented file with its
description; it is generated and never edited by hand.

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

The operator's master CV is the only source of truth for anything the site
asserts about him. Every claim on the site traces to it. Every number
carries its provenance. Where another file disagrees with the master, the
master wins and the disagreement is reported.

The master lives outside this repository, in the operator's private vault.
**Its path is deliberately not recorded here**, because this repository is
public. Content reaches this repository through a brief or through the
operator, never by this repository pointing at a private location.

This rule is not a preference. A site that states something the master does
not is a claim he cannot stand behind in an interview.

## Scope floor

Fourteen lines, all from ADR-0004, which carries the source of each. Do not
propose, add or reintroduce any of them. When you refuse something on this
floor, name the line.

1. No claim that is not in the master CV.
2. No skill level anywhere: no bars, no percentages, no stars, no
   years-per-technology.
3. No testimonials, endorsements or quotes attributed to named people.
4. No blog, no articles section, no currently block.
5. No number that cannot be reproduced on demand.
6. No login, no gated content, no CMS, no database.
7. No feature that holds the only copy of a fact. Anything that must be read
   sits in the initial HTML. Enhancement on top is permitted; there is no
   exception to the rule itself.
8. No autoplaying audio or video, and no motion that ignores
   `prefers-reduced-motion`.
9. No third-party embeds that phone home: chat widgets, social feeds,
   comment systems.
10. No cookies, no tracking, no consent banner.
11. No collection of visitor data beyond what the host logs by default.
12. No prices, quotes, invoicing or payment mechanism.
13. No paid service without prior discussion.
14. No dependency added by import.

Removing a line takes its own record. It is not an exception granted in
passing.

## Runtime

Python. The site is built by a small generator in this repository, per
ADR-0006. There is no site framework and there will not be one.

One templating library, named in the first implementing brief. **No second
dependency without a record**, which is scope floor line 14.

The generator's output is committed. The build runs locally, not in a
continuous integration service.

## Conventions

Every item's content lives as structured data in one place. Markup is
generated from it, never hand-written per item, so a date or a fact is
written once. ADR-0006.

Every internal link is root-relative. No absolute URL pointing at this
site's own origin appears in the built page, so moving to a custom domain
later is a DNS change and not a rewrite. A document read apart from the
site may give the full address, such as the CV PDF. ADR-0002, and its
Changes, 2026-10-21.

Every item carries a specific checkable fact; a summary and full depth
follow only where the master CV has material for them. Every layer an item
has ships in the initial HTML, collapsed by disclosure rather than deferred
to a later fetch. ADR-0010, which supersedes ADR-0005.

Layer 3 holds decisions, trade-offs, what failed, how each was verified,
and production-scope facts an interviewer would probe. Not a changelog.
Each layer 3 disclosure is named for its item.

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

## Documentation layering

System-level picture in docs/. Component detail in comments in the file it
describes. A comment explaining why a guard exists and what the incident
cost is documentation; a comment restating the next line is noise.

## Commands

Every command that exists, each with what it exits and why: the
environment, the gates, the architecture chat's commits, the build, the
monthly refresh, the map, the one-dependency check and the content
trace, in `docs/reference/commands.md`. Read it before running anything.
Do not infer a command that is not there, and do not treat its absence as
permission.

## Procedures in docs/reference/

- Decision records: their format, when one is written, how one is amended, and what a seat may and may not change in one: `docs/reference/decision-records.md`.
- The gates: what each of the seven blocks, the case that defeats it, and why they bind before the hooks are set: `docs/reference/gates.md`.
- Briefs: the three files in the gitignored `briefs/`, and how each is written, ticked and replaced: `docs/reference/briefs.md`.
- Audits: who writes an audit report and its index row, and who checks and commits them: `docs/reference/audits.md`.
- CAPABILITIES.md: what to update in it at a session's close, and whose lane each section is: `docs/reference/capabilities-lanes.md`.

## Committing and pushing

One commit per piece of work, each passing the gates. Before committing,
look for commits you did not make and say so. The operator pushes; this
seat pushes only when he hands it a push. After a push, check that every
live file equals the build.

## Heavy work

One Lighthouse set or browser harness at a time. Say a job's whole length
before it starts. Before finishing, stop any process this seat started,
and touch none it did not. Read a browser's version from its file; never
launch the operator's own browser to get it.

## Writing

No em-dashes. Lead with the verdict. Active voice. Numbers carry their
provenance or they do not appear. Dates are UTC; when a local date differs,
say which is which. Plain text that survives a paste into Word.

"Operator" and "seat" are the Working Method's words. They may stay in
the decision records, the logs, STATE.md, docs/reference/, docs/deferred/
and this file (his answer, 2026-10-21). Everything else a reader meets
uses his name, Waqas Sharif.
