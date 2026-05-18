---
title: "Latency Hiding"
type: concept
tags: [parallel-computing, performance, gpu]
sources: [parproc-ch02-recurring-performance-issues, parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Latency Hiding

A general technique for **dealing with long [[Latency|latencies]] you can't reduce**: do the long-latency operation *in parallel with something else*. While one access is in flight, useful work proceeds on data from earlier accesses that have now arrived.

## Canonical example: the GPU memory hierarchy

[[parproc-ch02-recurring-performance-issues]] §2.5:

> *"For example, GPUs tend to have very long memory access times, but this is solved by having many pending memory accesses at the same time. During the latency of some accesses, earlier ones that have now completed can now be acted upon."*

[[GPU|GPUs]] are designed around this idea — each streaming multiprocessor maintains many in-flight warps, and the scheduler swaps to a runnable warp the instant the current one hits a memory stall. The aggregate effect is that DRAM latency, which is hundreds of cycles, can be amortized down to near zero of *idle* time per SM.

## Other instances of the same idea

| Setting | "Long latency" | "Something else" |
|---|---|---|
| Out-of-order CPU | Cache miss to DRAM | Independent instructions further down the pipeline |
| Pipelined I/O | Disk read | Compute on previously-read blocks |
| MPI non-blocking | `MPI_Isend` / `MPI_Irecv` | Local work between post and wait |
| Software prefetching | `prefetch(addr)` | Compute on previously-fetched cache lines |

The pattern is always the same: turn a sequential *wait-then-use* into a *post-then-compute-then-collect*.

## Connections

- [[Latency]] — the cost being hidden.
- [[Bandwidth]] — orthogonal — hiding doesn't help with saturated channels.
- [[GPU]] — the chapter's exemplar of aggressive latency hiding.
- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.5.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.2.3 / §5.4.3.2 detail the CUDA implementation: the SM is *"an OS in hardware"* that schedules warps in fixed timeslices and swaps to another warp the moment one stalls on [[GlobalMemory|global memory]]. *"Each warp has its own set of registers, so a context switch does very little saving and restoring of context."* This is why CUDA programmers prefer **many small threads** — more in-flight warps = more latency to hide behind.
- [[Warp]] — the unit GPU latency hiding operates on.
- [[CUDA]] — programming model exposing the design pattern.
