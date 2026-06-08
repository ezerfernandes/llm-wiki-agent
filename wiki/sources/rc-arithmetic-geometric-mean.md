---
title: "Arithmetic-geometric mean (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, numerical-methods, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic-geometric_mean
---

## Summary
The task asks the programmer to write a function computing the arithmetic-geometric mean (AGM) of two numbers a and g. The AGM is the common limit of two interleaved sequences: each step replaces the pair with their arithmetic mean and geometric mean respectively. Because the difference between the two sequences shrinks quadratically, the iteration converges very rapidly, making it an efficient numerical method.

## Task Requirements
- Implement a function `agm(a, g)` that returns the arithmetic-geometric mean.
- Iterate the recurrence: a₀ = a, g₀ = g; aₙ₊₁ = ½(aₙ + gₙ), gₙ₊₁ = √(aₙ·gₙ), until the sequences converge.
- Demonstrate the function by computing agm(1, 1/√2).

## Language Coverage
116 languages implement this task, a very broad spread covering mainstream, functional, scientific, and esoteric languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Julia, Fortran, R, Mathematica/Wolfram Language, and Scheme.

## Connections
- [[NumericalAnalysis]] — AGM is a classic fixed-point iteration / convergence method
- [[ArithmeticMean]] — one of the two interleaved averaging operations
- [[GeometricMean]] — the second averaging operation in the recurrence
- [[EllipticIntegral]] — AGM is used to evaluate complete elliptic integrals and compute π
- [[FixedPointIteration]] — the algorithm iterates until the two sequences coincide

## Contradictions
- None — reference task page.
