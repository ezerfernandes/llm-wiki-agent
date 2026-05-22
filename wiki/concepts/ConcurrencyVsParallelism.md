---
title: "Concurrency vs Parallelism"
type: concept
tags: [parallel-computing, concurrency, multicore, os, scheduling]
sources: [dis-14-1-multicore]
last_updated: 2026-05-18
---

# Concurrency vs Parallelism

A foundational distinction that [[DiveIntoSystems]] [[dis-14-1-multicore|Ch 14.1.1]] codifies as the **programmer-facing payoff** of the [[MulticoreProcessor|multicore]] era. The two terms are routinely conflated in casual speech, but they refer to different phenomena observable at different hardware widths.

## The two definitions

**Concurrency** — *the appearance of simultaneous execution* produced by [[ContextSwitch|context-switch]] interleaving on a **single core**. [[dis-14-1-multicore|Ch 14.1.1]]: concurrency "occurs when the total execution time of one process overlaps with another," giving the **illusion** of parallelism even though only one instruction stream is physically advancing at any instant.

**Parallel execution** — *literally simultaneous execution* of instructions from **multiple processes (or threads) on multiple cores**. [[dis-14-1-multicore|Ch 14.1.1]], verbatim: *"the simultaneous execution of instructions from processes running on multiple cores is referred to as parallel execution."*

The split is purely a property of **how many cores are physically advancing instruction streams at the same wall-clock instant** — one (concurrency only) vs more than one (parallel execution).

## Worked contrast

Picture two CPU-bound processes P1 and P2, each needing 10 ms of [[CPU|CPU]] work:

| Hardware | Behavior | Wall-clock total |
|---|---|---|
| **1 core** | OS time-slices P1/P2 — each gets bursts of execution separated by [[ContextSwitch|context switches]]. Both *appear* to be running. **Concurrent**, not parallel. | ~20 ms + context-switch overhead |
| **2 cores** | OS schedules P1 on core 0, P2 on core 1. Both physically execute simultaneously. **Parallel execution.** | ~10 ms |

The two-core case **also** counts as concurrent — parallelism is the strictly stronger condition. Every parallel execution is concurrent, but not every concurrent execution is parallel.

## CPU time vs wall-clock time

A corollary the chapter makes explicit:

- **[[CPUTime|CPU time]]** — duration actually spent advancing on a processor.
- **[[WallClockTime|Wall-clock time]]** — elapsed time the user perceives.

On a single core, wall-clock time exceeds CPU time because of context-switch interleaving. Adding more cores **does not shrink any one process's CPU time** — it shrinks the wall-clock total by letting processes execute in parallel rather than time-sliced. This is why multicore raises [[Throughput|throughput]] (process-count / time) by default but only delivers single-process [[Speedup|speedup]] when the programmer opts in via [[Thread|threads]].

## Why the distinction matters

1. **Hardware purchase decisions** — a single-core machine running 8 concurrent threads gets no parallelism benefit; the OS just time-slices them. Concurrency is "free" (the OS schedules it); parallelism requires actual core count.
2. **Programming-language design** — concurrency primitives ([[Coroutine|coroutines]], async/await, the JavaScript event loop) provide concurrent execution **without** parallel execution (single thread). Adding parallelism requires worker pools, [[Thread|threads]], or multiprocess setups.
3. **Performance reasoning** — naively counting "I have 8 threads" doesn't predict speedup. The OS / runtime must actually map them to distinct cores; if they're all bound to one, you have concurrency without parallelism and zero speedup.

## Languages that conflate the two (and one that doesn't)

- **Python** — the GIL means `threading` gives concurrency but not parallelism for CPU-bound code; `multiprocessing` is the parallel escape hatch.
- **JavaScript** — single-threaded event loop is pure concurrency; Web Workers / Node `worker_threads` add parallelism.
- **Go** — goroutines are scheduled across an *M*:*N* threadpool, so the runtime delivers parallelism on multicore by default.
- **C with [[Pthreads]]** — threads map ~1:1 to OS threads, so parallelism on multicore is the default outcome — the model [[DiveIntoSystems]] Ch 14 develops.

## Connections

- [[ContextSwitch]] — the mechanism producing concurrency on a single core.
- [[MulticoreProcessor]] — the hardware that enables parallelism.
- [[Thread]] / [[Process]] — the schedulable units.
- [[Throughput]] — what multicore raises *without* requiring programmer effort.
- [[Speedup]] — what programmer-side threading converts hardware parallelism into.
- [[ParallelExecution]] — the formal name [[dis-14-1-multicore|Ch 14.1.1]] gives the parallel half.
- [[SharedMemoryParallelism]] — the paradigm Ch 14 develops on top of parallel execution.
- [[dis-14-1-multicore]] — DIS source.
- [[dis-13-2-processes]] — supplies the [[ContextSwitch]] / [[Process]] / [[CPUTime]] vocabulary 14.1 reuses.
