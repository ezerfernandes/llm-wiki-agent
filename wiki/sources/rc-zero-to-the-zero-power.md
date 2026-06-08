---
title: "Zero to the zero power (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, mathematics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zero_to_the_zero_power
---

## Summary
This task asks the programmer to compute and display the result of raising zero to the zeroth power (0^0). The point is to surface how different languages and runtimes treat this mathematically ambiguous case: most return 1 (the convention used in combinatorics and by IEEE-754 `pow`), but some raise errors, return NaN, or refuse to compile. The key insight is that 0^0 has no single agreed-upon value across mathematics, so the answer reveals a language's implementation choice rather than a universal truth.

## Task Requirements
- Compute 0^0 using the language's native exponentiation operator or function (e.g. `0**0`, `0^0`, `pow(0,0)`).
- If the language rejects the literal `0**0` or `0^0` at compile time, assign `x = 0`, `y = 0`, then evaluate `z = x**y` and display `z`.
- Show the actual result produced.
- Use whatever exponentiation symbol or notation the language supports.

## Language Coverage
163 languages implement this task, an unusually broad set spanning mainstream, legacy, and esoteric languages. Representative implementations include Python, C, Java, Haskell, Rust, JavaScript, Common Lisp, Fortran, APL, and REXX, with many BASIC dialects and assembly variants explicitly omitting it for lacking built-in exponentiation.

## Connections
- [[Exponentiation]] — the core operation being evaluated.
- [[IndeterminateForm]] — 0^0 is a classic indeterminate form in analysis.
- [[FloatingPointArithmetic]] — IEEE-754 `pow` defines 0^0 as 1.
- [[NumberTheory]] — the convention 0^0 = 1 underpins combinatorics and series.

## Contradictions
- None — reference task page.
