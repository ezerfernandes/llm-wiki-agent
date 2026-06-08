---
title: "Sorting algorithms/Heapsort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, data-structures, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Heapsort
---

## Summary
The task asks the programmer to implement heapsort, an in-place comparison sort with worst-case and average time complexity of O(n log n). The core idea is to reorganize the input array into a binary max-heap, then repeatedly swap the maximal root element to the end of the array, shrink the heap, and sift the new root back down to restore heap order, building the sorted output from back to front. Because the algorithm relies on indexing parent/child nodes arithmetically, it requires random-access (array-like) storage.

## Task Requirements
- Write a function that sorts a collection of integers using heapsort.
- Sort in place via the heap-based approach (heapify, then repeatedly extract the max).
- The reference pseudocode decomposes the work into `heapSort`, `heapify`, and `siftDown` helpers operating on array indices (left child at `2*root + 1`).

## Language Coverage
101 languages implement this task, spanning systems languages, scripting languages, functional languages, and several assembly dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Fortran, and multiple BASIC variants.

## Connections
- [[Heapsort]] — the algorithm this task implements.
- [[BinaryHeap]] — the underlying max-heap data structure that drives the sort.
- [[ComparisonSort]] — the family of O(n log n) in-place sorts this belongs to.
- [[SiftDown]] — the heap-restoration operation central to building and maintaining the heap.
- [[BigONotation]] — used to express the O(n log n) complexity bound.

## Contradictions
- None — reference task page.
