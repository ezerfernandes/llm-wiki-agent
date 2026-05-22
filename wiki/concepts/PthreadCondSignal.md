---
title: "pthread_cond_signal"
type: concept
tags: [pthreads, synchronization, condition-variable, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_cond_signal

[[Pthreads]] [[ConditionVariable|condition variable]] wake-one: `pthread_cond_signal(pthread_cond_t *cond)`. Wakes exactly **one** waiter blocked in [[PthreadCondWait|`pthread_cond_wait(&cond, &mutex)`]] (scheduler-chosen). Returns immediately even if no waiters exist — signals are not queued.

```c
pthread_mutex_lock(&mutex);
/* change predicate state */
pthread_cond_signal(&cond);    // wake one waiter
pthread_mutex_unlock(&mutex);
```

Contrast with [[PthreadCondBroadcast|`pthread_cond_broadcast`]] which wakes all waiters. Use `signal` when only one waiter can profit from the state change (one egg laid → one farmer can collect); use `broadcast` when the change can satisfy multiple waiters or when the waiters check different predicates.

## Connections

- [[ConditionVariable]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadCondWait]] — the waiter side.
- [[PthreadCondBroadcast]] — the wake-all alternative.
- [[Mutex]] — the partner that protects the predicate state.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
