---
type: reference
description: What the briefs folder is and how it behaves. Working scratch space, not a record. Briefs are overwritten; the durable trace is the session log.
status: current
---

# Briefs

**This folder is working space, not a record.** A brief is the specification
the architecture chat hands to a fresh implementing session. It is written,
executed, ticked, and overwritten by the next one.

Format: the brief template in the operator's cross-project Working Method.
That document set lives in his private vault and is deliberately not linked
from here, because this repository is public. A brief that needs the path
carries it, and a brief is never committed.

## Why the briefs themselves are not committed

Only this file is tracked. The briefs are in `.gitignore`.

A brief is transient by design, so committing every version would build a
pile of superseded specifications that no reader needs. The durable trace
already exists elsewhere and is better:

| Question | Where the answer lives |
|---|---|
| Why was this decided | `docs/decisions/` |
| What was asked for in that round | the session log's own summary |
| What actually happened | `logs/`, indexed in `logs/README.md` |
| What the state is now | `STATE.md` |

**So the session log carries the brief's substance.** A log that records only
what was built, without what was asked, breaks that chain. Write it so the
chain holds after the brief is gone.

There is a second reason. A brief can carry content that is not approved
yet, including wording drafted about the operator by the chat rather than by
him. This repository is public.

## Rank

A brief ranks below `CLAUDE.md` and every accepted record. Where it
contradicts one, follow the record and report the contradiction.

The only exception is a brief that names the record and the clause and
states that the operator approved the override.

## Convention

One brief in flight at a time. Number it, tick it when the seat reports back
and the chat has verified the report against the repository, then let the
next brief replace it.
