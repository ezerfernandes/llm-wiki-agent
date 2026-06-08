---
title: "Sorting algorithms/Cycle sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms, in-place]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Cycle_sort
---

## Summary
The task asks the programmer to implement cycle sort, an in-place, unstable comparison sort that is theoretically optimal in terms of the total number of writes to the original array. The key insight is that the permutation to be sorted can be factored into cycles, each of which is rotated independently so that every element is written either zero times (already correct) or exactly once (to its final position). Minimizing writes is valuable when writing is expensive, such as on flash/EEPROM memory where each write wears down the medium.

## Task Requirements
- Implement the cycle sort algorithm to sort an array in place.
- Achieve the minimal number of writes: each value is written zero times if already in its correct position, or one time directly to its correct position.
- Demonstrate sorting on a sample input.

## Language Coverage
46 languages implement this task, spanning systems, scripting, functional, and assembly languages. Representative examples include C, C++, Rust, D, Go, Java, Kotlin, Python, Ruby, Perl, Julia, Fortran, and 360 Assembly.

## Connections
- [[SortingAlgorithms]] — cycle sort is one member of the comparison-sort family.
- [[InPlaceAlgorithm]] — sorts using O(1) auxiliary space, rearranging within the original array.
- [[PermutationCycles]] — the algorithm factors the permutation into cycles and rotates each.
- [[ComparisonSort]] — ordering is determined purely by element comparisons.
- [[WriteOptimization]] — designed to minimize writes for wear-sensitive media like flash memory.

## Contradictions
- None — reference task page.
