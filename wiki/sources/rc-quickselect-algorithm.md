---
title: "Quickselect algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, selection-algorithm, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Quickselect_algorithm
---

## Summary
This task asks the programmer to implement the quickselect algorithm, a selection method that finds the k-th smallest (or largest) element of an unsorted collection without fully sorting it. Like quicksort, it picks a pivot and partitions the data, but it only recurses into the single partition that contains the target rank, giving average O(n) time instead of O(n log n). The concrete exercise applies it to the vector [9, 8, 7, 6, 5, 0, 1, 2, 3, 4] and prints the first through tenth largest members in order.

## Task Requirements
- Implement the quickselect algorithm.
- Apply it to the input vector [9, 8, 7, 6, 5, 0, 1, 2, 3, 4].
- Use it to report the first, second, third, and so on up to the tenth largest member, displayed in order.
- This is distinct from the separate Quicksort task.

## Language Coverage
70 languages implement this task, spanning systems languages, functional languages, scripting languages, and assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Ruby, and AArch64 Assembly.

## Connections
- [[Quickselect]] — the algorithm being implemented
- [[Quicksort]] — the partitioning-based relative this task contrasts against
- [[SelectionProblem]] — the general problem of finding the k-th order statistic
- [[Partitioning]] — the in-place rearrangement step around a pivot
- [[DivideAndConquer]] — the algorithmic paradigm both quickselect and quicksort share

## Contradictions
- None — reference task page.
