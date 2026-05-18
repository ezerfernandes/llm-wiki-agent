---
title: "Matrix-Vector Multiply"
type: concept
tags: [parallel-computing, linear-algebra, algorithms]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch02-recurring-performance-issues, parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Matrix-Vector Multiply

The computation $Y = AX$ for an $n \times n$ matrix $A$ and a length-$n$ vector $X$. The single most-used **running example** in *Programming on Parallel Machines* — it appears in both [[parproc-ch01-intro-parallel-processing|Chapter 1]] (as a [[Snow]] / R `clusterApply` demo) and [[parproc-ch02-recurring-performance-issues|Chapter 2]] (as the canonical task-assignment teaching example).

## Why it's the canonical example

Three properties make matrix-vector multiply nearly perfect for didactic purposes:

1. **[[EmbarrassinglyParallel|Embarrassingly parallel]] under both old and new meanings** — each row of $A$ is multiplied by $X$ independently. No cross-thread coordination needed within a single multiply.
2. **Tunable per-task cost** — choosing $n$ sets per-row work, and choosing chunk size sets per-chunk work. Convenient for illustrating the $O(1/\sqrt{m})$ chunk-time concentration argument.
3. **Easy to set up multiple decomposition strategies** — by rows, by row blocks, by columns of $A$, etc.

## In Chapter 2

[[parproc-ch02-recurring-performance-issues]] §2.4.1 uses **10000 rows, 10 threads** as a concrete sandbox to walk through every method:

- **Method A** (static, contiguous): thread 0 gets rows 0..999, thread 1 gets 1000..1999, etc. OpenMP `schedule(static)` default.
- **Method B** (dynamic): shared atomic `nextchunk` counter; each thread fetch-and-increments to claim its next row. OpenMP `schedule(dynamic)`.
- **Method C** (guided): chunk size shrinks over time. OpenMP `schedule(guided)`.
- **Method A'** (randomized static): generate a random permutation of `0..9999`, assign thread $k$ rows $i_{1000k}..i_{1000k+999}$. Still static (randomization is done before computation begins).

The conclusion: for genuinely i.i.d. per-row times, Method A's $O(1/\sqrt{m})$ concentration of total chunk runtime means there is essentially no load imbalance to fix — so the communication-free Method A wins. When task times are correlated within contiguous chunks (Mandelbrot, mutual outlinks), Method A' restores the i.i.d. property.

## In Chapter 1

[[parproc-ch01-intro-parallel-processing]] uses matrix-vector multiply as the R / [[Snow]] example: `clusterApply` to scatter blocks of rows to worker R processes, multiply, and gather the result.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.4 task-assignment teaching example.
- [[parproc-ch01-intro-parallel-processing]] — secondary source, R/snow worked example.
- [[StaticTaskAssignment]] — the canonical use case.
- [[DynamicTaskAssignment]] — the contrasted alternative.
- [[LoadBalancing]] — what the worked example is illustrating.
- [[EmbarrassinglyParallel]] — what makes the example work.
- [[Snow]] — R package used in the Ch1 version.
- [[OpenMP]] — used in the Ch2 version (implicitly — `#pragma omp for schedule(...)`).
- [[ScatterGather]] — the manager/worker paradigm under which scatter-the-rows / gather-the-results fits.
