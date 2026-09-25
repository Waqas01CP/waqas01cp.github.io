---
type: research
description: Evidence on whether to show skill levels and in what form, and on whether writing belongs on the site. Two floor lines were waiting on this. Evidence for decisions, never a decision.
status: current
---

# Research 0003: Skill display, and writing on the site

Gathered 2026-09-25 in the portfolio architecture chat, to settle two scope
floor lines that were left open on 2026-09-23.

**This is evidence, not a decision.** It ranks below every accepted record.

## What I said in advance, and what happened

Before searching I predicted no peer-reviewed evidence on skill bars exists,
and said that if so I would say it rather than dress practitioner opinion up
as a finding.

**That prediction held.** Nothing peer-reviewed on skill bars, stars or
percentage ratings was located. What exists is a very large volume of
commercial career-advice content, all of which fails the source standard.
One such page cited a "2023 Jobvista study" reporting 23% more parsing
errors for graphical skill indicators; **that study could not be traced to
any publisher and is rejected**, not used.

What is usable is one university career service guide, one peer-reviewed
paper already held, and the findings in research 0001.

## 1. Skill display

### What a legitimate source actually says

Princeton University Center for Career Development, Resume Guide, read
2026-09-25.

- On formatting: avoid using headers, footers, tables and columns, because
  applicant tracking systems cannot accurately read or parse information in
  those sections.
- On proof: demonstrate skills through bullet points in addition to listing
  them in a Skills section.
- On scanning: a resume should be easy to scan and digest in 15 to 30
  seconds.
- Its Skills section is organised by category, not rated: Languages,
  Certifications, Technology, and further subcategories.

**Its own sample resumes do use word-level proficiency.** Examples printed
in the guide: "Word (Advanced), Excel (Proficient), PowerPoint
(Intermediate)", "Dreamweaver (Advanced), Photoshop (Novice)", "Proficient
in Java, Python, MATLAB, Mathematica, SolidWorks, and AutoCAD", "Swedish
(Native); German (Fluent); Hebrew (Conversational)", and "French (4 years)
and Spanish (6 years)".

So a blanket "never show a level anywhere" is **not** what a legitimate
career service practises. A word-level label beside a tool is normal on a
resume. What appears nowhere in the guide is a bar, a percentage, a star
rating or a numeric scale.

### What does not transfer to a website

The ATS argument is the strongest argument against graphical skill displays,
and **it does not apply to this site at all.** No applicant tracking system
reads a personal website. Using it here would be borrowing authority from a
source that was answering a different question.

Three things do transfer.

1. **A percentage or a star has no measurement behind it.** "Python 90%" is
   90% of what, against whom. The operator's own standing rule is that a
   number carries its measurement or it does not appear. A self-rating
   cannot satisfy that rule, so it fails on the project's own terms before
   any external evidence is considered.
2. **Research 0001: polish without proof now reads as a warning sign.**
   Recruiters interviewed in Sep to Dec 2025 reported treating material that
   looks too polished or too perfectly matched as a reason for suspicion.
   A wall of confident self-ratings is exactly that shape.
3. **A bar is a graphic, and a graphic needs a text equivalent.** W3C WAI's
   Complex Images tutorial requires one for anything carrying substantial
   information. A bar at 90 percent with no text conveys nothing to a
   screen reader and nothing to an AI summariser, which per research 0001
   reads only the initial HTML.

### Where the strongest evidence points

Marlow and Dabbish, CSCW 2013, as summarised in its abstract and in
`arXiv:2303.14702`: hiring readers found profile activity more reliable than
resume claims, and used the signals that were cheap to verify.

A self-rating is the least verifiable thing on a page. A repository, a live
application or a named result is the most verifiable. The two sit at
opposite ends of the same axis, and the evidence favours one end.

### The operator's existing position, tested

His rule is that levels are internal only and never printed on a CV or
public profile. **Against a resume, that rule is stricter than Princeton
practises.** Against this site, nothing found contradicts it, and three
independent lines support it.

## 2. Writing on the site

### Direct evidence is thin, and that is the finding

No study was located that measures whether a blog or articles section on a
personal site changes hiring outcomes. Anyone claiming otherwise is
generalising.

### What the adjacent evidence says

**Writing as a signal has been measured, and it collapsed.** Galdin and
Silbert, `arXiv:2511.08785`, Nov 2025, found employers paid a premium for
tailored written applications before LLMs and did not after. A second,
independent Yale team, `arXiv:2509.25054`, Sep 2025, studied the same
question on the same platform and describes its evidence as complementary.
Two independent teams reaching compatible conclusions is the strongest
signalling evidence available here, and it points the same way: **text alone
no longer separates candidates, because anyone can produce it.**

Neither paper is peer-reviewed, and both study freelance cover letters
rather than blogs. The mechanism, though, is about the cost of producing
text, and that cost fell for all text at once.

**Recruiters are actively suspicious of generated prose.** Research 0001's
recruiter study found practitioners hunting for signs of AI authorship and
retreating to gut judgement when they find them. In 2026 an unremarkable
blog post is the artefact most likely to be read as machine-written.

**Open-source contribution is measurably different.** A 2025 economics paper
in a peer-reviewed journal, on career concerns and signalling in open source,
frames publicly visible contributions as a valuable signal precisely because
individual contributions are directly and transparently observable. I read
its abstract, not the full paper. The distinguishing property is
observability by a third party, which a self-published blog post does not
have and a merged pull request does.

### What that adds up to

The asymmetry is what matters. **A maintained, substantive piece of writing
can help. An unmaintained one is a dated artefact sitting on a page whose
whole argument is currency and verifiability**, and it costs something every
day it sits there. Against that, the same effort spent on a merged pull
request produces a signal a third party can verify.

