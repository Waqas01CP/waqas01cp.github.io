---
type: research
description: Evidence on how hiring readers and their AI tools read candidate material, 2013 to 2026, with source ratings. Evidence for decisions, never a decision.
status: current
---

# Research 0001: How hiring readers read candidate material

Gathered 2026-09-22 and 2026-09-23 in the portfolio architecture chat.

**This is evidence, not a decision.** It ranks below every accepted record.
Where a record disagrees with it, the record governs and this file is the
input that should be re-examined.

## Why this was gathered

The site is meant to carry extreme detail while answering in the manner a
hiring reader wants. Those two goals conflict unless the depth is layered.
This file is the evidence used to settle how.

## What was found

### 1. An AI summary is increasingly the first reader

Surati, Bellini and Black, FAccT 2026, `arXiv:2604.26851`. Peer-reviewed
conference paper. Semi-structured interviews with 22 US recruiters across
eight sectors, Sep to Dec 2025, with inter-rater agreement at Krippendorff's
alpha 0.80.

- Generative AI summarises resumes and interviews, and those summaries are
  passed to hiring managers with little review. One participant reports that
  the underlying transcripts exist but are rarely opened.
- Some recruiters accept an AI filter's output without double-checking it.
- Material that reads as too polished, or as a precise match to the job
  description, triggers suspicion rather than interest. One participant
  treats bolded keywords as a warning sign. That is a single report, not a
  measured rule.
- Recruiters retreat to gut instinct and culture-fit judgements when they
  distrust written artefacts.

**Limits:** 22 participants, US only, retrospective self-report, and three
participants withheld detail citing company policy.

### 2. Written polish signals less than it did

Galdin and Silbert, "Making Talk Cheap: Generative AI and Labor Market
Signaling", `arXiv:2511.08785`, submitted 11 Nov 2025. Economics working
paper, **not peer-reviewed**. Freelancer.com data plus a structural model.

- Employers paid a premium for tailored applications before LLMs were
  introduced, and did not after.
- The counterfactual simulation, not an observation: with written
  applications useless as a signal, top-quintile workers are hired 19% less
  often and bottom-quintile workers 14% more often.

**Limits:** one platform, freelance work, and the headline numbers come from
a simulated equilibrium rather than from measurement.

### 3. The major AI crawlers do not run JavaScript

Vercel and MERJ, "The rise of the AI crawler", 17 Dec 2024. Vendor
research, admitted under the tier-1 test: the publisher's own network, a
stated method, and scale reported per crawler.

- Measured over one month: GPTBot 569 million fetches, Claude 370 million,
  AppleBot 314 million, PerplexityBot 24.4 million, Googlebot 4.5 billion.
- Stated conclusion: none of the major AI crawlers currently render
  JavaScript. Named: OAI-SearchBot, ChatGPT-User, GPTBot, ClaudeBot,
  Meta-ExternalAgent, Bytespider, PerplexityBot, and CCBot.
- They do fetch JavaScript files without executing them: ChatGPT 11.50% of
  requests, Claude 23.84%.
- Gemini and AppleBot do render, via browser-based infrastructure.
- Content in the initial HTML response, including JSON, may still be read.
- Their recommendation: render critical content on the server, including
  main content, meta information and navigation. Client-side rendering is
  for non-essential enhancement.
- ChatGPT spent 34.82% of fetches on 404s and Claude 34.16%, against
  Googlebot's 8.22%, so URL stability matters more than usual.

**Limits:** measured Dec 2024 and not re-verified since. Anthropic's
on-request fetcher, as distinct from ClaudeBot, was not separately
identified. Microsoft Copilot was excluded for lacking a unique user agent.

### 4. Interviewers now probe the reasoning behind prior work

University of Miami Toppel Career Center, 14 May 2026. A university career
service summarising reported changes at named employers. Practitioner grade:
corroborating, not establishing.

- Google's 2026 loop is reported to add a code comprehension round and to
  extend its behavioural round into a technical design conversation about
  the candidate's prior engineering work.
- Meta is reported to evaluate problem solving, code quality, verification
  and communication.

**Limits:** second-hand reporting of internal documents. Not verified
against any first-party source.

### 5. Older findings that still hold

- NN/g, 2019: a survey of 204 UX professionals in charge of hiring. They
  rarely read a portfolio word for word; they want the process and the
  reasoning, not only the finished artefact; curation beats volume. Advice
  in the same article against flashy templates is the author's guidance,
  not a survey finding.
- Marlow and Dabbish, CSCW 2013: interviewees found GitHub activity more
  reliable than resume claims, but used only signals that were cheap to
  verify. Read from the abstract and from a summary in `arXiv:2303.14702`,
  not from the full paper.

## What this evidence does not cover

No study located measures engineering portfolio websites specifically.
Every source above is about resumes, GitHub profiles, UX portfolios or
crawler behaviour. Applying any of it to this site is an extension of the
source, and each record that does so says so in its Assumptions.

## Sources, with ratings

| Source | Rating | Date |
|---|---|---|
| Surati, Bellini and Black, FAccT 2026, arXiv:2604.26851 | Empirical, peer-reviewed | 2026 |
| Galdin and Silbert, arXiv:2511.08785 | Empirical, not peer-reviewed | 2025-11-11 |
| Vercel and MERJ, The rise of the AI crawler | Vendor, tier 1 | 2024-12-17 |
| NN/g, 5 Steps to Creating a UX-Design Portfolio | Established research organisation | 2019-08-04 |
| Marlow and Dabbish, CSCW 2013 | Empirical, peer-reviewed | 2013 |
| University of Miami Toppel Career Center | Practitioner, university career service | 2026-05-14 |
