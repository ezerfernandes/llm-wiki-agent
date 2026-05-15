---
title: "ODS Ch.11: Sorting Algorithms"
type: source
tags: [book, algorithms, sorting]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 11
pages: "217-238"
---

## Summary
Two parts. **Comparison-based sorting**: merge-sort, quicksort, heap-sort — three asymptotically-optimal Θ(n log n) algorithms whose lower bound is matched by the information-theoretic comparison-tree argument (Theorem at §11.1.4: any comparison sort makes Ω(n log n) comparisons in the worst case). **Non-comparison sorting**: counting sort and radix sort use array indexing on integer keys to break the n log n barrier — counting sort is O(n + U) for keys in {0, ..., U−1}; radix sort applied k times sorts integers in {0, ..., n^c − 1} in O(c·n) time.

## Key Claims
- **Merge-sort** runs in Θ(n log n) by divide-and-conquer recurrence. Theorem 11.1: at most n log n comparisons. Proof goes through the recursion tree (Figure 11.2).
- **Quicksort** uses a random pivot for expected Θ(n log n) — analysis via the same harmonic-number argument as [[ods-07-random-binary-search-trees]] (the recursion tree is *exactly* a random binary search tree built from input).
- **Heap-sort** = build BinaryHeap in O(n) + extract-min n times — Θ(n log n), in-place when reusing the input array.
- **Lower bound** on comparison-based sorting (§11.1.4): the decision tree for any comparison sort has n! leaves; minimum height = log(n!) = Θ(n log n) by Stirling. So no comparison sort beats Θ(n log n).
- **Counting sort**: for keys in {0,...,U−1}, count occurrences in O(n+U), then write keys back in sorted order. Linear when U = O(n).
- **Radix sort**: apply counting sort k times, once per digit, from least to most significant. For integer keys in {0,...,n^c − 1} with base n, total time is O(c·n).

## Key Quotes
> "If we allow other operations besides comparisons, then all bets are off. Indeed, by using array indexing, it is possible to sort a set of n integers in the range {0,...,n^c − 1} in O(cn) time."
> "No algorithm that uses only comparisons can avoid doing roughly n log n comparisons in the worst case and even the average case."

## Connections
- [[ods-07-random-binary-search-trees]] — quicksort recursion tree is a random BST.
- [[ods-10-heaps]] — heap-sort uses BinaryHeap.
- [[ods-06-binary-trees]] — comparison-tree lower-bound argument.
- [[ods-13-data-structures-for-integers]] — radix-sort intuition extends to BinaryTrie indexing.
- [[factorial]] / [[logarithms]] — Stirling's approximation grounds the n log n lower bound.

## Contradictions
None.
