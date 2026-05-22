---
title: "SIGINT"
type: concept
tags: [unix, signal, process]
sources: [dis-app2-9-process-control, dis-13-4-1-signals]
last_updated: 2026-05-18
---

# SIGINT

**SIGINT** (Signal 2, *Interrupt*) is the [[Signal|Unix signal]] sent to the foreground process when the user presses **CTRL-C** at the terminal. Default action: **terminate** the process.

## Usage

- `CTRL-C` — the standard interactive interrupt; terminates the running foreground command.
- `kill -2 <pid>` or `kill -INT <pid>` — same signal sent programmatically by [[Kill|`kill`]].
- Programs can install a [[SignalHandler|signal handler]] to override default termination (e.g., to clean up before exit).

## Related signals

| Signal | Number | Default | Trigger |
|---|---|---|---|
| SIGINT | 2 | terminate | CTRL-C |
| SIGTERM | 15 | terminate | `kill <pid>` default |
| SIGKILL | 9 | terminate (uncatchable) | `kill -9` |
| [[SIGTSTP]] | 20 | stop | CTRL-Z |
| [[SIGBUS]] | 7/10 | terminate | bus error |

## Connections

- [[Signal]] — umbrella IPC mechanism.
- [[Kill]] — sends SIGINT (and other signals).
- [[JobControl]] — the broader CTRL-key + signal vocabulary.
- [[dis-app2-9-process-control]] — source.
