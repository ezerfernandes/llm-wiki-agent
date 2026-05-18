---
title: "Blelloch Scan"
type: concept
tags: [parallel-computing, algorithm, prefix-scan, work-efficient]
sources: [parproc-ch10-parallel-prefix-problem]
last_updated: 2026-05-17
---

# Blelloch Scan

A work-efficient parallel algorithm for computing a [[PrefixScan|prefix scan]] in two tree-traversal passes, attributed to Guy Blelloch. Also called **up-sweep/down-sweep scan** or **reduce-then-scan**. Unlike [[HillisSteeleScan|Hillis-Steele]], it performs $O(n)$ total work — matching the sequential baseline — at the cost of two passes.

## Algorithm

### Pass 1: Up-sweep (reduce)

Build a binary reduction tree bottom-up over the $n$-element array. At level $d$ (0-indexed from the leaves), pairs of elements separated by $2^d$ are summed into the right element of the pair. After $\log_2 n$ levels, the root (last element) holds the total sum of all elements.

### Pass 2: Down-sweep

Set the root to the identity element (e.g., 0 for addition). Then sweep back down the tree: at each node, the left child keeps its value and the right child receives the left child's value XOR'ed/combined with the current node's value. After $\log_2 n$ levels, each element holds its exclusive prefix sum.

For an inclusive scan, add the original values back at the end.

## Complexity

| Dimension | Cost |
|---|---|
| Depth (span) | $O(\log n)$ |
| Total work | $O(n)$ |
| Sequential baseline | $O(n)$ |
| Passes | 2 |

Total work matches the sequential $O(n)$ algorithm, making this **work-efficient**. Each pass does $n - 1$ operations.

## Comparison with Hillis-Steele

| Property | [[HillisSteeleScan\|Hillis-Steele]] | Blelloch |
|---|---|---|
| Depth | $O(\log n)$ | $O(\log n)$ |
| Work | $O(n \log n)$ | $O(n)$ |
| Passes | 1 | 2 |
| Load balance | Poor | Better |
| GPU preference | Simpler to code | Standard for large n |

The CUDPP library and NVIDIA's reference GPU scan use Blelloch-style two-pass scan. [[HillisSteeleScan|Hillis-Steele]] is used when n is small or simplicity is paramount.

## Note on Ch10

[[parproc-ch10-parallel-prefix-problem]] does not explicitly name the Blelloch algorithm. Ch10's §10.2 presents the [[HillisSteeleScan|Hillis-Steele]] approach for n = p, and the three-phase blocked strategy for n > p. This page is included for completeness and cross-reference from [[PrefixScan]].

## See also

- [[PrefixScan]] — the general primitive; algorithm comparison table.
- [[HillisSteeleScan]] — the simpler $O(n \log n)$ work alternative.
- [[parproc-ch10-parallel-prefix-problem]] — §10.2 (context; CUDPP reference in §10.3).
