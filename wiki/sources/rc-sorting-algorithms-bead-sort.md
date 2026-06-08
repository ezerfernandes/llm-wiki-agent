---
title: "Sorting algorithms/Bead sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Bead_sort
---

## Summary
The task is to sort an array of positive integers using bead sort, a natural sorting algorithm also known as "gravity sort." Each integer is represented as a row of beads on vertical rods (an abacus-like grid); letting the beads fall under gravity rearranges them so that reading off the rows yields the sorted sequence. The key insight is that it sorts through a physical analogy rather than comparisons.

## Task Requirements
- Sort an array restricted to positive integers.
- Implement the bead sort (gravity sort) algorithm specifically, not another sort.
- Note the complexity: O(S) where S is the sum of the input integers, since each bead is moved individually in a software implementation lacking a mechanism to locate empty spaces below beads.

## Language Coverage
68 languages implement this task, showing broad coverage across functional, imperative, and assembly families. Representative implementations include C, C++, Java, Python, Rust, Go, Haskell, Common Lisp, Julia, Perl, Ruby, and 360 Assembly.

## Connections
- [[SortingAlgorithms]] — bead sort is one member of the sorting-algorithm family.
- [[GravitySort]] — bead sort's physical/natural-sorting alternate name and conceptual basis.
- [[NonComparisonSort]] — it sorts without pairwise element comparisons.
- [[ComputationalComplexity]] — characterized by its O(S) sum-dependent cost model.

## Contradictions
- None — reference task page.
