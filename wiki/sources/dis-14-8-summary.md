---
title: "Dive into Systems — Ch 14.8 Summary"
type: source
tags: [dive-into-systems, textbook, parallel-programming, summary]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/summary.html
---

## Summary

**Eighth leaf** of Ch 14 *Leveraging Shared Memory in the Multicore Era* of *[[DiveIntoSystems]]* — prose-close that recaps the chapter's arc from [[dis-14-1-multicore|14.1's]] motivation through [[dis-14-7-openmp|14.7's]] implicit-threading payoff. Four structural commitments:

1. **[[Thread|Threads]] are the fundamental concurrency unit**: lightweight, shared-address-space siblings of [[Process|processes]] that let one program span [[MulticoreProcessor|multiple cores]]. Each maintains its **own [[Stack|stack]] and registers** while **sharing program data, [[Heap|heap]], and instructions** with the parent process — the structural rule [[dis-14-1-multicore|14.1.2]] introduced.
2. **[[Synchronization]] is necessary but not sufficient**: [[RaceCondition|race conditions]] and [[DataRace|data races]] emerge whenever multiple threads access shared memory without coordination; primitives ([[Mutex|mutexes]], [[Semaphore|semaphores]], [[Barrier|barriers]], [[ConditionVariable|condition variables]]) make [[CriticalSection|critical sections]] atomic — but introduce their own serialization costs.
3. **Synchronization creates [[ParallelSpeedup|performance]] trade-offs**: oversized [[CriticalSection|critical sections]] serialize execution and erase parallelism gains; [[Deadlock|deadlock]] can occur when threads acquire interdependent locks in conflicting orders. The pragmatic discipline: minimize lock scope, prefer [[dis-14-3-1-mutex|local accumulator]] patterns.
4. **Parallelism has inherent limits**: not all work parallelizes — [[AmdahlsLaw|Amdahl's Law]] caps speedup at $1/S$, [[CacheCoherency|cache coherence]] and [[FalseSharing|false sharing]] tax shared writes, [[ThreadSafety|library functions]] may not be safe. Linear scaling is the exception, not the rule.

## Key Claims

- *"Threads are the fundamental unit of concurrent programs."*
- *"Synchronization constructs ensure that programs work correctly."*
- *"Be mindful when using synchronization constructs."*
- *"Not all components of a program are parallelizable."*

## Connections

- [[DiveIntoSystems]] — parent textbook; **eighth leaf** of Ch 14 *Leveraging Shared Memory in the Multicore Era* — the prose summary that recaps Ch 14's arc.
- [[dis-14-1-multicore]] / [[dis-14-2-posix]] / [[dis-14-3-synchronization]] / [[dis-14-4-performance]] / [[dis-14-5-cache-coherence]] / [[dis-14-6-thread-safety]] / [[dis-14-7-openmp]] — the seven preceding leaves the summary recaps.
- [[Thread]] / [[Synchronization]] / [[CriticalSection]] / [[RaceCondition]] / [[DataRace]] — the core concept vocabulary the chapter codified.
- [[Mutex]] / [[Semaphore]] / [[Barrier]] / [[ConditionVariable]] — the four primitives Ch 14.3 introduced.
- [[AmdahlsLaw]] / [[ParallelSpeedup]] / [[ParallelEfficiency]] — the performance theory from Ch 14.4.
- [[CacheCoherency]] / [[FalseSharing]] — the hardware pathologies from Ch 14.5.
- [[ThreadSafety]] / [[Reentrant]] — the library-function discipline from Ch 14.6.
- [[OpenMP]] — the implicit-threading payoff from Ch 14.7.
- Sibling summary leaves: [[dis-12-4-summary]] / [[dis-13-5-summary-advanced]] / [[dis-11-7-summary]] — the *summary closes chapter* pattern (though Ch 14 has an exercises leaf 14.9 still to come).

## Contradictions

- None — pure recap.

## Notes

- **139th ingested DIS chapter — penultimate Ch 14 leaf.** **No new concept pages** — pure summary of pages already minted by 14.1–14.7.
