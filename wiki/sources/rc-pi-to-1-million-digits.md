---
title: "Pi to 1 million digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arbitrary-precision, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pi_to_1_million_digits
---

## Summary
The task asks the programmer to compute the mathematical constant π to 1,000,000 digits — interpreted as "3." followed by 999,999 decimal places — and to display a clip of the first and last several digits. The key requirement is arbitrary-precision (big number) arithmetic, since standard floating-point types cannot hold a million significant digits. Optionally, programs report the calculation time as a contrast to the 23 hours a CDC 7600 needed for the same feat in 1973.

## Task Requirements
- If the language supports big numbers, compute π to 1,000,000 digits ("3." plus 999,999 decimal places).
- Show a clip of the first and last several digits of the result.
- Extra credit: report the calculation time, illustrating how computing power has advanced since 1973.
- Fast-but-complex implementations are discouraged in favor of clarity.

## Language Coverage
12 languages implement this task. Coverage is modest and skewed toward languages with native or library-backed bignum support, including Java, Julia, Mathematica/Wolfram Language, Perl, Phix, Python, R, Raku, and Wren, alongside Agena, FutureBasic, and Pluto.

## Connections
- [[ArbitraryPrecisionArithmetic]] — required to hold a million-digit result.
- [[Pi]] — the mathematical constant being computed.
- [[ChudnovskyAlgorithm]] — a fast-converging series commonly used for large-scale π computation.
- [[InfiniteSeries]] — arctan and other series historically used to extend π's known digits.

## Contradictions
- None — reference task page.
