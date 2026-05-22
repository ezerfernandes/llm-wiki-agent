---
title: "Condition Variable"
type: concept
tags: [concurrency, synchronization, pthreads]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# Condition Variable

Synchronization primitive that **blocks threads until specific conditions are satisfied, eliminating wasteful CPU polling** ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). Always paired with a [[Mutex|mutex]]: the condition variable holds the wait queue; the mutex protects the predicate state on which threads wait.

## Pthreads API

```c
#include <pthread.h>

pthread_cond_t  cond;
pthread_mutex_t mutex;

pthread_cond_init(&cond, NULL);
pthread_mutex_init(&mutex, NULL);

/* waiter */
pthread_mutex_lock(&mutex);
while (!predicate) {
    pthread_cond_wait(&cond, &mutex);
}
/* use shared state */
pthread_mutex_unlock(&mutex);

/* signaler */
pthread_mutex_lock(&mutex);
/* change predicate state */
pthread_cond_signal(&cond);   // or pthread_cond_broadcast
pthread_mutex_unlock(&mutex);

pthread_cond_destroy(&cond);
pthread_mutex_destroy(&mutex);
```

- [[PthreadCondInit|`pthread_cond_init(&cond, attr)`]] / [[PthreadCondDestroy|`pthread_cond_destroy(&cond)`]]: lifecycle.
- [[PthreadCondWait|`pthread_cond_wait(&cond, &mutex)`]]: **atomically** (a) release `mutex`, (b) block on `cond`. On wake: re-acquire `mutex` before returning. **The mutex must be held on entry.**
- [[PthreadCondSignal|`pthread_cond_signal(&cond)`]]: wake one waiter (scheduler-chosen).
- [[PthreadCondBroadcast|`pthread_cond_broadcast(&cond)`]]: wake all waiters.

## The predicate-loop discipline

[[dis-14-3-3-other-syncs|DIS Ch 14.3.3]] insists on `while`, not `if`:

```c
while (!predicate) {
    pthread_cond_wait(&cond, &mutex);
}
```

Two reasons:

1. **Spurious wakeups** — the OS may wake the waiter without a corresponding signal. Standards-permitted; pragmatically common.
2. **Condition-change races** — another consumer may race in between signal and waiter resumption and consume the produced state. The waiter must re-check.

This idiom is so canonical it's a load-bearing pattern across every textbook treatment.

## The egg-laying example

[[dis-14-3-3-other-syncs|DIS]] uses farmers + chickens: farmers (consumers) wait for chickens (producers) to lay eggs. Farmers block on the condition variable until signaled, then atomically collect eggs. Equivalent to the [[ProducerConsumer|producer/consumer]] pattern realizable also via [[Semaphore|semaphores]] — DIS notes the [[Semaphore|semaphore]] version is *"simpler and more efficient than mutex-condition variable combinations"* for pure resource-count problems.

## When to reach for condition variables vs alternatives

| Need | Use |
|---|---|
| Wait on predicate over arbitrary state | Condition variable |
| Wait on resource count | [[Semaphore]] (simpler) |
| Wait for all threads to reach point | [[Barrier]] |
| Mutual exclusion only | [[Mutex]] |

## Connections

- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
- [[PthreadCondInit]] / [[PthreadCondWait]] / [[PthreadCondSignal]] / [[PthreadCondBroadcast]] / [[PthreadCondDestroy]] — per-call concept pages.
- [[Mutex]] — the mandatory partner.
- [[Semaphore]] — sibling primitive; simpler for resource-count problems.
- [[Barrier]] — sibling rendezvous primitive.
- [[Pthreads]] — the API surface.
- [[Synchronization]] — umbrella.
- [[ProducerConsumer]] — the canonical pattern.
- [[SpuriousWakeup]] — the OS behavior the predicate loop defends against.
- [[CriticalSection]] / [[DataRace]] — parent vocabulary.
