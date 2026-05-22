---
title: "Semaphore"
type: concept
tags: [concurrency, synchronization, pthreads, posix]
sources: [dis-14-3-2-semaphores]
last_updated: 2026-05-18
---

# Semaphore

Synchronization primitive that **manages concurrent access to a resource pool by tracking availability count rather than ownership** ([[dis-14-3-2-semaphores|DIS Ch 14.3.2]]). Conceptually invented by Dijkstra (1965); operationalized in POSIX via `<semaphore.h>`.

## Counting vs binary

| Type | Value range | Use |
|---|---|---|
| **Counting** | 0 to *r* | Bounded resource pool (DB connection pool, fixed-size buffer slots) |
| **Binary** | 0 or 1 only | Mutex-shape — but **without** ownership |

A counting semaphore initialized to `value=N` permits up to `N` concurrent acquirers; the `N+1`-th blocks until someone posts.

## Core POSIX API

```c
#include <semaphore.h>

sem_t sem;
sem_init(&sem, /*pshared=*/0, /*value=*/N);   // initialize
sem_wait(&sem);    // acquire — decrement; block if 0
/* use one unit of the resource */
sem_post(&sem);    // release — increment; wake one waiter
sem_destroy(&sem); // teardown
```

- [[SemInit|`sem_init(sem, pshared, value)`]]: `pshared = 0` for thread sharing inside one process; nonzero for inter-process (place in shared memory).
- [[SemWait|`sem_wait(sem)`]]: *"Decrements the semaphore when acquiring a resource. If the value exceeds 0, execution continues immediately. If 0, the thread blocks."*
- [[SemPost|`sem_post(sem)`]]: increment; wake one waiter if any.
- [[SemDestroy|`sem_destroy(sem)`]]: deallocate.

**macOS portability note**: `sem_init` is deprecated → use `sem_open` / `sem_close` / `sem_unlink` (named semaphores).

## The key contrast with mutex

*"Any thread can unlock the semaphore (in contrast to a mutex, where the calling thread must unlock it)"* ([[dis-14-3-2-semaphores|DIS Ch 14.3.2]]).

| | [[Mutex]] | Semaphore |
|---|---|---|
| Model | Ownership | Resource count |
| Who can release | Acquirer only | Any thread |
| Use | Critical section | Producer/consumer, resource pool |

This asymmetry makes the semaphore the natural primitive for **producer/consumer**: producer posts after producing, consumer waits before consuming — they are different threads.

## Canonical pattern — bounded buffer

```c
sem_t empty_slots, filled_slots;
sem_init(&empty_slots, 0, BUFFER_SIZE);
sem_init(&filled_slots, 0, 0);

void producer() {
    sem_wait(&empty_slots);
    /* place item */
    sem_post(&filled_slots);
}

void consumer() {
    sem_wait(&filled_slots);
    /* take item */
    sem_post(&empty_slots);
}
```

Two semaphores coordinate empty-slot and filled-slot counts; no [[ConditionVariable|condition variable]] needed.

## Connections

- [[dis-14-3-2-semaphores]] — DIS Ch 14.3.2 source.
- [[SemInit]] / [[SemWait]] / [[SemPost]] / [[SemDestroy]] — per-call concept pages.
- [[Mutex]] — sibling primitive; ownership-based vs count-based.
- [[ConditionVariable]] — lower-level alternative for the same patterns; semaphores subsume both ownership and signaling.
- [[ProducerConsumer]] — the dominant pattern.
- [[Synchronization]] — umbrella.
- [[CriticalSection]] / [[DataRace]] — parent vocabulary.
- [[POSIX]] — the standard `<semaphore.h>` belongs to.
- [[Pthreads]] — sibling threading API.
