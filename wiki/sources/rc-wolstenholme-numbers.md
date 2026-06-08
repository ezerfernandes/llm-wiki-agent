---
title: "Wolstenholme numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, rational-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wolstenholme_numbers
---

## Summary
A Wolstenholme number is the fully reduced numerator of the second-order harmonic number H(n,2) = sum of 1/k^2 for k from 1 to n. The task asks the programmer to compute these numerators using exact rational arithmetic, identify which of them happen to be prime, and (in the stretch goals) measure how their digit counts grow. The key insight is that exact fraction reduction (GCD-based) is required, since floating point cannot recover the true numerator; note these are distinct from "Wolstenholme primes."

## Task Requirements
- Find and display the first 20 Wolstenholme numbers (OEIS A007406).
- Find and display the first 4 prime Wolstenholme numbers (OEIS A123751).
- Stretch: display the digit count of the 500th, 1000th, 2500th, 5000th, and 10000th Wolstenholme numbers.
- Stretch: display the digit count of the first 15 prime Wolstenholme numbers.

## Language Coverage
26 languages implement this task, spanning systems and mathematical languages well suited to big-integer and rational arithmetic. Representative implementations include Python, Go, Java, Julia, Raku, Perl, C, Maxima, Mathematica / Wolfram Language, and Wren.

## Connections
- [[HarmonicNumber]] — the task sums reciprocals of squares (second-order harmonic series).
- [[RationalArithmetic]] — requires exact fraction summation and reduction.
- [[GreatestCommonDivisor]] — used to fully reduce each fraction's numerator.
- [[PrimalityTest]] — needed to find the prime Wolstenholme numbers.
- [[BigInteger]] — numerators grow large, demanding arbitrary-precision integers.

## Contradictions
- None — reference task page.
