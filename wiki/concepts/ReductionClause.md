---
title: "OpenMP reduction Clause"
type: concept
tags: [openmp, parallel-computing, reduction, aggregation]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP reduction Clause

`reduction(op:var)` ([[OpenMP]] §4.3.5) is the canonical mechanism for aggregating a per-iteration value across the threads of a parallel loop. Functionally it gives each thread a **private copy** of `var` (initialized to `op`'s identity element), lets each thread accumulate into its copy without contention, and then combines the copies into the shared `var` at the end of the construct — *"in an atomic manner"* (one combine per thread, not per iteration).

```c
int z;
#pragma omp for reduction(+:z)
for (i = 0; i < n; i++) z += x[i];
```

## Why it matters

[[parproc-ch04-introduction-to-openmp]]: *"By maintaining separate copies of `z` until the loop is done, we are reducing the number of serializing atomic actions, and are avoiding time-costly cache coherency transactions and the like."* The hand-rolled equivalent — `private(myz)` + `omp critical { z += myz; }` — works but is fussier.

Drop-in property: *"if we had old serial code that we wanted to parallelize, we would have to make no change to it!"* — just add the `reduction` clause to the `for` pragma.

## Eligible operators and identities

C/C++ allows `+ - * & | ^ && ||`. Each has a designated identity used as the per-thread initial value:

| operator | initial value |
|---|---|
| `+` | 0 |
| `-` | 0 |
| `*` | 1 |
| `&` | bit string of 1s |
| `\|` | bit string of 0s |
| `^` | 0 |
| `&&` | 1 |
| `\|\|` | 0 |

You may specify multiple reduction variables: `reduction(+:z, w)`.

## Restrictions (C/C++)

- Reduction variable must be **scalar**.
- Must be **shared** by the threads — the chapter notes the only acceptable way to do so in this case is to declare it as a **global** variable.
- C/C++ lacks `min` / `max` as operators, so no min/max reduction. The FORTRAN OpenMP binding does have `min` / `max` and allows **array** reduction variables.
- Footnote in §4.3.5: even with `min`/`max`, the Dijkstra example needs the *vertex attaining the minimum*, not just the minimum value — so `reduction` would not have helped.

## Examples in this book

- The [[MandelbrotSet|Mandelbrot]] inset count (§4.4): `#pragma omp parallel reduction(+:count)` followed by `#pragma omp for reduction(+:count)`.
- Jacobi linear-system solver (§11.5.4) — cross-referenced from §4.16 as the showcase example.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.3.5 source.
- [[ParallelFor]] — `reduction` parameterizes `#pragma omp for`.
- [[AtomicClause]] — what the reduction's final combine implicitly uses.
- [[CriticalSection]] — the hand-rolled alternative.
- [[FalseSharing]] — implicitly avoided by per-thread storage.
- [[MandelbrotSet]] — §4.4 example.
