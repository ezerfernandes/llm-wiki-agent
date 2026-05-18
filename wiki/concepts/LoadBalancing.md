---
title: "Load Balancing"
type: concept
tags: [parallel-computing, performance]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Load Balancing

The problem of **keeping all processors busy as much as possible** in a parallel computation. [[NormMatloff]] calls it *"arguably the most central performance issue"* in parallel processing ([[parproc-ch02-recurring-performance-issues]] §2.2): every idle processor is wasted capacity, and a parallel computation finishes only when its *slowest* processor finishes.

## The two regimes

Load imbalance is essentially a **variance problem on processor finish times**. There are two distinct sources:

1. **Task-time heterogeneity** — some tasks take longer than others. Example: in the Mandelbrot computation, points inside the set require many iterations while points outside bail out after a few. If you naïvely assign each thread a contiguous block of grid points and the in-set points happen to cluster (as they do in the left half of the Mandelbrot image), one thread will finish *much* later than the others.
2. **Assignment skew** — the *number* of tasks per thread is uneven by construction. Example: the mutual-outlinks computation in §2.4.3 has an inner loop `j = i+1...n-1`, so contiguous chunking of the outer `i` loop gives thread 0 way more work than thread 9.

## The headline result: static usually beats dynamic

[[parproc-ch02-recurring-performance-issues]] §2.4 argues, against the obvious intuition, that **[[StaticTaskAssignment|static assignment]] typically beats [[DynamicTaskAssignment|dynamic assignment]]** when tasks have i.i.d. times. If a chunk of $m$ tasks has total time with mean $m E[T_1]$ and variance $m \mathrm{Var}[T_1]$, then the coefficient of variation $\sigma/\mu$ shrinks as $O(1/\sqrt{m})$. For large chunks the chunk runtime is essentially constant, so there's nothing for a dynamic scheduler to balance — and meanwhile the dynamic scheduler pays continuous communication costs for its shared atomic counter.

When the i.i.d. assumption fails (Mandelbrot's spatial correlation; mutual outlinks' lower-triangular structure), the fix is **not** to switch to dynamic — it's to **randomize the chunk composition** (Method A') or **pair the chunks symmetrically** (the mutual-outlinks `0..499` + `9500..9999` trick). See §2.4.2 and §2.4.3.

## Empirical: Mandelbrot timings (8 threads, 8000×8000 grid)

| OpenMP policy | Time (s) | Notes |
|---|---|---|
| `static`     | 47.8 | Method A — contiguous chunks; bites on Mandelbrot's spatial correlation |
| `dynamic`    | 21.4 | shared atomic counter; better balance, contention cost |
| `guided`     | 29.6 | chunk size shrinks over time |
| `random`     | **15.7** | Method A' — randomized static, wins by 26% |

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source.
- [[CommunicationBottleneck]] — communication and load balancing are the two sides of the same coin: dynamic schedulers trade load imbalance for communication overhead.
- [[StaticTaskAssignment]] — the recommended default.
- [[DynamicTaskAssignment]] — the more flexible but more expensive alternative.
- [[WorkStealing]] — a dynamic-assignment variant ([[Cilk]]) where idle threads raid other threads' queues.
- [[EmbarrassinglyParallel]] — the term, in its modern meaning, *means* low communication, which is what makes static assignment work.
- [[MatrixVectorMultiply]] — the canonical static-vs-dynamic teaching example.
- [[OpenMP]] — exposes `static` / `dynamic` / `guided` / `runtime` schedules on `#pragma omp for`.
