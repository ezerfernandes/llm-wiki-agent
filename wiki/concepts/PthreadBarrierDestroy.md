---
title: "pthread_barrier_destroy"
type: concept
tags: [pthreads, synchronization, barrier, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_barrier_destroy

[[Pthreads]] [[Barrier|barrier]] teardown: `pthread_barrier_destroy(pthread_barrier_t *barr)` ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). Frees resources associated with the barrier. Destroying a barrier on which threads currently wait is undefined behaviour — call after all phases requiring the barrier have completed and all threads have been [[PthreadJoin|joined]].

## Connections

- [[Barrier]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadBarrierInit]] / [[PthreadBarrierWait]] — lifecycle counterparts.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
