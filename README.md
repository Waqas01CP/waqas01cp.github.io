---
type: reference
description: What this project is, how it is organised, and where each document lives. The entry point for a reader who has never seen it.
status: current
---

# waqas01cp.github.io

Personal portfolio website for Waqas Sharif. The GitHub Pages user site,
served at the domain root. ADR-0002.

Every job CV became one page on 2026-09-21, so most of the evidence in the
master CV has nowhere else to live. This site is where it goes. It serves
employers first and Masters admissions readers second, from one version.

**The styled site is built, with every item from the master CV, and not
yet live.** A Python generator renders one page in eight sections from two
structured content files, styled to the visual system of ADR-0011, with a
little script for the menu, the theme switch, the disclosures and the
motion. Until the next push, the live site is still the earlier unstyled
page. `STATE.md` is the honest picture.

The repository is public, per ADR-0002. `CHAT_STATE.md` is the one file that
is never committed, because it names blockers and errors; it is in
`.gitignore` and will also be blocked by a gate.

Every internal link is root-relative and no absolute self-origin is
hardcoded, so moving to a custom domain later is a DNS change and a CNAME
file, not a link rewrite.

## How this project is run

Three seats, described in the operator's cross-project Working Method. That
document lives in his private vault and is deliberately not linked from
here, because this repository is public.

- **Operator, Waqas:** decides scope and cost, approves every non-trivial
  decision.
- **Architecture chat:** concludes decisions, writes records and briefs,
  verifies what comes back against this repository rather than against the
  report. Does not implement.
- **Implementing seat, Claude Code:** executes briefs, writes code and
  tests, logs every session, audits.

Claude Design builds the visual prototype. It keeps no version history, so
each export is committed by hand with a log entry.

## Where the documents are

| You want | Open |
|---|---|
| What exists, what is blocked and on whom | `STATE.md` |
| How to work here: authority, claim rules, scope floor | `CLAUDE.md` |
| Why a choice was made | `docs/decisions/`, indexed in its README |
| The evidence behind the decisions | `docs/research/` |
| What was deliberately not built, and what would reopen it | `docs/deferred/` |
| What the content schema is and how to add an item | `src/content/README.md` |
| How the page is checked against the master CV | `CLAUDE.md`, Commands, the content trace |
| What prior implementing sessions did | `logs/README.md` |
| Why briefs are not committed | `briefs/README.md` |
| Completed work moved out of the state file | `docs/reference/completed.md` |

## The rule that governs every claim

The operator's master CV is the only source of truth for anything this site
asserts. It lives in his private vault, and its path is deliberately not
recorded here, because this repository is public. Every claim traces to it
and every number carries its provenance.

## How to run it

With the project venv active, `python build.py` writes `index.html` and
`static/` at the root. Setting up the venv, and the other commands, are in
`CLAUDE.md` under Commands.
