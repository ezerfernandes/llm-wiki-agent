---
title: "SIGTSTP"
type: concept
tags: [unix, signal, process]
sources: [dis-app2-9-process-control]
last_updated: 2026-05-18
---

# SIGTSTP

**SIGTSTP** (Signal 20, *Terminal Stop*) is the [[Signal|Unix signal]] sent by **CTRL-Z** — it **suspends** the foreground process rather than terminating it. The process can be resumed later via `bg` (background) or `fg` (foreground), which sends `SIGCONT`.

Distinct from `SIGSTOP` (uncatchable kernel-only stop): SIGTSTP can be caught or ignored by the process if it wants to do cleanup before suspending.

## Connections

- [[Signal]] — umbrella IPC mechanism.
- [[JobControl]] — the suspend/resume vocabulary.
- [[SIGINT]] — sibling CTRL-key signal (terminate vs suspend).
- [[BackgroundProcess]] — the resumed state.
- [[dis-app2-9-process-control]] — source.
