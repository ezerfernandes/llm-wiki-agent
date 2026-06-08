---
title: "Remove duplicate elements (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, collections, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Remove_duplicate_elements
---

## Summary
The task asks the programmer to take an array and produce a sequence in which every duplicate element has been removed, keeping only distinct values. The key insight is that there are three classic strategies that trade generality for performance: a hash set (O(n) average, needs a hash function), sort-then-dedup consecutive equals (O(n log n), needs an ordering), or a brute-force scan comparing each element to the rest (O(n²), needs only equality).

## Task Requirements
- Given an array, derive a sequence with all duplicate elements removed.
- Solutions may use any of the three approaches: hash table (rejects duplicates), sort plus removal of consecutive duplicates, or pairwise comparison checking the remainder of the list.
- The chosen approach implies a constraint on the element type: hashability, comparability/ordering, or merely testability for equality.

## Language Coverage
154 languages implement this task, an exceptionally broad set spanning functional, imperative, array, and stack-oriented paradigms; representative examples include Python, Haskell, C++, Java, Ruby, Perl, Common Lisp, J, Rust, and Go, many of which reduce it to a single built-in such as a set constructor or a `uniq`/`distinct` primitive.

## Connections
- [[HashSet]] — the hash-table approach relies on a set that rejects duplicate keys.
- [[SortingAlgorithm]] — the sort-then-remove-consecutive-duplicates strategy.
- [[BinarySearchTree]] — a self-balancing BST is cited as a special case of the sorting approach.
- [[TimeComplexity]] — the three approaches are distinguished by their O(n), O(n log n), and O(n²) costs.

## Contradictions
- None — reference task page.
