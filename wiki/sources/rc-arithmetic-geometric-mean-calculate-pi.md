---
title: "Arithmetic-geometric mean/Calculate Pi (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic-geometric_mean/Calculate_Pi
---

## Summary
This task demonstrates how to compute many decimal digits of pi using the arithmetic-geometric mean (AGM) of 1 and 1/sqrt(2). Based on the 1988 Almkvist-Berndt paper, the AGM converges quadratically, so the number of correct digits roughly doubles each iteration, making it far more efficient than series like Leibniz's. The key insight is the closed form pi = 4·agm(1, 1/sqrt2)² / (1 − sum of 2^(n+1)(a_n² − g_n²)).

## Task Requirements
- Implement the AGM-based approximation of pi, truncating the infinite sum at a large N.
- Use the recurrence a_{k+1} = (a_k + g_k)/2 and g_{k+1} = sqrt(a_k·g_k), starting from a_0 = 1, g_0 = 1/sqrt(2).
- Accumulate the correction sum 2^(k+1)(a_k² − g_k²) over the iterations.
- Compute a large number of correct decimal digits of pi (requires arbitrary-precision arithmetic).

## Language Coverage
53 languages implement this task, spanning systems languages, functional languages, math-oriented environments, and even programmable calculators. Representative implementations include C, C++, Rust, Go, Haskell, Python, Julia, Perl, Raku, Java, Mathematica, and PARI/GP.

## Connections
- [[ArithmeticGeometricMean]] — the underlying iteration this task builds on
- [[ArbitraryPrecisionArithmetic]] — required to compute many digits of pi
- [[QuadraticConvergence]] — why AGM doubles correct digits each step
- [[Pi]] — the constant being computed
- [[NumericalAnalysis]] — domain of efficient transcendental constant evaluation

## Contradictions
- None — reference task page.
