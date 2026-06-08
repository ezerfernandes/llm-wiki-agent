---
title: "Map range (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, interpolation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Map_range
---

## Summary
The task asks the programmer to write a function that linearly remaps a real number from one numeric interval onto another. Given two ranges [a1, a2] and [b1, b2] and a value s, it computes t = b1 + (s − a1)(b2 − b1) / (a2 − a1). The key insight is that this is just an affine (linear) transformation that preserves the relative position of a value within its source interval, scaled and shifted into the target interval.

## Task Requirements
- Implement a function/subroutine taking two ranges and a real number, returning the value mapped from the first range into the second.
- Apply the mapping formula t = b1 + (s − a1)(b2 − b1) / (a2 − a1).
- Demonstrate by mapping values from the range [0, 10] onto the range [-1, 0].
- Extra credit: show additional idiomatic ways of performing the mapping using language-specific tools.

## Language Coverage
108 languages implement this task, reflecting broad coverage across functional, imperative, scripting, and assembly languages. Representative implementations include C, C++, Python, Haskell, Java, JavaScript, Rust, Go, Common Lisp, and APL-family languages such as J and K.

## Connections
- [[LinearInterpolation]] — the mapping is a form of linear interpolation between interval endpoints.
- [[AffineTransformation]] — the formula is a scale-and-shift (affine) transform of a scalar value.
- [[NumericalMethods]] — rescaling values between ranges is a common numerical/normalization operation.
- [[FloatingPointArithmetic]] — the computation operates on real numbers and is subject to floating-point precision.

## Contradictions
- None — reference task page.
