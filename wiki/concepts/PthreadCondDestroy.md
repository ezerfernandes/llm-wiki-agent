---
title: "pthread_cond_destroy"
type: concept
tags: [pthreads, synchronization, condition-variable, c-api]
sources: [dis-14-3-3-other-syncs]
last_updated: 2026-05-18
---

# pthread_cond_destroy

[[Pthreads]] [[ConditionVariable|condition variable]] teardown: `pthread_cond_destroy(pthread_cond_t *cond)` ([[dis-14-3-3-other-syncs|DIS Ch 14.3.3]]). Frees resources associated with the condition variable; destroying one on which threads currently wait is undefined behaviour. Pair with [[PthreadMutexDestroy|`pthread_mutex_destroy`]] for the partner mutex after all workers have been [[PthreadJoin|joined]].

## Connections

- [[ConditionVariable]] / [[Pthreads]] — the primitive and the API family.
- [[PthreadCondInit]] — lifecycle counterpart.
- [[PthreadCondWait]] / [[PthreadCondSignal]] / [[PthreadCondBroadcast]] — operational siblings.
- [[dis-14-3-3-other-syncs]] — DIS Ch 14.3.3 source.
