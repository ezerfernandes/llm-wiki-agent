---
title: "BitonicMergesort"
type: concept
tags: [algorithm, sorting, parallel-computing, sorting-network]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# BitonicMergesort

A parallel sorting algorithm based on the structural properties of bitonic sequences and [[CompareExchange]] operations. Sorts n elements (n a power of 2) in O(log² n) parallel steps.

## Bitonic Sequences

A sequence (a₀, a₁, …, a_{k-1}) is **bitonic** if either:
- (a) It is first nondecreasing then nonincreasing: a₀ ≤ a₁ ≤ … ≤ a_r ≥ a_{r+1} ≥ … ≥ a_{n-1}
- (b) It can be converted to form (a) by rotation (moving the last k elements from the right end to the left end).

Examples: (3,8,12,15,14,5,1,2) is bitonic by condition (b). V-shape sequences like (12,5,2,8,20) are bitonic (they can be rotated to form (2,8,20,12,5), an A-shape). Any 2-element array is bitonic.

## Sorting a Bitonic Sequence

Given a bitonic sequence of length k (k a power of 2), perform pairwise compare-exchanges between a_i and a_{n/2+i} for i = 0, …, n/2-1. The resulting lower half (a₀, …, a_{k/2-1}) and upper half (a_{k/2}, …, a_{k-1}) are both bitonic, and every element of the lower half ≤ every element of the upper half. Recurse:

```c
// x is bitonic of length n, n a power of 2
void sortbitonic(int *x, int n) {
    // do the pairwise compare-exchange operations
    if (n > 2) {
        sortbitonic(x, n/2);
        sortbitonic(x + n/2, n/2);
    }
}
```

## Sorting a General Sequence

Build successively larger bitonic sequences from the input:

1. For each i = 0, 2, 4, …, n-2: each pair (a_i, a_{i+1}) is trivially bitonic. Apply `sortbitonic()` to it (a single compare-exchange). If i/2 is odd, reverse the pair so that this pair and the preceding pair form a 4-element bitonic sequence.
2. For each i = 0, 4, 8, …, n-4: apply `sortbitonic()` to (a_i, a_{i+1}, a_{i+2}, a_{i+3}). If i/4 is odd, reverse the quartet so it and the preceding quartet form an 8-element bitonic sequence.
3. Continue doubling the group size until a single sorted n-element list results.

## Parallelization

Each level of the construction can be executed in parallel: all pairs, then all quartets, etc. In the hypercube setting, the algorithm performs compare-exchanges with all neighbors in the same pattern as [[Hyperquicksort]].

## Connections

- [[CompareExchange]] — the primitive operation; bitonic mergesort is a network of compare-exchanges.
- [[MergeSort]] — related sorting family; bitonic mergesort is a network-based parallel variant.
- [[Hyperquicksort]] — similar hypercube compare-exchange pattern.
- [[parproc-ch12-parallel-sorting]] — §12.2.5 source.
