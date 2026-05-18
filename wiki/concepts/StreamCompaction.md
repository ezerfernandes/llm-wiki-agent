---
title: "Stream Compaction"
type: concept
tags: [parallel-computing, algorithm, prefix-scan, thrust, cuda]
sources: [parproc-ch10-parallel-prefix-problem, parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Stream Compaction

A parallel primitive that removes unwanted elements from an array (or, equivalently, packs selected elements into a compact output array) in parallel. Also called **filter** or **select**.

## The core pattern

Given input array $x$ and a predicate $p$, produce output $y$ containing only elements where $p(x_i) = \text{true}$, in the original order.

The naive sequential approach scans $x$ left-to-right and appends matching elements. The parallel approach uses [[PrefixScan|prefix scan]] to determine write positions without sequential dependencies:

1. **Evaluate predicate**: compute indicator array $v_i = p(x_i) \in \{0, 1\}$.
2. **Exclusive scan** of $v$: gives the write offset $o_i$ for each selected element.
3. **Scatter**: for each $i$ where $v_i = 1$, write $x_i$ to $y[o_i]$.

Steps 1 and 3 are embarrassingly parallel; step 2 is a standard prefix scan ($O(\log n)$ depth, $O(n)$ work with [[BlellochScan|Blelloch]]).

## In Thrust

`thrust::copy_if` implements stream compaction directly:

```cpp
// Copy elements of dx where iseven predicate is true
auto newend = thrust::copy_if(dx.begin(), dx.end(),
                              seq.begin(),       // stencil
                              out.begin(),
                              iseven());
```

Used in [[parproc-ch10-parallel-prefix-problem]] §10.6 to extract run-counts from interleaved run-length data.

`thrust::remove_if` performs in-place compaction (removes elements matching a predicate).

## Applications

- [[RunLengthEncoding|Run-length decompression]]: extract run-counts from interleaved compressed array.
- Adjacency-matrix transformation: retain only non-zero edges (§5.13 in [[parproc-ch05-cuda-gpu-programming]]).
- Particle simulation: remove out-of-bounds particles.
- Ray tracing: discard rays that miss all geometry.
- Sparse-matrix construction: compact non-zeros from a dense array.

## Relationship to prefix scan

Stream compaction is one of the canonical applications of [[PrefixScan|prefix scan]]. The scan converts per-element boolean indicators (or counts) into write positions, enabling conflict-free parallel scatter. This relationship is why stream compaction is featured prominently in [[parproc-ch10-parallel-prefix-problem]] §10.6 and in CUDA textbooks.

## See also

- [[PrefixScan]] — the primitive underlying stream compaction.
- [[RunLengthEncoding]] — application in §10.5–10.6.
- [[Thrust]] — `copy_if`, `remove_if`.
- [[parproc-ch10-parallel-prefix-problem]] — §10.6.
- [[parproc-ch05-cuda-gpu-programming]] — §5.13 (adjacency-matrix compaction).
