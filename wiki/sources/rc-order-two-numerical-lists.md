---
title: "Order two numerical lists (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, comparison]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Order_two_numerical_lists
---

## Summary
This task asks the programmer to write a function that compares two lists of numbers and decides whether the first should be ordered before the second, returning `true` or `false`. Ordering follows lexicographic (dictionary-style) rules: elements are compared pairwise from the front, moving on only when a pair is equal. The key edge-case insight concerns differing lengths — if the first list is exhausted first it sorts before the second, but if the second (or both simultaneously) runs out, the result is false.

## Task Requirements
- Implement a function accepting two numeric lists/arrays as arguments.
- Compare them in lexicographic order: first elements, then second, and so on.
- Return `true` if the first list should come before the second, `false` otherwise.
- If the first list runs out of elements before any difference is found, return `true`.
- If the second list, or both lists, run out of elements first, return `false`.

## Language Coverage
96 languages implement this task, showing very broad coverage across functional, imperative, scripting, and assembly families. Representative entries include Python, C, C++, Java, Haskell, OCaml, Ruby, Rust, Go, Scheme, and ARM/AArch64 Assembly.

## Connections
- [[LexicographicOrder]] — the comparison rule the task is built on
- [[SortingAlgorithms]] — the task is categorized as a comparison primitive for sorting
- [[ComparisonFunction]] — produces a boolean precedence relation between two sequences
- [[TotalOrder]] — lexicographic comparison extends an element order to sequences

## Contradictions
- None — reference task page.
