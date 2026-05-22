---
title: "#pragma omp parallel"
type: concept
tags: [parallel-programming, openmp, compiler-directives]
sources: [dis-14-7-openmp]
last_updated: 2026-05-18
---

# `#pragma omp parallel`

The foundational [[OpenMP]] pragma — **creates a team of threads** that execute the following structured block concurrently. Every thread in the team runs the entire block; the implicit barrier at the end of the block joins them.

## Syntax

```c
#pragma omp parallel [clauses]
{
    /* code executed by every thread in the team */
}
```

Common clauses: `num_threads(N)`, `private(...)`, `shared(...)`, `firstprivate(...)`, `default(shared|none)`, `if(cond)`, `reduction(op:var)`.

## Semantics

- **Thread count**: defaults to `OMP_NUM_THREADS` (env var) or the number of cores. Override with `num_threads(N)`.
- **Replicated execution**: every thread in the team executes the block — **not** a work-share. To split work, use [[OpenMPForPragma|`#pragma omp for`]] inside the parallel region, or use the combined [[OpenMPParallelForPragma|`#pragma omp parallel for`]].
- **Implicit barrier**: at the closing `}`, all threads synchronize before the master thread continues.
- **Thread-id query**: inside the region, `omp_get_thread_num()` returns the calling thread's 0-based ID; `omp_get_num_threads()` returns the team size.

## Typical pattern

```c
#pragma omp parallel
{
    int tid = omp_get_thread_num();
    printf("Hello from thread %d\n", tid);
}
```

Prints one line per thread in nondeterministic order.

## Related

- [[OpenMP]] — parent concept.
- [[OpenMPForPragma]] — sibling work-share pragma (typically nested inside `parallel`).
- [[OpenMPParallelForPragma]] — combined `parallel` + `for` shortcut.
- [[OpenMPCriticalPragma]] — mutual exclusion inside a parallel region.
- [[ParallelPragma]] — pre-existing wiki anchor for the same pragma.
- [[dis-14-7-openmp]] — DIS introduction.
