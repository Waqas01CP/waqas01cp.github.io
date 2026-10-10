---
type: research
description: "Evidence on two questions the operator raised on 2026-10-07: whether this site belongs on itself as a project, and whether to open it for others to reuse, for credit. Licences, forks against templates, precedents with their numbers, what stars are worth. Evidence for decisions, never a decision."
status: current
---

# Research 0004: This site as a project, and as a template for others

Gathered 2026-10-07 UTC (2026-10-08 local) by the Brief 5 implementing
session, at the operator's request after Report 5. Figures from GitHub
were read through its public API at 21:33Z on 2026-10-07 and will drift.

**This is evidence, not a decision.** It ranks below every accepted record.
Both questions end in decisions for the operator and the architecture
chat, listed at the end.

## 1. Whether this site belongs on the site as a project

### What the rules already settle

- Scope floor line 1 (ADR-0004): no claim that is not in the master CV.
  The site cannot list itself, or any skill learned building it, until
  the operator adds it to the master CV. Content reaches this repository
  through the operator or a brief, never the other way.
- Scope floor line 2: no skill levels, so "learned" cannot appear as a
  level either.
- Scope floor line 5 and ADR-0010: every item carries a specific,
  checkable fact, and every number must be reproducible on demand.
- ADR-0008: where an item sits, and in which tier, is the chat's
  decision.

### What is checkable, from this public repository alone

Each of these can be verified by anyone who opens the repository, which
is the cheap-to-verify kind of signal research 0001 found hiring readers
trust (Marlow and Dabbish, CSCW 2013, as read there):

- a written decision record for every consequential choice: 11 records,
  10 accepted, one superseded;
- five repository gates on every commit and push (ADR-0007);
- every block of text on the page traced by a tool to the master CV
  (`tools/check_content.py`);
- performance goals from a published standard, measured (ADR-0009);
- accessibility verified three ways: axe, the accessibility tree at load
  compared with the page without layout skipping, and a recorded NVDA
  speech test, passed 2026-10-07;
- the process itself: briefs from an architecture chat, an implementing
  seat, session logs and a state file, 56 commits since 2026-09-26.

NN/g's survey of 204 UX professionals in charge of hiring (2019, in
research 0001) found they want the process and the reasoning, not only
the artefact. That points to
the process as the content of such an item, not the page.

### What the evidence does not support

- **Languages and frameworks as skills.** The code here was written by AI
  seats under the operator's direction, as the master already says of the
  job aggregator. Listing HTML, CSS, JavaScript or Jinja2 as skills is a
  claim an interviewer can test by asking him to write some. The rule
  that governs is the operator's own: a claim he cannot stand behind in
  an interview does not go on the site.
- **Accessibility expertise.** One NVDA speech test, guided step by step,
  supports "verified with a screen reader", not more.
