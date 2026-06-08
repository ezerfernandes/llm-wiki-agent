---
title: "Ramanujan's constant (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ramanujan's_constant
---

## Summary
The task asks the programmer to calculate Ramanujan's constant — the value of e^(π·√163) — to at least 32 digits of precision by any chosen method. The key insight is that this number is famously *almost* an integer (262537412640768743.99999999999925...), and the task optionally invites demonstrating the same near-integer phenomenon by evaluating e^(π·√x) at the last four Heegner numbers (43, 67, 163, and the smaller ones), where the closeness to an integer becomes more pronounced for larger Heegner numbers.

## Task Requirements
- Compute Ramanujan's constant with at least 32 digits of precision.
- Use any method of choice (the e^(π·√x) approach is suggested).
- Optionally show that evaluating e^(π·√x) at the last four Heegner numbers yields a result that is almost an integer.

## Language Coverage
21 languages implement this task, spanning systems and scripting languages plus several with strong arbitrary-precision math support. Representative implementations include C++, Fortran, Go, Haskell, Java, Julia, Mathematica/Wolfram Language, Pari/GP, Perl, Python, and Raku.

## Connections
- [[RamanujanConstant]] — the specific transcendental near-integer being computed
- [[HeegnerNumbers]] — the imaginary quadratic field discriminants underlying the near-integer behavior
- [[ArbitraryPrecisionArithmetic]] — required to capture 32+ digits accurately
- [[NumberTheory]] — the branch of mathematics from which this curiosity arises
- [[TranscendentalFunctions]] — the e^(π·√x) exponential evaluation involved

## Contradictions
- None — reference task page.
