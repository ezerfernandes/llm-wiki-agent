---
title: "Wall Time"
type: concept
tags: [operating-systems, performance, benchmarking, measurement]
sources: [dis-13-2-processes]
last_updated: 2026-05-17
---

# Wall Time

**Wall time** (or **wall-clock time**) is the **total elapsed real-world duration** between a [[Process|process]] starting and finishing — *"affected by concurrent processes"* ([[dis-13-2-processes|DIS Ch 13.2]]). It counts every [[ProcessState|state]] the process inhabits: Running **plus** Blocked **plus** Ready.

## Contrast with CPU time

| | Counts | Affected by other processes? |
|---|---|---|
| **Wall time** | Running + Blocked + Ready | **Yes** — competing CPU users delay you. |
| **[[CPUTime|CPU time]]** | Running **only** | **No** — only your own CPU work. |

A process that spends 5 seconds waiting on disk + 1 second computing reports **6 s wall time** and **1 s CPU time**. On a busy system the wall time grows further (more Ready waiting) without changing the CPU time.

## Why both clocks matter

- **Users care about wall time** — how long until the program is *done*.
- **Optimizers care about [[CPUTime|CPU time]]** — how much actual computation is happening.
- **[[Benchmarking|Benchmarks]] use both** — wall time on a quiet machine approximates CPU time but is honest about I/O; on a busy [[Multiprogramming|multiprogrammed]] system the two diverge.

POSIX exposes both: `gettimeofday` / `clock_gettime(CLOCK_REALTIME)` gives wall time; `clock()` / `getrusage` / `clock_gettime(CLOCK_PROCESS_CPUTIME_ID)` give CPU time.

## Connections

- [[dis-13-2-processes]] — primary source.
- [[CPUTime]] — the complementary clock.
- [[Process]] / [[ProcessState]] — wall time spans all states.
- [[Multiprogramming]] / [[Timesharing]] — the reason wall and CPU time diverge.
- [[Benchmarking]] — the application that consumes both clocks.
