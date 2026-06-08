---
title: "Largest int from concatenated ints (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Largest_int_from_concatenated_ints
---

## Summary
Given a set of positive integers, the task is to order them so that concatenating their decimal representations produces the largest possible integer, then return that integer. The key insight is that this is not a numeric sort: the correct ordering is determined by a pairwise comparison where, for any two numbers X and Y, X should precede Y when the concatenation "XY" is greater than or equal to "YX". This custom comparator yields the optimal arrangement without trying every permutation.

## Task Requirements
- Accept a set of positive integers.
- Order the integers so their string concatenation forms the largest possible integer.
- Return (and display) the resulting concatenated integer.
- Show output for the two test sets {1, 34, 3, 98, 9, 76, 45, 4} and {54, 546, 548, 60}.

## Language Coverage
83 languages implement this task, spanning systems, scripting, functional, and array families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Raku, Clojure, and J.

## Connections
- [[ComparisonSort]] — the task is solved with a sort driven by a custom comparator.
- [[CustomComparator]] — pairwise rule comparing "XY" vs "YX" rather than numeric value.
- [[StringConcatenation]] — candidate results are built by joining decimal digit strings.
- [[GreedyAlgorithm]] — the local pairwise ordering produces the globally optimal concatenation.
- [[CombinatorialOptimization]] — brute-force over permutations is the naive alternative.

## Contradictions
- None — reference task page.
