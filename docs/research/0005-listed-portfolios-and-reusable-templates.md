---
type: research
description: "A seeded survey of 200 developer portfolios from emmabostian/developer-portfolios, one load each, on four questions: what most do; which of this site's practices are rare, measured; ideas within the scope floor; and what already does what portfolio-gallery would. Evidence for decisions, never a decision."
status: current
---

# Research 0005: Listed portfolios, and what reusable templates offer

Gathered 2026-10-12 UTC (the same date locally) by the Brief 7
implementing session, at the operator's request, carried from Brief 6's
Addenda 2 and 4. The sites were loaded from 15:45Z to 16:09Z; GitHub's
figures were read the same afternoon and will drift.

**This is evidence, not a decision.** It ranks below every accepted
record. Anything it suggests reaches the site only through a decision
with the operator and a record. The answers to question 4 are for
`portfolio-gallery`'s own architecture chat; they decide nothing here.

## The answers in short

1. **What most do:** a projects section (70%), links to LinkedIn (81%)
   and GitHub (85%), an email link (61%), about and skills sections (55%,
   57%), something animated, and dark and light themes in CSS (64%).
   About half link a CV or resume (47%). Most are built with React or
   Next.js and hosted on Vercel.
2. **Which of this site's practices are rare:**
   - being complete without scripts is common (63%);
   - making no request to another site is uncommon (24%);
   - passing axe-core's default rules with no violation is rare (9%);
   - all three together, rarer still: 2 of 197 (1%).

   Claims traced to a source document, and public decision records,
   cannot be seen on any page, so no page can be measured for them.
3. **Ideas within the scope floor:** the site already has every common
   feature the floor allows. Two patterns are worth a decision, and both
   touch scope floor line 1: saying on the page how it is built and where
   its evidence is, and an accessibility statement.
4. **What does what the gallery would:**
   - templates are plentiful (1,817 repositories carry the topic) and
     mostly MIT;
   - two gallery precedents exist: Hugo's theme gallery, which takes
     submissions by pull request against written criteria, and CSS Zen
     Garden, contributed CSS on one fixed HTML page;
   - none of the nine profiled checks accessibility or performance, or
     records its decisions;
   - in the sample, no page credits a public template by link.

## How it was gathered

**The list.** emmabostian/developer-portfolios at commit be7238e
(2026-10-12T15:28:31Z), `README.md`, SHA-256 67a6ecdc...0769. Its header
says 2,034 portfolios. 2,037 lines have the form "- [name](link)", and
2,035 of those carry a well-formed http or https link. Two malformed
lines were left out.

**The draw.** 200 of the 2,035, without replacement, in file order:

```
import random, re
text = open("README.md", encoding="utf-8").read()
links = re.findall(r"^- \[[^\]]*\]\((https?://[^)\s]+)\)", text, re.M)
picks = sorted(random.Random(20261012).sample(range(len(links)), 200))
```

Anyone with the list at that commit draws the same 200 (sample SHA-256
00c3e19e...c030). They are 200 distinct hosts. At this size, a 95%
interval on a proportion is at most about plus or minus 7 points; each
figure below carries its Wilson interval.

**The load.** Each listed address was loaded once, as listed, in headless
Chrome 154 at 1366 by 900 px:

- sequentially, with no link followed and no second page;
- with a 30-second limit on loading.

Every measure comes from that one load:

- the main document's own HTML, as a reader or crawler without scripts
  receives it;
- the page after its scripts ran, read 3 seconds after the load event;
- the requests the page made, and the stylesheets and scripts it loaded;
- axe-core 4.14.0's default rules, run in this browser against the loaded
  page, sending nothing anywhere.

No name from the list was kept: the sample records an index and an
address. No code or design was copied: the measures are counts and flags.

**What the measures are.** Each is a pattern in the page, not a judgement
of quality:

- **A section exists** when a heading (h1 to h3) or a navigation link
  names it. A section under an unusual name is missed.
- **One page** means at most two links to other pages of the same site.
- **Complete without scripts** means the HTML as served holds at least
  90% as many words as the page shows after its scripts ran; under 10% is
  "near empty". This is measured only on pages showing 20 words or more.
- **A request to another site** is any request to a host outside the
  page's own registrable domain. On a shared host such as `vercel.app`,
  each subdomain counts as its own site.
- **Analytics or tracking** is a request to a host on a named list of
  analytics, tag, monitoring and session-recording services.
- **Motion** is a CSS keyframe defined, or an animation library loaded.
  A defined animation may never run, so this overcounts motion.
- **Reduced-motion handling** is the string `prefers-reduced-motion` in
  the site's own CSS. Animation libraries carry the string in their code
  whether or not the site uses it, so a count over CSS and scripts
  together is only an upper bound.

