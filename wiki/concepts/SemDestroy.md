---
title: "sem_destroy"
type: concept
tags: [pthreads, posix, semaphore, synchronization, c-api]
sources: [dis-14-3-2-semaphores]
last_updated: 2026-05-18
---

# sem_destroy

POSIX [[Semaphore|semaphore]] teardown: `sem_destroy(sem_t *sem)` ([[dis-14-3-2-semaphores|DIS Ch 14.3.2]]). Called after all threads have completed their use of the semaphore. Destroying a semaphore on which threads currently block is undefined behaviour.

**macOS counterparts**: `sem_close` releases per-process resources; `sem_unlink` removes the system-wide name (named semaphores via `sem_open`).

## Connections

- [[Semaphore]] / [[POSIX]] — the primitive and the API origin.
- [[SemInit]] — the lifecycle counterpart.
- [[SemWait]] / [[SemPost]] — the operational pair.
- [[dis-14-3-2-semaphores]] — DIS Ch 14.3.2 source.
