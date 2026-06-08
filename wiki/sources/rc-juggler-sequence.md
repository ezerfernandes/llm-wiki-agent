---
title: "Juggler sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequences, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Juggler_sequence
---

## Summary
A juggler sequence starts from a positive integer a[0] and applies a recurrence: take floor(a[k]^0.5) when a[k] is even, or floor(a[k]^1.5) when a[k] is odd. The terms rise and fall erratically (hence "juggler"), and the sequence is conjectured — but not proven — to always reach 1. The key implementation insight is that the maximum values can grow to thousands or millions of digits, so exact computation requires big integers with an integer square root function rather than floating-point powers.

## Task Requirements
- For initial terms n from 20 to 39 inclusive, compute and show: l[n] = number of terms needed to reach 1; h[n] = maximum value reached; i[n] = index (from 0) where the maximum first occurs.
- If the language supports big integers with an integer square root, do the same for selected larger n (113, 173, 193, 2183, 11229, 15065, 15845, 30817, 48443, 275485, 1267909, 2264915, 5812827; optionally 7110201).
- For those large cases, report d[n] = the number of digits in h[n] instead of h[n] itself, since the maxima are enormous.
- Results may be verified against the referenced archived table and OEIS sequences A007320 and A094716.

## Language Coverage
36 languages implement this task, spanning systems and applied languages alike. Representative entries include C++, C#, Go, Java, Python, Haskell, Julia, Perl, Raku, Nim, Wren, and array languages such as J and BQN.

## Connections
- [[NumberTheory]] — integer sequence defined by a parity-based recurrence
- [[IntegerSquareRoot]] — even-step floor of the square root requires an exact isqrt for big integers
- [[BigIntegers]] — maxima reach thousands or millions of digits, ruling out floating point
- [[HailstoneSequence]] — closely related rise-and-fall integer sequence with an unproven termination conjecture
- [[IntegerSequences]] — catalogued in OEIS as A007320 and A094716

## Contradictions
- None — reference task page.