**The control.** The same harness, one load of this site, live, on the
same day:

- complete without scripts: 3,457 words in the HTML against 821 shown,
  the rest inside collapsed panels;
- no request to another site;
- 0 axe violations;
- a skip link, CV links, a theme control and reduced-motion CSS.

It also flagged the words "decision records", found in the job
aggregator's bullet: the text search finds words, not practices.

**What was not measured, and why.**

- **Cookies.** The harness read every cookie in the browser, and all 200
  visits shared one browser. The count accumulated across sites and is
  not per site, so it is reported nowhere. A fix would need a second load
  of each site, which the survey's rule forbids.
- **Claims traced to a source, and decision records.** No page shows
  either practice. The only measure is a text search for the words.
- **Late-revealed text.** Pages that reveal text on scroll may show fewer
  words at 3 seconds than a reader would see.

**Reach.** 197 of 200 answered with a page. The other three: a timeout, an
expired certificate, and a 403. 15 of the 197 showed under 20 words, being
3D intros, "enter" screens or an interactive shell. They count for every
measure except the word ratio.

## 1. What most of them do

Of 197 reachable pages; 95% intervals in brackets.

| Feature | Pages |
|---|---|
| A projects section | 137 (70%) [63 to 76] |
| About | 109 (55%) [48 to 62] |
| Skills | 112 (57%) [50 to 64] |
| Contact | 100 (51%) [44 to 58] |
| Experience | 79 (40%) [34 to 47] |
| Blog or writing | 53 (27%) [21 to 33] |
| Education | 37 (19%) [14 to 25] |
| Certifications or awards | 26 (13%) [9 to 19] |
| Services | 18 (9%) [6 to 14] |
| Testimonials | 12 (6%) [4 to 10] |
| One page | 117 (59%) [52 to 66] |
| Motion, as defined | 179 (91%) [86 to 94] |
| A canvas, WebGL, three.js or Spline | 113 (57%) [50 to 64] |
| Of those with motion: reduced motion handled in their own CSS | 97 of 179 (54%) [47 to 61]; 132 (74%) at most, counting scripts |
| Dark and light themes in CSS or scripts, or a theme control | 126 (64%) [57 to 70] |
| A visible theme control | 50 (25%) [20 to 32] |
| Links to at least one GitHub repository | 83 (42%) [35 to 49] |
| The words "case study" | 15 (8%) [5 to 12] |
| A CV or resume link | 92 (47%) [40 to 54]; a PDF link, 55 (28%) |
| An email link | 121 (61%) [54 to 68] |
| A contact form | 62 (31%) [25 to 38] |
| A LinkedIn link | 159 (81%) [75 to 86] |
| A GitHub link | 167 (85%) [79 to 89] |

**How they are built.** By the page's own fingerprints:

- Next.js, 73 (37%);
- a client-side React app with an empty root, 52 (26%);
- no framework detected, 41 (21%);
- Astro, 18 (9%);
- the others, one to three pages each: Svelte 3; Jekyll, WordPress and
  Vue 2 each; Angular, Webflow, Gatsby and Nuxt 1 each.

**Where they are hosted:**

- Vercel, on its own subdomain or under a custom domain, 94 (48%);
- Cloudflare, under a custom domain, 37 (19%);
- GitHub Pages, 33 (17%);
- Netlify, 17 (9%).

## 2. Which of this site's practices are rare, measured

| Practice | Sampled pages | This site |
|---|---|---|
| Complete without scripts, of the 182 pages showing 20 words or more | 115 (63%) [56 to 70]; near empty, 55 (30%) | Yes |
| No request to another site | 47 (24%) [18 to 30] | Yes |
| No analytics or tracking request | 91 (46%) | Yes |
| No font from another site | 118 (60%) | Yes |
| axe-core default rules: no violation | 18 of 196 (9%) [6 to 14] | Yes, in 12 cells (Brief 6) |
| No serious or critical violation | 40 of 196 (20%) [15 to 27] | Yes |
| Complete without scripts and no request to another site | 26 (13%) [9 to 19] | Yes |
| Both, and no serious or critical axe violation | 2 (1%) [0 to 4] | Yes |
| A skip link among the first five links | 28 (14%) [10 to 20] | Yes |
| The word "accessibility" on the page | 11 (6%) [3 to 10] | No |
| The words "decision record" or "ADR" | 1 (1%) | Yes, in CV text, not as a practice |
| A statement that its claims are traced or verified | 2 (1%) | No |

**What the numbers say:**

- **Complete without scripts does not set this site apart on its own.**
  Most server-rendered sites manage it: 55 of 66 Next.js pages showing 20
  words or more did. Client-side React apps mostly do not: 46 of 49 were
  near empty without scripts.
