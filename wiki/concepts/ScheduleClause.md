---
title: "OpenMP schedule Clause"
type: concept
tags: [openmp, parallel-computing, scheduling, load-balancing]
sources: [parproc-ch04-introduction-to-openmp, parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# OpenMP schedule Clause

`schedule(kind[,chunk])` is the [[OpenMP]] clause that controls the iteration→thread mapping for [[ParallelFor|`#pragma omp for`]]. Without it, the standard leaves the mapping unspecified. [[parproc-ch04-introduction-to-openmp]] §4.3.3 enumerates four kinds:

| kind | behavior | default chunk |
|---|---|---|
| `static` | round-robin chunks, fixed at compile time | `n / nth` |
| `dynamic` | work-queue; threads request next chunk when done | 1 |
| `guided` | dynamic with chunk size *decreasing* over time | — |
| `runtime` | defer choice to `omp_set_schedule()` or `OMP_SCHEDULE` env var | — |

```c
#pragma omp for schedule(static)
#pragma omp for schedule(static, 20)
#pragma omp for schedule(dynamic)
#pragma omp for schedule(guided)
#pragma omp for schedule(runtime)
```

## The big-chunk / small-chunk tradeoff

The chapter's framing (§4.3.3 / §4.4 / §2.4):
- **Large chunks** → less overhead (fewer trips through the runtime's critical section per chunk hand-off).
- **Small chunks** → better tail-end load balance (no thread sits idle while another finishes a giant last chunk).

`guided` is the structural answer: start big, end small, so amortize early and balance late.

## Runtime selection

- `omp_set_schedule(omp_sched_static, chunk)` at runtime, paired with `#pragma omp for schedule(runtime)`.
- Or `setenv OMP_SCHEDULE "static,20"` (csh) / `export OMP_SCHEDULE=static,20`.

Compile-time `schedule(static, chunk)` is *not* runtime-tunable — the chunk argument is fixed at compile time. Use `schedule(runtime)` if you want to vary it.

## Schedule × Mandelbrot

The recurring example: [[Mandelbrot]] set computation on an 8000×8000 grid, two threads.
- `static` 47.8s — most Mandelbrot points lie left-of-center; thread 0 spends all its time iterating long orbits while thread 1 sits idle.
- `dynamic` 21.4s — work-queue compensates by giving thread 1 fast rows from thread 0's region.
- `guided` 29.6s.
- Randomized [[StaticTaskAssignment|static]] (Method A' from Ch2) — 15.7s, the winner.

[[parproc-ch02-recurring-performance-issues]] uses these numbers to argue that randomized static beats dynamic; [[parproc-ch04-introduction-to-openmp]] §4.4 reproduces them under explicit `#ifdef STATIC|DYNAMIC|GUIDED|RC` switches.

## Connections
- [[OpenMP]] — parent.
- [[ParallelFor]] — `schedule` parameterizes `#pragma omp for`.
- [[parproc-ch04-introduction-to-openmp]] — §4.3.3 / §4.4 source.
- [[parproc-ch02-recurring-performance-issues]] — Ch2 supplies the timing argument the schedule clause operationalizes.
- [[LoadBalancing]] — the clause's purpose.
- [[StaticTaskAssignment]] / [[DynamicTaskAssignment]] — `schedule(static)` vs `schedule(dynamic)`.
- [[MandelbrotSet]] — the canonical worked example.
