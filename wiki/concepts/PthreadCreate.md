---
title: "pthread_create"
type: concept
tags: [pthreads, posix, threading, c, api, parallel-computing]
sources: [dis-14-2-posix, parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-18
---

# pthread_create

The [[Pthreads]] thread-spawn primitive. Creates a new [[Thread|thread]] that begins execution at a user-supplied [[ThreadFunction|thread function]] and runs concurrently with its caller.

## Signature

```c
pthread_create(pthread_t *thread,
               const pthread_attr_t *attr,
               void *(*thread_function)(void *),
               void *thread_args)
```

## Parameters

- **`pthread_t *thread`** — **out-parameter**. The system writes the newly-created thread's identification data (the `pthread_t` value, i.e. the library-level [[ThreadID|thread ID]]) here so the caller can later reference the thread (most importantly to [[PthreadJoin|join]] it).
- **`const pthread_attr_t *attr`** — thread attributes; typically `NULL` for default behaviour ([[dis-14-2-posix|Ch 14.2]]'s worked example uses `NULL` throughout).
- **`void *(*thread_function)(void *)`** — pointer to the [[ThreadFunction|thread function]] the new thread executes. The function must take a [[VoidStar|`void *`]] argument and return a [[VoidStar|`void *`]].
- **`void *thread_args`** — single [[VoidStar|`void *`]] argument passed through to `thread_function`. The standard idiom for passing multiple values is to allocate a `struct` and pass its address.

## Usage pattern ([[dis-14-2-posix|DIS Ch 14.2]])

```c
pthread_t threads[N];
long ids[N];
for (int i = 0; i < N; i++) {
    ids[i] = i;
    pthread_create(&threads[i], NULL, thread_function, &ids[i]);
}
```

Each call returns immediately — the spawned thread runs concurrently with `main`. Each worker receives its **own** per-iteration `&ids[i]` pointer so [[ThreadID|TID]]s don't alias. (Passing `&i` directly would be a bug: every worker would see the loop variable's final value.)

## Connections

- [[Pthreads]] — the API family.
- [[PthreadJoin]] — paired operation; every `pthread_create` must eventually be joined.
- [[ThreadFunction]] — the prototype every `thread_function` argument must follow.
- [[ThreadID]] — the per-thread identifier typically passed as `thread_args`.
- [[VoidStar]] — the generic-typing convention enabling type-agnostic argument and return.
- [[dis-14-2-posix]] — primary source; full API codification.
- [[parproc-ch01-intro-parallel-processing]] — Pacheco's introduction of the same API.
