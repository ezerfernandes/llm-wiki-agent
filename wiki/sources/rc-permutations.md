---
title: "Permutations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Permutations
---

## Summary
This Rosetta Code task asks the programmer to write a program that generates all permutations of *n* distinct objects (in practice, numerals). For *n* objects there are n! orderings, and the core challenge is to enumerate every arrangement systematically without omission or duplication. Common approaches include recursive backtracking, Heap's algorithm, and lexicographic next-permutation iteration.

## Task Requirements
- Generate and output all permutations of *n* different objects.
- Use distinct numerals (or comparable distinct elements) as the objects.
- Produce the complete set of n! arrangements.

## Language Coverage
119 languages implement this task, an exceptionally broad cross-section reflecting how fundamental permutation generation is across paradigms. Representative implementations include Python, C, C++, Java, Haskell, Ruby, Rust, Go, Lisp, and Prolog, with many languages leaning on built-in library functions such as itertools.permutations or next_permutation.

## Connections
- [[Permutation]] — the combinatorial structure being enumerated
- [[Combinatorics]] — the branch of mathematics this task belongs to
- [[Recursion]] — the most common generation strategy
- [[HeapsAlgorithm]] — a classic minimal-swap permutation algorithm
- [[Factorial]] — the count of permutations of n objects is n!

## Contradictions
- None — reference task page.
