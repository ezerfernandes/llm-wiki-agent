---
title: "Combinations with repetitions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Combinations_with_repetitions
---

## Summary
This task asks the programmer to generate all multisets of size k drawn from a set of n element types, where elements may repeat and order does not matter. The canonical illustration is counting the ways to pick two doughnuts from three types (iced, jam, plain), which yields 6 selections. The key insight is that, unlike ordinary combinations, repeated elements are allowed, so the count follows the multiset coefficient formula C(n + k - 1, k).

## Task Requirements
- Write a function/routine that generates all combinations with repetitions of n types taken k at a time.
- Use it to show the answer to the doughnut example: choosing 2 doughnuts from {iced, jam, plain}, producing the 6 multisets.
- For extra credit, compute and show only the *count* of ways to choose 3 doughnuts from 10 types (do not enumerate the individual choices).

## Language Coverage
81 languages implement this task, giving very broad coverage across functional, imperative, and array-oriented paradigms. Representative implementations include Python, C, C++, Java, Haskell, Common Lisp, J, Rust, Ruby, Go, and Raku.

## Connections
- [[Combinatorics]] — the task is a core combinatorial enumeration problem
- [[Multiset]] — each generated selection is a multiset, not an ordered tuple
- [[BinomialCoefficient]] — the count equals the multiset coefficient C(n+k-1, k)
- [[Recursion]] — most implementations enumerate selections via recursive generation
- [[StarsAndBars]] — the combinatorial identity underlying the counting formula

## Contradictions
- None — reference task page.
