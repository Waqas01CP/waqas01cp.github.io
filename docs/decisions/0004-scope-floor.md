---
status: accepted
topic: process
description: The scope floor. Fourteen things the site will not do, each with its source. Every brief carries it. Read before proposing anything that adds surface area.
date: 2026-09-25
decision-makers: Waqas Sharif
# consulted:
# informed:
---

# ADR-0004: The scope floor

## Context and Problem Statement

A personal site has no natural boundary. Every feature that exists on some
other portfolio is arguable here, and each one is arguable again in every
later session unless the answer is written down once.

The Working Method requires a scope floor in `CLAUDE.md` and in every brief,
and requires each floor line to cite a record that contains it. Without the
record the floor is a preference that a later session can talk its way past.

Three of the proposed lines could not be settled by preference and waited on
evidence: whether to show a skill level, whether the site carries writing,
and what if anything is exempt from the rule that readable content sits in
the initial HTML. Research 0003 and 0001 settled the first two and the
operator closed the third on 2026-09-25.

## Decision Drivers

- The Working Method: a brief without a floor is incomplete.
- Research 0001: an AI summary is often the first reader, and it executes no
  JavaScript; polish without proof now reads as suspicion.
- Research 0003: counting exposure is the low-validity form of evidence,
  .11 against .45 for describing what was accomplished.
- The standing free-by-default cost constraint.
- The master CV as the only source of truth for claims.

## Assumptions

- A1. The readers are employers first and Masters admissions readers second,
  and neither needs anything this floor excludes. **Stated** by the operator
  2026-09-22 as the site's purpose. The first half is his to state; **the
  second half is not evidenced and is the part most likely to be wrong.**
- A2. The research behind lines 2, 4 and 8 holds, with the limits recorded
  in those files rather than restated here. **Sourced**: research 0001,
  0002 and 0003.

## Considered Options

- A floor of fourteen stated lines, gated where a gate is possible
- Only the lines that are hard constraints, leaving taste undecided
- No floor, deciding each feature when it is proposed
- A floor plus a written exception process

## Decision Outcome

Chosen option: "A floor of fourteen stated lines, gated where a gate is
possible".

We will hold the following fourteen lines. Each is cited to where it comes
from. Anything that breaches one is refused, and the refusal names the line.

**Claims**

1. No claim that is not in the master CV. Operator, standing rule.
2. No skill level anywhere: no bars, no percentages, no stars, no
   years-per-technology. Research 0003, and the operator's own rule that a
   number carries its measurement or it does not appear.
3. No testimonials, endorsements or quotes attributed to named people.
   Operator, 2026-09-23, who noted this one may change later.
4. No blog, no articles section, no currently block. Research 0003.
5. No number that cannot be reproduced on demand. Operator, standing rule.

**Features**

6. No login, no gated content, no CMS, no database. Operator, 2026-09-23.
7. No feature that holds the only copy of a fact. Anything that must be read
   sits in the initial HTML. Research 0001. Enhancement on top is permitted;
   the operator confirmed this reading and withdrew his "not absolute"
   qualifier on 2026-09-25, so no exception exists.
8. No autoplaying audio or video, and no motion that ignores
   `prefers-reduced-motion`. Operator, 2026-09-23.
9. No third-party embeds that phone home: chat widgets, social feeds,
   comment systems. Operator, 2026-09-23.

**Data**

10. No cookies, no tracking, no consent banner. Operator, 2026-09-23. A
    consent banner is also self-defeating: content behind consent is what an
    AI crawler sees instead of the work. Research 0001.
11. No collection of visitor data beyond what the host logs by default.
    Operator, 2026-09-23.

**Commerce and build**

12. No prices, quotes, invoicing or payment mechanism. ADR-0002, which
    records the GitHub Pages term this keeps the site inside.
13. No paid service without prior discussion. Operator, standing constraint.
14. No dependency added by import. Operator, 2026-09-23.

We will name the breached line whenever we refuse something on this floor,
rather than refusing on judgement.
We will treat a line's removal as a decision requiring its own record, not
as an exception granted in passing.

### Consequences

- Positive: a later session, human or otherwise, cannot argue a feature in
  by restating its benefits. The floor is a citation, not an opinion.
- Positive: lines 2, 4 and 7 now carry evidence rather than preference,
  which is what makes them hold under pressure.
- Negative: fourteen lines is a lot to hold in mind, and only some can be
  gated, so the rest depend on the reviewer actually reading this file.
- Negative: line 3 is expected to change. Recording it anyway means a record
  that is known to be temporary.
- Negative: a floor set before the site exists may exclude something that
  turns out to matter. A1's second half names that risk.
- Neutral: "no timeline" was line 6 of the fifteen originally proposed on
  2026-09-23 and is not here. ADR-0003 reversed it, which is why the floor
  is fourteen and not fifteen.

### Confirmation

Gateable, and to be built as gates before the first feature:

- Line 7: fetch the built page with JavaScript disabled and confirm every
  claim is present. A build where any claim appears only after script
  execution fails.
- Line 10: grep the built output for cookie APIs and known analytics hosts.
  Any match fails.
- Line 9: grep the built output for external script and iframe sources
  outside an allowlist. Any match fails.
- Line 14: a dependency added without a record fails the review.

Not gateable, and therefore dependent on review against this file: lines 1
to 5 other than 2, plus 3, 6, 8, 11, 12 and 13. **Saying so is the point.**
A floor that claims enforcement it does not have is worse than one that
names its soft edges.

## Pros and Cons of the Options

### A floor of fourteen stated lines

- Good: settles the recurring arguments once, with citations.
- Bad: some lines are review-only, so the floor is partly honour system.

### Only the hard constraints

- Good: shorter, fully gateable.
- Bad: leaves lines 2, 3 and 4 open, which are exactly the ones that took
  research to settle and would otherwise be re-argued every session.

### No floor

- Good: nothing to maintain.
- Bad: every feature is re-litigated, and the Working Method requires a
  floor in every brief, so briefs could not be written.

### A floor plus a written exception process

- Good: handles the case where a line turns out to be wrong.
- Bad: an exception process is the mechanism by which floors erode. Removing
  a line through its own record is slower and that is the intent.

## More Information

- Evidence: `docs/research/0001`, `0002`, `0003`.
- Line 3 has a known reopen path: the operator said it may change.
- Line 2's reasoning distinguishes a website from a resume. Princeton's
  career service prints word-level proficiency on resumes, and research 0003
  explains why that does not transfer here.
- This record is what `CLAUDE.md`'s scope floor section cites. Until this
  record existed, that section was marked "Not yet decided".
- Revisit a line only by a record that removes it.

## Changes
