---
title: "Count the coins (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, combinatorics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Count_the_coins
---

## Summary
The task asks the programmer to count the number of distinct ways to make change for a given amount using a fixed set of coin denominations (order of coins does not matter). The canonical example uses US coins — quarters, dimes, nickels, pennies — to make change for one dollar. The key insight is that this is the classic coin-change counting problem, solvable elegantly with a recursive formula (count ways using the first denomination plus count ways excluding it) or, far more efficiently, with bottom-up dynamic programming over a 1D table.

## Task Requirements
- Count how many ways there are to make change for a dollar (100 cents) using quarters (25), dimes (10), nickels (5), and pennies (1).
- Optional extension: add dollar coins (100 cents) and half dollars (50 cents), then count the ways to make change for $1000.
- The optional answer exceeds 2^32, so an implementation must use big or 64-bit-plus integers.

## Language Coverage
96 languages implement this task, spanning functional, imperative, assembly, and BASIC dialects. Representative implementations include C, C++, Python, Haskell, Java, Scheme, Common Lisp, Rust, Go, and Perl.

## Connections
- [[DynamicProgramming]] — the efficient bottom-up tabulation that solves the problem in pseudo-polynomial time
- [[CoinChangeProblem]] — the named combinatorial problem this task instantiates
- [[Recursion]] — the natural recursive decomposition (include vs. exclude a denomination)
- [[Combinatorics]] — counting unordered partitions of an amount into denomination summands
- [[StructureAndInterpretationOfComputerPrograms]] — referenced source of the classic counting algorithm

## Contradictions
- None — reference task page.
