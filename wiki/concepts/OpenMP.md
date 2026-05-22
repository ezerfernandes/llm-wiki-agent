---
title: "OpenMP"
type: concept
tags: [parallel-programming, shared-memory, implicit-threading, compiler-directives, openmp]
sources: [dis-14-7-openmp]
last_updated: 2026-05-18
---

# OpenMP

**OpenMP** (Open Multi-Processing) is the dominant **[[ImplicitThreading|implicit-threading]]** API for [[SharedMemoryParallelism|shared-memory parallelism]] in C, C++, and Fortran. The programmer annotates **existing sequential code** with **`#pragma omp`** compiler directives; the compiler and runtime generate the thread-spawn / join / scheduling machinery automatically. The contrasting explicit-threading API is [[Pthreads]] — OpenMP trades [[Pthreads|Pthreads']] fine-grained control for dramatic ergonomic ease.

## DIS framing

[[dis-14-7-openmp|DIS Ch 14.7]] introduces OpenMP as the **payoff** at the end of the Ch 14 parallel-programming arc — after six leaves of manual [[Pthreads]] discipline ([[PthreadCreate|`pthread_create`]] / [[PthreadJoin|`pthread_join`]] / [[Mutex|mutex]] / [[Semaphore|semaphore]] / [[Barrier|barrier]] / [[ThreadSafety|thread-safety audits]]), OpenMP collapses most of that machinery into single-line pragmas: *"all the low-level work of creating and joining threads is abstracted away from the programmer."*

## Compiler & language support

- **C / C++ / Fortran** — the three blessed languages.
- **[[GCC]] / [[LLVM]] / [[Clang]]** — all production compilers implement OpenMP.
- Compile flag: **`-fopenmp`** (GCC / Clang).

## Core pragma vocabulary

The four pragmas that cover most parallel loops:

| Pragma | Purpose |
|---|---|
| [[OpenMPParallelPragma|`#pragma omp parallel`]] | Create a team of threads executing the following block. |
| [[OpenMPForPragma|`#pragma omp for`]] | Distribute the iterations of the following `for` loop across the team. |
| [[OpenMPParallelForPragma|`#pragma omp parallel for`]] | Combined idiom — the most common form. |
| [[OpenMPCriticalPragma|`#pragma omp critical`]] | Mutual-exclusion block; the OpenMP analog of [[Mutex|`pthread_mutex_lock` / `_unlock`]]. |

The wider catalog ([[OpenMPLocks]], [[OpenMPSingle]], [[OpenMPTaskDirective]], [[FlushPragma]], [[ScheduleClause]], `reduction`, `barrier`, `master`, `atomic`, `sections`, `task`) extends this base.

## The canonical pattern

```c
#include <omp.h>
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    a[i] = b[i] * c[i];
}
```

Compile: `gcc -fopenmp prog.c`. Run: the loop iterations are split across `OMP_NUM_THREADS` (default = number of cores).

## Default scheduling

[[OpenMPForPragma|`#pragma omp for`]] uses **static chunking** by default — the iteration range is divided into equal-sized contiguous chunks, one per thread, assigned **before** the loop runs. Cheap and predictable; load-imbalanced when per-iteration work varies. Alternative schedules (`dynamic`, `guided`, `runtime`, `auto`) selectable via the [[ScheduleClause|`schedule(...)`]] clause.

## Variable visibility

Default rule: variables declared **outside** a `#pragma omp parallel` block are **shared** across threads; variables declared **inside** are **private**. Override with explicit clauses:

- `private(x, y)` — each thread gets its own uninitialized copy.
- `shared(z)` — explicit override; all threads see the same memory.
- `firstprivate(x)` — private but initialized from the enclosing scope's value.
- `reduction(+:sum)` — private accumulator per thread, combined via `+` (or `*`, `min`, `max`, `&`, `|`) at the end of the parallel region. The single most common safe way to combine per-thread results.

## OpenMP vs Pthreads — the trade-off

| Dimension | [[OpenMP]] | [[Pthreads]] |
|---|---|---|
| **Style** | Implicit; annotate existing loops | Explicit; manual `pthread_create` / `_join` |
| **Boilerplate** | Single `#pragma` line | Per-thread function, args struct, lifecycle |
| **Control** | Limited — restricted to OpenMP's worldview | Total — custom attributes, scheduling, [[ConditionVariable|condition variables]] |
| **Synchronization** | `critical`, `atomic`, `barrier` pragmas | [[Mutex]] / [[Semaphore]] / [[Barrier]] / [[ConditionVariable]] full POSIX API |
| **Portability** | Compiler-dependent | POSIX-portable |
| **Best for** | Embarrassingly-parallel loops, scientific kernels | Server threads, custom thread pools, irregular workloads |

Production parallel libraries often mix both — OpenMP for inner loops, Pthreads for thread-pool / event-loop scaffolding.

## Related concepts

- [[ImplicitThreading]] — the broader concept OpenMP exemplifies.
- [[SharedMemoryParallelism]] — the substrate OpenMP exploits.
- [[CacheCoherency]] / [[FalseSharing]] — hardware pathologies OpenMP code inherits from [[Pthreads]] code.
- [[AmdahlsLaw]] — caps OpenMP speedup just as it caps Pthreads speedup.
- [[GustafsonsLaw]] — the problem-scaling counter-argument.
- [[MPI]] — the explicit distributed-memory alternative OpenMP doesn't compete with.
- [[CUDA]] — GPU-side parallelism; orthogonal to OpenMP (though OpenMP 4.0+ supports GPU offload via `target` directives).

## Sources

- [[dis-14-7-openmp]] — DIS Ch 14.7 introduces OpenMP and the four core pragmas.
