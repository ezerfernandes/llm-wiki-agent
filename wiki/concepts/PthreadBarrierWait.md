---
title: "pthread_barrier_wait"
type: concept
tags: [pthreads, synchronization, barrier, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_barrier_wait

[[Pthreads]] [[Barrier|barrier]] rendezvous: `pthread_barrier_wait(pthread_barrier_t *barr)` ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). First `N-1` callers (where `N` was passed to [[PthreadBarrierInit|`pthread_barrier_init`]]) block; the `N`-th caller releases all blocked threads. The barrier then auto-resets and can be re-used.

Use case: phase-separator — all threads must finish phase *k* before any starts phase *k+1*. DIS's worked example uses a barrier so all threads print startup messages before any begins array processing.

## Connections

- [[Barrier]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadBarrierInit]] — must be called first.
- [[PthreadBarrierDestroy]] — the teardown.
- [[ConditionVariable]] — the lower-level primitive barriers can be built from.
- [[TreeBarrier]] / [[ButterflyBarrier]] — parallelized barrier-implementation variants ([[parproc-ch03-shared-memory-parallelism]]).
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
