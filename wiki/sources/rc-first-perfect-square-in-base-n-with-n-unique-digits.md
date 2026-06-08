---
title: "First perfect square in base n with n unique digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/First_perfect_square_in_base_n_with_n_unique_digits
---

## Summary
The task is to find, for a given base N, the smallest perfect square that has at least N digits and exactly N significant unique digits when written in base N (i.e. it is pandigital in that base). For example, in base 10 the first such square is 1026753849 = 32043². The key insight is that this is OEIS A260182, and that the search space can be pruned analytically (e.g. by skipping squares whose digit count is too small, or by casting out nines / digit-permutation reasoning) but an actual search is still required rather than hardcoding answers.

## Task Requirements
- For each base N from 2 through 12, find and display the first perfect square that uses exactly N unique significant digits, shown in base N.
- Optional: extend the computation to bases 13 through 16.
- Stretch goal: continue to bases 17 and beyond, which requires big-integer arithmetic.
- The program must perform a genuine search; analytical methods may reduce the search space, but magic numbers or pre-fed answers are not allowed.

## Language Coverage
41 languages implement this task, reflecting broad coverage across systems, scripting, functional, and array languages. Representative implementations include C, C++, Go, Rust-adjacent C#, Java, Python, Haskell, Julia, Raku, Wren, and array language J/Uiua.

## Connections
- [[NumberTheory]] — squares and base representations
- [[PerfectSquare]] — the values searched for
- [[Pandigital]] — the unique-digit / full-digit-set property being tested
- [[CastingOutNines]] — related divisibility/digit-sum technique for pruning
- [[BigInteger]] — required for the higher-base stretch goal

## Contradictions
- None — reference task page.
