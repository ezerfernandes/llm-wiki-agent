---
title: "Sorting algorithms/Strand sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Strand_sort
---

## Summary
The task asks the programmer to implement the strand sort algorithm. Strand sort works by repeatedly pulling out a "strand" — a subsequence of already-in-order elements — from the unsorted input, then merging that strand into a growing sorted result list. The key insight is that it exploits pre-existing runs of sorted data, so inputs that are already partially ordered are handled efficiently.

## Task Requirements
- Implement the strand sort algorithm.
- Sort a list of numbers by repeatedly extracting shorter sequences of already-sorted numbers from the unsorted list and merging them into the output.

## Language Coverage
51 languages implement this task, showing broad coverage across functional, imperative, and scripting paradigms. Representative implementations include C, C++, Java, Python, Haskell, Go, Rust, Ruby, Common Lisp, and Raku.

## Connections
- [[SortingAlgorithm]] — strand sort is one member of this family of tasks
- [[MergeSort]] — strand sort relies on merging sorted sublists, the same primitive used in merge sort
- [[LinkedList]] — implementations commonly use linked-list-style extraction and splicing of strands
- [[ComputationalComplexity]] — worst case O(n^2), best case O(n) on already-sorted input

## Contradictions
- None — reference task page.
