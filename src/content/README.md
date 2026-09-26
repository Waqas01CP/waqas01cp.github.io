---
type: reference
description: The content schema. What every item in items.json carries, which rules the build enforces on it, and how to add an item. Read before adding or editing content.
status: current
---

# Content

`items.json` holds every item on the site, one entry each, as a JSON array.
Markup is generated from it by `build.py`, so a date or a fact is written
once, here, and nowhere else (ADR-0006).

**Why JSON and not YAML.** The standard library has no YAML parser, so YAML
would need a second dependency, which scope floor line 14 forbids without a
record. Brief 1 named `items.yaml` and allowed JSON as the fallback.

Every claim in this file traces to the operator's master CV. The master is
the only source of truth (scope floor line 1). Where this file and the
master disagree, the master wins and the disagreement is reported.

## Fields

| Field | Required | Type | Notes |
|---|---|---|---|
| `id` | yes | text | Stable lowercase slug, letters, digits and single hyphens. Used as the item's anchor. Unique, and not one of the page's own ids: `main`, `timeline`, `projects`, `certifications`. |
| `title` | yes | text | As written in the master CV. |
| `tier` | yes | 1, 2 or 3 | Controls order and prominence, never which layers render: every item carries all three layers. Tier 1 additionally links out to a standalone case study. Never a visible label (ADR-0005 Changes, ADR-0008). The build fails if tier decreases down this file within a section; it never sorts by tier. |
| `lane` | yes | text | `builds`, `opensource`, `work`, `certifications` or `band`. |
| `start` | yes | `YYYY-MM` | |
| `end` | yes | `YYYY-MM` or `present` | `present` resolves to the build's as-of month: the current UTC month, or the one given with `--as-of`. |
| `stack` | no | text | The stack from the master's italic line. |
| `source` | **yes** | text | Where in the master CV the item traces to, as `master-cv:<section>/<item>`. |
| `proof` | one of | list of `{label, url}` | Public artefacts that check layer 1. |
| `verification` | one of | text | The verification route, when no link can exist. |
| `layer1` | yes | text | One or two sentences, specific and checkable (ADR-0005). |
| `layer2` | yes | text | A short summary for a reader deciding whether to go deeper. |
| `layer3` | yes | list of text | Blocks rendered in order, inside a collapsed `<details>`. Limited to decisions, trade-offs, what failed and how each was verified (ADR-0005). |

`opensource` is in the lane list because ADR-0003 keeps the Open source lane
in the data model. Nothing renders in it until it holds a merged pull
request.

## Markup inside fields

Every field is plain text and is escaped on output, except `layer3`.

`layer3` blocks are HTML fragments limited to `<strong>` and `<a href="...">`,
properly nested, because the master's bullets carry bold and links and
Markdown would need a second dependency. They are rendered unescaped, so the
build checks every block and fails on any other tag, attribute, comment or
unclosed element. No other field is rendered unescaped.

## What the build enforces

`python build.py` checks every item before writing anything, reports every
failing item by id, and exits non-zero. The previous output stays as it was.

The two content gates from ADR-0006:

- **Missing source.** An item with no `source` fails.
- **Missing proof route.** An item with neither `proof` nor `verification`
  fails, and so does an item with both.

The schema checks:

- A field not in the table above fails, so a misspelt field cannot pass
  silently.
- A missing required field, a wrong type, an empty value, a bad `tier`, an
  unknown `lane`, or a malformed date fails.
- An `end` before its `start` fails.
- A `start` before January 2024 fails, except in the `band` lane, which is
  drawn from the top of the timeline and marked as starting earlier
  (ADR-0003).
- A link that points at this site's own origin, `waqas01cp.github.io`, fails,
  in `proof` and inside `layer3`. Write it root-relative instead, for
  example `/Rahzaan/` (ADR-0002).
- A duplicate `id` fails.
- An item whose lane has no page section fails. Today only `builds`
  (Projects) and `certifications` (Certifications) have a section, the two
  ADR-0001 names. The headings for `work`, `opensource` and `band` are not
  decided.
- Within a section, an item of a higher tier number above one of a lower
  tier number fails, naming both, for example
  `item 'x' (tier 3) is above item 'y' (tier 2)`.

## Order

Within a page section, items appear in the order they appear in this file,
and that is the only order. ADR-0001 orders projects by importance and
ADR-0008 sets the tiers, so this file lists tier 1 first, then tier 2, then
tier 3. Tier is an assertion this order must satisfy, checked by the build,
never a second sort (ADR-0005 Changes).

The timeline sorts every item by `start`, and items that start in the same
month keep this file's order.

## Timeline position

Computed by `build.grid_position`, never written here. Row 1 is January
2024, and each month is four rows (ADR-0003). An item's start row is
`(months since 2024-01) * 4 + 1`, and its span is `(months from start to end
inclusive) * 4`.

## Adding an item

1. Copy the wording from the master CV. Do not tighten or reword a claim.
2. Give it a `source`, and either `proof` or `verification`.
3. Put it where it belongs in importance order.
4. Run `python build.py` with the venv active and read what it reports.