- **No requests to other sites is uncommon.** Three in four pages make
  one, for a median of 3 other hosts. The most common are Google Fonts
  (77 pages), Google Tag Manager (52), Google Analytics (41), Cloudflare's
  analytics beacon (34) and public script CDNs (jsDelivr 27, cdnjs 17,
  unpkg 16).
- **Automated accessibility is where pages fail most.** 156 of 196 pages
  had at least one serious or critical violation. The most common rules
  failed:
  - content outside a landmark region, on 104 pages;
  - colour contrast, 87;
  - a link with no name, 55;
  - no main landmark, 48;
  - heading order, 39.

  The median page failed 3 rules. axe finds a subset of failures and
  never proves their absence, so the 9% with none are not shown to be
  accessible.
- **This site's distinctive combination is rare:** 2 of 197 sampled pages
  share it.
- **Its two other practices are invisible.** A visitor sees neither
  claims traced to a source nor public decision records, so they set the
  site apart only for a reader who opens the repository.

## 3. Ideas within the scope floor

The site already has every common feature the floor allows: a projects
section, an about Intro, skills, work and education, email, LinkedIn and
GitHub links, a CV download, a theme control, reduced motion respected,
and self-hosted fonts. The common features it lacks are the floor's own
exclusions:

- a contact form (31%): lines 6 and 11, and 9 or 13 if a service handles
  it;
- a blog (27%): line 4;
- analytics (54%): line 10;
- testimonials (6%): line 3;
- services (9%): line 1, as nothing of the kind is in the master CV.

Two patterns would show what the survey finds rare, at the level of a
pattern, with what each touches:

1. **Say on the page how it is built, and where the evidence is.** 38
   pages (19%) say "built with" in their text, usually naming a stack. 7
   (4%) link their own source repository. This site's rarest practices
   are visible only in its repository. Touches:
   - scope floor line 1: a sentence about the site is a claim, and
     research 0004's decision 1, whether the site lists itself, waits on
     the master CV;
   - ADR-0008, for where it would sit;
   - ADR-0012, since the link would point to a repository readers may
     read but not reuse.
2. **An accessibility statement** that names the checks run and their
   dates, such as the standing checks and the NVDA test. 11 pages (6%)
   mention accessibility at all. Touches:
   - scope floor line 1, for the same reason;
   - line 5, so each figure in it must be reproducible on demand;
   - ADR-0008 and ADR-0010, for placement and depth.

## 4. What already does what the gallery would do

Read 2026-10-12 from GitHub's REST API, unauthenticated, and from each
repository's own files:

- stars and forks drift; these are that day's figures;
- contributors are GitHub's count, anonymous contributors included;
- "checks" are the workflow files' names in `.github/workflows/`, read,
  not run. A check whose name does not say what it does may do more.

GitHub's topic "portfolio-template" holds 1,817 repositories (search,
2026-10-12). A search of names and descriptions for "portfolio template"
returns 29,843. Nine are profiled: the most-starred templates of three
kinds, and the three collections closest to the gallery's model.

| Repository | What it offers | Licence | How contributions arrive, and what they pass | Stars, forks, contributors, last push |
|---|---|---|---|---|
| academicpages/academicpages.github.io | A Jekyll template for academic portfolios on GitHub Pages; marked a template repository | MIT | Pull requests against a CONTRIBUTING file and a pull request template. Workflows: Jekyll builds, a talks scraper, and one on `pull_request_target` that labels, closes and locks any pull request whose body is empty or still holds the template's comment block, telling the author to ask in Discussions instead | 17,712; 9,588; 85; 2026-10-12 |
| cobiwave/simplefolio | A one-page developer template | MIT | No CONTRIBUTING file, no pull request template. One workflow, a GitHub Pages deploy | 14,222; 6,087; 20; 2026-01-21 |
| saadpasta/developerFolio | A React developer template, described as "not being actively maintained" | GPL-3.0 | A pull request template; workflows for deploy and Prettier formatting | 6,638; 3,883; 84; 2024-12-16 |
| RyanFitzgerald/devportfolio | An Astro and Tailwind template; marked a template repository | MIT | No CONTRIBUTING file, no workflows | 4,983; 4,162; 11; 2026-05-14 |
| HugoBlox/hugo-theme-academic-cv | A Hugo academic template; marked a template repository | MIT | Workflows for build, deploy, publication import and upgrades | 5,075; 6,433; 10; 2026-10-11 |
| arifszn/gitprofile | A portfolio generated from a GitHub username | MIT | CONTRIBUTING: an issue first, then a fork, a branch and a pull request; workflows for deploy and a test deploy | 2,321; 2,158; 30; 2026-09-01 |
| gohugoio/hugoThemesSiteBuilder | The source of themes.gohugo.io, a gallery of community Hugo themes | Apache-2.0 | A theme is added by a pull request of one line to `themes.txt`. It must carry `theme.toml` metadata, a README, a screenshot of at least 1500 by 1000 px and a thumbnail, both at 3:2, and an open-source licence. A fork of another theme must be "notably different", and a derivative's licence must allow it. The pull request must pass a Netlify deploy preview. Themes not updated for 18 months are removed | 287; 345; 297; 2026-10-12 |
| emmabostian/developer-portfolios | The list this survey drew from | None detected | A pull request adding one line in alphabetical order, with a three-item checklist: the link loads and is not parked, the order is kept, `feed.json` is untouched. A weekly link checker and a parked-domain checker flag dead entries for removal | 27,100; 5,298; 2,663; 2026-10-12 |
| mezzoblue/csszengarden.com | The source of CSS Zen Garden: "The HTML remains the same, the only thing that has changed is the external CSS file" (csszengarden.com); each design is a numbered folder | GitHub detects none ("NOASSERTION"); the site asks designers to release their CSS under its Creative Commons Attribution-NonCommercial-ShareAlike 3.0 licence | Through the site, not the repository: a designer hosts the CSS on their own server and submits it. "You may modify the style sheet in any way you wish, but not the HTML"; original artwork, copyright respected. No CONTRIBUTING file, pull request template or workflows in the repository | 1,950; 577; 33; 2024-07-14 |

