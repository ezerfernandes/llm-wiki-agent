---
title: "#pragma omp critical"
type: concept
tags: [parallel-programming, openmp, compiler-directives, synchronization, mutual-exclusion]
sources: [dis-14-7-openmp]
last_updated: 2026-05-18
---

# `#pragma omp critical`

The [[OpenMP]] **mutual-exclusion** pragma — guarantees that only **one thread in the team** executes the protected block at a time. The OpenMP analog of [[Mutex|`pthread_mutex_lock(&m)` / `pthread_mutex_unlock(&m)`]] but with no explicit lock variable to declare, initialize, or destroy.

## Syntax

```c
#pragma omp parallel
{
    /* ...concurrent work... */

    #pragma omp critical [(name)]
    {
        /* exactly one thread at a time inside */
        shared_counter += local_partial;
    }

    /* ...more concurrent work... */
}
```

## Semantics

- **One-at-a-time**: the runtime serializes entries; threads queue until the critical section is free.
- **Optional name**: `#pragma omp critical (counter_lock)` — named critical sections share their own dedicated lock per name. Different names do not block each other; all unnamed critical sections share a single global lock.
- **No deadlock from misordering**: a thread cannot accidentally fail to unlock the way a [[Pthreads]] caller can forget [[Mutex|`pthread_mutex_unlock`]] — the closing `}` is the implicit unlock.

## When to use it vs alternatives

| Need | Use |
|---|---|
| **Combine per-thread partials at loop end** | `reduction(op:var)` clause on [[OpenMPParallelForPragma|`parallel for`]] — better. |
| **Single atomic memory op** (single increment, store) | `#pragma omp atomic` — cheaper than `critical`. |
| **Multi-statement update of shared state** | `#pragma omp critical` — the right tool. |
| **Print to `stdout` from many threads** | `#pragma omp critical` — keep lines from interleaving. |

The DIS chapter introduces `critical` as the **safe way to update shared state from a parallel region** — but warns (echoing [[dis-14-3-1-mutex|14.3.1's]] mutex lesson) that placing a `critical` inside an inner loop body serializes execution and erases parallelism gains. Prefer `reduction` or local accumulators where possible.

## Related

- [[OpenMP]] — parent concept.
- [[OpenMPParallelPragma]] / [[OpenMPForPragma]] / [[OpenMPParallelForPragma]] — pragmas this typically nests inside.
- [[Mutex]] — the [[Pthreads]] explicit equivalent.
- [[CriticalSection]] — the underlying concept.
- [[Synchronization]] — broader umbrella.
- [[OpenMPLocks]] — explicit lock API for cases `critical` cannot express.
- [[dis-14-7-openmp]] — DIS introduction.
- [[dis-14-3-1-mutex]] — the [[Pthreads]] sibling that taught the lock-coarsening lesson.
