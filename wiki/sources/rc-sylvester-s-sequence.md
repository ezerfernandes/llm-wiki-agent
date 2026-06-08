---
title: "Sylvester's sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sylvester's_sequence
---

## Summary
Sylvester's sequence is an integer sequence (OEIS A000058) in which each term equals the product of all previous terms plus one, starting from 2. The values grow doubly exponentially, so even the first ten terms require arbitrary-precision integers. The key insight is that the sum of the reciprocals of the first k terms is the closest possible k-term Egyptian-fraction underestimate of 1, converging to 1 faster than any other unit-fraction series of equal length.

## Task Requirements
- Write a routine (function, procedure, or generator) that calculates Sylvester's sequence.
- Use it to display the first 10 elements of the sequence.
- Show the sum of the reciprocals of the first 10 elements, ideally as an exact fraction.

## Language Coverage
46 languages implement this task, spanning mainstream, functional, array, and esoteric paradigms. Representative implementations include Python, C++, C#, Java, Haskell, Julia, Go, Raku, Perl, J, and Wren.

## Connections
- [[NumberTheory]] — the sequence is a number-theoretic integer sequence
- [[EgyptianFractions]] — partial reciprocal sums are optimal k-term Egyptian-fraction underestimates of 1
- [[BigIntegers]] — doubly exponential growth forces arbitrary-precision arithmetic
- [[RationalArithmetic]] — exact reciprocal sums require fraction (rational) representation
- [[Recurrence]] — each term is defined recursively from the product of prior terms

## Contradictions
- None — reference task page.
