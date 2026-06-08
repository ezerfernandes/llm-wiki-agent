---
title: "Rare numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rare_numbers
---

## Summary
A rare number is a positive integer n (in base ten) whose digit-reversal r is different from n (non-palindromic), where both the sum n+r and the difference n-r are positive perfect squares. The task is to find and display the first several rare numbers. Because they are extremely sparse, the practical insight is to derive digit-level constraints (on leading/trailing digits and digit relationships) rather than brute-forcing every integer.

## Task Requirements
- Reverse the decimal digits of n to form r.
- Require n to be non-palindromic (n ≠ r).
- Require the difference n - r to be positive.
- Require both the sum (n + r) and the difference (n - r) to be perfect squares.
- Find and show the first 5 rare numbers; optionally the first 8; and as a stretch goal, find more.

## Language Coverage
33 languages implement this task, spanning systems and applied languages with both naive and constraint-optimized approaches. Representative implementations include C++, D, Go, Java, Julia, Python, Rust, Perl, Raku, REXX, and Wren.

## Connections
- [[NumberTheory]] — rare numbers are a number-theoretic curiosity (OEIS A035519).
- [[PerfectSquare]] — both the sum and difference must be perfect squares.
- [[DigitReversal]] — the core operation forming r from n.
- [[Palindrome]] — n must explicitly be non-palindromic.
- [[ConstraintPropagation]] — efficient solutions prune the search space via digit constraints.

## Contradictions
- None — reference task page.
