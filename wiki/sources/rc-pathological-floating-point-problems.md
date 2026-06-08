---
title: "Pathological floating point problems (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-analysis, floating-point]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pathological_floating_point_problems
---

## Summary
This task demonstrates how a language copes with calculations that are catastrophically sensitive to floating-point imprecision. It presents three classic ill-conditioned problems where naive binary floating-point arithmetic produces wildly wrong answers, and the intended solution typically requires exact rational or arbitrary-precision arithmetic. The key insight is that small representation errors can be amplified to dominate the result, so the "correct" answer often differs entirely from the IEEE 754 double-precision one.

## Task Requirements
- Task 1: Compute the recurrence v1 = 2, v2 = -4, vn = 111 - 1130/v(n-1) + 3000/(v(n-1)*v(n-2)), and display values for n = 3, 4, 5, 6, 7, 8, 20, 30, 50, 100 to at least 16 decimal places. The true limit is 6, but rounding error drives it toward 100.
- Task 2 (Chaotic Bank Society): Start with a balance of e - 1, then each year set Balance = Balance * year - 1, for 25 years; report the final balance (≈ 0.0399387296732302).
- Task 3 (extra credit): Evaluate Siegfried Rump's 1988 function f(a,b) = 333.75·b^6 + a^2·(11·a^2·b^2 - b^6 - 121·b^4 - 2) + 5.5·b^8 + a/(2b) at a = 77617.0, b = 33096.0; the correct value is about -0.827396059946821.
- Demonstrate solving at least one of the first two problems (and the third if ambitious).

## Language Coverage
45 languages implement this task, spanning systems and scripting languages as well as those with native exact-arithmetic support. Representative examples include C, C#, Java, Go, Haskell, Python, Perl, Raku, Julia, Fortran, REXX, and Mathematica/Wolfram Language.

## Connections
- [[FloatingPointArithmetic]] — the core subject; IEEE 754 representation error
- [[NumericalStability]] — these problems are ill-conditioned and error-amplifying
- [[ArbitraryPrecisionArithmetic]] — common remedy via rational or bignum types
- [[RecurrenceRelation]] — Task 1's sequence is defined recursively
- [[CatastrophicCancellation]] — Rump's example exhibits severe cancellation

## Contradictions
- None — reference task page.