**What none of the nine offers,** by its files as read:

- an accessibility check;
- a performance check;
- recorded decisions;
- contributions reviewed against written criteria beyond format.

The Hugo gallery comes closest to written criteria (metadata, images,
licence, "notably different") and runs a build check. None has a
CODEOWNERS file.

**Among the sampled portfolios,** a public template can be told from the
page in none:

- No page linked a known template source. The seven pages that linked a
  repository named like a portfolio linked their owners' own repositories.
- 38 say "built with", 13 "powered by", and 4 "inspired by"; none of
  these was checked to name a template.
- One carries the generator tag of an AI site generator (v0.dev).
- One is on Webflow, a site builder with templates.

Forking leaves no trace on a page, so template use is likely
undercounted; how much is not known.

**Two precedents the gallery's brief can use directly.**

- **CSS Zen Garden** is the CSS-only model the gallery brief recommends:
  one page, many contributed stylesheets, the HTML closed to
  contributors. It shows the model works for designs. Its licence is
  noncommercial and stated on the site rather than in a file GitHub can
  read, and its submissions arrive outside GitHub with no automated
  check.
- **academicpages** shows a template's recurring problem: users of a
  template open pull requests meant for their own copy. It closes them
  with a `pull_request_target` workflow. The gallery's planned scope
  check meets the same problem: it fails any pull request touching
  anything outside one design folder, and gives the author a readable
  reason.

## Decisions this informs

None is taken here.

- **For the operator and the chat:** whether to state on the page how
  the site is built and where its evidence is, or to add an accessibility
  statement (section 3). Both first need the master CV, under scope floor
  line 1.
- **For portfolio-gallery's chat:** whether to adopt Hugo's written
  criteria (metadata, images, licence, "notably different", removal when
  stale) and academicpages' handling of misdirected pull requests. Also
  whether checked accessibility and performance, the gap all nine leave,
  is what the gallery leads with.

## Not verified

- Whether the sampled sites look the same on a phone; every load was at
  1366 px.
- Whether "complete without scripts" holds below the first screen on
  pages that reveal text on scroll.
- Which of the 9% with no axe violation are accessible in use.
- Whether any sampled site keeps decision records or traces its claims
  in a repository it does not link.
- Cookies, per site (the harness defect above).
- The nine repositories' workflows beyond their file names.

## Sources, with ratings

| Source | Rating | Date read |
|---|---|---|
| emmabostian/developer-portfolios, `README.md` and `CONTRIBUTING.md` at be7238e | Primary; the population sampled | 2026-10-12 |
| The 200 sampled portfolios' home pages, one load each | Primary observation, by the measures defined above | 2026-10-12, 15:45Z to 16:09Z |
| axe-core 4.14.0, its default rules | Established tool; finds a subset of accessibility failures and never proves their absence | 2026-10-12 |
| GitHub REST API: repository metadata, contributor counts, directory listings; repository search | First-party data | 2026-10-12 |
| The nine repositories' own `README.md`, `CONTRIBUTING.md` and workflow files | Primary | 2026-10-12 |
| csszengarden.com, its home page and Participation text | Primary, a precedent | 2026-10-12 |
| Research 0004 of this repository: precedents, licences, fake stars | As rated there | |
