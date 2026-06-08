---
title: "Sort an array of composite structures (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_an_array_of_composite_structures
---

## Summary
This task asks the programmer to sort an array of composite records (structs/objects holding multiple fields) by one chosen field rather than by the value as a whole. The canonical example uses name-value pairs sorted by the name key. The key insight is that sorting only needs a way to compare two elements on the selected field, so it is a direct application of comparator-based or key-extraction sorting.

## Task Requirements
- Define a composite structure containing more than one field (e.g. a pair of name and value strings).
- Build an array of such structures.
- Implement a routine that sorts that array using one designated field (the key, e.g. `name`) as the ordering criterion.
- Languages without native support are pointed to the related Sorting Using a Custom Comparator task.

## Language Coverage
94 languages implement this task, spanning systems languages, functional languages, scripting languages, and assembly. Representative examples include C, C++, Rust, Java, Python, Haskell, OCaml, Ruby, Go, Common Lisp, and SQL.

## Connections
- [[SortingAlgorithms]] — this task is a member of the sorting algorithm family
- [[CustomComparator]] — the general technique used to sort by an arbitrary key
- [[KeyExtraction]] — extracting one field as the sort key from a record
- [[DataStructures]] — operates on composite/record types

## Contradictions
- None — reference task page.
