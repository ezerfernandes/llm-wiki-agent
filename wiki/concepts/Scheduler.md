---
title: "Scheduler"
type: concept
tags: [operating-systems, scheduling, processes, policy]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Scheduler

The **scheduler** is the [[Kernel|OS kernel]] component that decides **which [[ProcessState|Ready]] [[Process|process]] runs on a CPU next** and **for how long**. [[dis-13-2-processes|DIS Ch 13.2]] frames it as the **policy** half of the OS's process-execution stack, paired with [[ContextSwitch|context switching]] as the **mechanism**:

| Layer | Question | Answered by |
|---|---|---|
| **Mechanism** | *How* does the OS swap one process for another? | [[ContextSwitch]] |
| **Policy** | *Which* process should run next, and for how long? | Scheduler / [[ProcessScheduling]] |

## What the scheduler does

1. **Maintains the [[ProcessState|Ready]] set** — the [[ProcessControlBlock|PCBs]] of processes that *could* run if a CPU were free. Blocked and Exited processes are not candidates.
2. **Picks the next process** — by a *[[ProcessScheduling|scheduling policy]]* (round-robin, priority-based, fair-share, multilevel feedback queue, etc.).
3. **Sets a [[Timesharing|time slice]]** — bounds how long the chosen process holds the CPU before the hardware timer interrupts and forces a reschedule.
4. **Triggers a [[ContextSwitch|context switch]]** — saves the outgoing PCB's register snapshot and loads the incoming PCB's.

## What it does *not* do

- It does **not** save/restore register state — that is [[ContextSwitch|context switching]].
- It does **not** create or destroy processes — that is [[Fork|`fork`]] / [[Exit|`exit`]].
- It does **not** decide *what* I/O to perform — that is [[SystemCall|syscall]] handling.

The mechanism / policy split is the load-bearing abstraction: a kernel can swap *policies* without changing the *mechanism*.

## Pedagogical scope in DIS

[[dis-13-2-processes|DIS 13.2]] explicitly **defers** scheduling-policy detail to an operating-systems textbook — the chapter establishes that the scheduler exists, what its inputs are ([[ProcessState|process states]]), and what its output is (a [[ContextSwitch|context switch]]). The reader leaves Ch 13.2 understanding *that* policy and mechanism are separable, not which specific policies modern Linux uses.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[ProcessScheduling]] — the policy catalog the scheduler implements.
- [[ContextSwitch]] — the mechanism the scheduler triggers.
- [[ProcessState]] — Ready is the scheduler's candidate set.
- [[ProcessControlBlock]] — what the scheduler reads/writes.
- [[Timesharing]] — the quantum-bounded shape of scheduler-driven preemption.
- [[Multiprogramming]] — the precondition that makes scheduling necessary.
- [[Process]] — the entity scheduled.
- [[OperatingSystem]] / [[Kernel]].
