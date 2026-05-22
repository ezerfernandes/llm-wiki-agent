---
title: "sem_wait"
type: concept
tags: [pthreads, posix, semaphore, synchronization, c-api]
sources: [dis-14-3-2-semaphores]
last_updated: 2026-05-18
---

# sem_wait

POSIX [[Semaphore|semaphore]] acquire: `sem_wait(sem_t *sem)`. *"Decrements the semaphore when acquiring a resource. If the value exceeds 0, execution continues immediately. If 0, the thread blocks until a resource becomes available"* ([[dis-14-3-2-semaphores|DIS Ch 14.3.2]]).

```c
sem_wait(&sem);   // decrement; block if count was 0
/* use one unit of the resource */
sem_post(&sem);   // release
```

Variants: `sem_trywait` (non-blocking, returns error on count = 0), `sem_timedwait` (block with timeout).

## Connections

- [[Semaphore]] / [[POSIX]] — the primitive and the API origin.
- [[SemPost]] — the release counterpart.
- [[SemInit]] / [[SemDestroy]] — lifecycle bookends.
- [[Synchronization]] — umbrella.
- [[dis-14-3-2-semaphores]] — DIS Ch 14.3.2 source.
