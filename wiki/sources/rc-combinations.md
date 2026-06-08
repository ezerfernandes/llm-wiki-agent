---
title: "Combinations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Combinations
---

## Summary
Given non-negative integers m and n, generate every size-m combination of the integers from 0 to n-1, with each combination internally sorted and the full list emitted in lexicographic order. The key insight is that enumerating combinations in sorted order maps naturally to either a recursive choose/skip strategy or to advancing an index vector while keeping it strictly increasing.

## Task Requirements
- Accept two non-negative integers, m (size of each combination) and n (range size).
- Produce all C(n, m) combinations of the integers 0 .. n-1.
- Each combination must be sorted internally, and the overall table must be in sorted (lexicographic) order.
- Example: 3 comb 5 yields 10 rows from "0 1 2" through "2 3 4".
- Counting from 1 to n instead of 0 to n-1 is acceptable when more natural to the language.

## Language Coverage
125 languages implement this task, spanning functional, imperative, array, and stack-based paradigms, with many leaning on built-in combination generators. Representative entries include Python, Haskell, C, Java, Julia, J, APL, Common Lisp, Rust, and Mathematica.

## Connections
- [[Combinatorics]] — combinations are a core counting structure
- [[BinomialCoefficient]] — the number of results equals C(n, m)
- [[Recursion]] — the canonical generation approach uses choose/skip recursion
- [[Backtracking]] — index-vector advancement is a form of systematic enumeration
- [[LexicographicOrder]] — required output ordering of the combinations

## Contradictions
- None — reference task page.
