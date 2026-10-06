---
type: reference
description: The content schema. What items.json and site.json carry, which rules the build enforces on them, how shortened text is checked against its source, and how to add an item. Read before adding or editing content.
status: current
---

# Content

Two files hold every word on the site. Markup is generated from them by
`build.py`, so a date or a fact is written once, here, and nowhere else
(ADR-0006).

- `items.json`: every dated item, one entry each, as a JSON array. The six
  projects, the two work entries, the degree and the five certificates.
- `site.json`: the text that belongs to the page rather than to one item.
  The Intro, the figures on the opening screen and at the head of
  Projects, the skills, and the contact labels.

**Why JSON and not YAML.** The standard library has no YAML parser, so YAML
would need a second dependency, which scope floor line 14 forbids without a
record.

Every claim in these files traces to the operator's master CV, the only
source of truth (scope floor line 1). Where they and the master disagree,
the master wins and the disagreement is reported. One paragraph in
`site.json` is not in the master: `approved`, the Intro's second paragraph,
approved by the operator on 2026-10-06. It says so in the file, and
`tools/check_content.py` reports it on every run.

## Written once, and shortened text checked

Master text is stored as the master writes it: each project's bullets, its
italic line split into `stack`, `status` and `layer2`, each work entry's
bullets, the degree's coursework, the summary and the skills.

Where the page shows a shorter form, the shorter form is stored as written,
and **the build refuses any that is not a cut of the item's own text**: the
same words in the same order, some left out. So `layer1`, `detail`,
`org_short`, and the highlights and feature in `site.json` cannot drift from
their source. Change a number in a bullet and every cut of that bullet
that carries the number fails the build until it is changed too. Changing
a fact by cutting words is not something a program can detect; that stays
a reviewer's check against the master.

## items.json

Fields every item carries:

| Field | Type | Notes |
|---|---|---|
| `id` | text | Lowercase slug, letters, digits and single hyphens. The item's anchor. Unique. Not one of the page's own ids (`main`, `top`, the eight section ids) and not starting with `depth-`, `toggle-`, `tl-` or `h-`. |
| `lane` | text | `builds`, `work`, `band`, `certifications` or `opensource`. |
| `title` | text | As the master writes it. A project title with a colon, such as `Rahzaan: AI Career Guidance Platform`, is shown as a name and a subtitle. |
| `start` | `YYYY-MM` | |
| `end` | `YYYY-MM` or `present` | `present` resolves to the as-of month. |
| `source` | text | **Required.** Where in the master CV the item traces to, as `master-cv:<section>/<item>`. |

And exactly one proof route:

| Field | Notes |
|---|---|
| `proof` | A list of `{label, url}`: public artefacts that check the item. Root-relative or absolute `http(s)`; never this site's own origin (ADR-0002). |
| `verification` | A verification route, as text, where no link can exist. No item uses it now. |
| `no_proof` | The record that exempts the item, `ADR-0010`. Allowed only for `hubit`, `pac-kamra` and `be-software-engineering`, the three items ADR-0010 names; any other item without a proof link fails. |

Fields by lane:

| Lane | Required | Optional |
|---|---|---|
| `builds` (Projects) | `tier`, `stack` (list), `layer1`, `bullets` (list) | `status`, `layer2`, `detail` |
| `work` (Work) | `org`, `location`, `bullets` | `org_short`, `date_style`, `detail` |
| `band` (Education, and the degree band on the timeline) | `org`, `org_short`, `cgpa`, `cgpa_scale`, `coursework` (list) | `date_style` |
| `certifications` (Certifications) | | `org`, `date_style` |
| `opensource` | | `org`, `detail`, `date_style` |

What each one is:

- `tier`, projects only: 1, 2 or 3. Order only, never a visible label, never
  which layers render (ADR-0008, ADR-0010). Tier 1 takes a full row.
- `stack`: the stack sentence of the master's italic line, one entry per
  item. No model provider.
- `status`: the italic line's status sentence, shown in bold before the
  summary, such as the job aggregator's "In development, and running in
  production since 17 Sep 2026."
- `layer2`: the summary, the rest of the italic line. For WordPy, whose
  italic line is its stack alone, a cut of its bullet.
- `layer1`: the one-line fact, **a cut of one of the item's bullets**.
- `bullets`: every master bullet, as HTML fragments limited to `<strong>`
  and `<a href>`, properly nested. They are rendered unescaped, so the build
  checks each one and fails on any other tag, attribute, comment or
  unclosed element. They form layer 3, the "In depth" panel named for the
  item. A project with one bullet has no panel, so **its `layer2` then its
  `layer1` must carry the whole bullet, word for word**; the build checks.
  Work entries show their bullets in full, with no panel.
