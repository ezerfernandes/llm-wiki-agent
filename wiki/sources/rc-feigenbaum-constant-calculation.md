---
title: "Feigenbaum constant calculation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, chaos-theory, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Feigenbaum_constant_calculation
---

## Summary
The task asks the programmer to numerically calculate the Feigenbaum constant (δ ≈ 4.669201...), the universal ratio that describes how the period-doubling bifurcations of a one-dimensional map (such as the logistic map) accelerate toward the onset of chaos. The key insight is that δ is the limiting ratio of successive intervals between bifurcation parameter values, so the standard approach iterates the period-doubling cascade and takes the ratio of consecutive gaps as it converges.

## Task Requirements
- Compute the Feigenbaum (first) constant δ.
- Follow the method described in the referenced Wikipedia article on Feigenbaum constants, typically by tracking successive period-doubling bifurcation points and forming the ratio of the differences between them.

## Language Coverage
51 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C, C++, Go, Rust-adjacent V (Vlang), Haskell, Julia, Python, Perl, Raku, Fortran, and Wren.

## Connections
- [[ChaosTheory]] — δ characterizes the route to chaos via period doubling
- [[LogisticMap]] — the canonical map whose bifurcations yield the constant
- [[Bifurcation]] — successive period-doubling events define the ratios
- [[NumericalMethods]] — iterative convergence and limit estimation
- [[MathematicalConstants]] — δ is a universal constant of nonlinear dynamics

## Contradictions
- None — reference task page.
