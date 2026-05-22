---
title: "Thread ID (TID)"
type: concept
tags: [pthreads, posix, threading, c, parallel-computing]
sources: [dis-14-2-posix]
last_updated: 2026-05-18
---

# Thread ID (TID)

A unique per-[[Thread|thread]] identifier used to distinguish threads inside the [[ThreadFunction|thread function]] for work distribution. In the [[dis-14-2-posix|DIS Ch 14.2]] [[Pthreads]] convention, **the user supplies the TID** — typically as a `long` passed via [[PthreadCreate|`pthread_create`]]'s `thread_args` parameter — alongside whatever library-level identifier (the `pthread_t`) [[Pthreads]] separately assigns.

## Why the user-supplied TID matters

Without an explicit TID, every worker running the same [[ThreadFunction|thread function]] is indistinguishable. With one, the function can:
- Compute the worker's chunk of an array (`for (i = tid * chunk; i < (tid+1)*chunk; i++)`).
- Tag debug output (per [[dis-3-6-gdb-pthreads|Ch 3.6]]'s "include the thread ID in debug print output" recommendation).
- Branch on thread role (one thread handles I/O, others compute, etc.).

## Idiomatic pattern ([[dis-14-2-posix|DIS Ch 14.2]])

```c
long ids[N];
for (int i = 0; i < N; i++) {
    ids[i] = i;
    pthread_create(&threads[i], NULL, thread_function, &ids[i]);
}
```

Critical detail: **each worker gets its own slot** `&ids[i]`. Passing `&i` directly would alias — every worker would observe the loop variable's final value.

## Library-level identifier (the `pthread_t`)

Distinct from the user-supplied TID, [[Pthreads]] assigns each thread a `pthread_t` (the value [[PthreadCreate|`pthread_create`]] writes back through its out-parameter). [[dis-3-6-gdb-pthreads|Ch 3.6]] further details that [[GDB]] tracks **three** identifiers per thread: the `pthread_t`, the kernel's **LWP ID**, and [[GDB]]'s own thread number. The user-supplied TID covered here is **none of those** — it's an *application-level* labelling convention layered on top.

## Connections

- [[Pthreads]] — the API family.
- [[PthreadCreate]] — receives the user-supplied TID as `thread_args`.
- [[ThreadFunction]] — casts and dereferences the TID inside the body.
- [[Thread]] — the abstraction being labeled.
- [[dis-14-2-posix]] — primary source.
- [[dis-3-6-gdb-pthreads]] — describes the three *library/kernel/debugger* identifiers (`pthread_t` / LWP ID / GDB thread number) that are distinct from this user-level TID.
