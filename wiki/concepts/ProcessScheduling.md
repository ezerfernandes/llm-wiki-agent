---
title: "Process Scheduling"
type: concept
tags: [operating-systems, scheduling, policy]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Process Scheduling

**Process scheduling** is the **policy** of selecting which [[ProcessState|Ready]] [[Process|process]] gets the CPU next and for how long. It is implemented by the [[Scheduler|scheduler]] and enforced by [[ContextSwitch|context switching]] + the [[Timesharing|quantum timer]].

## Inputs

- The **set of [[ProcessState|Ready]] processes** ([[ProcessControlBlock|PCBs]] tagged `READY`).
- Per-process attributes — priority, age, CPU-vs-I/O burstiness, niceness, real-time class.
- System-wide goals — throughput, latency, fairness, energy.

## Outputs

- The next [[Process|process]] to run.
- Its [[Timesharing|time-slice]] / quantum length.
- Whether to **preempt** the currently running process or let it finish its quantum.

## Why policy is separable from mechanism

[[dis-13-2-processes|DIS Ch 13.2]] makes the mechanism / policy split explicit: [[ContextSwitch|context switching]] is *how* the OS swaps processes; **process scheduling** is *which* and *when*. The same context-switch machinery serves any policy — round-robin, priority-based, multilevel feedback queue, completely-fair scheduler (Linux CFS), real-time deadlines, etc. — without modification.

This is a load-bearing kernel-design abstraction: the kernel can swap schedulers (Linux has historically had several) without rewriting the register-save / register-restore primitive.

## Pedagogical scope in DIS

[[dis-13-2-processes|DIS 13.2]] explicitly leaves the **specific policies** to a dedicated operating-systems textbook. Ch 13.2's job is to establish:

- That a [[Scheduler|scheduler]] exists.
- That it consumes [[ProcessState|process states]] and produces [[ContextSwitch|context switches]].
- That only [[ProcessState|Ready]] processes are candidates ([[ProcessState|Blocked]] processes are skipped until their event fires).
- That [[Multiprogramming|multiprogramming]] (switch on I/O blocks) and [[Timesharing|timesharing]] (switch on quantum expiry) are the two complementary triggers.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[Scheduler]] — the OS component that implements process scheduling.
- [[ContextSwitch]] — the mechanism the scheduler dispatches.
- [[ProcessState]] — input attribute (only Ready processes are scheduled).
- [[Timesharing]] — the quantum-driven preemption trigger.
- [[Multiprogramming]] — the I/O-block-driven switch trigger.
- [[Process]] / [[ProcessControlBlock]].
- [[OperatingSystem]] / [[Kernel]].
