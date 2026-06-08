---
title: "Euler method (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-analysis, differential-equations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Euler_method
---

## Summary
The task asks the programmer to implement Euler's method, the simplest explicit scheme for numerically approximating the solution of a first-order ordinary differential equation given an initial value. The core idea is to replace the derivative with a finite-difference approximation, yielding the iterative update rule y(n+1) = y(n) + h·f(t(n), y(n)), where the step size h trades accuracy against computation cost.

## Task Requirements
- Implement a reusable Euler's-method routine that advances an ODE of the form dy/dt = f(t, y) from an initial value.
- Apply it to Newton's cooling law, dT/dt = -k(T - T_R), for three step sizes: 2 s, 5 s, and 10 s.
- Use the initial values T0 = 100 °C, T_R = 20 °C, k = 0.07, over the time interval 0 s to 100 s.
- Compare the numerical approximation against the analytical solution T(t) = T_R + (T0 - T_R)·e^(-kt), illustrating how larger step sizes reduce accuracy.

## Language Coverage
89 languages implement this task, giving broad coverage across functional, imperative, scientific, and esoteric languages. Representative implementations include C, C++, Python, Haskell, Common Lisp (the reference solution), Julia, Fortran, MATLAB, Rust, and Scala.

## Connections
- [[EulerMethod]] — the numerical integration scheme being implemented
- [[OrdinaryDifferentialEquations]] — the class of problems being solved
- [[FiniteDifferenceMethod]] — the approximation used to discretize the derivative
- [[InitialValueProblem]] — the problem formulation with a given starting condition
- [[NumericalIntegration]] — the broader family of techniques this belongs to

## Contradictions
- None — reference task page.
