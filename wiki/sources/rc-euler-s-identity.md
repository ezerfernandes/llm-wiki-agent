---
title: "Euler's identity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, complex-numbers, numerical-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Euler's_identity
---

## Summary
The task asks the programmer to demonstrate Euler's identity, the equation e^(iπ) + 1 = 0, which elegantly links five fundamental constants (0, 1, π, e, i) and three arithmetic operations. The key insight is that evaluating the complex exponential e^(iπ) yields -1, so adding 1 gives 0. Most languages relying on IEEE 754 floating point cannot produce an exact zero and must instead show the result is approximately zero, reporting the small residual error.

## Task Requirements
- Show in your language that Euler's identity (e^(iπ) + 1 = 0) holds true.
- Mimic the form of the equation as closely as practical.
- For floating-point languages, show the result is approximately equal to zero and report the magnitude of the calculation error.
- Bonus: if the language supports symbolic computation, show the result is exactly zero.

## Language Coverage
52 languages implement this task. Coverage spans systems and application languages (C, C++, Rust, Go, Java, C#), functional languages (Haskell, OCaml, F#, Scheme, Common Lisp), symbolic/math systems (Mathematica/Wolfram, Maxima), and scripting languages (Python, Perl, Raku, Ruby, Julia), reflecting how widely complex-number support is available.

## Connections
- [[ComplexNumbers]] — the calculation relies on complex exponentiation
- [[EulersNumber]] — the base e raised to an imaginary power
- [[ImaginaryUnit]] — i, where i² = -1
- [[FloatingPointPrecision]] — IEEE 754 limits produce small residual errors
- [[SymbolicComputation]] — exact-zero results require a symbolic algebra system

## Contradictions
- None — reference task page.
