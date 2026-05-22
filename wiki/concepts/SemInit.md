---
title: "sem_init"
type: concept
tags: [pthreads, posix, semaphore, synchronization, c-api]
sources: [dis-14-3-2-semaphores]
last_updated: 2026-05-18
---

# sem_init

POSIX [[Semaphore|semaphore]] initialization: `sem_init(sem_t *sem, int pshared, unsigned int value)` ([[dis-14-3-2-semaphores|DIS Ch 14.3.2]]). Three parameters: the semaphore address, sharing scope (`0` for threads in one process; nonzero for inter-process — requires placement in shared memory), and initial count.

```c
sem_t sem;
sem_init(&sem, 0, /*value=*/N);   // N threads can sem_wait without blocking
```

**macOS portability gotcha**: `sem_init` is deprecated → use `sem_open(name, O_CREAT, mode, value)` for named semaphores instead.

## Connections

- [[Semaphore]] / [[POSIX]] — the primitive and the API origin.
- [[SemWait]] / [[SemPost]] / [[SemDestroy]] — the rest of the four-function lifecycle.
- [[dis-14-3-2-semaphores]] — DIS Ch 14.3.2 source.
- [[Pthreads]] — sibling threading API; semaphores live in `<semaphore.h>`.
