---
type: reference
description: What the briefs folder is and how it behaves. Working scratch space, not a record. Briefs are overwritten; the durable trace is the session log.
status: current
---

# Briefs

**This folder is working space, not a record.** It holds the latest brief or
report addressed to each seat. A brief is the specification the architecture
chat hands to a fresh implementing session. Each file is written, executed,
ticked, and overwritten by the next one.

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

From 2026-10-11, one file per receiving seat, each overwritten by the next
(the operator's Working Method, section 9.4; `CLAUDE.md`, Briefs):

| File | From | To |
|---|---|---|
| `implementation-seat.md` | the architecture chat | the implementing seat |
| `architecture.md` | the implementing seat | the architecture chat |
| `implementing.md` | the implementing seat | its own next session, as a handoff |

Each file is unexecuted, with an empty box on its first line and any
addendum appended to it; executed, ticked with the date when the operator
says it was acted on; and replaced only after it has been read for what it
still says. The chat ticks its brief once it has verified the seat's report
against the repository. The numbered briefs written before 2026-10-11 are
history and are not executed again.
