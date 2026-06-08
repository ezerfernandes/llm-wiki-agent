---
title: "Sorting algorithms/Quicksort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, recursion, divide-and-conquer]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
---

## Summary
The task asks the programmer to sort an array or list using the quicksort (partition-exchange) algorithm. The core idea is to pick a pivot, partition the remaining elements into those less than and those greater than the pivot, recursively sort each partition, and concatenate. The key insight is that partitioning does the real work — once both sides are sorted, joining them is trivial because every element of the left partition is no greater than every element of the right.

## Task Requirements
- Sort an array/list whose elements have a strict weak order (sort integers if generic types are unavailable).
- Choose any element as the pivot.
- Partition the remaining elements: those less than the pivot in one part, those greater in another.
- Recursively quicksort both partitions.
- Concatenate the sorted lower partition, the pivot (equal elements), and the sorted upper partition.
- Implementations may allocate new arrays or sort in place, and may choose the pivot freely (first, middle, or median-of-three).

## Language Coverage
164 languages implement this task, spanning functional, imperative, array, and low-level assembly styles. Representative examples include C, C++, Java, Python, Haskell, Rust, Go, Common Lisp, OCaml, Erlang, APL, and ARM/AArch64 Assembly. The breadth highlights how the algorithm reads very differently in array languages and pure-functional concatenation styles versus in-place swapping implementations.

## Connections
- [[Quicksort]] — the algorithm this task implements
- [[DivideAndConquer]] — quicksort is a conquer-then-divide member of this family
- [[Recursion]] — both partitions are sorted by recursive calls
- [[MergeSort]] — frequently contrasted divide-then-conquer sort with the same average O(n log n) time
- [[BigONotation]] — runtime ranges from O(n log n) with good pivots to O(n^2) worst case

## Contradictions
- None — reference task page.
