---
type: reference
description: The design system for the site. Tokens in both themes, two candidate prose faces, the component styles, an isolated 3D prototype, and the measurements taken on them. Read before styling any template.
status: draft
---

# Design system

Built 2026-10-03 (UTC) from docs/design/DESIGN.md, before the styled site.
The same system is published as a Design System artifact on claude.ai,
which shows each component live in light and dark. This folder is its copy
in the repository. Nothing here is wired into the build yet.

## Files

| File | What |
|---|---|
| tokens.json | The tokens: colour per theme with contrast in each usage note, type, spacing, radius, timeline geometry. The source for tokens.css. |
| tokens.css | The tokens as custom properties. Light by default, dark by system setting, `data-theme` overrides both. Includes the `@font-face` rules. |
| components.css | Styles for every component, written against the tokens only. Includes the metric-matched fallback faces. |
| pipeline-graph.js | The 3D prototype. Raw WebGL, no library. |
| specimen.html | Every component on one page with theme and prose-face switches. Open it from a local server, not as a file, so the fonts load. |
| fonts/ | Latin-subset woff2 files from fontsource 5.3.0. |
| licences/ | The SIL Open Font License for each family. |

## Not decided yet

- **Prose face.** A, Source Serif 4, or B, Atkinson Hyperlegible Next. The
  site ships one. Both pair with IBM Plex Mono 400.
- **Whether the 3D graph stays.** Measurements below.
- **The timeline below 720px.** Proposed: one-sided, chronological, not to
  scale. ADR-0003 left the breakpoint behaviour open.
- **The LinkedIn mark.** Its official file is not in this folder yet.

## Changes the templates will need

- item.html.j2: add the component classes (see the artifact's Entry card),
  name each disclosure for its item, and drop the disclosure when an item
  has no layer 3.
- timeline.html.j2: emit `--row`, `--span` and `--col` as custom
  properties instead of inline `grid-row` and `grid-column`, assign a
  sub-column (`-a` or `-b`) to concurrent items in one lane, and put the
  lane name in a visually hidden span.

## Measurements

Taken 2026-10-03 on the specimen page, served locally without compression,
in a cloud container: Lighthouse 12.8.2, default mobile settings
(simulated 150 ms RTT, 1.6 Mbps down, 4x CPU slowdown), headless Chromium
with software WebGL. Median of five runs each. Per ADR-0009, results from
this machine are not comparable with results from another.

| Page | LCP | CLS | TBT | Bytes |
|---|---|---|---|---|
| Without the graph | 2107 ms | 0 | 0 ms | 209,412 |
| With the graph | 1977 ms | 0 | 0 ms | 220,685 |

The LCP difference is inside run-to-run spread (1664 to 2121 ms without,
1810 to 2270 ms with). Lighthouse does not see the graph's running cost,
because the graph starts after the page settles. Measured separately with
Chrome's performance metrics at 4x CPU slowdown, 412 px viewport, over
five seconds with the graph on screen: main thread busy 37% while the wave
runs (14 seconds), 0% once it rests, 0% under reduced motion. Before it was
capped at 30 frames a second and two passes, it held the main thread at
64 to 67% indefinitely.

Not yet done: ADR-0009's check that the measurement can fail, by making
the page deliberately slow and confirming the run fails.

## Contrast

Every text and meaningful-line pairing was computed with the WCAG 2 formula
from the hex values. Lowest results: `ink-muted` on `sunken` 5.97:1 (light);
`rule-strong` on `sunken` 3.61:1 (light); `accent` on `accent-tint` 5.44:1
(light). The full list is in tokens.json usage notes.
