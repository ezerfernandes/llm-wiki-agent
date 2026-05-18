---
title: "OpenMP for Pragma (parallel for)"
type: concept
tags: [openmp, parallel-computing, pragma, loops]
sources: [parproc-ch04-introduction-to-openmp]
last_invoked: 2026-05-17
last_updated: 2026-05-17
---

# OpenMP for Pragma

`#pragma omp for` is the [[OpenMP]] [[WorkSharing|work-sharing]] construct that distributes the iterations of an immediately-following C/C++ `for` loop across the threads of the surrounding team.

```c
#pragma omp parallel
{
    #pragma omp for
    for (i = 1; i < nv; i++) {
        if (mind[mv] + ohd[mv*nv+i] < mind[i])
            mind[i] = mind[mv] + ohd[mv*nv+i];
    }
}
```

## Rules

- **Iterations must be independent** ([[parproc-ch04-introduction-to-openmp]] §4.3): *"one iteration cannot depend on the result of another."* No cross-iteration writes to shared state without `reduction` / `atomic` / `critical`.
- **Loop index is private by default.** *"For obvious reasons OpenMP treats the loop index, `i` here, as private even if by context it would be shared"* (§4.3.1).
- **Implicit barrier** at the end of the `for` block. Override with `nowait`.
- **Must be inside a `parallel`** (or use the combined `#pragma omp parallel for`).

## Nested loops & `collapse(N)`

By default `for` parallelizes only the outermost loop. To parallelize multiple levels:
- Insert another `#pragma omp for` inside (requires a nested `parallel` or specific runtime support), or
- Since OpenMP 3.0: `#pragma omp parallel for collapse(2)` flattens 2 levels of nesting before assigning iterations to threads.

## Schedule control

The default thread-to-iteration mapping is unspecified by the OpenMP standard. Use a [[ScheduleClause|`schedule` clause]] to control it:

```c
#pragma omp for schedule(static)
#pragma omp for schedule(dynamic, 100)
#pragma omp for schedule(guided)
#pragma omp for schedule(runtime)
```

## Combined form

`#pragma omp parallel for` collapses team-spawning + work-distribution into one directive — convenient when the `parallel` region contains nothing besides the loop.

## Reduction interplay

For loops that need cross-iteration aggregation (sum, product, …), pair `for` with the [[ReductionClause|`reduction` clause]]:

```c
#pragma omp parallel for reduction(+:count)
for (x = 0; x < nptsside; x++) {
    // ...
    if (inset(z)) count++;
}
```

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.3 source.
- [[WorkSharing]] — `for` is the headline work-sharing construct.
- [[ParallelPragma]] — required outer team-spawning directive.
- [[ScheduleClause]] — controls iteration→thread mapping.
- [[ReductionClause]] — pairs with `for` for aggregation.
- [[Barrier]] — implicit at the end of `for`.
- [[LoadBalancing]] — the `schedule` clause's reason for being.
