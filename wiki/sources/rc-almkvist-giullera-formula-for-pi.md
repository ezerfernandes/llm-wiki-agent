---
title: "Almkvist-Giullera formula for pi (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Almkvist-Giullera_formula_for_pi
---

## Summary
The task implements the Almkvist-Giullera formula, a rapidly converging Ramanujan-like series for 1/pi^2 derived from the Calabi-Yau differential equations originally used in string theory. The key insight is that each term factors into a large integer part (involving the factorial ratio (6n)!/(3*n!^6) and the polynomial 532n^2+126n+9) multiplied by a negative power of ten, 10^-(6n+3), so the integer portions can be computed exactly before scaling.

## Task Requirements
- Print the integer portions of the first 10 terms (the formula without the power-of-1000 divisor): 32*(6n)!/(3*n!^6)*(532n^2+126n+9).
- Use the full series to calculate and print pi to 70 decimal digits of precision.

## Language Coverage
39 languages implement this task, spanning systems languages, functional languages, and dedicated math tools. Representative implementations include Python, Rust, Go, Java, C++, Haskell, Julia, Raku, PARI/GP, and Mathematica/Wolfram Language, with several assembly entries (AArch64, ARM) demonstrating low-level big-integer handling.

## Connections
- [[RamanujanTypeSeries]] — the formula belongs to the family of fast-converging Ramanujan-like series for 1/pi^2.
- [[ArbitraryPrecisionArithmetic]] — reaching 70 digits requires big-integer and high-precision decimal computation.
- [[Pi]] — the constant being computed via the series.
- [[CalabiYauManifold]] — the differential equations underlying the formula come from string-theory manifolds.
- [[Factorial]] — each term depends on the ratio of factorials (6n)! and n!^6.

## Solved in (Rosetta Code languages)
Solved in **34** of the wiki's catalogued languages (Rosetta Code shows 39 language sections for this task). (5 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[ARM Assembly]], [[C++]], [[Common Lisp]], [[Erlang]], [[Factor]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Nim]], [[PARI-GP]], [[Perl]], [[Phix]], [[PicoLisp]], [[Pluto]], [[Python]], [[Quackery]], [[Raku]], [[REXX]], [[RPL]], [[Rust]], [[Scala]], [[Sidef]], [[Visual Basic .NET]], [[Wren]]

## Contradictions
- None — reference task page.
