---
title: "Sorting algorithms/Merge sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, divide-and-conquer, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
---

## Summary
This task asks the programmer to implement merge sort, a recursive divide-and-conquer sorting algorithm that splits a collection in half until each group holds one or zero elements (trivially sorted), then merges the groups back together in order. The key insight is that two already-sorted lists can be combined into one sorted list in linear time, giving overall O(n*log n) worst-case and average complexity, with O(n) best case on pre-sorted input.

## Task Requirements
- Write a function to sort a collection of integers using merge sort.
- Structure the implementation as two parts: a recursive `mergesort` function and a `merge` function.
- `mergesort`: return the input unchanged if length ≤ 1; otherwise split at the midpoint into left and right halves, recursively sort each, then merge the results.
- `merge`: repeatedly take the smaller of the two front elements from the left and right lists, appending it to the result, then append any remaining elements.
- The reference pseudocode is given for both functions; an optional optimization (insertion sort below a threshold) is mentioned but not required.

## Language Coverage
122 languages implement this task, spanning a very broad cross-section from assembly to functional and esoteric languages. Representative examples include C, C++, Java, Python, Haskell, Rust, Go, Common Lisp, Scheme, OCaml, Prolog, and 360 Assembly.

## Connections
- [[MergeSort]] — the algorithm this task implements
- [[DivideAndConquer]] — the algorithmic paradigm behind splitting and merging
- [[Recursion]] — the recursive halving structure of `mergesort`
- [[SortingAlgorithms]] — the broader family this task belongs to
- [[TimeComplexity]] — the O(n*log n) / O(n) analysis the task highlights

## Contradictions
- None — reference task page.
