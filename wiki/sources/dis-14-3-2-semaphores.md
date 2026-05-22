---
title: "Dive into Systems — Ch 14.3.2 Semaphores"
type: source
tags: [book, textbook, dive-into-systems, pthreads, semaphore, synchronization, concurrency, posix]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/semaphores.html
---

## Summary

Chapter 14.3.2 of *[[DiveIntoSystems]]* — **second sub-leaf** of [[dis-14-3-synchronization|Ch 14.3 *Synchronizing Threads*]]. Introduces **[[Semaphore|semaphores]]** as the resource-count synchronization primitive that complements the [[Mutex|mutex]]'s ownership model — *"semaphores manage concurrent access to resource pools by tracking availability count rather than ownership."* Codifies the **counting vs binary** distinction: counting semaphores range from 0 to *r* (a resource limit; threads decrement to acquire, increment to release; value 0 means no resources available — acquirers block), binary semaphores have only locked/unlocked states. **Critical distinction from mutex**: *"any thread can unlock the semaphore (in contrast to a mutex, where the calling thread must unlock it)"* — semaphores have no ownership concept, making them the natural primitive for **producer/consumer** patterns where one thread produces resources and a *different* thread consumes them. **Core POSIX API**: [[SemInit|`sem_init(sem, pshared, value)`]] (three params — address, sharing scope `0` for threads / nonzero for inter-process, initial count), [[SemWait|`sem_wait(sem)`]] (decrement-and-block — returns immediately if count > 0, blocks if count = 0), [[SemPost|`sem_post(sem)`]] (increment-and-wake — returns immediately, wakes one waiter if any block on the semaphore), [[SemDestroy|`sem_destroy(sem)`]] (deallocate). **macOS note**: `sem_init` is deprecated on macOS — use `sem_open` / `sem_unlink` / `sem_close` instead. **Use-case framing**: *"Semaphores excel where the goal isn't *who* owns what, but *how many* resources are still available — particularly useful for managing resource pools more simply and efficiently than mutex-condition variable combinations."* **131st ingested DIS chapter.** Mints **5 new concept pages** ([[Semaphore]], [[SemInit]], [[SemWait]], [[SemPost]], [[SemDestroy]]).

## Key Claims

- **[[Semaphore]] = count-based concurrent-access manager.** *"Semaphores manage concurrent access to resource pools by tracking availability count rather than ownership."* The fundamental dual to the [[Mutex|mutex]]'s ownership-based exclusion.
- **Counting vs binary**:
  - **Counting**: range 0 to *r* resources. Decrement on acquire ([[SemWait|`sem_wait`]]), increment on release ([[SemPost|`sem_post`]]). 0 = no resources available; acquirers block.
  - **Binary**: locked/unlocked only — degenerates to mutex-shape but **without** ownership.
- **Anyone can post.** *"Any thread can unlock the semaphore (in contrast to a mutex, where the calling thread must unlock it)."* The structural distinction that makes semaphores the right primitive for producer/consumer.
- **API surface (four calls)**:
  - [[SemInit|`sem_init(&sem, pshared, value)`]]: initialize. `pshared = 0` for thread sharing inside one process; nonzero for inter-process (requires placement in shared memory).
  - [[SemWait|`sem_wait(&sem)`]]: *"Decrements the semaphore when acquiring a resource. If the value exceeds 0, execution continues immediately. If 0, the thread blocks until a resource becomes available."*
  - [[SemPost|`sem_post(&sem)`]]: *"Increments the semaphore when releasing a resource, returning immediately. If threads are waiting, one gains ownership of the freed resource."*
  - [[SemDestroy|`sem_destroy(&sem)`]]: deallocate.
- **macOS portability gotcha**: `sem_init` deprecated → use `sem_open` / `sem_close` / `sem_unlink` (named semaphores).
- **Use case**: bounded resource pools (DB connection pool, fixed-size buffer slots, etc.) where the question is *how many remain*, not *who holds which*.

## Key Quotes

> *"Any thread can unlock the semaphore (in contrast to a mutex, where the calling thread must unlock it)."*

> *"The goal isn't who owns what, but how many resources are still available."*

> *"If the value exceeds 0, execution continues immediately. If 0, the thread blocks until a resource becomes available."*

## Connections

- [[DiveIntoSystems]] — Ch 14.3.2.
- [[dis-14-3-synchronization]] — parent hub.
- [[Semaphore]] — new concept; canonical anchor.
- [[SemInit]] / [[SemWait]] / [[SemPost]] / [[SemDestroy]] — new concept pages, one per API call.
- [[Mutex]] — sibling primitive; ownership-based vs count-based; chapter explicitly contrasts the two.
- [[Pthreads]] — the threading API surface (semaphores are POSIX but live in `<semaphore.h>`, not strictly Pthreads).
- [[ConditionVariable]] — the lower-level alternative; *"managing resource pools more simply and efficiently than mutex-condition variable combinations."*
- [[Synchronization]] — umbrella.
- [[ProducerConsumer]] — the canonical pattern semaphores were invented for (Dijkstra 1965).
- [[CriticalSection]] / [[DataRace]] — the parent concepts.

## Contradictions

None. First wiki coverage of [[Semaphore|semaphores]] as a first-class primitive — prior mentions in [[dis-14-2-posix]] / [[parproc-ch01-intro-parallel-processing]] / [[SharedMemoryParallelism]] were forward references.
