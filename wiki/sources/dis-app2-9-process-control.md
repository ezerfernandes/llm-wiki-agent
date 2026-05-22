---
title: "Dive into Systems — App 2.9 Process Control"
type: source
tags: [book, unix, shell, process, signals]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/pskill.html
---

## Summary
Ninth subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix* (Ch 17). Codifies **process control** at the [[UnixShell|shell]] level: foreground vs background execution (`&`), job control (`fg`/`bg`/`CTRL-Z`), and process termination via [[Signal|signals]] delivered by [[Kill|`kill`]]/`pkill`. Extends [[Ps]] and [[Kill]] (previously introduced in Ch 3.4 GDB context) with their Unix-CLI day-to-day usage.

## Key Claims
- Trailing `&` runs a command in the **background** so the shell returns immediately for further commands.
- [[Ps|`ps`]] lists processes with [[ProcessID|PID]], terminal, CPU time, and command — *"list[s] all the programs running in the shell."*
- `CTRL-Z` suspends a foreground process; `bg` resumes it in the background; `fg` returns a background process to the foreground.
- [[Kill|`kill <pid>`]] sends [[Signal|`SIGTERM` (15)]] by default; `kill -9` sends `SIGKILL` for forced termination; `pkill <name>` targets all processes matching a command name.
- `CTRL-C` sends [[SIGINT]] to the foreground process — the standard interactive interrupt.

## Connections
- [[JobControl]] — fg/bg/CTRL-Z mechanism this section codifies.
- [[Ps]] — extended in place with the Appendix-2.9 day-to-day shell usage.
- [[Kill]] — extended in place with `pkill` + `SIGTERM`/`SIGKILL` framing.
- [[Signal]] — IPC primitive from Ch 13.4.1 reused here at the shell level.
- [[SIGINT]] — CTRL-C signal.
- [[BackgroundProcess]] — `&` execution model.
- [[DiveIntoSystems]] — Appendix 2.9.
