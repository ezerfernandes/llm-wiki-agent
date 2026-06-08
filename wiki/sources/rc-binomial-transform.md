---
title: "Binomial transform (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequence-transform]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Binomial_transform
---

## Summary
The binomial transform is a bijective transform on integer sequences, formed by convolving a sequence with binomial coefficients; it can be seen as an nth forward difference where odd differences carry a negative sign. This task uses the OEIS-standardized variant with complementary forward and inverse operations: the forward transform maps `a` to `b` via `b_n = Σ C(n,k)·a_k`, and the inverse recovers `a` via `a_n = Σ (-1)^(n-k)·C(n,k)·b_k`. The key insight is that applying the inverse to a forward-transformed sequence returns the original.

## Task Requirements
- Implement both a forward and an inverse binomial transform routine.
- Use them to compute, for several test sequences: the forward transform, the inverse transform, and the inverse-of-the-forward (which must return the original).
- Show at least the first 15 values of each resulting sequence.
- Test on these sequences (hard-coded or generated): Catalan numbers, the prime flip-flop sequence (1 if prime, else 0), the Fibonacci sequence, and the Padovan sequence (starting 1,0,0).

## Language Coverage
34 languages implement this task, spanning systems and scripting languages as well as math-oriented ones. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wolfram Language.

## Connections
- [[BinomialCoefficient]] — the transform sums products of `C(n,k)` with sequence terms.
- [[FiniteDifference]] — equivalent to an nth forward difference with sign alternation.
- [[CatalanNumbers]] — one of the test sequences (forward transform yields OEIS A007317).
- [[FibonacciSequence]] — test sequence whose binomial transform is the bisection F(2n).
- [[PadovanSequence]] — fourth test sequence for the transform.

## Contradictions
- None — reference task page.
