---
title: "Sorting algorithms/Stooge sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Stooge_sort
---

## Summary
The task asks the programmer to implement Stooge sort, a recursive comparison sort applied to an array of integers. The key insight is its deliberately inefficient divide-and-conquer structure: after swapping the first and last elements if they are out of order, it recursively sorts the initial two-thirds, then the final two-thirds, then the initial two-thirds again. This triple recursion on overlapping two-thirds slices makes it notoriously slow, with a time complexity of roughly O(n^2.71).

## Task Requirements
- Implement the Stooge sort algorithm and demonstrate it on an array of integers.
- Follow the given pseudocode: take the array `L` with indices `i` (default 0) and `j` (default length-1).
- If `L[j] < L[i]`, swap those two elements.
- If `j - i > 1`, set `t = (j - i + 1)/3` and recurse on `(i, j-t)`, then `(i+t, j)`, then `(i, j-t)` again.
- Return the sorted array.

## Language Coverage
84 languages implement this task, giving very broad coverage across paradigms — from systems languages to functional and scripting languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Ruby, and Fortran.

## Connections
- [[SortingAlgorithm]] — Stooge sort is a comparison-based sorting algorithm.
- [[Recursion]] — the algorithm is defined entirely through triple recursive calls.
- [[DivideAndConquer]] — it splits the array into overlapping two-thirds segments.
- [[ComputationalComplexity]] — notable for its poor O(n^2.71) running time.

## Contradictions
- None — reference task page.
