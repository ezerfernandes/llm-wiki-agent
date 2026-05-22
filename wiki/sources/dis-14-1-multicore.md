---
title: "Dive into Systems — Ch 14.1 Programming Multicore Systems"
type: source
tags: [textbook, systems, multicore, parallelism, threads, shared-memory]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/multicore.html
---

# Dive into Systems — Ch 14.1 Programming Multicore Systems

## Summary

**Opening leaf of Ch 14 *Leveraging Shared Memory in the Multicore Era*** from [[DiveIntoSystems]]. Section 14.1 motivates explicit parallel programming as the **mandatory** response to the post-[[PowerWall|power-wall]] [[MulticoreProcessor|multicore]] reality that [[dis-5-9-modern|Ch 5.9]] foreshadowed: because "most major programming languages predate the multicore era," they cannot automatically exploit extra cores, so the programmer must reach for [[Thread|threads]] to convert hardware parallelism into single-process [[Speedup|speedup]]. The section is split across two subsections — **14.1.1 *The Impact of Multicore Systems on Process Execution*** (multicore raises **[[Throughput|throughput]]** of many concurrent processes but not the CPU time of any one process) and **14.1.2 *Expediting Process Execution with Threads*** (threads as the lightweight shared-address-space sibling of processes that *can* split one program's work across cores), with an *Example: Scalar Multiplication* worked example showing the **1/c speedup approximation** when thread count `t` matches core count `c`.

## Key Claims

- **Programming-language inertia is the headline problem**: "most major programming languages were created prior to the multicore era and were not designed with multicore systems in mind. Consequently, none of these languages can take full advantage of multicore systems automatically."
- **Concurrency vs parallelism distinction**: [[ConcurrencyVsParallelism|*concurrency*]] is the appearance of simultaneous execution via [[ContextSwitch|context-switch]] interleaving on a single core, while *parallel execution* is the **simultaneous execution of instructions from processes running on multiple cores** — and *"the simultaneous execution of instructions from processes running on multiple cores is referred to as parallel execution."*
- **CPU time vs wall-clock time**: CPU time is on-processor execution duration; wall-clock time is user-perceived elapsed time, which on a single core balloons because of context switches between concurrent processes. Multicore execution shrinks **wall-clock time** for a batch of processes without shrinking any single process's **CPU time**.
- **Multicore raises throughput, not single-process speed (by itself)**: *"a multicore processor increases the throughput of process execution, or the number of processes that can complete in a given period of time."* Single-process speedup requires the programmer to opt in to threads.
- **Threads are the in-process speedup mechanism**: [[Thread|threads]] are "lightweight, independent execution flows" that share program data, instructions, and heap with their parent [[Process|process]] but maintain separate call stacks — making them schedulable onto separate cores in parallel.
- **Linear-speedup approximation rule**: *"in general, if the number of threads matches the number of cores (c) and the operating system schedules each thread to run on a separate core in parallel, then the multithreaded process should run in approximately 1/c of the time."* Resource contention prevents reaching the ideal in practice.

## Key Quotes

> "The simultaneous execution of instructions from processes running on multiple cores is referred to as parallel execution." — 14.1.1, defining parallel execution as distinct from single-core concurrency.

> "A multicore processor increases the throughput of process execution, or the number of processes that can complete in a given period of time." — 14.1.1, the throughput-not-latency framing of multicore's default win.

> "In general, if the number of threads matches the number of cores (c) and the operating system schedules each thread to run on a separate core in parallel, then the multithreaded process should run in approximately 1/c of the time." — 14.1.2, the linear-speedup approximation under thread-count-equals-core-count.

## Connections

- [[DiveIntoSystems]] — parent book; 127th ingested chapter, opens Ch 14.
- [[MulticoreProcessor]] — the hardware substrate the chapter is about; already named in [[dis-0-introduction|Ch 0]] and [[dis-5-9-modern|Ch 5.9]].
- [[ParallelComputing]] — the programming paradigm multicore makes mandatory.
- [[ParallelExecution]] — the formal definition Ch 14.1 supplies (multi-core simultaneity, contrasted against single-core concurrency).
- [[SharedMemoryParallelism]] — the chapter-level paradigm Ch 14 will develop on top of 14.1's motivation.
- [[ConcurrencyVsParallelism]] — the conceptual split Ch 14.1.1 codifies.
- [[Speedup]] — the **1/c approximation** Ch 14.1.2 supplies (Amdahl's Law itself is **not** covered here — deferred).
- [[Thread]] — the in-process unit of execution Ch 14.1.2 introduces; was already in the wiki via [[parproc-ch01-intro-parallel-processing]] / [[dis-3-6-gdb-pthreads|Ch 3.6]] but DIS Ch 14.1 is the first DIS-side **first-class** treatment.
- [[Process]] — the surrounding OS abstraction (from [[dis-13-2-processes|Ch 13.2]]) — threads are *"lightweight execution flows"* inside one process.
- [[ContextSwitch]] — the single-core mechanism behind concurrency; from [[dis-13-2-processes|Ch 13.2]].
- [[Throughput]] — the metric multicore raises by default (process-count / time).
- [[Pthreads]] — the concrete API Ch 14 will operationalize (named in Ch 3.6 / Ch 13.4.3 forward references).
- [[PowerWall]] — the architectural fork ([[dis-5-9-modern|Ch 5.9]]) that ended single-thread free-lunch and forced this chapter's existence.
- [[InstructionLevelParallelism]] — the alternative hardware-side parallelism that single-thread programs *do* get for free; multicore parallelism is the explicit-programmer alternative.

## Contradictions

None. Ch 14.1 cleanly extends [[dis-5-9-modern|Ch 5.9]]'s architectural framing (multicore as the post-power-wall pivot) and [[dis-13-2-processes|Ch 13.2]]'s process/context-switch vocabulary into the programmer-facing parallel-programming surface, and is consistent with [[parproc-ch01-intro-parallel-processing]]'s thread definition (the *"lightweight, independent execution flows"* phrasing aligns with Matloff's *"similar to a process in an operating system, but with much less overhead"*).

## Scope notes

- **Amdahl's Law is NOT covered** in 14.1 — neither the formula nor the term appears. The chapter supplies only the informal *1/c approximation* under best-case thread-count-matches-core-count scheduling, and verbally notes that *"resource contention prevents ideal speedup in practice."* Formal serial-vs-parallel-fraction analysis is deferred (presumably to a later Ch 14 section).
- **Synchronization machinery** ([[Mutex|mutexes]], [[Semaphore|semaphores]], [[Barrier|barriers]], [[CriticalSection|critical sections]]) is not introduced here — Ch 14.1 is pure motivation + thread-level *what*, with the *how* deferred to subsequent Ch 14 sections.
- **No code** is shown — the *Scalar Multiplication* example is described qualitatively as a candidate workload for the 1/c speedup approximation, not via a `pthread_create` listing.
