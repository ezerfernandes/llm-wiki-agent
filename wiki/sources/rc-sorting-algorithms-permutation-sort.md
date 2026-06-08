---
title: "Sorting algorithms/Permutation sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Permutation_sort
---

## Summary
The task asks the programmer to implement permutation sort, a deliberately inefficient sorting method that works by enumerating permutations of the input list until it stumbles upon one that is already in order. The key insight is that it is a brute-force, generate-and-test algorithm with factorial-time worst-case behavior, valued for pedagogy and contrast rather than practical use.

## Task Requirements
- Generate the possible permutations of the input array/list one at a time.
- After each permutation, test whether the list is in order.
- Stop and return the result once a sorted permutation is found.
- Follows the pseudocode: while the list is not in order, advance to the next permutation.

## Language Coverage
69 languages implement this task, spanning functional, imperative, assembly, and scripting paradigms. Representative implementations include C, C++, Python, Haskell, Java, Rust, Go, Ruby, Common Lisp, and ARM Assembly.

## Connections
- [[SortingAlgorithm]] — permutation sort is one of the canonical comparison sorts in the Rosetta Code sorting series.
- [[Permutation]] — the algorithm's core operation is enumerating permutations of the list.
- [[Combinatorics]] — its factorial complexity stems from the combinatorial number of orderings.
- [[BruteForceSearch]] — it is a generate-and-test brute-force method over all arrangements.
- [[BogosortComparison]] — closely related in spirit to randomized "bogosort" but systematic in its enumeration.

## Contradictions
- None — reference task page.
