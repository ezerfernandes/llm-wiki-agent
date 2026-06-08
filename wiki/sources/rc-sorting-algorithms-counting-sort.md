---
title: "Sorting algorithms/Counting sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Counting_sort
---

## Summary
The task is to implement counting sort, a non-comparison sorting method for integers whose minimum and maximum values are known (or computed beforehand). It tallies how many times each value in the range appears, then reconstructs the array in order from those counts. The key insight is that it runs in O(n + k) time (k being the value range) but its memory cost scales with that range, so it is only practical when the spread of values is small.

## Task Requirements
- Implement counting sort over an array of integers.
- Allocate a count array of size (max - min + 1), initialized to zero.
- Increment count[number - min] for each element in the input.
- Reconstruct the sorted array by emitting each value i (from min to max) count[i - min] times.
- Min and max may be supplied a priori or computed from the data; note the memory blowup for wide ranges and the sparse-array mitigation.

## Language Coverage
89 languages implement this task, spanning systems, scripting, functional, and assembly languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Racket, Common Lisp, and 360 Assembly.

## Connections
- [[CountingSort]] — the algorithm itself
- [[SortingAlgorithms]] — the broader category of ordering methods
- [[NonComparisonSort]] — class of sorts that avoid element comparisons
- [[RadixSort]] — uses counting sort as a stable per-digit subroutine
- [[TimeComplexity]] — O(n + k) runtime versus O(k) auxiliary space tradeoff

## Contradictions
- None — reference task page.
