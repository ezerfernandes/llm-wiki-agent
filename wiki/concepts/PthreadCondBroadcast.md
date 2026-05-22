---
title: "pthread_cond_broadcast"
type: concept
tags: [pthreads, synchronization, condition-variable, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_cond_broadcast

[[Pthreads]] [[ConditionVariable|condition variable]] wake-all: `pthread_cond_broadcast(pthread_cond_t *cond)` ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). Wakes **all** waiters blocked in [[PthreadCondWait|`pthread_cond_wait(&cond, &mutex)`]]. Each woken waiter re-acquires the mutex one at a time (serialized) and re-checks its predicate.

Use when: (a) the state change can satisfy multiple waiters, (b) waiters wait on different predicates over the same condition variable, or (c) implementing a phase-release semantic where all waiters should re-check.

## Connections

- [[ConditionVariable]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadCondSignal]] — the wake-one alternative.
- [[PthreadCondWait]] — the waiter side.
- [[Barrier]] — barriers can be built from `pthread_cond_broadcast` on the predicate "all threads have arrived".
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
