---
title: "pthread_mutex_lock"
type: concept
tags: [pthreads, synchronization, mutex, c-api]
sources: [dis-14-3-1-mutex]
last_updated: 2026-05-18
---

# pthread_mutex_lock

[[Pthreads]] [[Mutex|mutex]] acquire: `pthread_mutex_lock(pthread_mutex_t *mutex)`. *"Acquires the lock; blocks if already held by another thread"* ([[dis-14-3-1-mutex|DIS Ch 14.3.1]]). The serialization that prevents [[DataRace|data races]] on shared variables.

```c
pthread_mutex_lock(&mutex);
/* critical section */
pthread_mutex_unlock(&mutex);
```

The **ownership rule**: only the thread that locked the mutex may unlock it (contrast with [[Semaphore|semaphores]], where any thread can post).

Composition risk: nested or interdependent locks can [[Deadlock|deadlock]] (thread A holds X waiting for Y; thread B holds Y waiting for X — banking-scenario example in [[dis-14-3-1-mutex|DIS Ch 14.3.1]]).

## Connections

- [[Mutex]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadMutexUnlock]] — the mandatory paired release.
- [[PthreadMutexInit]] / [[PthreadMutexDestroy]] — lifecycle bookends.
- [[CriticalSection]] — the abstraction lock/unlock realizes.
- [[Deadlock]] — the composition risk.
- [[dis-14-3-1-mutex]] — DIS Ch 14.3.1 source.
