---
title: "Sorting algorithms/Pancake sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Pancake_sort
---

## Summary
The task asks the programmer to sort an array of integers into ascending order using pancake sorting, where the only permitted operation is "flipping" a prefix of the list (reversing everything from one fixed end up to a chosen position). The key insight is that, like flipping a stack of pancakes with a spatula, you repeatedly bring the largest unsorted element to the top with one flip and then flip it down into its final position, so each element is placed using at most two prefix reversals.

## Task Requirements
- Sort an array of integers of any convenient size into ascending order.
- Use only the "flip" operation: reverse one end of the list up to a chosen point.
- The flipped end must stay the same (one fixed end) throughout the entire solution; it cannot be changed arbitrarily mid-sort.
- Show both the initial unsorted list and the final sorted list (intermediate steps optional).
- Optimizations are optional but recommended.

## Language Coverage
77 languages implement this task, spanning systems languages, scripting languages, functional languages, and several assembly dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, Ruby, and ARM Assembly.

## Connections
- [[SortingAlgorithm]] — pancake sort is a comparison-based sorting method.
- [[PancakeSorting]] — the underlying problem of sorting by prefix reversals.
- [[PrefixReversal]] — the single allowed primitive operation.
- [[ArrayReversal]] — each flip reverses a contiguous prefix segment.
- [[SelectionSort]] — pancake sort follows a selection-style "find max, place it" structure.

## Contradictions
- None — reference task page.
