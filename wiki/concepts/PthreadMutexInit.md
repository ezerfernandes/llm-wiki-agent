---
title: "pthread_mutex_init"
type: concept
tags: [pthreads, synchronization, mutex, c-api]
sources: [dis-14-3-1-mutex]
last_updated: 2026-05-18
---

# pthread_mutex_init

[[Pthreads]] [[Mutex|mutex]] initialization: `pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr)`. Called in `main` before [[PthreadCreate|`pthread_create`]] so all workers see an initialized lock; `attr = NULL` selects default mutex behaviour.

```c
pthread_mutex_t mutex;
pthread_mutex_init(&mutex, NULL);
```

Paired with [[PthreadMutexDestroy|`pthread_mutex_destroy`]] after all workers have been [[PthreadJoin|joined]]. The acquire/release pair [[PthreadMutexLock|`pthread_mutex_lock`]] / [[PthreadMutexUnlock|`pthread_mutex_unlock`]] runs inside each worker.

## Connections

- [[Mutex]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadMutexLock]] / [[PthreadMutexUnlock]] / [[PthreadMutexDestroy]] — the rest of the four-function lifecycle.
- [[dis-14-3-1-mutex]] — DIS Ch 14.3.1 source.
- [[Synchronization]] / [[CriticalSection]] — the umbrella + atomicity-boundary concepts.
