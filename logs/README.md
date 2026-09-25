---
type: index
description: The session log index. Read this first for what prior sessions did, then chain backwards through the most recent relevant log only as far as needed.
status: current
---

# Session logs

One log per session, newest at the top. This table is the navigation index
for all session history.

## How to use this file

Read this table first. It tells you what prior sessions did.

When you need detail beyond this table, read the most recent relevant log.
That log references the one before it. Chain backwards only as far as you
need, and stop when you have enough. Do not read the directory.

This rule is what keeps the reading cost flat as the log count grows.

## How to maintain it

Append your row in the same commit as your work. A log with no row here is
invisible.

Never delete or modify an existing row. A correction is a new row saying so.

Rows are compressed: no prose, no reasoning, nothing beyond what a future
session needs to decide whether to open the log.

If a log file exists with no row here, read it and add the row before doing
anything else.

One session, one file. A session that continues across several rounds adds
a row per round, each naming the same file.

## Log format

`Working Method\Templates\session-log.md`. File name
`logs/YYYY-MM-DD-short-description.md`, dated in UTC. There is no
project-specific log-format record yet.

## Reorganisation

When this directory passes about 80 files at its root, split by lane into
subdirectories and leave this index at the top pointing into them. Decide it
before the root becomes unscannable, not after.

## Index

| Date (UTC) | Log file | Session | What was done | Outcome |
|---|---|---|---|---|

No implementing session has run yet. The architecture chat's own history is
in `CHAT_STATE.md`, not here.
