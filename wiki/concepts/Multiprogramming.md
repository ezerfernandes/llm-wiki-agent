---
title: "Multiprogramming"
type: concept
tags: [operating-systems, concurrency, scheduling, history]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Multiprogramming

**Multiprogramming** is the OS-design discipline of **keeping multiple [[Process|processes]] resident in memory simultaneously** so the [[OperatingSystem|OS]] can switch to another process whenever the current one blocks on I/O. The goal: **keep the CPU busy** instead of idling while a disk read or terminal input completes.

## Mechanism

- Multiple processes' [[ProcessControlBlock|PCBs]] exist in the kernel process table at once.
- When the running process makes a blocking [[SystemCall|syscall]] (e.g., `read` waiting on disk), the [[Scheduler|scheduler]] switches it from [[ProcessState|Running]] to [[ProcessState|Blocked]] and dispatches a different [[ProcessState|Ready]] process onto the CPU via a [[ContextSwitch|context switch]].
- When the blocking event completes, the original process becomes Ready again — eligible to run when the scheduler next picks it.

## Multiprogramming vs Timesharing

[[dis-13-2-processes|DIS 13.2]] uses both terms with related but distinct meanings:

| | Trigger for switch | Goal |
|---|---|---|
| **Multiprogramming** | A process **blocks on I/O**. | CPU utilization. |
| **[[Timesharing]]** | A process's **[[Timesharing|time slice]] / quantum expires** (timer interrupt). | Responsiveness + fairness. |

[[Timesharing]] is the variant that adds a **mandatory quantum bound** on every running process — without it, a CPU-bound process could monopolize the CPU forever. Modern OSes do both: switch on I/O blocks **and** on quantum expiry.

## Why it matters

Multiprogramming is the historical pivot from **batch** systems (one job at a time, CPU idle during I/O) to **interactive** systems (many jobs co-resident, CPU saturated by work from whichever process is currently Ready). Every subsequent scheduling concept — [[Timesharing]], priority queues, fair-share, real-time — assumes multiprogramming as the substrate.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Timesharing]] — the quantum-driven sibling discipline.
- [[Scheduler]] / [[ProcessScheduling]] — pick which process to run next.
- [[ContextSwitch]] — the mechanism multiprogramming relies on.
- [[ProcessState]] — Blocked / Ready transitions are the multiprogramming control points.
- [[Process]] / [[OperatingSystem]] / [[Kernel]].
