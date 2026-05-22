---
title: "Thread Function"
type: concept
tags: [pthreads, posix, threading, c, api, parallel-computing]
sources: [dis-14-2-posix]
last_updated: 2026-05-18
---

# Thread Function

The user-supplied function a worker [[Thread|thread]] executes from start to finish. In [[Pthreads]], every spawned thread runs **exactly one** thread function — *"a thread function is analogous to a `main` function for a worker (created) thread — a thread begins execution at the start of its thread function and terminates when it reaches the end"* ([[dis-14-2-posix|DIS Ch 14.2]]).

## Required prototype

```c
void *thread_function(void *arg);
```

Both the argument and the return type are [[VoidStar|`void *`]] — the generic-pointer typing that lets a single API surface ([[PthreadCreate|`pthread_create`]] / [[PthreadJoin|`pthread_join`]]) handle any data shape. Callers cast on the way in and on the way out.

## Idiomatic body

```c
void *thread_function(void *id) {
    long *myid = (long *) id;
    printf("Thread %ld\n", *myid);
    return NULL;
}
```

Standard structure:
1. **Cast** the [[VoidStar|`void *`]] argument back to its real type.
2. **Dereference** / extract per-thread state (often the [[ThreadID|TID]]).
3. **Do the worker's work** — each call executes against the thread's own private stack and registers.
4. **Return** a pointer ([[VoidStar|`void *`]]) — or `NULL` if no return value is needed. The returned pointer is what [[PthreadJoin|`pthread_join`]]'s `void **return_val` parameter captures.

## Per-thread execution state

> *"Each thread executes the thread function using its private execution state (i.e., its own stack memory and register values)."*

Local variables declared inside the thread function are **per-thread** (separate stack frames). Globals and heap allocations are **shared** — the foundation for both data sharing and [[RaceCondition|race conditions]].

## Connections

- [[Pthreads]] — the API family.
- [[PthreadCreate]] — receives a function pointer of this prototype.
- [[PthreadJoin]] — captures the return value.
- [[ThreadID]] — the typical content of the thread function's argument.
- [[VoidStar]] — the generic-pointer convention this prototype rests on.
- [[Thread]] — the abstraction the thread function defines work for.
- [[dis-14-2-posix]] — primary source.
