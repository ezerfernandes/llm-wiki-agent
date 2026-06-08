---
title: "Sorting algorithms/Comb sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Comb_sort
---

## Summary
This task asks the programmer to implement comb sort, an in-place comparison sort that improves on bubble sort by comparing and swapping elements separated by a shrinking gap rather than only adjacent ones. Starting from a gap equal to the array size, each pass divides the gap by a shrink factor and the sort terminates only when the gap reaches 1 and a full pass produces no swaps. The key insight is that the large initial gaps quickly move small "turtle" values out of the tail of the list, eliminating the main weakness of bubble sort.

## Task Requirements
- Implement comb sort over an input list/array.
- Initialize the gap to the size of the input, then on each pass shrink it by a factor (ideally about 1.247, though 1.3 is more practical), clamping the minimum gap to 1.
- In each pass, compare every pair `input[i]` and `input[i+gap]`, swapping when out of order and recording that a swap occurred.
- Continue looping until the gap is 1 and no swaps happen in a pass.
- Optional variants noted: Combsort11 forces the gap sequence to end in (11, 8, 6, 4, 3, 2, 1) for speed, and some implementations switch to insertion sort once the gap is small.

## Language Coverage
85 languages implement this task, spanning systems languages, scripting languages, functional languages, and many BASIC/assembly dialects. Representative examples include C, C++, C#, Java, Python, Go, Rust, Haskell, Perl, Ruby, Fortran, and Common Lisp.

## Connections
- [[CombSort]] — the algorithm this task implements
- [[BubbleSort]] — the simpler adjacent-swap sort that comb sort generalizes
- [[ShellSort]] — also uses a shrinking gap sequence over the input
- [[SortingAlgorithm]] — comb sort is one in-place comparison sort among many
- [[InsertionSort]] — used as a small-gap finishing pass in some variants

## Contradictions
- None — reference task page.
