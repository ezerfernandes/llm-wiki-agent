---
title: "time Command"
type: concept
tags: [unix, shell, timing, performance]
sources: [dis-app2-10-timing]
last_updated: 2026-05-18
---

# `time` Command

The Unix **`time`** command measures how long a program takes to run. Invoked as a prefix:

```bash
time ./my_program arg1 arg2
```

Outputs **three** metrics:

| Metric | Meaning |
|---|---|
| **real** | Wall-clock elapsed time from start to finish ([[WallClockTime]]). |
| **user** | [[CPUTime|CPU time]] spent in [[UserMode|user mode]]. |
| **sys** | [[CPUTime|CPU time]] spent in [[KernelMode|kernel/system mode]] (system calls). |

## Key insight (from [[dis-app2-10-timing|DIS App 2.10]])

*"user time plus the sys time do not add up to real time"* — the gap is time the process spent **blocked** on I/O or **descheduled** by the OS.

- **CPU-bound** workload: `user + sys ≈ real`.
- **I/O-bound** workload: `user + sys ≪ real`.

## Flags

- `time -p` — POSIX-standard output format for automation / cross-platform comparison.
- `/usr/bin/time -v` (GNU) — verbose mode with memory, context switches, etc.

## Connections

- [[WallClockTime]] / [[CPUTime]] — the real-vs-user/sys distinction.
- [[Profiling]] — the simplest profiler; [[Callgrind]] / [[Massif]] are the deeper tools (Ch 12).
- [[Benchmarking]] — `time` is the bottom-rung benchmark tool.
- [[UserMode]] / [[KernelMode]] — the user/sys split.
- [[dis-app2-10-timing]] — source.
