---
title: "pthread_cond_init"
type: concept
tags: [pthreads, synchronization, condition-variable, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_cond_init

[[Pthreads]] [[ConditionVariable|condition variable]] initialization: `pthread_cond_init(pthread_cond_t *cond, const pthread_condattr_t *attr)` ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). `attr = NULL` selects default behaviour.

```c
pthread_cond_t  cond;
pthread_mutex_t mutex;
pthread_cond_init(&cond, NULL);
pthread_mutex_init(&mutex, NULL);   // mandatory partner
```

A condition variable is always used together with a [[Mutex|mutex]] that protects the predicate state.

## Connections

- [[ConditionVariable]] / [[Pthreads]] — the primitive and the API family.
- [[Mutex]] — the mandatory partner.
- [[PthreadCondWait]] / [[PthreadCondSignal]] / [[PthreadCondBroadcast]] / [[PthreadCondDestroy]] — the rest of the five-function lifecycle.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
