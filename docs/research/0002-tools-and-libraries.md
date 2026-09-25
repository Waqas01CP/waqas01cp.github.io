---
type: research
description: Tools and libraries considered for building the site. Frameworks, motion, 3D, timeline rendering, compute for an assistant, and the Claude Design surface. Evidence for decisions, never a decision.
status: current
---

# Research 0002: Tools and libraries

Gathered 2026-09-22 and 2026-09-23 in the portfolio architecture chat, from
each tool's own documentation.

**This is evidence, not a decision.** It ranks below every accepted record.

Every finding below was read from the named source on the named date. Where
something was not checked, it is in the "Not verified" section rather than
being softened into a claim.

## 1. Site framework and rendering

### Astro

Read from `docs.astro.build/en/concepts/islands/`, 2026-09-22.

- Islands architecture: the page renders to static HTML, with JavaScript
  added only for components that need interactivity.
- Stated behaviour: by default Astro renders every UI component to just HTML
  and CSS, stripping out all client-side JavaScript automatically. A
  component becomes interactive only when given a `client:*` directive.
- Loading is controlled per component: `client:load`, `client:idle`, and
  `client:visible`, the last of which loads only when the component enters
  the viewport.
- Supports React, Preact, Svelte, Vue and SolidJS inside islands, and more
  than one framework in the same project.
- The documentation includes a GitHub Pages deployment guide.

**Why this matters here.** Research 0001 found that the major AI crawlers do
not execute JavaScript. A framework whose default output is HTML with no
client-side runtime is aligned with that constraint by default rather than
by discipline.

**Against it.** Astro's performance claims are Astro's own. Nothing here is
measured. A hand-written static site has the same property with no build
step and no dependency at all.

## 2. Motion

### CSS scroll-driven animations

Read from MDN, `animation-timeline`, 2026-09-23. That page was last modified
2026-09-16.

- **`animation-timeline` is marked "Limited availability" and is explicitly
  not Baseline.** MDN's stated reason: the feature does not work in some of
  the most widely-used browsers.
- It animates along a scroll progress timeline or a view progress timeline
  instead of the document's time-based timeline, in CSS alone.

**Consequence.** This cannot carry anything load-bearing. It is usable only
as progressive enhancement behind a feature query, where the page is correct
and complete without it. This finding reverses the tentative read taken on
2026-09-22, when browser support had not been checked.

### GSAP

Read from `gsap.com/pricing`, 2026-09-22.

- Stated on that page: GSAP is now 100% free for all users, thanks to
  Webflow's support. The page lists the plugins as included, among them
  ScrollTrigger, ScrollSmoother, SplitText, MorphSVG, DrawSVG, Flip,
  Draggable and Inertia.
- Maintained by the original GSAP team, working at Webflow. The page footer
  reads "©2026 GSAP - A Webflow Product".

**Not verified.** Only the pricing page was read, not the licence text. The
licence is to be read in full before GSAP is added as a dependency.

## 3. Three-dimensional content

### React Three Fiber

Read from `r3f.docs.pmnd.rs/advanced/scaling-performance`, 2026-09-22. A
React renderer for three.js.

Its own performance guidance, which is effectively a list of the costs:

- Running WebGL is expensive depending on the device, and a constantly
  running game loop is what drains batteries and spins up fans.
- `frameloop="demand"` renders only when something changes.
- Geometries and materials should be reused; each one is GPU overhead.
- Draw calls: no more than 1000 as the very maximum, and optimally a few
  hundred or less. Repeating objects should be instanced.
- Level of detail via the `<Detailed />` component reduces vertex count with
  distance.
- `PerformanceMonitor` measures average frames per second and calls back so
  the application can lower resolution or quality, with hysteresis bounds to
  stop it oscillating.
- Movement regression: quality is reduced while the scene moves and restored
  at rest, the technique used by sites that must stay fluid on any device.

**Reading.** The library is capable, and the documentation is candid that 3D
on the open web is a performance-management problem rather than a feature.
Nothing here says whether 3D fits this site, because no performance budget
exists yet.

## 4. Timeline rendering

### TimelineJS

Read from `timeline.knightlab.com`, 2026-09-22. Knight Lab, Northwestern
University.

- Released under the Mozilla Public License 2.0. Free for commercial use,
  no permission or fee needed beyond the licence.
- Data comes from a published Google Sheet, or from JSON with the timeline
  instantiated directly in JavaScript. The JSON route is the only one that
  avoids depending on a public Google Sheet.
