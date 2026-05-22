---
title: "pthread_barrier_init"
type: concept
tags: [pthreads, synchronization, barrier, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_barrier_init

[[Pthreads]] [[Barrier|barrier]] initialization: `pthread_barrier_init(pthread_barrier_t *barr, const pthread_barrierattr_t *attr, unsigned count)` ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). The third parameter `count` is the number of threads that must reach the [[PthreadBarrierWait|`pthread_barrier_wait`]] before any are released.

```c
pthread_barrier_t barr;
pthread_barrier_init(&barr, NULL, N);   // N threads required
```

## Connections

- [[Barrier]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadBarrierWait]] / [[PthreadBarrierDestroy]] — the rest of the three-function lifecycle.
- [[Synchronization]] — umbrella.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