- **The site's own polish as evidence of skill.** No study located
  measures how engineering portfolio sites are read (research 0001, "What
  this evidence does not cover").

### The cost

A project about the portfolio itself can read as filler beside deployed
systems. No source located measures this; it is a judgement, which is why
placement is the chat's under ADR-0008.

## 2. Opening the site for others to reuse

### Where it stands now

The repository is public and carries no licence. GitHub's terms let
others view and fork it on GitHub, but without a licence "nobody else can
copy, distribute, or modify your work without being at risk of
take-downs, shake-downs, or litigation" (choosealicense.com). Today a
copy is unlicensed, and nothing asks the copier to credit anyone.

### Licences

- **MIT.** Its only condition is that the copyright and licence notices
  are preserved in copies (choosealicense.com). It cannot require a
  visible credit on the copier's site, only the notice in the code.
- **CC BY 4.0.** Requires credit, a link to the licence and an indication
  of changes. Creative Commons itself recommends against its licences for
  software and points to software licences instead.
- **Content is separate from code.** The operator's name, CV text, the
  approved Intro paragraph and the contact details are not anyone's to
  reuse under a code licence; a licence for the code can exclude them by
  saying so, which most portfolio templates leave unclear.

The working precedent: Brittany Chiang's portfolio, bchiang7/v4, is MIT
licensed and its README says: "Yes, you can fork this repo. Please give me
proper credit by linking back to brittanychiang.com. Thanks!" The credit
is a request, not a condition.

### Fork, or template

From GitHub's documentation:

- A fork includes the entire commit history. A repository created from a
  template starts with a single commit, and branches from it "have
  unrelated histories".
- Commits to a fork do not appear in its owner's contribution graph;
  commits to a repository created from a template do.
- A fork's page shows "forked from" its parent, checked on a fork of
  bchiang7/v4. Whether a template copy shows anything comparable was not
  confirmed in the documentation.
- Making a repository a template is one setting: Settings, Template
  repository. The repository then shows a "Use this template" button.

So a fork carries visible credit and counts in the original's forks; a
template is easier for the copier and may carry no visible credit at all.

### This repository is not a template as it stands

- The content is the operator's, by design: one content file of his
  items, traced to his private master CV.
- The gates encode his workflow: gate A blocks paths into his private
  material and holds a digest of his vault's root folder name.
- The decision records, logs, briefs folder and state file describe how
  he works, which is part of what a reader of this repository is meant
  to see.

A reusable version would be a separate repository: the generator, the
templates and the stylesheet, with sample content, a setup guide and a
live demo, and without his CV text or his gates. That is real work: the
content model, the build checks that assume his master CV, and the
documentation all need a generic form.

### Precedents, with their numbers

Read from GitHub's API at 21:33Z on 2026-10-07:

| Repository | Stars | Forks | Licence | Created |
|---|---|---|---|---|
| emmabostian/developer-portfolios (a list, not a template) | 26,996 | 5,283 | none | 2019-09-13 |
| bchiang7/v4 | 8,284 | 4,211 | MIT | 2018-08-16 |
| codewithsadee/vcard-personal-portfolio | 8,114 | 4,464 | MIT | 2022-03-19 |
| saadpasta/developerFolio | 6,639 | 3,883 | GPL-3.0 | 2019-10-29 |
| soumyajit4419/Portfolio | 6,490 | 3,447 | none | 2019-05-17 |
| arifszn/gitprofile | 2,317 | 2,159 | MIT | 2021-08-21 |

None of the five templates is marked as a GitHub template repository; all
are reused by forking. Each took years to reach these numbers, and these
are the visible successes, not a sample of what most templates achieve.

### A cheaper route to the same visibility

emmabostian/developer-portfolios lists developers' portfolios and is the
most starred repository above. A portfolio is added by pull request, in
the form "- [Name](link) [Title | Expertise]", in strict alphabetical
order by first name, with a link that loads; broken or parked links are
removed weekly by an automated workflow. That puts this site in front of
the list's readers without building or maintaining a template.

### What stars are worth

- No source located measures whether stars on a portfolio template help a
  candidate get hired. Research 0001 found hiring readers trust signals
  that are cheap to verify; a star count is cheap to see but says nothing
  about who starred or why.
- Stars are gamed. He et al., accepted at ICSE 2026 (arXiv:2412.13459,
  "Six Million (Suspected) Fake Stars in GitHub"), report fake-star
  campaigns surging since 2024 and find that fake stars give "a promotion
  effect in the short term (i.e., less than two months) and become a
  liability in the long term".
- Stars on a portfolio template signal design and convenience. The
  operator's positioning is LLM reliability and agentic systems, which a
  template's stars do not show.

### What would set a reusable version apart

From this repository's own records, not from any source: every claim
traced to a source document by a tool; accessibility verified with a
real screen reader; content readable without scripts and by AI crawlers
(research 0001); no tracking, cookies or third-party requests (ADR-0004);
measured performance goals. Four of the five templates above are mostly
JavaScript or TypeScript by GitHub's language count, and one is plain HTML
and CSS; this one is a small Python build, simpler to read and a barrier
for people without Python.

## Decisions this informs

For the operator:

1. Whether to add this site to the master CV, and with which claims. Only
   then can it appear on the site.

For the architecture chat:

2. If it is added: placement and tier under ADR-0008, and a brief.
3. Whether to license this repository's code, and how to exclude the
   operator's content. A licence is a decision with consequences for
   every later copy, so it takes a record.
4. Whether to build a separate, reusable repository, and when. It is a
   project of its own, with maintenance that does not end.
5. Whether to submit the site to emmabostian/developer-portfolios.

## Addendum, 2026-10-10: the operator's priority, and the licence

The operator set his priority for a template repository on 2026-10-10, in
his words: "what i want now is credibility like if there is a choice
between getting stars, forks and people starting to interact and do PRs and
other practices then i would prefer this over even if later they sell the
repo", and "i do not want a license that scares away people". He also
proposed that someone who changes 30% or more may use it freely.

- **Less restrictive licences draw more interest.** Stewart, Ammeter and
  Maruping, Information Systems Research 17(2), 2006: users are most
  attracted to projects that "employ nonrestrictive licenses" and are
  sponsored by nonmarket organisations. Empirical, peer-reviewed; its
  "restrictive" means copyleft, measured on Freshmeat projects, so applying
  it to a noncommercial licence is an extension, which goes further than
  copyleft in restricting use. Read from its abstract.
- **A noncommercial licence is not open source** (Open Source Definition,
  criterion 6, above), and its line between commercial and not is unclear
  for a job-seeker's portfolio (PolyForm Noncommercial, above).
- **There is no 30% rule.** "No statute or court precedent uses a numerical
  formula" for how much change makes a work one's own (Nelson Mullins; also
  Gerben Law: practitioner, two firms agreeing). A licence built on a
  percentage would be unmeasurable, and a licence nobody can look up is the
  kind that turns people away.
