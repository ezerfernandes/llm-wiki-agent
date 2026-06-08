---
title: "Sorting algorithms/Cocktail sort with shifting bounds (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort_with_shifting_bounds
---

## Summary
This task asks the programmer to implement a cocktail sort (a bidirectional bubble sort, also called cocktail shaker sort) using the improved "shifting bounds" variant. The key insight is that after each forward and backward pass, the program tracks the index of the last swap to shrink the active region from both ends, rather than just decrementing a fixed counter. This halves the number of comparisons by skipping the already-sorted prefix and suffix on every iteration.

## Task Requirements
- Implement a cocktail sort that bubbles values in both directions through the array (one forward pass, one backward pass per iteration).
- Use shifting bounds: after a forward pass set the new upper bound to the last swap position, and after a backward pass set the new lower bound to the last swap position.
- Optionally display the sorted output on the page.

## Language Coverage
37 languages implement this task, spanning systems languages, assembly, scripting, and array/functional languages. Representative entries include C, C++, Rust, Go, Java, Python, Perl, Raku, Fortran, REXX, and several assembly variants (360 Assembly, AArch64, ARM).

## Connections
- [[CocktailSort]] — the bidirectional sorting algorithm being implemented
- [[BubbleSort]] — the base algorithm that cocktail sort improves upon
- [[SortingAlgorithms]] — the broader family of comparison-based sorts
- [[InPlaceAlgorithm]] — the swap-based approach sorts the array without extra storage

## Contradictions
- None — reference task page.
