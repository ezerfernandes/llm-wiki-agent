---
title: "Barrier (synchronization)"
type: concept
tags: [parallel-computing, concurrency, synchronization, pthreads]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch03-shared-memory-parallelism, dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# Barrier

Synchronization primitive: "a point in the code that all threads must reach before continuing." [[parproc-ch01-intro-parallel-processing]] introduces the barrier in the context of the prime-sieve example to prevent premature counting of results — "which would result in possibly wrong output if we start counting primes before some threads are done."

Concrete API forms surveyed by the chapter:
- **[[Pthreads]]**: declare `pthread_barrier_t barr;` then call `pthread_barrier_wait(&barr);` from each thread.
- **`pthread_join` over all workers** is a *degenerate* barrier — the chapter notes "the `pthread_join()` function actually causes the given thread to exit, so that we then 'join' the thread that created it, i.e. `main()`. Thus some may argue that this is not really a true barrier."
- **[[OpenMP]] explicit**: `#pragma omp barrier`.
- **OpenMP implicit**: `#pragma omp single` has an implied barrier at the end of its block.
- **[[Rdsm]]**: `barr()` — used to ensure all rthreads have written before one designated thread does wrap-up (e.g. `which.max` in the time-series maximal-burst example).

The chapter promises more detailed treatment of barriers in chapter 3. The repeated theme: barriers are crucial for correctness whenever subsequent computation reads values that earlier-phase threads may still be writing.

## Ch3 follow-up: implementations and parallelization

[[parproc-ch03-shared-memory-parallelism|Ch3]] §3.12 delivers the deferred treatment. *"Implementing a barrier in a fully correct manner is actually a bit tricky."* Three iterations:

- **Use-once version** (§3.12.1): single `Count` + mutex + spin. Works for one call, breaks on reset.
- **Naïve reusable** (§3.12.2): one-counter-with-reset. **Race condition**: a fast processor can race ahead, increment `Count` for iteration 2 *before* a slow processor resets it from iteration 1.
- **Correct reusable** (§3.12.3): **two `Count[2]` counters with an alternating `EvenOdd` parity bit**. The fast processor increments a different counter than the slow processor resets — race resolved.
- **Refinement** (§3.12.4.1): use `pthread_cond_wait` / `pthread_cond_broadcast` to swap busy-spin for a blocking wait; the OS deschedules waiting threads, freeing the CPU for other work.

Parallelization of the barrier itself (§3.12.4.2):

- **[[TreeBarrier]]**: $\log_2 n$ levels of nested sub-barriers, reducing serial fan-in.
- **[[ButterflyBarrier]]**: each node bit-flip-handshakes with a $\log_2 n$-partner schedule; *"a butterfly exchange amounts to a number of simultaneously tree operations."*

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces barriers across Pthreads / OpenMP / Rdsm.
- [[parproc-ch03-shared-memory-parallelism]] — §3.12 delivers the correct-implementation walkthrough plus tree/butterfly parallelizations.
- [[Pthreads]] — `pthread_barrier_wait`, `pthread_cond_wait`, `pthread_cond_broadcast`.
- [[OpenMP]] — `#pragma omp barrier` + the implicit barrier at end of `single`.
- [[Rdsm]] — `barr()`.
- [[TreeBarrier]] — Ch3 §3.12.4.2.1.
- [[ButterflyBarrier]] — Ch3 §3.12.4.2.2.
- [[JIAJIA]] — `jia_barrier()` is the SDSM API.
- [[CriticalSection]] — the other dominant shared-memory synchronization primitive.
- [[Thread]] — the entity barriers coordinate.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3; *"forces all threads to reach a common execution point before proceeding concurrently."* Three-function Pthreads API: [[PthreadBarrierInit|`pthread_barrier_init(&barr, NULL, N)`]] (where `N` is the thread count required to release), [[PthreadBarrierWait|`pthread_barrier_wait(&barr)`]] (the rendezvous — first `N-1` callers block, the `N`-th releases all), [[PthreadBarrierDestroy|`pthread_barrier_destroy(&barr)`]]. Worked example: a barrier prevents array processing until every thread prints its startup message — the canonical phase-separator use case.
- [[PthreadBarrierInit]] / [[PthreadBarrierWait]] / [[PthreadBarrierDestroy]] — per-call concept pages.
- [[ConditionVariable]] — alternative primitive for blocking until a predicate; barriers are syntactic sugar for a count-based predicate.
- [[Synchronization]] — umbrella.
