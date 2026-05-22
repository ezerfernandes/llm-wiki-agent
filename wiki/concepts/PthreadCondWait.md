---
title: "pthread_cond_wait"
type: concept
tags: [pthreads, synchronization, condition-variable, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_cond_wait

[[Pthreads]] [[ConditionVariable|condition variable]] block-on-predicate: `pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)`. *"Causes the calling thread to block on the condition variable `cond` until another thread signals it"* ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]).

**Atomic behaviour**: on entry the mutex *must* be held; the call atomically (a) releases `mutex` and (b) blocks on `cond`. On wake: re-acquires `mutex` before returning.

## The mandatory predicate-loop idiom

```c
pthread_mutex_lock(&mutex);
while (!predicate) {
    pthread_cond_wait(&cond, &mutex);
}
/* use shared state */
pthread_mutex_unlock(&mutex);
```

[[dis-14-3-3-other-syncs|DIS Ch 14.3.3]] insists on `while`, not `if`. Two reasons: **spurious wakeups** (the OS may wake the waiter without a corresponding signal — standards-permitted) and **condition-change races** (another consumer races in between signal and waiter resumption and consumes the produced state).

## Connections

- [[ConditionVariable]] / [[Mutex]] / [[Pthreads]] — the primitives.
- [[PthreadCondSignal]] / [[PthreadCondBroadcast]] — what wakes the waiter.
- [[PthreadCondInit]] / [[PthreadCondDestroy]] — lifecycle bookends.
- [[ProducerConsumer]] — the dominant pattern.
- [[SpuriousWakeup]] — the OS behaviour the predicate loop defends against.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