- Its own guidance recommends no more than about 20 slides, and says to pick
  stories that have a strong chronological narrative, adding that it does not
  work well for stories that need to jump around in the timeline.
- A `group` property places events in the same or adjacent rows.
- Presentation is slide-based: the reader clicks through one event at a time.

### vis-timeline

Read from `github.com/visjs/vis-timeline`, 2026-09-22.

- Dual licensed, Apache-2.0 OR MIT.
- Items can be a single date or a start and end range, and a `point` type
  exists. Ranges and points render together, so overlap is visible.
- The timeline is freely draggable and zoomable, and the time axis scale
  adjusts automatically from milliseconds to years.
- Four builds: standalone with no dependencies, peer which requires Vis Data
  and Moment to be loaded separately, esnext for bundlers, and a legacy build
  the project marks deprecated and says not to use.
- At the time of reading: 2.6k stars, 380 forks, 4,248 commits.

**Configuration options, read from `visjs.github.io/vis-timeline/docs/timeline/`,
2026-09-23.** Checked specifically against the operator's timeline spec.

- **Orientation is horizontal only.** The `orientation` option takes
  `'top'`, `'bottom'`, `'both'` or `'none'`, and those values place the time
  axis at the top or bottom of a horizontal chart. Groups are stacked as
  rows beneath it. There is no option for a vertical time axis anywhere in
  the documented option set.
- **Collapsible lanes are supported.** A group takes `nestedGroups`, an array
  of group ids nested inside it, and `showNested`, a boolean that sets the
  initial state to shown or collapsed, defaulting to true. A group also takes
  `visible` to toggle display.
- **Zoom and drag can be switched off.** `zoomable` and `moveable` both
  default to true and can be set false. `zoomMin`, `zoomMax`, `min` and `max`
  bound the range further. `horizontalScroll` is documented as applicable
  only when `zoomKey` is defined or `zoomable` is false.
- **A fixed month scale is supported for the labels.** `timeAxis.scale`
  accepts `'month'` among other values, with `timeAxis.step` setting the
  interval. This fixes the axis labelling, not the pixel width of a month:
  that follows from the window set by `start` and `end` against the container
  width, so a fixed number of pixels per month means fixing all three.
- **No accessibility or keyboard support is documented.** The events list
  contains only pointer events: `click`, `contextmenu`, `doubleClick`,
  `dragover`, `drop`, `mouseOver`, `mouseDown`, `mouseUp`, `mouseMove`. The
  page contains no mention of ARIA, focus, or keyboard interaction. This is
  an absence in the documentation, which is not the same as proof that none
  exists.
- XSS protection is on by default and item content may be HTML.
- Its own performance guidance: define `start` and `end` in the options to
  improve initial loading time, and avoid heavy CSS such as box shadows and
  gradients on items.

### What this means for a hand-built timeline

The deciding fact is the axis. The operator's design is a vertical spine with
lanes either side and lane headers that travel down the page. vis-timeline is
horizontal by documented design, so it is not an inadequate fit for that
layout, it is the wrong axis and cannot be configured into it.

If the layout were horizontal instead, vis-timeline would fit well: nested
groups give collapsible lanes, `timeAxis.scale: 'month'` gives month
labelling, and `zoomable: false` with `moveable: false` gives a fixed view.
The cost of going horizontal is that a span of several years at a readable
month width is far wider than a phone screen, so the chart scrolls sideways
on mobile.

TimelineJS is ruled out for a different reason: it is slide-based, showing
one event at a time rather than the whole span.

Building such a timeline by hand in CSS Grid or SVG avoids fighting either
library, and avoids a dependency whose accessibility is unverified. The cost
is that spacing, responsive behaviour, and the text equivalent required by
W3C WAI for a complex graphic all become work to be done rather than
inherited.

## 5. Compute, if an assistant is ever built

### Cloudflare Workers, free plan

Read from `developers.cloudflare.com/workers/platform/limits/`, 2026-09-22.
That page states it was last updated 2026-09-05.

- 100,000 requests per day, resetting at midnight UTC. Exceeding it returns
  Cloudflare Error 1027.
- 10 ms of CPU time per request. CPU time does not include waiting on
  network requests, so relaying a call to another API is cheap in CPU terms.
- 128 MB memory per isolate, 50 subrequests per invocation, 6 simultaneous
  outgoing connections waiting on response headers.
