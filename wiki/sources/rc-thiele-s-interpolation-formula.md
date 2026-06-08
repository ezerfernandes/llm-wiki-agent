---
title: "Thiele's interpolation formula (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-analysis, interpolation, continued-fractions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Thiele's_interpolation_formula
---

## Summary
The task asks the programmer to implement Thiele's interpolation formula, which approximates a single-variable function as a continued fraction built from reciprocal differences of sample points. The key insight is that the continued-fraction form (using the recursively defined reciprocal-difference operator rho) often converges better than polynomial interpolation, and once you have the interpolant you can also invert it numerically.

## Task Requirements
- Build a 32-row table of values for x from 0 by 0.05 to 1.55 for the trig functions sin, cos, and tan.
- Using the table columns, define an inverse for each trig function via Thiele's interpolation.
- Verify the trig identities: 6 * arcsin(1/2) = pi, 3 * arccos(1/2) = pi, and 4 * arctan(1) = pi.

## Language Coverage
34 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Fortran, Haskell, Common Lisp, Julia, Python, Perl, J, and Wren.

## Connections
- [[Interpolation]] — Thiele's formula is a method for interpolating a function from sampled points.
- [[ContinuedFractions]] — the interpolant is expressed as a continued fraction.
- [[ReciprocalDifferences]] — the recursively defined rho operator that drives the formula.
- [[NumericalAnalysis]] — the broader field this approximation technique belongs to.
- [[TrigonometricFunctions]] — sin, cos, and tan are interpolated and inverted in the demonstration.

## Contradictions
- None — reference task page.
