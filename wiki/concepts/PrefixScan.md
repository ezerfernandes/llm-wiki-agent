---
title: "Prefix Scan"
type: concept
tags: [parallel-computing, algorithm, scan, thrust, cuda, openmp]
sources: [parproc-ch05-cuda-gpu-programming, parproc-ch06-thrust-programming, parproc-ch10-parallel-prefix-problem]
last_updated: 2026-05-17
---

# Prefix Scan

A core parallel primitive: given an array $a_0, a_1, ..., a_{n-1}$ and a binary associative operator $\oplus$, produce the array of running results.

- **Inclusive scan**: $b_i = a_0 \oplus a_1 \oplus \cdots \oplus a_i$.
- **Exclusive scan** (a.k.a. prescan): $b_i = a_0 \oplus a_1 \oplus \cdots \oplus a_{i-1}$ (with $b_0 = $ identity).

When $\oplus$ is $+$, prefix scan is also called **prefix sum** or **cumulative sum**.

The operator must be associative but need **not** be commutative. Elements need not be scalars — [[parproc-ch10-parallel-prefix-problem]] §10.1 uses permutation matrices with matrix multiplication as $\oplus$.

## Why it matters

Prefix scan admits a parallel implementation with $O(\log n)$ depth (span), making a superficially sequential problem tractable in parallel. It appears as a subroutine in [[StreamCompaction|stream compaction]], radix sort, sparse-matrix operations, histogram-to-offset conversion, [[RunLengthEncoding|run-length decompression]], [[MovingAverage|moving average]], and edge-list construction — anywhere per-element counts must be converted to starting positions.

[[parproc-ch05-cuda-gpu-programming]] §5.11 (Finding Cumulative Sums) covers it as a CUDA worked example using a single block: each thread computes the scan of its own contiguous chunk; `__syncthreads()`; thread `i > 0` adds the sum of all preceding chunks' high values to every element of its chunk. The multi-block / general case is addressed in Ch10.

## Parallel Algorithms

### Hillis-Steele (data-parallel, n = p)

The [[HillisSteeleScan|Hillis-Steele]] algorithm works in $\log_2 n$ rounds when one thread is available per element ([[parproc-ch10-parallel-prefix-problem]] §10.2):

- Round 1: each position $j$ adds the element 1 step to its left.
- Round 2: each position $j$ adds the element 2 steps to its left.
- Round $k$: each position $j \geq 2^{k-1}$ adds the element $2^{k-1}$ steps to its left.

After $\log_2 n$ rounds, every position holds the inclusive prefix sum of all elements up to and including itself.

**Cost**: depth $O(\log n)$, but total work is $O(n \log n)$ — worse than the sequential $O(n)$. Load balancing degrades each round (more threads idle). An auxiliary **red/black** double-buffer must alternate between odd and even steps to avoid read-before-write hazards.

### Blelloch (work-efficient, two-pass)

The [[BlellochScan|Blelloch]] algorithm (also called up-sweep/down-sweep or reduce-then-scan) runs in two tree-traversal passes over the array:

1. **Up-sweep (reduce)**: build a binary tree of partial sums bottom-up in $O(\log n)$ steps — $O(n)$ total work.
2. **Down-sweep**: propagate prefix values back down the tree in $O(\log n)$ steps — $O(n)$ total work.

Total work is $O(n)$, matching sequential complexity while maintaining $O(\log n)$ depth. This is the work-efficient counterpart to Hillis-Steele; preferred for GPU implementations where total work determines throughput.

### Blocked strategy (n > p)

When there are more data elements than threads, the standard three-phase approach ([[parproc-ch10-parallel-prefix-problem]] §10.2, [[parproc-ch05-cuda-gpu-programming]] §5.11):

1. Each of $p$ threads serially scans its contiguous chunk of $n/p$ elements — $O(n/p)$ per thread.
2. The $p$ rightmost chunk elements form array $G$; apply a parallel scan to $G$ — $O(\log p)$ depth.
3. Thread $i > 0$ adds $G[i-1]$ to every element in its chunk — $O(n/p)$ per thread.

Total time: $O(n/p + \log p)$. This is the strategy used in the [[OpenMP]] implementation of §10.4.

## In [[Thrust]]

Thrust exposes the primitive as one-line algorithm calls ([[parproc-ch06-thrust-programming]] §6.11):

```cpp
#include <thrust/scan.h>

thrust::inclusive_scan(hx.begin(), hx.end(), hx.begin());
// in-place inclusive prefix sum (default op is +)

thrust::exclusive_scan(begin, end, out);
// exclusive variant

thrust::inclusive_scan(begin, end, out, thrust::multiplies<T>());
// custom associative op
```

> *"Thrust includes functions for prefix scan (see Chapter 10)."* ([[parproc-ch06-thrust-programming]] §6.11)

Applied examples: [[RunLengthEncoding|run-length decompression]] (§10.6) and [[MovingAverage|moving average]] (§10.7) in [[parproc-ch10-parallel-prefix-problem]].

## Platform Support

| Platform | API |
|---|---|
| MPI | `MPI_Scan()` (max, min, sum, product, etc.) |
| Intel TBB | built-in prefix scan |
| Thrust (CUDA / OpenMP) | `thrust::inclusive_scan()`, `thrust::exclusive_scan()` |
| CUDPP | CUDA Data Parallel Primitives Library; scan-based sorting |

([[parproc-ch10-parallel-prefix-problem]] §10.3)

## Applications

- **[[StreamCompaction]]**: exclusive scan of boolean indicators → write-position offsets.
- **[[RunLengthEncoding|Run-length decompression]]**: exclusive scan of run-counts → start offsets; fill runs in parallel.
- **[[MovingAverage]]**: exclusive cumulative sum of input; $a_i = (c_i - c_{i-w}) / w$.
- **Histogram to offset**: convert per-bin counts to bin start indices.
- **Radix sort**: scan of per-digit counts for output-position computation.
- **Sparse matrix operations**: row-pointer array construction from per-row nnz counts.

## Two-phase usage pattern

A standard pattern (visible across CUDA / Thrust / OpenMP implementations):

1. **Per-element work** produces a count or indicator value at position `i`.
2. **Exclusive scan** of those values produces the **starting offset** for element `i`'s output.
3. **Per-element finalization** writes results into the output array at its computed offset.

This is the structure of [[parproc-ch05-cuda-gpu-programming]] §5.13's adjacency-matrix transformation and of [[StreamCompaction]] problems generally.

## See also

- [[HillisSteeleScan]] — the $\log_2 n$-round data-parallel algorithm.
- [[BlellochScan]] — the work-efficient two-pass algorithm.
- [[Thrust]] — `inclusive_scan` / `exclusive_scan`.
- [[StreamCompaction]] — canonical application.
- [[RunLengthEncoding]] — §10.5–10.6 application.
- [[MovingAverage]] — §10.7 application.
- [[parproc-ch05-cuda-gpu-programming]] — §5.11 (CUDA single-block implementation).
- [[parproc-ch06-thrust-programming]] — §6.11 (Thrust API).
- [[parproc-ch10-parallel-prefix-problem]] — §10.2–10.7 (algorithms, OpenMP/Thrust implementations, applications).
- [[ParallelComputing]] — domain.
