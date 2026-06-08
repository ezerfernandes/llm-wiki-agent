---
title: "Roots of a function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-analysis, root-finding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Roots_of_a_function
---

## Summary
The task is to write a program that locates and prints the roots (zeros) of a given function over a specified range, scanning at some step width. The canonical example uses the cubic ƒ(x) = x³ − 3x² + 2x, which factors as x(x−1)(x−2) and therefore has exact roots at 0, 1, and 2. The key insight is that a stepped scan must distinguish a value that is exactly zero from one that merely brackets a sign change, where the root is only approximate.

## Task Requirements
- Find and output the roots of a given function across a range with a step width.
- Use the specific function ƒ(x) = x³ − 3x² + 2x.
- Report for each root whether it is exact (function value is precisely zero) or approximate (detected via a sign change between consecutive samples).

## Language Coverage
72 languages implement this task, spanning systems languages, scripting languages, functional languages, and math/CAS environments. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Common Lisp, Mathematica, and REXX.

## Connections
- [[RootFinding]] — the core numerical problem the task addresses
- [[BisectionMethod]] — common technique for refining a root inside a sign-change bracket
- [[NumericalAnalysis]] — the broader field covering approximate-root detection
- [[PolynomialEquations]] — the example function is a cubic polynomial
- [[FloatingPointArithmetic]] — explains why exact-zero tests are fragile and approximate roots arise

## Contradictions
- None — reference task page.
