---
title: "Longest increasing subsequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Longest_increasing_subsequence
---

## Summary
The task asks the programmer to find and display a longest strictly increasing subsequence of a given list of numbers — that is, the longest ordered subset of elements (not necessarily contiguous) whose values strictly increase. The key insight is that a list may admit several distinct subsequences of the same maximum length, so any one valid answer is acceptable.

## Task Requirements
- Compute a longest increasing subsequence of `{3, 2, 6, 4, 5, 1}`.
- Compute a longest increasing subsequence of `{0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}`.
- Show the result for each list.
- Acknowledge that the maximum-length subsequence need not be unique.

## Language Coverage
64 languages implement this task, spanning systems, functional, scripting, and assembly families. Representative entries include C, C++, Rust, Go, Java, Haskell, OCaml, Python, Ruby, Perl, and 360 Assembly.

## Connections
- [[DynamicProgramming]] — the canonical O(n²) approach builds per-element best-length tables
- [[PatienceSorting]] — the referenced O(n log n) solution based on patience sorting and binary search
- [[BinarySearch]] — used to place elements onto pile tops in the efficient variant
- [[Subsequence]] — the underlying combinatorial structure being optimized

## Contradictions
- None — reference task page.
