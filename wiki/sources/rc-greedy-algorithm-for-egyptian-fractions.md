---
title: "Greedy algorithm for Egyptian fractions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, fractions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Greedy_algorithm_for_Egyptian_fractions
---

## Summary
An Egyptian fraction expresses a rational number as a sum of distinct unit fractions (each with numerator 1 and a distinct positive-integer denominator). The task implements Fibonacci's greedy algorithm, which repeatedly subtracts the largest possible unit fraction by replacing x/y with 1/ceil(y/x) plus a remainder term that is simplified and processed recursively. The key insight is that at each step the new numerator (-y mod x) strictly decreases, guaranteeing termination.

## Task Requirements
- Implement the Fibonacci greedy expansion using the replacement x/y = 1/ceil(y/x) + ((-y) mod x)/(y*ceil(y/x)), simplifying the second term as needed.
- Support both proper fractions (a < b) and improper fractions (a >= b); for improper fractions isolate the integer part first and show it in square brackets [n] before the unit fractions.
- Show the Egyptian fractions for 43/48, 5/121, and 2014/59.
- For all proper fractions a/b with one- or two-digit positive integers, find and show the one with the largest number of terms and the one with the largest denominator.
- Extra credit: do the same scan over all one-, two-, and three-digit integers.

## Language Coverage
44 languages implement this task, spanning systems and functional languages alongside math-oriented and BASIC dialects. Representative implementations include C, C++, Go, Rust, Java, Haskell, Python, Perl, Raku, Julia, REXX, and Mathematica. Big-integer support matters here because the three-digit extra-credit scan produces very large denominators.

## Connections
- [[EgyptianFraction]] — the unit-fraction representation being computed.
- [[GreedyAlgorithm]] — the core strategy of taking the largest unit fraction at each step.
- [[NumberTheory]] — rational arithmetic, GCD simplification, and ceiling-based division.
- [[Fibonacci]] — historical attribution of the greedy expansion method.
- [[ArbitraryPrecisionArithmetic]] — needed because denominators can grow enormously.

## Contradictions
- None — reference task page.
