---
type: reference
description: The seven repository gates of ADR-0007. What each blocks, when it fires and the case that defeats it, with the notes on gates A and E. Moved word for word from CLAUDE.md. Read before committing, and before building or changing a gate.
status: current
---

# The repository gates

Moved word for word from `CLAUDE.md`'s section "The hook blocks" on
2026-10-23 (UTC), which the operator approved that day (Brief 14,
Part 3). `CLAUDE.md` points here. A section named in the text, such as
Commands, is one of `CLAUDE.md`'s.

Seven gates, ADR-0007, in `tools/gates.py`, called by `.githooks/pre-commit`
and `.githooks/pre-push`. Each was proven by the case built to defeat it,
and each case was also shown to get through with its gate neutered. They
enforce only once `core.hooksPath` is set (Commands); until then they are
requests, so treat them as binding anyway.

| Gate | When | Blocks | Defeated by |
|---|---|---|---|
| A, never-commit | pre-commit | `CHAT_STATE.md` at any path; anything in `briefs/`; any staged text file holding a filesystem path into the operator's private material: a drive-letter absolute path, a climb out of the repository, a path segment naming the Working Method or the Operating Plan folder, the master CV's file name, or the vault's root folder name. Prints the file, line and matched text. | Staging `CHAT_STATE.md` with `-f`; a planted template path. Control: prose naming the Working Method passes. |
| B, rebuild | pre-commit | Staged output that differs from a fresh build of the staged source, as of the month recorded in the staged `index.html`. | A one-character edit to `index.html`; `items.json` changed without rebuilding. |
| C, map | pre-commit | A `MAP.md` that is stale against the staged files, or a staged Markdown header GitHub would refuse to read: an unquoted value holding ": " or " #", or beginning with a character YAML reserves. Standard library only; known patterns, not every YAML rule (ADR-0007 Changes, 2026-10-12). | A new Markdown file committed without regenerating the map; a description holding an unquoted ": ". |
| D, missing tool | every hook | A missing venv interpreter, gate script, map generator or `build.py`: a refusal naming it, never a skip. | Renaming the map generator; moving the venv. |
| E, STATE.md moved | pre-push | A push whose range touches `build.py`, `requirements.txt`, `index.html`, `src/`, `static/`, `tools/` or `.githooks/` with no commit in the range touching `STATE.md`. The last commit of a series is enough. | Pushing a `src/` change with no `STATE.md` change. Control: a series with `STATE.md` only in its last commit passes. |
| F, every claim readable | pre-commit | On gate B's fresh build, a string in `site.json` or `items.json` that, markup stripped, is not in `index.html`'s readable text: its text with script, style and template bodies and any element marked `hidden` left out. A title counts as its name and subtitle. Keys never printed as written (ids, months, provenance, addresses) are named in the gate; every other key is checked. Scope floor line 7 (ADR-0007 Changes, 2026-10-23). | A template rendering a field only into a data attribute. Control: the same field in a data attribute and in the text passes. |
| G, no third parties, no tracking | pre-commit | In the staged `index.html` and `static/`'s scripts and stylesheets: an absolute or scheme-relative address in any attribute but a plain link's `href`, in a stylesheet outside a comment, or in a script's string; in script code, `document.cookie`, `cookieStore`, `localStorage`, `sessionStorage`, `indexedDB`, `sendBeacon`, `fetch`, `XMLHttpRequest` or `WebSocket`; anywhere in them, a known analytics host. The allowlist is empty; XML namespace names pass. Known patterns, not every route. Scope floor lines 9 and 10 (ADR-0007 Changes, 2026-10-23). | A planted Google Tag Manager script; `document.cookie` in `site.js`. Control: an external plain link passes. |

Gate A matches path forms, never prose, and cannot match its own source.
Every pattern is written so the source never contains the text it matches,
and the vault's root folder name, which has never been committed, is held
only as a digest. A brief that needs a private path carries it, and briefs
are never committed. Gate E's list of implementation paths is recorded
in ADR-0007 Changes, 2026-09-26.
