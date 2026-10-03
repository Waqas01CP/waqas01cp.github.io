# DESIGN.md: Waqas Sharif portfolio

## What this is
The design brief for a personal engineering portfolio website. It sets
goals and a short list of hard limits. Everything else is yours to decide:
type, colour, layout, depth, gradients, motion and 3D are all open. Choose
deliberately, and state your reasoning for the typeface, the colour and any
3D or motion before I give feedback.

## Audience
Hiring engineers and engineering managers assessing a candidate for agentic
AI and LLM reliability work. Masters admissions readers second. Technical,
skimming first and reading deeply second, and distrustful of anything that
looks marketed at them.

## Goal
A polished, current site that makes dense, evidence-heavy content a
pleasure to read: long prose, dated entries, numbers with sources,
collapsible detail, a vertical timeline with items on both sides of a
centre spine, and three contact routes (email, LinkedIn, GitHub).

## How to work
Explore. Try ideas, including 3D, and keep what earns its place. Here 3D
means depth in the interface itself: elements that respond in three
dimensions when hovered or touched, sections and a timeline that a reader
can interact with. It does not mean illustrations of a project's internals,
which belong in that project's case study. Anything that responds to hover
must also work by touch, because phones have no hover. Add any
heavy element one at a time, so the cost of each one is visible on its own
and it can be kept or cut on that basis.

## Measured goals
- **Speed on an ordinary phone.** The page meets Google's "good" Core Web
  Vitals thresholds: largest content visible within 2.5 seconds, layout
  shift of 0.1 or less, response to input within 200 milliseconds. Checked
  with Lighthouse's default mobile run, which emulates a slow 4G connection
  (150 ms latency, 1.6 Mbps down) and a CPU four times slower than the test
  machine. Input response needs real visitors to measure, so the lab run
  uses Total Blocking Time under 200 milliseconds as its stand-in.
  Anything, 3D included, stays only if the page still meets this with it.
- **Every width.** Works at 360 px wide and on a desktop. On a wide screen,
  use the width with layout rather than leaving it empty, while keeping
  running text to readable lines: WCAG 1.4.8 sets no more than 80
  characters.
- **Both themes.** Light and dark both hold.

## Hard limits
1. Every word a reader needs is real text in the page. Nothing lives only
   inside a 3D scene, an animation, a canvas or an image.
2. All motion respects reduced-motion settings. Nothing autoplays sound or
   video.
3. No distinction relies on colour alone, and text contrast meets WCAG AA.
4. Collapsed and expanded detail are both legible.
5. LinkedIn and GitHub appear only as their official marks, unmodified;
   LinkedIn's in blue, black or white only.
6. Everything is served from the site itself. No fonts, scripts or embeds
   loaded from other sites. A 3D or animation library would be a new
   dependency, which needs its own decision first; the browser's own CSS,
   SVG and WebGL need none.

## Context, not rules
- First impressions of a website's look form within 50 milliseconds, and
  in a peer-reviewed study with human participants, sites with low visual
  complexity and a familiar layout were rated the most appealing (Tuch et
  al., International Journal of Human-Computer Studies, 2012). Polish and
  complexity are different things; a 3D element has to add the first
  without costing too much of the second.
- Inter and Roboto are what most sites already use.
