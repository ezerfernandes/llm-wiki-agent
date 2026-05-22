---
title: "Job Control"
type: concept
tags: [unix, shell, process]
sources: [dis-app2-9-process-control]
last_updated: 2026-05-18
---

# Job Control

Unix **job control** is the [[UnixShell|shell]] machinery for managing multiple processes started from a single terminal — running them in the **foreground** (shell blocks until completion) or the **background** (shell returns immediately).

## Operators (from [[dis-app2-9-process-control|DIS App 2.9]])

- Trailing `&` — start a command in the background: `./long_running &`.
- `CTRL-Z` — suspend the foreground process (sends [[SIGTSTP]]).
- `bg` — resume the suspended process in the **background**.
- `fg` — bring a background process to the **foreground**.
- `jobs` — list the shell's tracked jobs with `[N]` job identifiers.

## Mechanism

Job control is layered on top of [[Signal|Unix signals]] (Ch 13.4.1) — `CTRL-Z` delivers `SIGTSTP`, `CTRL-C` delivers [[SIGINT]], and `bg`/`fg` send `SIGCONT` to resume. The kernel tracks **process groups** so a single key press affects every process in the foreground pipeline.

## Connections

- [[Ps]] — inspect tracked processes.
- [[Kill]] — terminate a job by [[ProcessID|PID]].
- [[BackgroundProcess]] — the `&` execution model.
- [[Signal]] — the underlying IPC primitive.
- [[UnixShell]] — host of job control.