- **Contributions take the repository's licence by default.** GitHub's
  Terms of Service, D.6: "Whenever you add Content to a repository
  containing notice of a license, you license that Content under the same
  terms" ("inbound=outbound"). No contributor agreement is needed.
- **The precedents' licences**, read 2026-10-07: of the five templates
  above, three MIT, one GPL-3.0, one none; none noncommercial.

What it adds up to, as evidence: against his stated priority, MIT fits and
PolyForm Noncommercial does not. MIT lets anyone use, change, share and
sell it, and keeps only his copyright notice in every copy; visible credit
can be asked for, not required.

## Not verified

- Whether a repository created from a template shows any visible link to
  its template on GitHub. GitHub's documentation, as read, does not say.
- Whether stars on a portfolio template, or a listing in a portfolio
  list, affect hiring. No source located.
- Whether the precedents' numbers include fake stars. Not checked.
- Stewart, Ammeter and Maruping (2006) beyond its abstract.
- The full text of Marlow and Dabbish (2013); as in research 0001, read
  through its abstract and a summary only.

## Sources, with ratings

| Source | Rating | Date read |
|---|---|---|
| GitHub Docs, Creating a template repository; Creating a repository from a template | First-party documentation | 2026-10-07 |
| choosealicense.com, No license; MIT License | Established reference | 2026-10-07 |
| Creative Commons, CC BY 4.0 deed; FAQ on software | First-party | 2026-10-07 |
| He et al., Six Million (Suspected) Fake Stars in GitHub, ICSE 2026, arXiv:2412.13459 v2 | Empirical, peer-reviewed | 2026-10-07 |
| bchiang7/v4 README | Primary, a precedent | 2026-10-07 |
| emmabostian/developer-portfolios README and CONTRIBUTING.md | Primary | 2026-10-07 |
| GitHub REST API, repository metadata and language counts for the six repositories above | First-party data | 2026-10-07, from 21:33Z |
| Research 0001 of this repository (NN/g 2019; Marlow and Dabbish 2013) | As rated there | |
| GitHub Terms of Service, sections D.5 and D.6 | First-party | 2026-10-10 |
| Open Source Initiative, The Open Source Definition, criterion 6 | Primary | 2026-10-10 |
| PolyForm Noncommercial License 1.0.0, from the PolyForm project's repository | Primary | 2026-10-10 |
| Stewart, Ammeter and Maruping, Information Systems Research 17(2), 2006, abstract | Empirical, peer-reviewed | 2026-10-10 |
| Nelson Mullins and Gerben Law, on the "30 percent rule" | Practitioner, two firms agreeing | 2026-10-10 |
