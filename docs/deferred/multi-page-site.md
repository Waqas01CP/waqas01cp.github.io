---
type: deferred
description: Separate pages for the site's sections (home, Projects, Timeline, Work and the rest) instead of one page with a section menu. Deferred 2026-10-03 when the operator chose one page; kept so the option can be explored later. Trigger inside.
status: open
---

# Separate pages instead of one page

**Deferred 2026-10-03.** The operator chose one page with a section menu
that stays in view (ADR-0008 Changes, 2026-10-03), and asked that the other
option be kept on record in case he wants to explore it.

## The option

A short home page carrying the Intro and the highlights, and a page of its
own for Projects, Timeline, Work, Education, Certifications, Skills and
Contact. Among the operator's reference sites of 2026-10-03, rubenmarcus.dev,
orchid.security and studio-nikita.com work this way; matteovincenti.com,
khaledoghli.com and the RecordRecharge page use one page with a menu.

## Why it was not chosen

- ADR-0008 settled one page, and the operator removed per-project pages on
  2026-09-26 because the Rahzaan case study is already the deep
  destination; a page in between added a click and nothing else.
- One page puts every word in one response, which is simplest for search
  engines and AI tools (research 0001).
- The references showed one page can be as rich as a multi-page site.

## What it would cost

A change to ADR-0008's Decision Outcome, more pages for the build to
generate and the gates to check, and links between them. Each page would be
lighter, which helps ADR-0009's goals.

## Trigger

The operator asks to explore it, or a measured problem with the one page:
it fails ADR-0009's goals with its content at full size, or readers cannot
find a section the menu points to.
