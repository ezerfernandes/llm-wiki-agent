---
title: "Sort stability (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_stability
---

## Summary
This task asks the programmer to investigate a language's built-in sort routine and report on its stability — whether it preserves the relative order of records that compare equal on the sort key. The key insight is illustrated with a table of country/city pairs: a stable sort on the city column keeps "US Birmingham" above "UK Birmingham" because that was their original order, whereas an unstable sort offers no such guarantee.

## Task Requirements
- Examine the documentation for any built-in sort routine(s) provided by the language.
- Indicate whether the language supplies a built-in sort routine.
- If supplied, indicate whether or not that built-in routine is stable.

## Language Coverage
71 languages implement this task, spanning systems, functional, scripting, and assembly families. Representative examples include C, C++, C#, Java, Python, Rust, Go, Haskell, Ruby, Perl, JavaScript, and OCaml — most modern standard libraries either guarantee a stable sort (e.g. Python's Timsort, Java's merge sort for objects) or document the absence of such a guarantee.

## Connections
- [[StableSort]] — the property this task examines
- [[SortingAlgorithm]] — the broader family of routines being evaluated
- [[MergeSort]] — a common stable sorting algorithm
- [[Timsort]] — the stable algorithm behind several standard-library sorts
- [[Quicksort]] — a fast but typically unstable comparison sort

## Contradictions
- None — reference task page.
