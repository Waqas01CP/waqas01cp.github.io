---
status: accepted
topic: process
description: The repository gates. What each one blocks, where it fires, and the case that must defeat it. Read before building or changing any gate.
date: 2026-09-26
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0007: The repository gates

## Context and Problem Statement

The Working Method requires four gates before the first feature, each proven
able to fire. This project has none. Everything holding it together so far is
a document that a reader has to choose to obey.

That is not hypothetical here. The chat wrote the no-private-paths rule into
`CLAUDE.md` and then breached it in six files, that one included. Seven
pointers across six files, found only when the implementing seat scanned
every commit. The rule existed the whole time. Nothing enforced it.

Three shaping facts arrived before the gates were built. The repository is
public and the site is live, so every committed file is a served URL. Commits
are made in series, one per concern, so a per-commit rule that demands
bookkeeping punishes the correct shape. And the build's output is committed,
so a gate comparing a fresh build to the committed one has to agree with it
about what month it is.

## Decision Drivers

- The vault-pointer incident: a documented rule with no enforcement failed
  seven times in four days.
- ADR-0006 rule 6 requires a rebuild gate, and rule 5 commits the output.
- ADR-0005 makes tier an assertion about order that something has to check.
- The Working Method's four gates, and its rule that a gate which cannot fail
  is worse than no gate.
- Commits by concern, agreed 2026-09-26, are the correct shape and must not
  be penalised.

## Assumptions

- A1. Local hooks are sufficient; no server-side enforcement is needed.
  **Stated** by the operator's single-contributor working setup. A hook is
  bypassable with `--no-verify` and absent from a fresh clone until
  installed. Both are accepted.
- A2. Every committed file is publicly served. **Measured** by the
  implementing seat 2026-09-26: the site serves committed Markdown raw, and
  the served bytes match the committed output.

## Considered Options

- Local git hooks, per-commit and pre-push as each gate requires
- A single pre-push check running everything
- Checks in the build only
- A hosted continuous integration service

## Decision Outcome

Chosen option: "Local git hooks, per-commit and pre-push as each gate
requires".

We will block any commit that stages a never-commit path, matching
`CHAT_STATE.md`, the briefs, and **any path segment naming the operator's
Working Method, its templates, or the vault that holds them**.
We will fail any commit whose staged content is not what a fresh build
produces, comparing against the as-of month recorded in the output rather
than against the build date.
We will fail any commit that leaves the generated map stale, checked by
running the generator in check mode.
We will treat a missing tool as a hard failure and never as a skip.
We will check that `STATE.md` moved **on push, not on commit**, across the
whole range being pushed.
We will prove every gate with the case built to defeat it before it counts as
built, and record that case beside the gate.

### Consequences

- Positive: the rule that failed seven times becomes a blocked commit.
- Positive: pre-push for the state gate lets commits stay one per concern,
  with bookkeeping riding the last one.
- Positive: the as-of month stops the rebuild gate failing every repository
  on the first of each month for no reason.
- Negative: hooks live in the working copy, so a fresh clone has none until
  they are installed. The installation step is itself uncaught.
- Negative: `--no-verify` bypasses all of it. Accepted per A1.
- Negative: the pointer pattern will produce false positives on prose that
  happens to name the Working Method. The gate must let a reviewer see what
  matched and why, not merely refuse.
- Neutral: nothing here runs on a server, so nothing catches a push made from
  another machine.

### Confirmation

Each gate is built with its defeating case and neither counts without the
other.

- Stage `CHAT_STATE.md` with `-f`. **Pass: refused. Fail: staged.**
- Stage a file containing a Working Method path. **Pass: refused, naming the
  file and the matched text. Fail: committed.**
- Hand-edit one character of `index.html` and commit. **Pass: refused.**
- Change `items.json` without rebuilding and commit. **Pass: refused.**
- Set the clock forward one month and rebuild. **Pass: output unchanged,
  because the as-of month is read from the output. Fail: output changes.**
- Add a file with frontmatter and commit without regenerating the map.
  **Pass: refused.**
- Rename the map generator and commit. **Pass: hard failure. Fail: a skip
  message and a successful commit.**
- Push a range touching `src/` with no `STATE.md` change. **Pass: refused.
  Fail: pushed.**
- Push a range of several commits where only the last touches `STATE.md`.
  **Pass: allowed.** This is the case that distinguishes pre-push from
  pre-commit, and a gate that refuses it is wrong.

## Pros and Cons of the Options

### Local git hooks, per-commit and pre-push as each requires

- Good: each gate fires at the point where its rule can still be honoured
  cheaply.
- Good: no service, no cost, no network.
- Bad: bypassable, and absent from a fresh clone.

### A single pre-push check running everything

- Good: one place, one installation step.
- Bad: a staged never-commit path is already in local history by then, and
  the point of that gate is to stop it entering history at all.

### Checks in the build only

- Good: nothing to install; the two content gates already work this way.
- Bad: a build check cannot see the index, so it cannot stop a file being
  committed. Wrong layer for four of the five gates here.

### A hosted continuous integration service

- Good: survives a fresh clone and cannot be bypassed locally.
- Bad: a service dependency for a single-contributor static site, against
  the free-by-default constraint, and it catches problems after they are
  already pushed to a public repository.

## More Information

- The four gates originate in the Working Method's new-project setup, which
  lives in the operator's private vault and is deliberately not linked here.
- The pointer gate's pattern is wider than the incident that caused it: the
  ruling on 2026-09-26 was that a named template path is a pointer, not only
  a path to the master CV.
- Not decided here: where the hooks live and how they are installed. That is
  the implementing brief's call, within these rules.
- The seventh pointer and the third file were both found by the implementing
  seat, not by the chat. The gate exists because the chat's own checking was
  recollection rather than search.
- Revisit if a second contributor joins, which breaks A1, or if a push from
  an ungated machine causes a real problem.

## Changes

| Date | Change | Why |
|---|---|---|
| 2026-09-26 | Context corrected: the breach was in six files, not "four files ... and in README.md and two folder indexes", which read as seven. | A factual error in the chat's own drafting, found on re-read before the record was committed. The next sentence already gave the right figure, seven pointers across six files. |