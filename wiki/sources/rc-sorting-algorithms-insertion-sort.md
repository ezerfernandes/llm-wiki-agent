---
title: "Sorting algorithms/Insertion sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort
---

## Summary
This task asks the programmer to implement insertion sort, an O(n²) comparison sort that builds the final sorted array one element at a time. Each new element is inserted into its correct position within the already-sorted prefix, shifting larger elements up to make room. The key insight is that despite its quadratic worst case, its simplicity, low overhead, and good locality of reference make it efficient for small inputs and as the finishing pass for divide-and-conquer sorts like mergesort and quicksort.

## Task Requirements
- Implement the insertion sort algorithm, sorting an array in place.
- Treat the first element as the initial sorted region, then iterate over the remaining elements, moving each into position within the sorted prefix by shifting higher-ranked elements up.
- Sorting an array of integers is sufficient to demonstrate the task.

## Language Coverage
143 languages implement this task, giving very broad coverage across paradigms — imperative, functional, assembly, and array languages alike. Representative examples include C, C++, Python, Java, Rust, Haskell, Go, Common Lisp, Fortran, and 360 Assembly.

## Connections
- [[InsertionSort]] — the algorithm this task implements
- [[SortingAlgorithms]] — the family of comparison sorts it belongs to
- [[TimeComplexity]] — its O(n²) worst-case and best-case linear behavior on nearly-sorted data
- [[MergeSort]] — uses insertion sort as a finishing pass for small subarrays
- [[QuickSort]] — likewise switches to insertion sort below a size threshold

## Contradictions
- None — reference task page.