- `detail`: the text on the item's timeline card, **a cut of its status and
  `layer2`, its `layer1`, or one bullet**.
- `org_short`: a shorter organisation name for the timeline and the Intro,
  **a cut of `org`**.
- `date_style`: how the dates read in the item's own section, in the
  master's forms. `compact`, the default: "Nov to Dec 2025", "Aug 2024 to Jan
  2025", "Feb 2026 to Present". `full`: both years always, "Jan 2024 to Feb
  2024". `long`: month names in full, "June 2026 to July 2026". The timeline
  always uses `compact`.
- `cgpa`, `cgpa_scale`, `coursework`: the degree's, as the master writes
  them.

## site.json

| Field | Notes |
|---|---|
| `source` | Where the file traces to in the master CV. |
| `name`, `headline`, `location`, `availability`, `email` | From the master's header. `headline` is a list, rendered joined by `|`. |
| `linkedin`, `github` | `{url, text}` from the master's header. |
| `summary` | The master's Professional Summary, whole. |
| `approved` | `{text, approved_by}`: operator-approved text that is not in the master. Rendered as the Intro's second paragraph. |
| `highlights` | The figures on the opening screen. Each names an `item`, a source in `from`, and a `figure` with the `text` after it and optionally `before` it. **The words, in order, must be a cut of the source**, which is `site/summary` or `<item>/bullets/<n>`, counted from 1. |
| `feature` | The figure at the head of Projects: a `label`, a `figure` and its `text`, `pairs` and a `note`, **each a cut of its source**. |
| `skills` | The master's eight groups, `{label, items}`, labels and items as written; the two Coursework groups keep that label. No levels (scope floor line 2). |
| `contact` | Email, LinkedIn and GitHub, in that order, each with its label and, for LinkedIn and GitHub, the line saying what it is for. Email's line is `availability`. |

## What the build enforces

`python build.py` checks everything before writing anything, reports every
failing item by id, and exits non-zero. The previous output stays as it was.

- **Missing source** fails (ADR-0006).
- **No proof route**, or more than one, fails; `no_proof` outside the three
  items ADR-0010 names fails.
- A field the item's lane does not define fails, so a misspelt field cannot
  pass silently. A missing required field, a wrong type, an empty value, a
  bad `tier`, an unknown `lane` or `date_style`, or a malformed date fails.
- An `end` before its `start` fails, and so does a `start` after the as-of
  month, or an `end` after it outside the band.
- A `start` before January 2024 fails, except in the band, which is drawn
  running past the bottom of the timeline (ADR-0003).
- Every cut named above that is not a cut fails, naming the field.
- A link to this site's own origin fails, in `proof` and inside bullets.
- A duplicate `id` fails, and so does more than one item in the band.
- An item whose lane has no page section fails. Today that is
  `opensource`, which has no section until it holds a merged pull request
  (ADR-0003, ADR-0008).
- **Tier order**: in Projects, an item of a higher tier number above one of
  a lower fails, naming both, for example `item 'x' (tier 3) is above item
  'y' (tier 2)`. The build never sorts by tier.
- A highlight or the feature that names a missing item or source fails.

## Order

Within a section, items appear in this file's order, and that is the only
order. Projects are in tier order (ADR-0008); work, certifications and the
degree follow the master, newest first.

The timeline lists every item newest first: by start month, then end month,
then this file's order.

## Timeline position

Computed by `build.grid_position`, never written here. Four rows per month
(ADR-0003); row 1 is the as-of month at the top, and the axis ends at January
2024. An item's top row is set by its end month and its span by its length:
`row = (as-of month - end month) * 4 + 1`, `span = months * 4`. Items that
overlap in one lane are set side by side by `build.sub_columns`.

## The CV link

The Intro and the footer link to `/cv/Waqas_Sharif_CV.pdf` only when that
file exists in the tree being built (ADR-0008), so gate B's rebuild of the
staged tree agrees with the committed output.

## Adding an item

1. Copy the wording from the master CV. Shorten only by cutting words.
2. Give it a `source`, and a `proof` link unless ADR-0010 names it.
3. Put it where it belongs: tier order in Projects, newest first elsewhere.
4. Run `python build.py` with the venv active and read what it reports.
5. Run `python tools/check_content.py --master <path to the master CV>` and
   read what it reports. See CLAUDE.md, Commands.
