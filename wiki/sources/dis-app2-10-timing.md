---
title: "Dive into Systems — App 2.10 Timing"
type: source
tags: [book, unix, shell, timing, performance]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/timing.html
---

## Summary
Tenth subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Introduces the [[TimeCommand|`time`]] command for measuring program execution. Codifies the three time metrics — **real** (wall clock), **user** (CPU in user mode), **sys** (CPU in kernel mode) — and the discrepancy `user + sys ≠ real` caused by I/O blocking and OS scheduling.

## Key Claims
- [[TimeCommand|`time <cmd>`]] runs the command and prints elapsed timings.
- **real** = wall-clock elapsed time; **user** = CPU-time in [[UserMode|user mode]]; **sys** = CPU-time in [[KernelMode|kernel/system mode]].
- *"user time plus the sys time do not add up to real time"* — processes block on I/O or get descheduled.
- CPU-bound programs show `user + sys ≈ real`; I/O-bound programs show `user + sys ≪ real`.
- `time -p` enables POSIX-standard output for cross-platform automation.

## Connections
- [[TimeCommand]] — minted here.
- [[WallClockTime]] / [[CPUTime]] — the real-vs-user distinction codified in [[dis-14-1-multicore|Ch 14.1]] reappears here at the shell level.
- [[UserMode]] / [[KernelMode]] — the user/sys split.
- [[Profiling]] — `time` is the simplest profiling tool, complementing [[Callgrind]]/[[Massif]] from Ch 12.
- [[DiveIntoSystems]] — Appendix 2.10.
