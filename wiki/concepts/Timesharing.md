---
title: "Timesharing"
type: concept
tags: [operating-systems, scheduling, concurrency, parallel-computing]
sources: [parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Timesharing

**Timesharing** is the OS mechanism by which multiple processes appear to run simultaneously on a single CPU by taking turns in rapid succession. Each process is given a short turn called a *quantum* or *timeslice* (typically 50–60 ms); when the quantum expires the OS suspends the current process and runs the next one. The rapid alternation creates the illusion of simultaneous execution.

## How it works

Quanta are enforced by a hardware timer, not by the OS itself — because the OS is not running while a user process runs. A timer device (e.g., the 8253 on x86 machines, interrupting 100 times per second) emits an interrupt at fixed intervals. The CPU, on receiving the interrupt, suspends the current process and jumps to the OS interrupt handler. The OS then decides whether to perform a [[ContextSwitch]].

A typical configuration: the 8253 fires every 10 ms; the OS performs a context switch every 6th interrupt, yielding 60 ms quanta. The quantum size is tunable by adjusting the interrupt count threshold.

A process' turn can also end early if it voluntarily yields the CPU — for example, by making a system call that blocks on I/O (e.g., `scanf()` / `cin`). The OS marks the process as *Sleep* and will return it to *Run* state when the awaited event (e.g., a keypress) occurs.

## Context switching

A [[ContextSwitch]] saves all register values of the outgoing process (including the Program Counter and EFLAGS register) and restores those of the incoming process. From the CPU's perspective, nothing special happens — it simply fetches and executes instructions from wherever the PC points.

## Multicore machines

On a multicore machine several processes can run truly in parallel (one per core), but the OS-managed turn-taking mechanism operates identically on each core. Each core runs its own timesharing schedule; the OS distributes processes across cores.

## Parallel programming implications

Timesharing is the reason that parallel benchmarks should be run with care: other processes on the same machine take CPU time away from the benchmark. For accurate wall-clock measurement, either run on a quiet machine or use process-binding/pinning tools (e.g., `taskset` on Linux) to restrict a process to specific cores. Also, threaded programs spawn multiple processes/threads that are each subject to timesharing, which can cause unexpected context-switch overhead under heavy system load.

## Connections

- [[parproc-appA-systems-issues]] — §A.1; primary source.
- [[ContextSwitch]] — the OS operation triggered at each quantum boundary.
- [[MemoryHierarchy]] — companion systems topic in the same appendix.
- [[LoadBalancing]] — parallel programming analogue: distributing work across processors, similar in spirit to the OS distributing processes across CPU quanta.
