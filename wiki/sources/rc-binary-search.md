---
title: "Binary search (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, algorithms, searching, divide-and-conquer]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Binary_search
---

## Summary
The task asks the programmer to implement a binary search over a sorted integer array: given a range and a target value, repeatedly halve the search interval until the value is found or the range is exhausted, then report whether the value was present and at what index. It is presented as the classic example of a divide-and-conquer algorithm, analogous to a higher/lower number-guessing game. The key subtlety highlighted is the integer-overflow bug in the naive midpoint calculation.

## Task Requirements
- Implement binary search through a sorted integer array given a start point, end point, and the target ("secret") value.
- Provide a recursive and/or iterative implementation (both if possible).
- Print whether the number was found, and if so print its index.
- Extra credit: avoid the overflow bug in `mid = (low + high) / 2` by using `mid = low + (high - low) / 2` or a logical right shift `(low + high) >>> 1`.

## Language Coverage
136 languages implement this task, an exceptionally broad spread reflecting its status as a foundational CS exercise, ranging from low-level assembly (8080, ARM, AArch64, z/Arch, MACRO-11) through systems languages (C, C++, Rust, Zig, Go) to functional and scripting languages such as Haskell, OCaml, Scheme, Python, Ruby, Perl, and JavaScript.

## Connections
- [[BinarySearchAlgorithm]] — the algorithm this task implements
- [[DivideAndConquer]] — the algorithmic paradigm it exemplifies
- [[IntegerOverflow]] — the midpoint-calculation bug the extra credit addresses
- [[Recursion]] — one of the two implementation styles required
- [[SearchingAlgorithms]] — the broader category this task belongs to

## Contradictions
- None — reference task page.
