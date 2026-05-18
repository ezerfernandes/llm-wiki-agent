---
title: "Hardware Multithreading"
type: concept
tags: [computer-architecture, cpu, parallelism, multithreading]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Hardware Multithreading

**Hardware multithreading** is a CPU-design technique in which **a single processor core supports multiple independent execution streams** — multiple architectural register sets, program counters, and thread-state — so it can switch between threads (or run them concurrently) without OS-mediated context-switch overhead. [[dis-5-9-modern|Ch 5.9]] introduces it as one of the two post-[[PowerWall|power-wall]] scaling responses (alongside [[MulticoreProcessor|multicore]]).

## Two variants (Ch 5.9)

| Variant | When threads run | Pipelines / ALUs | Max IPC | Example |
|---|---|---|---|---|
| **Interleaved multithreading** | One thread per cycle, alternating | Shared between threads | **1** | Intel **[[HyperThreading|Hyper-Threading]]** (per Ch 5.9's classification) |
| **[[SimultaneousMultithreading|Simultaneous multithreading (SMT)]]** | **Multiple threads in the same cycle** | Replicated ([[Superscalar|superscalar]] issue) | **> 1** | IBM Power 9 (8-way SMT) |

The key distinction: interleaved multithreading **shares** execution resources cycle-by-cycle, while SMT **co-issues** instructions from different threads in parallel via [[Superscalar|superscalar]] hardware.

## Why it exists

Hardware multithreading hides latency (cache misses, long-latency ops) by switching to a ready thread instead of stalling. With [[Superscalar|superscalar]] cores in particular, idle issue slots in one thread's instruction stream can be filled with another thread's ready instructions — converting dependency-induced bubbles into useful work (the [[SimultaneousMultithreading|SMT]] argument).

## Connections

- [[SimultaneousMultithreading]] — the throughput-maximizing variant.
- [[HyperThreading]] — Intel's interleaved-multithreading product (per Ch 5.9, not true SMT).
- [[Superscalar]] — the hardware substrate SMT relies on.
- [[MulticoreProcessor]] — the *between-core* parallelism HW multithreading complements *within-core*.
- [[PowerWall]] — the constraint that motivated this layer of parallelism.
- [[CPU]] — the device class.
- [[OperatingSystem]] — the layer that schedules software threads onto hardware threads.
- [[dis-5-9-modern]] — primary source.
