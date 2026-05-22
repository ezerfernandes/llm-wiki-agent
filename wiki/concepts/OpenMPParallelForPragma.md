---
title: "#pragma omp parallel for"
type: concept
tags: [parallel-programming, openmp, compiler-directives, work-sharing]
sources: [dis-14-7-openmp]
last_updated: 2026-05-18
---

# `#pragma omp parallel for`

The **combined** [[OpenMP]] pragma — equivalent to `#pragma omp parallel` immediately followed by `#pragma omp for`. The single most common OpenMP idiom: parallelize one loop in one line.

## Syntax

```c
#pragma omp parallel for [clauses]
for (int i = 0; i < N; i++) {
    a[i] = b[i] + c[i];
}
```

The compiler spawns a team of threads (per [[OpenMPParallelPragma|`parallel`]]) AND distributes the loop iterations across the team (per [[OpenMPForPragma|`for`]]) — both in one declaration. At the loop's end, threads synchronize at the implicit barrier and the master thread continues serial execution.

## Clause vocabulary

All clauses valid on `parallel` (`num_threads`, `private`, `shared`, `default`, `firstprivate`, `if`) and on `for` ([[ScheduleClause|`schedule`]], `nowait`, `collapse`, `ordered`) are accepted. The most-used reduction pattern:

```c
double sum = 0;
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < N; i++) {
    sum += a[i];
}
```

`reduction(+:sum)` gives each thread a **private** zero-initialized accumulator; at the end of the loop, all threads' partials are combined with `+` into the shared `sum`. The structurally correct way to accumulate across iterations without a [[OpenMPCriticalPragma|critical section]] or [[Mutex|mutex]].

## When to use it

Embarrassingly-parallel loops with independent iterations and uniform per-iteration cost. Examples:

- Vector operations (`a[i] = b[i] + c[i]`).
- Pointwise transforms (`y[i] = sigmoid(x[i])`).
- Independent simulations / Monte Carlo trials.

For non-uniform cost, add [[ScheduleClause|`schedule(dynamic, k)`]]. For loops with dependencies, refactor or use [[OpenMPTaskDirective|`#pragma omp task`]].

## Related

- [[OpenMP]] — parent concept.
- [[OpenMPParallelPragma]] / [[OpenMPForPragma]] — the two pragmas this combines.
- [[ScheduleClause]] — loop-distribution selector.
- [[OpenMPCriticalPragma]] — alternative for non-reducible per-iteration shared writes.
- [[ParallelPragma]] — pre-existing wiki anchor.
- [[dis-14-7-openmp]] — DIS introduction.
