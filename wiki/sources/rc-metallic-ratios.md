---
title: "Metallic ratios (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recurrence-relations, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Metallic_ratios
---

## Summary
The metallic ratios generalize the Golden ratio: they are the positive real roots of x² − bx − 1 = 0, giving x = (b + √(b² + 4)) / 2 for integer b. Setting b = 1, 2, 3 yields the Golden, Silver, and Bronze ratios respectively, and each equals the infinite continued fraction [b; b, b, b, …]. The key insight the task exploits is that each ratio can be approximated by a Fibonacci-like Lucas sequence xₙ = b·xₙ₋₁ + xₙ₋₂, whose successive-term ratios converge to the metallic ratio (the Golden ratio converging slowest of all).

## Task Requirements
- For each b from 0 through 9 (the first 10 metallic ratios), generate the Lucas-like sequence xₙ = b·xₙ₋₁ + xₙ₋₂ starting from terms 1, 1.
- Show at least the first 15 elements of each sequence.
- Use successive approximations (the (n+1)th term divided by the nth) to compute the ratio accurate to 32 decimal places.
- Display the approximated value at that accuracy and the value of n (iteration count) at which it stabilizes.
- Convergence is assumed reached when the next iteration no longer changes the value at the desired precision.
- Optional stretch goal: approximate the Golden ratio to 256 decimal places and report its iteration count.

## Language Coverage
30 languages implement this task, spanning systems, functional, scripting, and array/math-oriented styles. Representative implementations include Ada, C++, C#, F#, Go, Java, Julia, Python, Perl, Raku, Mathematica/Wolfram Language, J, and Wren.

## Connections
- [[GoldenRatio]] — the b = 1 case, the most famous metallic ratio
- [[FibonacciSequence]] — the b = 1 Lucas-like sequence used for approximation
- [[ContinuedFraction]] — each ratio equals the periodic continued fraction [b; b, b, …]
- [[LucasSequence]] — the recurrence family generating successive approximations
- [[ArbitraryPrecisionArithmetic]] — needed to reach 32 and 256 decimal places

## Contradictions
- None — reference task page.
