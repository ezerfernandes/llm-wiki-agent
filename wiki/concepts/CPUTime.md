---
title: "CPU Time"
type: concept
tags: [operating-systems, performance, benchmarking, measurement]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# CPU Time

**CPU time** (or **process time**) is the duration a [[Process|process]] **actually held a CPU** — counting only its [[ProcessState|Running]] state, not Blocked or Ready waiting. *"Unaffected by other processes running concurrently"* ([[dis-13-2-processes|DIS Ch 13.2]]).

## Contrast with wall time

| | Counts | Affected by other processes? |
|---|---|---|
| [[WallTime|Wall time]] | Running + Blocked + Ready | **Yes** — disk + competing users delay you. |
| **CPU time** | Running **only** | **No** — your CPU work alone. |

A program with 1 second of computation on a busy server might report **1 s CPU time** but **30 s [[WallTime|wall time]]** — most of the wait is in the Ready queue or blocked on I/O. The CPU-time number is stable; the wall-time number depends on the rest of the system.

## Multicore subtlety

On a parallel program, CPU time can **exceed** wall time — if four cores work for 1 second each on the same process, CPU time = 4 s, wall time = 1 s. The ratio is a [[ParallelSpeedup|speedup]] proxy.

## How it is measured

- POSIX `clock()` — CPU ticks since program start (`CLOCKS_PER_SEC` units).
- POSIX `clock_gettime(CLOCK_PROCESS_CPUTIME_ID, ...)` — finer resolution.
- POSIX `getrusage` — splits CPU time into **user** (process code) and **system** (kernel code on the process's behalf).
- `time` shell utility — reports `real` (wall) + `user` + `sys` (the latter two summing to CPU time).

## When to prefer it

- **Optimization work** — the only honest number for "did I make the algorithm faster?" when other processes are running.
- **Cross-machine comparison** — wall time mixes in system load; CPU time isolates per-machine compute cost.
- **CPU-cost-based billing** — cloud providers historically billed by CPU-seconds, not wall-seconds, for shared-CPU instances.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[WallTime]] — the complementary clock.
- [[Process]] / [[ProcessState]] — CPU time corresponds to time spent Running.
- [[Multiprogramming]] / [[Timesharing]] — the reason CPU time and wall time diverge.
- [[Benchmarking]] / [[Profiling]] — primary consumers of CPU time.
