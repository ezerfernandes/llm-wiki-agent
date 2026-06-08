---
title: "Apéry's constant (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, series-convergence, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Apéry's_constant
---

## Summary
The task asks the programmer to compute Apéry's constant, ζ(3) — the sum of the reciprocals of the positive cubes — to 100 decimal digits using at least three different methods. The key insight is that the naive definition converges far too slowly (1000 direct terms give only ~6 correct digits), so accelerated series representations by Markov/Apéry and Wedeniwski are needed, with the Wedeniwski form yielding about 5 correct digits per term. Computing this accurately requires arbitrary-precision arithmetic.

## Task Requirements
- Show the value of Apéry's constant calculated at least three different ways.
- Method 1: sum at least the first 1000 terms of the direct definition ζ(3) = Σ 1/k³, truncated to 100 decimal digits.
- Method 2: sum the first 158 terms of the Markov / Apéry representation, truncated to 100 decimal digits.
- Method 3: sum the first 20 terms of the Wedeniwski representation, truncated to 100 decimal digits.

## Language Coverage
25 languages implement this task, covering systems and functional languages alongside math-oriented and scripting environments. Representative implementations include Ada, ALGOL 68, C#, F#, Java, Julia, Mathematica/Wolfram Language, PARI/GP, Perl, Python, Raku, and REXX.

## Connections
- [[RiemannZetaFunction]] — Apéry's constant is the value ζ(3) of this function.
- [[ArbitraryPrecisionArithmetic]] — required to reach 100 correct decimal digits.
- [[SeriesAcceleration]] — the Markov/Apéry and Wedeniwski forms converge far faster than the naive sum.
- [[IrrationalNumbers]] — Apéry proved ζ(3) is irrational in 1978.
- [[NumberTheory]] — the constant arises in analytic number theory.

## Contradictions
- None — reference task page.
