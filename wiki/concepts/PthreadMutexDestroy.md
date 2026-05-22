---
title: "pthread_mutex_destroy"
type: concept
tags: [pthreads, synchronization, mutex, c-api]
sources: [dis-14-3-1-mutex]
last_updated: 2026-05-18
---

# pthread_mutex_destroy

[[Pthreads]] [[Mutex|mutex]] teardown: `pthread_mutex_destroy(pthread_mutex_t *mutex)`. Frees resources associated with the mutex; called after all workers have been [[PthreadJoin|joined]] so no thread is using or waiting on the lock.

```c
for (int i = 0; i < N; i++) pthread_join(threads[i], NULL);
pthread_mutex_destroy(&mutex);
```

Destroying a mutex that is currently locked or has a waiter is undefined behaviour.

## Connections

- [[Mutex]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadMutexInit]] — the lifecycle counterpart.
- [[PthreadMutexLock]] / [[PthreadMutexUnlock]] — the operational pair.
- [[PthreadJoin]] — must be called on all workers first.
- [[dis-14-3-1-mutex]] — DIS Ch 14.3.1 source.