- No duration limit on an HTTP-triggered Worker while the client stays
  connected.

**Reading.** The proxy itself would be free at any plausible traffic level
for this site. The cost of an assistant is the model API calls behind it,
not the compute in front of them.

For GitHub Pages hosting limits, see ADR-0002, which records them with their
source and date rather than repeating them here.

## 6. The design surface

### Claude Design

Read from Anthropic's launch post of 2026-04-17, the Claude Design product
page, and two Claude help articles, all 2026-09-22.

- Launched 2026-04-17 as an Anthropic Labs product.
- Available in beta on Pro, Max, Team and Enterprise plans. Not on Free.
- Now usable inside any conversation, in Claude Code, in the Artifacts tab,
  and at `claude.ai/design`, which keeps working as a standalone experience
  with its own setting.
- **It has no version history.** Stated in the help article's own known
  limitations list.
- Exports: download as .zip, PDF, PPTX, standalone HTML, Google Slides only
  at `claude.ai/design`, plus a handoff to Claude Code, either to a local
  coding agent or to Claude Code on the web.
- It draws on the same usage allowance as the rest of Claude, including
  Claude Code. It previously had a separate weekly allowance; that is gone.
- Other stated limitations: inline comments can fail to appear on the page,
  very large repositories should be linked from Claude Code rather than
  loaded, a "chat upstream error" is worked around by starting a new chat tab
  in the same project, editing on the canvas and changing sharing settings
  are not available on mobile, simultaneous editing by two people is basic
  and may not work reliably, and design system import is only as good as its
  source.
- Claude Code's own `/design` command is narrower: it draws artboards that
  export as PNG or PDF only, and requires Claude Code v2.1.265 or later.
- `/design-sync` converts a repository's React design system and uploads it.
  It does not apply here, because no React design system exists.

**Consequence.** Because there is no version history, every export has to be
committed by hand with a log entry, or the design work has no history at all.

### The frontend-design plugin

Read from its README in `anthropics/claude-code` and Anthropic's blog post
of 2025-11-12, both 2026-09-22.

- Described as generating distinctive, production-grade frontend interfaces
  that avoid generic AI aesthetics. It is a plugin to install, not a default.
- The blog post attributes the generic look to distributional convergence,
  and names the defaults it produces: Inter fonts, purple gradients on white
  backgrounds, and minimal animations.

**Measured against existing work.** The current Rahzaan case study uses Inter
with indigo and violet, which is the pattern the post names. Measured by
reading `GitHub Repositories\Rahzaan\index.html`, 2026-09-22.

## Not verified

Each of these is an open check, not a soft claim.

- GSAP's licence text. Only the pricing page was read.
- vis-timeline's keyboard accessibility, its most recent release date, and
  its behaviour at mobile widths. Its documentation page documents no
  keyboard support at all, checked 2026-09-23, which is an absence rather
  than a confirmed lack.
- Whether Astro's default output actually produces the page-weight and
  load-time this site needs. No budget exists to measure against.
- Whether any 3D content can meet a performance budget on a mid-range phone.
- The four-check test on Claude Design: whether a design's Export menu offers
  both a Claude Code handoff and standalone HTML, whether republishing
  produces a version picker, whether a shared link opens signed out, and
  whether the web capture tool still exists at `claude.ai/design`.
- Whether Anthropic's on-request fetcher behaves as ClaudeBot does. Carried
  over from research 0001.
- The Cloudflare and GitHub limits recorded here will drift. Re-read them
  before any decision depends on them again.

## Sources, with ratings

| Source | Rating | Read |
|---|---|---|
| Astro documentation, Islands architecture | First-party documentation | 2026-09-22 |
| MDN, `animation-timeline` | Established reference, page modified 2026-09-16 | 2026-09-23 |
| GSAP pricing page | Vendor, first-party, tier 1 for its own licence terms | 2026-09-22 |
| React Three Fiber, Scaling performance | First-party documentation | 2026-09-22 |
| TimelineJS, Knight Lab | University research lab, first-party | 2026-09-22 |
| vis-timeline repository | First-party repository | 2026-09-22 |
| Cloudflare Workers limits | First-party documentation, updated 2026-09-05 | 2026-09-22 |
| Anthropic launch post, product page, two help articles | First-party documentation | 2026-09-22 |
| frontend-design plugin README and Anthropic blog | First-party documentation | 2026-09-22 |
| `Rahzaan\index.html` | Direct measurement of existing work | 2026-09-22 |
