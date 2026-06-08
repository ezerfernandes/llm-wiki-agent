---
title: "Sorting algorithms/Patience sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Patience_sort
---

## Summary
The task asks the programmer to sort an array of numbers into ascending order using patience sorting, an algorithm modeled on the patience (solitaire) card game. The key insight is that elements are dealt onto a series of "piles" — each new card goes on the leftmost pile whose top card is greater (or equal), or starts a new pile if none qualifies — and then the sorted output is produced by repeatedly removing the smallest pile-top via a merge. This decomposes the input into a set of already-sorted runs that are merged, running in O(n log n) time.

## Task Requirements
- Sort an array of numbers (of any convenient size) into ascending order.
- Use the patience sorting algorithm specifically (deal into piles, then merge pile tops).

## Language Coverage
54 languages implement this task, giving broad coverage across functional, imperative, and low-level styles. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Ruby, Perl, Julia, and several assembly variants (ARM, AArch64, RISC-V).

## Connections
- [[PatienceSorting]] — the named algorithm the task implements
- [[SortingAlgorithms]] — the broader family of comparison sorts this belongs to
- [[MergeAlgorithm]] — sorted pile-tops are combined via a merge step
- [[LongestIncreasingSubsequence]] — patience sorting's pile count yields the length of the longest increasing subsequence
- [[PriorityQueue]] — a heap over pile tops yields the efficient O(n log n) merge

## Contradictions
- None — reference task page.
