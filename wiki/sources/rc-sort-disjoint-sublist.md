---
title: "Sort disjoint sublist (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, array-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_disjoint_sublist
---

## Summary
Given a list of values plus a set of integer indices into that list, sort only the values located at those indices while leaving every other value untouched in its original position. The key insight is that the chosen positions form a "disjoint" sublist: you extract the values at those indices, sort them, then write them back into the same positions (in ascending index order), so the surrounding elements never move.

## Task Requirements
- Accept a list of values and a set of indices into that list.
- Sort the values found at the given indices, in place, while preserving all values at indices not in the set.
- Treat the indices as a set (no duplicates) and produce a result independent of the order in which the indices are supplied.
- Demonstrate with values `[7, 6, 5, 4, 3, 2, 1, 0]` and zero-based indices `{6, 1, 7}`, yielding `[7, 0, 5, 4, 3, 2, 1, 6]`.

## Language Coverage
88 languages implement this task, spanning functional, imperative, array, and assembly styles. Representative implementations include Python, Haskell, J, APL, C, C++, Java, Go, Rust, Perl, and Common Lisp.

## Connections
- [[SortingAlgorithm]] — the core operation applied to the extracted subset
- [[ArrayIndexing]] — selecting elements by an index set
- [[InPlaceAlgorithm]] — values are written back to their original positions
- [[SetDataStructure]] — indices are modeled as an unordered set

## Contradictions
- None — reference task page.
