---
title: "Compare sorting algorithms' performance (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, benchmarking, algorithm-analysis]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compare_sorting_algorithms'_performance
---

## Summary
This task asks the programmer to empirically measure and compare the runtime performance of at least two sorting implementations. Each algorithm is timed against inputs of growing length and three distinct distributions, then execution time is plotted against sequence length (typically on log-log axes) to reveal each algorithm's empirical complexity. The key insight is that real-world behavior depends heavily on input shape: an already-sorted or all-equal sequence can be a best case for one algorithm and a worst case for another.

## Task Requirements
- Measure the relative performance of two or more sorting routines (different algorithms, or different implementations of the same algorithm such as quicksort with varying pivot selection).
- Test against three input sequence types: all ones (constant), range (already ascending/sorted), and shuffled range (random order).
- Define sequence generators and record timings as input length grows; where possible reuse existing sort implementations.
- Plot execution time versus input sequence length (example figures use log2(microseconds) vs log2(length)).
- Draw conclusions about the algorithms' relative performance from the resulting plots.

## Language Coverage
29 languages implement this task, spanning systems, scripting, functional, and array-oriented paradigms. Representative entries include C, C++, Rust, Go, D, Java, Python, Haskell, Julia, R, Perl, Ruby, J, and Wren.

## Connections
- [[SortingAlgorithm]] — the routines being benchmarked
- [[Quicksort]] — a canonical algorithm used here, often with varied pivot strategies
- [[BubbleSort]] — a simple O(n^2) baseline for comparison
- [[InsertionSort]] — exhibits best-case linear behavior on sorted input
- [[BigONotation]] — empirical timing curves estimate asymptotic complexity
- [[Benchmarking]] — the core methodology of timing and plotting

## Contradictions
- None — reference task page.
