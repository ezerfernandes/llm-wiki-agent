---
title: "Averages/Median (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Median
---

## Summary
This task asks the programmer to compute the median of a vector of floating-point numbers — the middle value once the data is ordered. The key wrinkle is that an even-length input has no single middle element, so the program must return the average of the two central values. The implementation need not handle the empty-vector case.

## Task Requirements
- Find the median value of a vector of floating-point numbers.
- Handle the even-length case by returning the average of the two middle elements.
- The empty-vector case need not be handled.
- Any correct approach is acceptable: sorting then indexing the middle (O(n log n)), a priority queue (O(n log n)), or a selection algorithm for an optimal O(n) solution.

## Language Coverage
143 languages implement this task, an exceptionally broad cross-section spanning systems languages, scripting languages, array languages, and statistical tools. Representative examples include C, C++, Rust, Go, Python, Haskell, Java, R, APL, and Julia.

## Connections
- [[Median]] — the central statistical measure being computed
- [[SelectionAlgorithm]] — the optimal O(n) approach to finding the median
- [[Quickselect]] — the linked partition-based selection method
- [[Sorting]] — the straightforward O(n log n) approach via ordering
- [[DescriptiveStatistics]] — the broader family of statistical-measure tasks

## Contradictions
- None — reference task page.
