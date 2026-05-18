---
title: "Process State"
type: concept
tags: [operating-systems, processes, scheduling]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Process State

The **process state** is the discrete label the [[OperatingSystem|OS]] assigns to each [[Process|process]] indicating its current life-cycle phase. [[dis-13-2-processes|DIS Ch 13.2]] codifies the canonical **four-state model**:

| State | Meaning |
|---|---|
| **Ready** | Could run on a CPU but is not currently scheduled. Newly created processes start here; so do processes whose [[Timesharing|time slice]] just expired. |
| **Running** | Actively executing instructions on a CPU. |
| **Blocked** | Waiting for an event (disk I/O, child termination, [[Signal|signal]]) before it can continue. **Not** a [[Scheduler|scheduling]] candidate until the event fires. |
| **Exited** | Has terminated but still has a [[ProcessControlBlock|PCB]] entry pending parent cleanup ([[Zombie|zombie]]). Will never run again. |

## Transitions

- **(new) → Ready** — at creation (e.g., child of [[Fork|`fork()`]]).
- **Ready → Running** — the [[Scheduler|scheduler]] dispatches the process onto a CPU.
- **Running → Ready** — [[Timesharing|time slice]] expiration; pre-emption.
- **Running → Blocked** — process issues a blocking [[SystemCall|syscall]] (e.g., `read` waiting on disk).
- **Blocked → Ready** — awaited event completes (I/O finishes, [[Signal|`SIGCHLD`]] arrives).
- **Running → Exited** — process calls [[Exit|`exit`]] or is killed.
- **Exited → (gone)** — parent calls [[Wait|`wait` / `waitpid`]] and reaps the [[Zombie|zombie]].

## Why it matters for scheduling

The [[Scheduler|scheduler]] only considers processes in **Ready**. Blocked processes cannot make progress on the CPU, so trying to schedule them would waste a [[ContextSwitch|context switch]]. The Exited state exists specifically so the parent can read the child's [[ExitStatus|exit status]] — without it, the status would be lost.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Process]] — the entity these states label.
- [[ProcessControlBlock]] — stores the current state field.
- [[Scheduler]] / [[ProcessScheduling]] — operate over the *Ready* set.
- [[ContextSwitch]] — triggered on every state transition involving the CPU.
- [[Fork]] / [[Exec]] / [[Wait]] / [[Exit]] — the [[SystemCall|syscalls]] that drive transitions.
- [[Zombie]] — the colloquial name for the Exited-but-not-reaped state.
- [[Timesharing]] — the mechanism that drives Running → Ready preemption.
