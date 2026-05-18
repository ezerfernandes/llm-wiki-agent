---
title: "OS in Hardware (CUDA)"
type: concept
tags: [gpu, cuda, scheduling, latency-hiding]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# OS in Hardware (CUDA)

Matloff's coinage for the [[StreamingMultiprocessor|SM]]'s warp scheduler ([[parproc-ch05-cuda-gpu-programming]] §5.4.2.3). Each SM time-shares its [[StreamingProcessor|SPs]] among in-flight [[Warp|warps]] in fixed-length timeslices — *"just like an operating system (OS). This time-sharing is implemented in the hardware, though, not in software as in the OS case."*

## The OS analogy, point by point

| Ordinary OS | SM "hardware OS" |
|---|---|
| Processes take turns on the CPU in fixed timeslices | Warps take turns on the SP cluster in fixed timeslices |
| OS suspends an I/O-blocked process, runs another | SM suspends a memory-stalled warp, schedules another ready warp |
| Context switch saves/restores process registers to memory | Context switch nearly free — each warp has its own physical register set |
| Goal: overlap I/O with compute on a single CPU | Goal: overlap [[GlobalMemory|global-memory]] latency with compute on a single SM |

## Why it works at fine grain

The crucial point — the structural reason CUDA's "OS" is more aggressive than a software OS — is *"each warp has its own set of registers, so a context switch does very little saving and restoring of context, quite a contrast to the OS case."* Software OS context switches are expensive (save FPU, registers, page tables, flush TLB), so they only pay off when the blocked-process I/O latency is *very* long. The SM's nearly-free warp switch lets it hide *every* memory access.

## The granularity consequence

Because the SM hides latency by **finding another runnable warp**, CUDA programmers want **many warps per SM** — which means **small per-thread workloads** and **lots of threads**. *"CUDA programmers typically employ a large number of threads, each of which does only a small amount of work — again, quite a contrast to something like OpenMP, where coarser granularity is generally needed."*

This is the headline difference between Matloff's Ch4 ([[OpenMP]], coarse threads, ~4 of them) and Ch5 (CUDA, fine threads, thousands).

## See also

- [[Warp]] — the scheduling unit.
- [[StreamingMultiprocessor]] — the hardware "OS."
- [[LatencyHiding]] — the general technique this implements.
- [[SIMT]] — the execution model that pairs with warp-level scheduling.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.2.3.
