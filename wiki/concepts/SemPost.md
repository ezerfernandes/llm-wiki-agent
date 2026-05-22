---
title: "sem_post"
type: concept
tags: [pthreads, posix, semaphore, synchronization, c-api]
sources: [dis-14-3-2-semaphores]
last_updated: 2026-05-18
---

# sem_post

POSIX [[Semaphore|semaphore]] release: `sem_post(sem_t *sem)`. *"Increments the semaphore when releasing a resource, returning immediately. If threads are waiting, one gains ownership of the freed resource"* ([[dis-14-3-2-semaphores|DIS Ch 14.3.2]]).

**Any thread can post** — *"in contrast to a mutex, where the calling thread must unlock it"*. This asymmetry is what makes the semaphore the natural primitive for [[ProducerConsumer|producer/consumer]] patterns where producer and consumer are different threads.

## Connections

- [[Semaphore]] / [[POSIX]] — the primitive and the API origin.
- [[SemWait]] — the acquire counterpart.
- [[SemInit]] / [[SemDestroy]] — lifecycle bookends.
- [[Mutex]] — sibling primitive; mutex requires ownership for unlock.
- [[ProducerConsumer]] — the dominant pattern.
- [[dis-14-3-2-semaphores]] — DIS Ch 14.3.2 source.
