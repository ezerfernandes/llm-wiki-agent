---
title: "OpenMP Locks (omp_lock_t)"
type: concept
tags: [openmp, parallel-computing, locks, synchronization]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP Locks

For the rare case where the high-level [[OpenMP]] constructs ([[CriticalSection|`critical`]], [[AtomicClause|`atomic`]], [[Barrier|`barrier`]], [[ReductionClause|`reduction`]]) are insufficient, the OpenMP runtime exposes a **lock API** ([[parproc-ch04-introduction-to-openmp]] §4.15):

- Declare a lock variable: `omp_lock_t my_lock;`
- Initialize: `omp_init_lock(&my_lock);`
- Acquire: `omp_set_lock(&my_lock);`
- Release: `omp_unset_lock(&my_lock);`
- Destroy: `omp_destroy_lock(&my_lock);`

(The chapter explicitly lists only `omp_lock_t`, `omp_set_lock`, `omp_unset_lock`; the rest are part of the broader OpenMP runtime surface.)

## When to use

[[parproc-ch04-introduction-to-openmp]]: *"Though one of OpenMP's best virtues is that you can avoid working with those pesky lock variables needed for straight threads programming, there are still some instances in which lock variables may be useful."*

Typical scenarios:
- Multiple **distinct** critical sections that should not serialize against each other. `#pragma omp critical` without a name uses a single global mutex; named `critical` sections (`critical (name)`) help but are coarser than per-data-structure locks.
- Lock state that must persist across function boundaries — explicit locks survive function returns; `critical` blocks do not.
- Bridge code that interacts with non-OpenMP threading code.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.15 source.
- [[CriticalSection]] — the higher-level alternative the chapter generally prefers.
- [[AtomicClause]] — even lower overhead, single-statement only.
- [[Pthreads]] — the API OpenMP locks mirror in spirit (`pthread_mutex_t` ↔ `omp_lock_t`).
- [[TestAndSet]] — likely substrate.