This is reasoning from adjacent evidence, not a measured result, and it is
recorded as such.

## 3. Years of experience per skill

Asked separately by the operator on 2026-09-25, after the recommendation
above was approved. This is the one part of the question with strong
peer-reviewed evidence behind it.

### The source

Schmidt, Oh and Shaffer, "The Validity and Utility of Selection Methods in
Personnel Psychology: Practical and Theoretical Implications of 100 Years of
Research Findings", working paper 2016, read 2026-09-25. It updates Schmidt
and Hunter (1998) in Psychological Bulletin, which the authors note has been
cited over 3,400 times. It reports meta-analytic operational validity for 31
selection methods against job performance.

### The numbers that matter here

| Method | Operational validity |
|---|---|
| Job knowledge tests | .48 |
| Behavioral Consistency Method, describing past achievements | .45 |
| Work sample tests | .33 |
| **Job experience, years** | **.16** |
| **Training and Experience point method, counting years** | **.11** |
| Years of education | .10 |
| Age | about zero |

**The comparison that answers the question is the last two rows against the
second.** The paper describes the Training and Experience point method as
credentialistic: an applicant receives a fixed number of points for each
year or month of experience and each year of schooling, with no attempt to
evaluate past achievements, accomplishments or job performance. It assumes
achievement is determined solely by exposure. Its validity is .11.

The Behavioral Consistency Method asks applicants to describe past
achievements that illustrate their ability, and the paper grounds it in the
principle that the best predictor of future performance is past performance.
Its validity is .45.

**Same underlying information, the candidate's own past, and roughly four
times the validity.** The difference is counting exposure versus describing
what was accomplished.

### The finding that cuts the other way, and must be stated

Job experience overall scores .16, but that figure spans people with under
six months to over thirty years. The paper reports that Schmidt, Hunter and
Outerbridge (1986) found that in groups where job experience does not exceed
five years, the correlation with job performance is considerably larger: .33
against supervisory ratings and .47 against a work sample test. The relation
is non-linear, rising roughly linearly to about five years and flattening
after that.

**Every one of this operator's spans is under five years**, so his years sit
in the steep part of that curve rather than the flat part. Years are not
meaningless for him. That is the honest counter-argument and it is why the
recommendation below rests on a different point rather than on "years do not
matter".

### Caveat on the absolute numbers

Sackett, Zhang, Berry and Lievens (2022) revised the criterion-reliability
correction used in this literature, producing more conservative estimates
across the board, with GMA falling from .51 to .31 in one commonly cited
restatement. Reports of that revision state the relative ranking of methods
stayed broadly the same. **The ranking is what this section relies on, not
the absolute values.** The Sackett paper itself was not read.

### Why a years number still does not belong on this site

Three reasons, in order of strength.

1. **The site already carries the better version of the same fact.**
   ADR-0003 puts every project, role and certificate on a dated timeline.
   A reader who wants to know how long something ran can see it and check
   it against a linked repository. A printed "3 years" is the same claim
   asserted instead of shown, and it can drift out of sync with the
   timeline it duplicates.
2. **Counting is the low-validity form of the evidence.** .11 against .45.
   The same line of the page spent naming what was built with the tool is
   the higher-validity form.
3. **"Years" has no agreed unit.** A language used in one course in 2023
   and in projects from 2025: is that three years or one. The ambiguity is
   in the counting rule, not the arithmetic, and no rule exists that a
   reader could apply to check the number. That fails the operator's own
   standing rule that a number carries its measurement or it does not
   appear.

Note that reason 3 does **not** apply to a language on a resume, where
Princeton's guide prints "French (4 years)". A spoken language studied for
four continuous school years has an unambiguous unit. A programming language
used intermittently across coursework and projects does not.

## Not verified

- No peer-reviewed or career-service source was found addressing skill bars,
  stars or percentages on a personal website rather than a resume.
- The "2023 Jobvista study" on parsing errors is untraceable and rejected.
- Neither signalling paper is peer-reviewed, and both study freelance cover
  letters, not portfolio writing.
- The open-source signalling paper was read at abstract level only.
- Princeton's guide is one institution. Its sample resumes were read, its
  underlying research was not.
- Nothing here measures the effect of any of this on an engineering
  portfolio website, because no such study was located in research 0001
  either.

## Sources, with ratings

| Source | Rating | Read |
|---|---|---|
| Princeton University Center for Career Development, Resume Guide | University career service, first-party | 2026-09-25 |
| Marlow and Dabbish, CSCW 2013 | Empirical, peer-reviewed. Abstract and a summary only | 2026-09-22 |
| Galdin and Silbert, arXiv:2511.08785 | Empirical, not peer-reviewed | 2026-09-22 |
| Cui, Santamarina and Ye, arXiv:2509.25054 | Empirical, not peer-reviewed. Abstract only | 2026-09-25 |
| Career concerns and signalling in open source, ScienceDirect, 2025 | Peer-reviewed journal. Abstract only | 2026-09-25 |
| Surati, Bellini and Black, FAccT 2026 | Empirical, peer-reviewed. Via research 0001 | 2026-09-22 |
| W3C WAI, Complex Images | Standards body. Via research 0001 | 2026-09-22 |
| Schmidt, Oh and Shaffer, 100 Years of Research Findings, 2016 working paper | Update by the original authors to a Psychological Bulletin paper cited 3,400+ times | 2026-09-25 |
| Sackett, Zhang, Berry and Lievens, 2022 revision | Peer-reviewed. **Not read**, known only through restatements | 2026-09-25 |
| Commercial career-advice sites | **Rejected**, fail the source standard | 2026-09-25 |
