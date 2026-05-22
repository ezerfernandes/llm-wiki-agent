---
title: "pthread_join"
type: concept
tags: [pthreads, posix, threading, c, api, synchronization, parallel-computing]
sources: [dis-14-2-posix, parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-18
---

# pthread_join

The [[Pthreads]] thread-wait primitive. Suspends the caller until the named [[Thread|thread]] terminates and reclaims its execution-context resources.

## Signature

```c
pthread_join(pthread_t thread, void **return_val)
```

## Parameters

- **`pthread_t thread`** — the thread to wait on (the [[Pthreads|`pthread_t`]] value previously written by [[PthreadCreate|`pthread_create`]]).
- **`void **return_val`** — optional out-parameter receiving the [[ThreadFunction|thread function]]'s return pointer. Pass `NULL` to discard.

## Semantics ([[dis-14-2-posix|DIS Ch 14.2]])

> *"The `pthread_join` function suspends the execution of its caller until the thread it references terminates."*

Two cases:

- **Target thread still running** — `pthread_join` **blocks** the caller until the target reaches the end of its [[ThreadFunction|thread function]] (or otherwise terminates).
- **Target thread already terminated** — `pthread_join` returns immediately; the kernel/library frees the thread's execution context and resources.

Joining is therefore **both** a synchronization barrier *and* the resource-reclamation hook — every [[PthreadCreate|`pthread_create`]] must eventually be matched by a `pthread_join` (or the thread must be detached) to avoid leaking thread resources.

## Usage pattern

```c
for (int i = 0; i < N; i++) {
    pthread_join(threads[i], NULL);
}
```

`main` blocks at the first un-finished worker, then proceeds through the rest. Order of join calls does **not** force order of thread completion — the loop simply guarantees `main` doesn't exit until *every* worker has finished.

## Connections

- [[Pthreads]] — the API family.
- [[PthreadCreate]] — paired operation.
- [[ThreadFunction]] — supplies the return value `pthread_join` may capture.
- [[Thread]] — the abstraction being waited on.
- [[Barrier]] — a generalized N-way synchronization primitive; `pthread_join` is the asymmetric "wait for *that* specific thread" variant.
- [[dis-14-2-posix]] — primary source.
- [[parproc-ch01-intro-parallel-processing]] — Pacheco's parallel introduction.
