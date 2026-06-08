---
title: "Sorting algorithms/Circle sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Circle_sort
---

## Summary
The task asks the programmer to sort an array of integers into ascending order using Circlesort. The algorithm compares the outermost pair of elements (first vs. last), swapping if out of order, then works inward (second vs. second-last, and so on), before recursively splitting the array in half and repeating on each half down to single elements. The key insight is that a single pass may not fully sort the data, so the whole procedure is repeated until a pass produces zero swaps (quiescence).

## Task Requirements
- Sort an array of integers of any convenient size into ascending order using Circlesort.
- Compare first-to-last, second-to-second-last, etc., swapping out-of-order pairs.
- Recursively split the array in two and recurse until each subarray has one element.
- Repeat the full procedure until a pass makes no swaps.
- Display both the initial unsorted list and the final sorted list (intermediate steps optional).
- Optimizations such as doing ~0.5·log2(n) iterations then switching to insertion sort are optional.

## Language Coverage
53 languages implement this task, spanning systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Raku, and several assembly variants (AArch64, ARM).

## Connections
- [[SortingAlgorithm]] — Circle sort is a comparison-based sorting algorithm.
- [[Recursion]] — the array is recursively split in half until single elements remain.
- [[InsertionSort]] — cited as an optional optimization to finish the sort.
- [[DivideAndConquer]] — the split-and-recurse structure mirrors divide-and-conquer.

## Contradictions
- None — reference task page.
