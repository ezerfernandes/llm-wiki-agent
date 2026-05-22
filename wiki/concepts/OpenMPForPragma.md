---
title: "#pragma omp for"
type: concept
tags: [parallel-programming, openmp, compiler-directives, work-sharing]
sources: [dis-14-7-openmp]
last_updated: 2026-05-18
---

# `#pragma omp for`

The [[OpenMP]] **work-sharing** pragma — distributes the iterations of the following `for` loop across the threads in an enclosing [[OpenMPParallelPragma|parallel region]]. It does **not** spawn threads by itself; it must appear inside a `#pragma omp parallel` block (or use the combined [[OpenMPParallelForPragma|`#pragma omp parallel for`]] shortcut).

## Syntax

```c
#pragma omp parallel
{
    #pragma omp for [clauses]
    for (int i = 0; i < N; i++) {
        /* iteration body */
    }
}
```

## Default scheduling — static chunking

*"The `omp for` pragma uses static chunking as its default scheduling method, distributing loop iterations evenly across threads beforehand"* ([[dis-14-7-openmp|DIS Ch 14.7]]). With `T` threads and `N` iterations, each thread receives a contiguous chunk of roughly `N/T` iterations, assigned before the loop runs.

## Alternative schedules

Via the [[ScheduleClause|`schedule(kind[, chunk])`]] clause:

| Kind | Behavior |
|---|---|
| `static` | Default; equal contiguous chunks, assigned ahead of time. |
| `static, chunk` | Round-robin chunks of size `chunk`. |
| `dynamic[, chunk]` | First-come-first-served; threads request chunks as they finish. Good for variable per-iteration cost. |
| `guided[, chunk]` | Like `dynamic` but chunk size shrinks over time. |
| `runtime` | Defer to `OMP_SCHEDULE` env var. |
| `auto` | Compiler / runtime chooses. |

## Loop-form requirements

OpenMP requires loops with **canonical form** — countable from the headers (initialization, condition, increment all syntactically simple integer / pointer / random-access-iterator operations). `while` loops and irregular `for` loops cannot be parallelized with `omp for`; use [[OpenMPTaskDirective|`#pragma omp task`]] instead.

## Implicit barrier

A barrier is implicit at the end of `omp for` — all threads wait before continuing. Suppress with the `nowait` clause when the next region is independent.

## Related

- [[OpenMP]] — parent concept.
- [[OpenMPParallelPragma]] — required enclosing region.
- [[OpenMPParallelForPragma]] — combined shortcut.
- [[ScheduleClause]] — schedule selector.
- [[OpenMPTaskDirective]] — task-parallel alternative for non-canonical loops.
- [[dis-14-7-openmp]] — DIS introduction.
