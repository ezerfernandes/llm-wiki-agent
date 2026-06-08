---
title: "Euler's constant 0.5772... (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, mathematical-constant]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Euler's_constant_0.5772...
---

## Summary
This task asks the programmer to compute the Euler-Mascheroni constant gamma (≈ 0.5772...), which measures the limiting difference between the partial sums of the harmonic series and the natural logarithm. The naive definition converges far too slowly to be practical, so the key insight is to use a faster method — Euler's own summation formula (Euler-Maclaurin, requiring Bernoulli numbers) suffices for single precision, while higher precision historically relied on Sweeney's exponential-integral expansion or the Brent-McMillan Bessel-function algorithm.

## Task Requirements
- Compute the Euler constant gamma, defined as lim n→∞ (1 + 1/2 + 1/3 + ... + 1/n − log(n)).
- Produce an accurate numerical value (at least the leading digits 0.5772...).
- Because the defining limit converges too slowly, use a numerically useful method such as the Euler-Maclaurin summation formula rather than direct summation.

## Language Coverage
46 languages implement this task, spanning systems, scripting, functional, and array/math-oriented languages. Representative entries include C, C++, Rust, Java, Python, Julia, Perl, Raku, Mathematica/Wolfram Language, PARI/GP, J, and Scheme.

## Connections
- [[EulerMascheroniConstant]] — the constant gamma being computed
- [[HarmonicSeries]] — its defining divergent series
- [[EulerMaclaurinFormula]] — the practical summation method for single precision
- [[BernoulliNumbers]] — required coefficients in the Euler-Maclaurin expansion
- [[NaturalLogarithm]] — the approximating integral subtracted from the partial sums

## Contradictions
- None — reference task page.
