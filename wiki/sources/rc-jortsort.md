---
title: "JortSort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, satire]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/JortSort
---

## Summary
JortSort is a satirical "sorting" tool, originally presented by Jenn "Moneydollars" Schiffer at JSConf, that makes the user do the actual sorting work. The function takes an array of comparable objects, sorts a copy of it in ascending order, and compares that to the original. The key insight (and the joke) is that it never modifies or returns the sorted data — it merely reports whether the input was already sorted, so "you don't have to sort ever again."

## Task Requirements
- Implement a function that accepts a single array of comparable objects.
- Sort the array in ascending order and compare the sorted version to the original input.
- Return `true` if they match (the original was already sorted), otherwise return `false`.
- Solutions are encouraged to preserve the intentionally roundabout, satirical spirit rather than collapse to the most concise idiom.

## Language Coverage
71 languages implement this task, spanning mainstream, functional, scripting, assembly, and esoteric ecosystems. Representative examples include C, C++, Java, Python, JavaScript, Haskell, Rust, Go, Ruby, Perl, and Tcl.

## Connections
- [[SortingAlgorithms]] — JortSort is a parody framed within the sorting-algorithm family.
- [[ArrayEquality]] — the core operation compares the original array against its sorted copy.
- [[IsSortedPredicate]] — functionally equivalent to a "is this already sorted?" check.
- [[ComparisonSort]] — relies on ordering comparable elements in ascending order.

## Contradictions
- None — reference task page.
