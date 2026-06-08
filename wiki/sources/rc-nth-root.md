---
title: "Nth root (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, root-finding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nth_root
---

## Summary
This task asks the programmer to compute the principal nth root of a positive real number A, i.e. the value x such that x^n = A. The intended approach is the iterative nth root algorithm, which is a specialization of Newton's method: starting from a guess, repeatedly refine via x_{k+1} = ((n-1)·x_k + A / x_k^(n-1)) / n until the change falls below a chosen tolerance. The key insight is that this converges quadratically and avoids relying on a built-in pow/log function.

## Task Requirements
- Implement the algorithm that computes the principal nth root of a positive real number A.
- Follow the iterative nth root algorithm described on the referenced Wikipedia page.
- Handle convergence to a desired precision rather than producing a closed-form result.

## Language Coverage
111 languages implement this task, reflecting very broad coverage typical of a "Simple" classic numerical problem. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, JavaScript, Common Lisp, and Fortran, spanning systems, functional, and scripting paradigms.

## Connections
- [[NewtonsMethod]] — the iteration is a direct specialization of Newton's method applied to x^n − A.
- [[FixedPointIteration]] — the refinement loop is a fixed-point convergence scheme.
- [[NumericalAnalysis]] — addresses precision, tolerance, and convergence rate.
- [[SquareRoot]] — the n = 2 case reduces to a classic square-root algorithm.

## Contradictions
- None — reference task page.
