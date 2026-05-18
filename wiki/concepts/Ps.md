---
title: "`ps` (Process Status Utility)"
type: concept
tags: [unix, posix, process, cli, debugging, tooling]
sources: [dis-3-4-gdb-advanced]
last_updated: 2026-05-17
---

# `ps` (Process Status Utility)

[[OperatingSystem|Unix]] command-line utility that **lists running [[Process|processes]]** — the canonical primitive for discovering [[ProcessID|PIDs]]. Introduced in [[dis-3-4-gdb-advanced|DIS Ch 3.4]] as the PID-discovery step for [[GdbAttach|`gdb <prog> <pid>`]] attach-mode debugging.

## Common forms

| Invocation | What it shows |
|---|---|
| `ps` | Processes belonging to the current shell session. |
| `ps -A` (or `ps -e`) | **All** processes on the system. |
| `ps -A \| grep a.out` | Filter to processes matching a name — the [[GdbAttach|attach-mode]] recipe. |
| `ps -ef` | All processes, full format (UID, PID, PPID, start time, command). |
| `ps aux` | BSD-style: USER, %CPU, %MEM, VSZ, RSS, START, TIME, COMMAND. |
| `ps -p <pid>` | Information about one specific [[Process|process]]. |

The [[dis-3-4-gdb-advanced|Ch 3.4]] recipe is `ps -A | grep a.out` → read the [[ProcessID|PID]] in the first column → `gdb ./a.out <pid>`.

## Why it matters here

- **Required step for [[GdbAttach|`gdb attach`]]** — [[GDB]] needs a [[ProcessID|PID]] to attach to, and `ps` is the universal way to find one.
- **Cross-shell debugging workflow**: long-running program in shell A → `ps -A | grep` in shell B → attach in shell B without touching shell A's terminal.
- **First [[OperatingSystem|OS]]-introspection tool in the corpus** — every prior chapter assumed a single program in isolation; `ps` is the user-side view of the [[OperatingSystem|kernel]]'s [[Process|process]] table.

## Related

- [[Process]] / [[ProcessID]] — what `ps` enumerates.
- [[GdbAttach]] — the canonical consumer of `ps` output in *Dive into Systems*.
- [[OperatingSystem]] — owner of the process table `ps` reads from (`/proc` on Linux, `sysctl` on BSD/macOS).
- [[Kill]] — companion utility — `ps` finds the PID, `kill` signals it.
