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

**The styled site is live,** with every item from the master CV. A Python
generator renders one page in eight sections from two structured content
files, styled to the visual system of ADR-0011, with a little script for
the menu, the theme switch, the disclosures and the motion. `STATE.md` is
the honest picture; `CAPABILITIES.md` describes everything the site does.

The repository is public, per ADR-0002. `CHAT_STATE.md` is the one file that
is never committed, because it names blockers and errors; it is in
`.gitignore` and will also be blocked by a gate.

Every internal link is root-relative and no absolute self-origin is
hardcoded, so moving to a custom domain later is a DNS change and a CNAME
file, not a link rewrite.

## How this project is run

Waqas Sharif designs the architecture, its rules and the site's look,
makes the trade-offs, sets the standards, reviews the logic and the tests,
and decides every change; nothing goes live without his word.
Implementation is delegated, for speed, to Claude Code, which builds to
specifications he approves, writes the tests, runs the checks and logs
every session. Claude, in a separate chat, works his decisions into the
records in `docs/decisions/` and checks each report against this
repository. Claude Design built the visual prototype (ADR-0011); its
export is kept locally and never served, because it loads a framework
from a third-party CDN. How the work is organised is his own Working
Method, kept in his private vault and deliberately not linked from here.

## Where the documents are

| You want | Open |
|---|---|
| Everything the site is and does, for a reader who opens nothing else | `CAPABILITIES.md` |
| What exists, what is blocked and on whom | `STATE.md` |
| How to work here: authority, claim rules, scope floor | `CLAUDE.md` |
| Why a choice was made | `docs/decisions/`, indexed in its README |
| The evidence behind the decisions | `docs/research/` |
| What was deliberately not built, and what would reopen it | `docs/deferred/` |
| What the content schema is and how to add an item | `src/content/README.md` |
| How the page is checked against the master CV | `docs/reference/commands.md`, the content trace |
| The checks every change to the page runs | `docs/reference/standing-checks.md` |
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
`docs/reference/commands.md`.

## Licence

All rights reserved: see `LICENSE`. This repository is published to be
read, not reused. A separate template repository, with its own licence, is
planned for anyone who wants a site like this one.
