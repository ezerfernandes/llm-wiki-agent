---
title: "Permutations/Derangements (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Permutations/Derangements
---

## Summary
A derangement is a permutation of distinct items in which no item remains in its original position. The task asks the programmer to generate these derangements and to count them, where the number of derangements of n items is the subfactorial !n. The key insight is the recurrence !n = (n-1)·(!(n-1) + !(n-2)), which lets the count be computed directly rather than by enumerating and filtering all n! permutations.

## Task Requirements
- Create a named routine that generates the derangements of the integers 0..n-1 (or 1..n).
- Generate and display all derangements of 4 integers using that routine.
- Create a function that calculates the subfactorial !n.
- Print a table comparing the counted number of derangements of n against the calculated !n, for n from 0 to 9 inclusive.
- Optional stretch goal: calculate !20.

## Language Coverage
54 languages implement this task, spanning functional, imperative, scripting, and assembly styles. Representative implementations include Python, Haskell, C, C++, Java, Rust, Ruby, Perl, Raku, Go, Common Lisp, and 360 Assembly.

## Connections
- [[Derangement]] — the central combinatorial object being generated and counted
- [[Subfactorial]] — !n, the count of derangements, computed via recurrence
- [[Permutations]] — derangements are the fixed-point-free subset of permutations
- [[Combinatorics]] — the broader mathematical domain of the task
- [[Recurrence Relation]] — !n = (n-1)(!(n-1) + !(n-2)) drives the efficient count

## Contradictions
- None — reference task page.
