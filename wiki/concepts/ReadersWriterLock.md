---
title: "Readers-Writer Lock"
type: concept
tags: [concurrency, synchronization, pthreads]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# Readers-Writer Lock

Synchronization primitive specializing the [[Mutex|mutex]] for **read-heavy** workloads: allows **many concurrent readers OR one exclusive writer**, never both. Surveyed in [[dis-14-3-3-other-syncs|DIS Ch 14.3.3]] as one of the "other synchronization constructs" beyond the [[Mutex|mutex]] / [[Semaphore|semaphore]] / [[Barrier|barrier]] / [[ConditionVariable|condition-variable]] core four.

## Pthreads API

```c
#include <pthread.h>

pthread_rwlock_t rwlock;
pthread_rwlock_init(&rwlock, NULL);

/* reader */
pthread_rwlock_rdlock(&rwlock);
/* read shared state */
pthread_rwlock_unlock(&rwlock);

/* writer */
pthread_rwlock_wrlock(&rwlock);
/* mutate shared state */
pthread_rwlock_unlock(&rwlock);

pthread_rwlock_destroy(&rwlock);
```

| Call | Behavior |
|---|---|
| `pthread_rwlock_rdlock` | Acquire shared (read) lock; blocks if a writer holds the lock. Multiple readers admitted concurrently. |
| `pthread_rwlock_wrlock` | Acquire exclusive (write) lock; blocks until no readers and no writer. |
| `pthread_rwlock_unlock` | Release whichever mode the caller holds. |

## When it helps

The performance argument: when reads vastly outnumber writes (catalogue lookups, configuration tables, routing data), a plain [[Mutex|mutex]] serializes readers unnecessarily. The readers-writer lock admits readers in parallel and demotes the serialization to the (rare) writer.

## When it hurts

- **Writer starvation**: a steady stream of readers can indefinitely block a writer. Pthreads attribute `pthread_rwlockattr_setkind_np` controls writer-preference policy on Linux.
- **Lock overhead**: the bookkeeping (reader count, writer flag, queue management) makes a single uncontended read slower than a plain [[Mutex|mutex]]. Worth it only when reader parallelism actually fires.
- **Cache contention**: even under "shared" mode, readers all atomically increment the reader count — the cache line bounces between cores.

For very-read-heavy + simple shared state, [[RCU|read-copy-update]] or [[Atomic|atomics]] often beat the readers-writer lock.

## Connections

- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source; introduces the primitive at the catalogue level.
- [[Mutex]] — the symmetric primitive readers-writer locks specialize.
- [[Synchronization]] — umbrella.
- [[CriticalSection]] — the abstraction the writer-mode lock implements; reader-mode is *not* a critical section since multiple readers admitted.
- [[Pthreads]] — the API surface.
- [[Semaphore]] — could implement read/write coordination with two semaphores at higher cost.
- [[ConditionVariable]] — what some rwlock implementations use internally for waiter queues.
- [[DataRace]] — the failure mode the lock prevents on writes; reads in shared mode are safe because no concurrent writer.
