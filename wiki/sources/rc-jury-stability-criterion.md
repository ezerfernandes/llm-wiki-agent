---
title: "Jury stability criterion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-systems, numerical-methods, polynomials]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jury_stability_criterion
---

## Summary
The task is to implement the Jury stability criterion, an algebraic test that determines whether all roots of a real polynomial lie strictly inside the unit circle in the complex plane — the stability condition for discrete-time control systems. The key insight is that this can be decided without computing the roots: by checking a few necessary conditions on the polynomial and then building a "Jury array" of derived row coefficients and comparing magnitudes of their endpoints.

## Task Requirements
- Given a characteristic polynomial P(z) = a0·z^n + a1·z^(n-1) + ... + an with real coefficients and a0 ≠ 0, decide whether all roots are inside the unit circle.
- Verify the necessary conditions: P(1) > 0; (-1)^n · P(-1) > 0; and |an| < a0.
- Construct the Jury array, where each successive row is derived from 2×2 determinants of the previous row and has one fewer element, continuing until a single-element row remains.
- Apply the full stability criterion: |b0| > |b_{n-1}|, |c0| > |c_{n-2}|, and so on for every row.
- Report whether the system is stable (all conditions hold).

## Language Coverage
7 languages implement this task — a small, specialized set reflecting its control-theory niche. Representative implementations include Fortran, FreeBASIC, Julia, Mathematica/Wolfram Language, Phix, Python, and Wren.

## Connections
- [[ControlSystems]] — the criterion's primary application domain
- [[Polynomials]] — operates on polynomial coefficients
- [[NumericalStability]] — high-order polynomials introduce numerical issues
- [[Determinant]] — array rows are built from 2×2 determinants
- [[SchurCohnTheorem]] — alternative root-location stability test

## Contradictions
- None — reference task page.
