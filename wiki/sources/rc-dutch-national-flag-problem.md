---
title: "Dutch national flag problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, partitioning]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dutch_national_flag_problem
---

## Summary
Posed by Edsger Dijkstra, the task is to arrange a collection of red, white, and blue balls into the order of the Dutch national flag — red, then white, then blue. The classic insight is that with only three distinct key values, the array can be partitioned in a single linear pass using three pointers (low, mid, high), minimizing swaps and color comparisons rather than relying on a general comparison sort.

## Task Requirements
- Generate a randomized order of balls, explicitly ensuring the initial arrangement is not already in flag order.
- Sort the balls in a way idiomatic to the implementing language.
- Verify the sorted result is in the correct red/white/blue order.

## Language Coverage
83 languages implement this task, reflecting broad coverage across paradigms. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Clojure, Prolog, and even shell-based ones like AWK and sed.

## Connections
- [[ThreeWayPartitioning]] — the in-place low/mid/high pointer technique behind the optimal solution
- [[Quicksort]] — three-way partitioning generalizes Quicksort's partition step for duplicate keys
- [[Sorting]] — the task is a constrained sorting problem over three key values
- [[EdsgerDijkstra]] — originator of the problem and its successive refinements

## Contradictions
- None — reference task page.
