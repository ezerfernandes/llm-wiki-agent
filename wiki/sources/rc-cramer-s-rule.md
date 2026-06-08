---
title: "Cramer's rule (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, determinants]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cramer's_rule
---

## Summary
Cramer's rule is an explicit closed-form method for solving a square system of linear equations that has a unique solution. Each unknown equals the ratio of two determinants: the numerator is the determinant of the coefficient matrix with one column replaced by the right-hand-side vector, and the denominator is the determinant of the unmodified coefficient matrix. The task asks the programmer to implement this rule and use it to solve a concrete 4x4 system. The key insight is that determinant-based solving is elegant but scales poorly compared to Gaussian elimination.

## Task Requirements
- Implement Cramer's rule for a system of linear equations with as many equations as unknowns.
- Compute the solution as the ratio of determinants: replace column i of the coefficient matrix with the constants vector to get the numerator for unknown i, divided by the determinant of the original coefficient matrix.
- Use the rule to solve the given 4x4 system in unknowns w, x, y, z.

## Language Coverage
48 languages implement this task, reflecting broad coverage across general-purpose, functional, array-oriented, and computer-algebra languages. Representative entries include C, C++, Java, Python, Haskell, Julia, Rust, Go, J, and Mathematica/Wolfram Language.

## Connections
- [[LinearAlgebra]] — the mathematical domain Cramer's rule belongs to
- [[Determinant]] — the core operation the rule is built on
- [[SystemOfLinearEquations]] — the problem class being solved
- [[MatrixMultiplication]] — related matrix operations often used alongside it
- [[GaussianElimination]] — the more scalable alternative solving method

## Contradictions
- None — reference task page.
