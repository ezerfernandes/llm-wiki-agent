---
title: "Ukkonen's suffix tree construction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ukkonen’s_suffix_tree_construction
---

## Summary
The task asks the programmer to implement Ukkonen's algorithm, which builds a suffix tree for a string in linear time. The key insight of Ukkonen's method is its online, left-to-right construction using suffix links, active points, and the "skip/count" trick to achieve O(n) time despite a naive approach being O(n²) or worse. As a concrete benchmark, the implementation is applied to the decimal digits of pi to locate the longest repeated substring.

## Task Requirements
- Implement a function realizing Ukkonen's algorithm to construct a usable suffix tree.
- Generate the first 1000, 10000, and 100000 decimal digits of pi (e.g., via the Arithmetic-geometric mean / Calculate Pi task).
- Using an alphabet of digits 0-9 plus a sentinel terminator (e.g. `$`) to make the tree explicit, find the longest repeated string in each digit sequence.
- Time the runs and demonstrate linear scaling (10000 digits should take roughly 10x as long as 1000).
- List sizes may be adjusted to produce reasonable answers.

## Language Coverage
11 languages implement this task, a relatively narrow set reflecting the algorithm's complexity. Representative implementations include C++, Java, Rust, Go, Julia, Nim, JavaScript, Fortran, Phix, FreeBASIC, and Wren.

## Connections
- [[SuffixTree]] — the data structure being constructed
- [[StringMatching]] — primary application domain of suffix trees
- [[LongestRepeatedSubstring]] — the concrete problem solved as a benchmark
- [[LinearTimeAlgorithm]] — the asymptotic guarantee Ukkonen's method provides
- [[ComputationalBiology]] — a major field that relies on suffix trees

## Contradictions
- None — reference task page.
