---
title: "Sorting algorithms/Bubble sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort
---

## Summary
This task asks the programmer to implement the bubble sort (also called sinking sort), generally considered the simplest sorting algorithm. It repeatedly passes over a list, comparing each adjacent pair and swapping them when out of order, so large values "bubble" toward the end. The key insight is the optimization: track whether any swap occurred in a pass and stop early once a pass makes no changes, and shrink the scanned range each pass since the largest remaining element settles at the end. Its O(n^2) cost makes it pedagogical rather than practical for large datasets.

## Task Requirements
- Sort an array of elements using the bubble sort algorithm.
- Elements must have a total order; the array index may be of any discrete type.
- For languages where arbitrary element types are not possible, sort an array of integers instead.
- Follow the given pseudo-code pattern: repeat full passes, swapping adjacent out-of-order items, until a pass completes with no changes.

## Language Coverage
159 languages implement this task, an exceptionally broad cross-section spanning systems, scripting, functional, and assembly languages. Representative examples include C, C++, Java, Python, Go, Rust, Haskell, Common Lisp, Ada, and x86 Assembly.

## Connections
- [[BubbleSort]] — the algorithm this task implements
- [[SortingAlgorithms]] — the broader family of comparison sorts
- [[ComputationalComplexity]] — its O(n^2) quadratic time behavior
- [[ComparisonSort]] — sorts based on pairwise element comparison
- [[InPlaceAlgorithm]] — swaps elements without extra storage

## Contradictions
- None — reference task page.
