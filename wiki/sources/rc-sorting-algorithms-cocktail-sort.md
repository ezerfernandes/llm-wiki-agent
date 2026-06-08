---
title: "Sorting algorithms/Cocktail sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort
---

## Summary
The task asks the programmer to implement the cocktail shaker sort, a bidirectional variant of bubble sort. Where bubble sort only pushes large elements toward the end on each pass, cocktail sort alternates direction: one forward pass bubbles the largest unsorted element up, then a backward pass bubbles the smallest down. The key insight is that this two-way sweeping moves out-of-place "turtle" elements (small values near the end) much faster than plain bubble sort, while keeping the same simple compare-and-swap structure.

## Task Requirements
- Sort a list of sortable items using the cocktail shaker algorithm.
- Repeatedly sweep the array forward (swapping adjacent out-of-order pairs), then backward, within an outer loop.
- Track whether any swap occurred; if a full sweep makes no swaps, the list is sorted and the algorithm terminates early.

## Language Coverage
101 languages implement this task, reflecting very broad coverage typical of the classic sorting-algorithm tasks. Representative implementations include C, C++, C#, Java, Python, Haskell, Rust, Go, Ruby, Perl, Fortran, and several assembly dialects (6502, ARM, AArch64).

## Connections
- [[BubbleSort]] — cocktail sort is a direct bidirectional improvement on it
- [[SortingAlgorithms]] — the broader family of comparison sorts this belongs to
- [[ComparisonSort]] — relies solely on pairwise comparisons and swaps
- [[InPlaceAlgorithm]] — sorts the array using only constant extra space

## Contradictions
- None — reference task page.
