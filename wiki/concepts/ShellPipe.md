---
title: "Shell Pipe"
type: concept
tags: [unix, shell, ipc]
sources: [dis-app2-13-pipes, dis-13-4-2-message-passing]
last_updated: 2026-05-18
---

# Shell Pipe (`|`)

The **shell pipe** `|` connects two processes so the [[Stdout]] of the upstream command becomes the [[Stdin]] of the downstream command, **without** any intermediate file:

```bash
cat access.log | grep ERROR | wc -l
```

This is the **shell-level surface** of the [[Pipe]] [[InterprocessCommunication|IPC]] primitive — under the hood the shell calls `pipe(2)` to allocate a kernel buffer, `fork(2)` to create the child processes, and `dup2(2)` to wire the pipe endpoints onto fds 1 and 0 before `exec`'ing the commands.

## Properties

- **Streaming** — downstream reads start as soon as upstream writes; no temp files.
- **Chainable** — arbitrarily many stages: `a | b | c | d`.
- **Buffered** — pipe has a small kernel buffer (~64 KB on Linux); upstream blocks if downstream is slow.
- **stdout-only** by default — [[Stderr|stderr]] is **not** piped unless you write `cmd 2>&1 | ...`.

## Idioms

| Pattern | Use |
|---|---|
| `cmd \| less` | Page through long output. |
| `cmd \| grep pattern` | Filter lines. |
| `cmd \| wc -l` | Count lines. |
| `cmd \| sort \| uniq -c \| sort -rn` | Frequency table. |
| `find . \| xargs grep TODO` | Per-arg execution via [[Xargs]]. |

## Connections

- [[Pipe]] — the underlying [[InterprocessCommunication|IPC]] primitive ([[dis-13-4-2-message-passing|Ch 13.4.2]]).
- [[IORedirection]] — sibling stream-rewiring mechanism (file-based).
- [[StandardStream]] / [[Stdin]] / [[Stdout]] — the streams being rewired.
- [[Grep]] / [[Xargs]] — common pipe consumers.
- [[dis-app2-13-pipes]] — source.
