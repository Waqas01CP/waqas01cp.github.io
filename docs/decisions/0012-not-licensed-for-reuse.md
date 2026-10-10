---
status: accepted
topic: process
description: "This repository is published to be read, not reused: all rights reserved. Reuse goes through a separate template repository, which may carry a copy of the engine but none of the operator's content. Read before adding a licence, accepting a contribution, or copying code out."
date: 2026-10-11
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# This repository is not licensed for reuse; reuse goes through a separate one

## Context and Problem Statement

This repository is public, because GitHub Free serves Pages only from
public repositories (scope floor line 13). Until 2026-10-10 it carried no
licence, so anyone could read it and nobody was given leave to reuse it,
with nothing that said either. Research 0004 found that a licence is a
decision with consequences for every later copy, and so takes a record.

There are two tensions. First, the repository is meant to be read: its
records, logs and checks show how the operator works, and that is part of
its value to a reader. A reader who likes it may want to copy it. Second,
it holds his own content, which no code licence should hand on: his name,
his CV text, the approved Intro paragraph and his contact details. It also
holds the checks that guard his private material. The operator wants
others to build from his work and credit it, and he wants this site to
stay his.

## Decision Drivers

- Scope floor line 13: free hosting, so the repository stays public.
- Research 0004 and its addendum of 2026-10-10.
- The operator's decision of 2026-10-10: this repository is not for
  reuse, and a separate repository is.
- The operator's priority for that separate repository, in his words:
  "if there is a choice between getting stars, forks and people starting
  to interact and do PRs and other practices then i would prefer this
  over even if later they sell the repo".

## Assumptions

- A1. A notice cannot remove what GitHub's terms give every user of a
  public repository, "to view and 'fork' your repositories". **Sourced**:
  GitHub Terms of Service, section D.5, read by the implementing seat
  2026-10-10 (research 0004). Not re-read by the chat.
- A2. Downloads of a public repository cannot be switched off, and forking
  can be prevented only for a private repository owned by an
  organization. **Sourced**: GitHub's documentation, read by the
  implementing seat 2026-10-10 (log 2026-10-07, round 8). Not re-read by
  the chat.
- A3. The operator may license a copy of this repository's code under
  other terms elsewhere. **Stated** by the operator, as its owner.
  **Not verified**: how far copyright covers code written by AI seats
  under his direction. The US Copyright Office's report Copyright and
  Artificial Intelligence, Part 2 (January 2025) concludes that "prompts
  do not alone provide sufficient control", and protects the human
  contribution perceptible in the output and its creative selection,
  coordination or arrangement. Pakistani law was not checked. His written
  content is his own authorship either way. The chat is not a lawyer.

## Considered Options

- All rights reserved here; reuse through a separate repository
- A code licence here, such as MIT, excluding his content
- No licence at all

## Decision Outcome

Chosen option: "All rights reserved here; reuse through a separate
repository".

We will keep this repository readable by anyone and licensed to no one,
under the notice in `LICENSE` of 2026-10-10. It reserves all rights beyond
what GitHub's terms give every user, and names the fonts' and the marks'
own terms.
We will point anyone who wants a site like this one to a separate template
repository, `portfolio-gallery`, planned on 2026-10-10. `LICENSE` and
`README.md` will name its address once it is published.
We will let a copy of this repository's engine go into that repository
under that repository's own licence: the generator, the templates, the
stylesheet, the scripts and the generic checks. The copy will carry none
of his content and none of the checks' private forms, such as gate A's
digest of his vault's folder name. That repository's records choose its
licence.
We will not link to or list that repository on this site before it is in
the master CV (scope floor line 1).

### Consequences

- Positive: his content and his records stay his. A reader can study the
  whole method, and a copier is pointed to a repository built to be
  copied.
- Positive: the separate repository can take a permissive licence and
  outside contributions without either touching this one.
- Negative: forks of this repository still happen under A1. A fork
  carries no permission, but enforcing that would take a takedown notice
  per fork.
- Negative: two repositories to maintain. Fixes to the engine here do not
  reach the copy by themselves.
- Neutral: under A3, the notice may protect less of the AI-written code
  than of his own writing. It reserves whatever rights exist.

### Confirmation

- `LICENSE` at the root says all rights reserved, and names the fonts'
  and the marks' terms. Present since fb48c97.
- No file in this repository grants a licence to its code or content.
  Test: search the tree for "Permission is hereby granted" and for SPDX
  identifiers. Pass: none outside the font licence files.
- Before a copy of the engine is published elsewhere, the copy is
  searched for his name, his email, the master CV's text and gate A's
  digest. Pass: none found.

## Pros and Cons of the Options

### All rights reserved here; reuse through a separate repository

- Good: keeps the site his and the method readable, and still offers
  reuse where it belongs.
- Bad: a second repository to build and run.

### A code licence here, excluding his content

- Good: one repository; copiers get clear terms.
- Bad: his content and code are interleaved in one content file and the
  gates. An exclusion clause is easy to misread, and copies would carry
  his workflow's private checks.

### No licence at all

- Good: no work.
- Bad: copiers get no terms and no direction, and nothing states his
  intent (research 0004, choosealicense.com).

## More Information

- Evidence: `docs/research/0004-this-site-as-a-project-and-as-a-template.md`,
  section 2 and the addendum.
- `portfolio-gallery`'s licence is that repository's decision. Research
  0004's addendum finds MIT fits the operator's stated priority and
  PolyForm Noncommercial does not. The operator's confirmation is pending.
- Revisit if the separate repository is abandoned, or if the operator
  decides to accept outside contributions here.

## Changes

| Date | Change | Why |
|---|---|---|
