---
title: "Gamma function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-analysis, special-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gamma_function
---

## Summary
This task asks the programmer to implement at least one algorithm to compute the Gamma function Γ(x) over the real numbers. The Gamma function generalizes the factorial (Γ(n) = (n−1)! for positive integers) and is defined by the improper integral Γ(x) = ∫₀^∞ t^(x−1) e^(−t) dt. The key insight is that direct numerical integration is correct but inefficient, so practical solutions favor faster approximations; implementers are also encouraged to compare results against a built-in or library Gamma where available.

## Task Requirements
- Implement one or more algorithms to compute Γ(x) in the real field.
- Acceptable approaches include numerical integration of the defining integral, the Lanczos approximation, or Stirling's approximation.
- If the language provides a built-in or library Gamma function, compare your implementation's output against it.

## Language Coverage
93 languages implement this task, showing very broad coverage across mathematical, scripting, functional, and assembly languages. Representative implementations include C, C++, Python, Haskell, Julia, Fortran, Rust, Java, Scheme, and Mathematica/Wolfram Language.

## Connections
- [[GammaFunction]] — the special function being computed
- [[LanczosApproximation]] — recommended efficient evaluation method
- [[StirlingApproximation]] — asymptotic approximation for large arguments
- [[NumericalIntegration]] — the straightforward but slow approach from the definition
- [[Factorial]] — the discrete function Γ generalizes

## Contradictions
- None — reference task page.
