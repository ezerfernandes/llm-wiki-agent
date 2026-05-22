---
title: "pthread_mutex_unlock"
type: concept
tags: [pthreads, synchronization, mutex, c-api]
sources: [dis-14-3-1-mutex]
last_updated: 2026-05-18
---

# pthread_mutex_unlock

[[Pthreads]] [[Mutex|mutex]] release: `pthread_mutex_unlock(pthread_mutex_t *mutex)`. *"Releases the lock, allowing other threads to acquire it"* ([[dis-14-3-1-mutex|DIS Ch 14.3.1]]). Paired with [[PthreadMutexLock|`pthread_mutex_lock`]] to bracket a [[CriticalSection|critical section]].

**Ownership rule**: only the thread that locked may unlock — the structural distinction from [[Semaphore|semaphores]] where any thread can [[SemPost|post]].

## Connections

- [[Mutex]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadMutexLock]] — the mandatory paired acquire.
- [[PthreadMutexInit]] / [[PthreadMutexDestroy]] — lifecycle bookends.
- [[CriticalSection]] — the abstraction lock/unlock realizes.
- [[Semaphore]] — sibling primitive; any thread can post (no ownership).
- [[dis-14-3-1-mutex]] — DIS Ch 14.3.1 source.
