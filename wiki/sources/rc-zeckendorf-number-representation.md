---
title: "Zeckendorf number representation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, fibonacci]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zeckendorf_number_representation
---

## Summary
The task asks the programmer to express positive integers as sums of distinct Fibonacci numbers, where the chosen Fibonacci terms may never be two consecutive members of the sequence. Zeckendorf's theorem guarantees that every positive integer has exactly one such representation, which is encoded as a binary-like positional string over the Fibonacci basis (1, 2, 3, 5, 8, 13, ...). For example, decimal 11 is uniquely 8 + 3, written as 10100.

## Task Requirements
- Compute the Zeckendorf representation of an arbitrary integer.
- Generate and display a table of the Zeckendorf representations for the decimal numbers 0 through 20 in order.
- Enforce the non-consecutive-Fibonacci constraint to obtain the unique form (drop leading zeroes).
- (Iterating the form via bit twiddling is explicitly left to a separate task.)

## Language Coverage
105 languages implement this task, showing very broad coverage across functional, imperative, assembly, and esoteric families. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Common Lisp, Perl, Raku, and even 8080 Assembly and Befunge.

## Connections
- [[FibonacciSequence]] — the basis set for the representation
- [[ZeckendorfTheorem]] — guarantees uniqueness under the non-consecutive rule
- [[NumberTheory]] — domain of integer representation systems
- [[PositionalNotation]] — the encoding model generalized from binary/decimal
- [[GreedyAlgorithm]] — the standard method (subtract the largest fitting Fibonacci number) for finding the representation

## Contradictions
- None — reference task page.
