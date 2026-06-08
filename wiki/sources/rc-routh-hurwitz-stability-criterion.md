---
title: "Routh–Hurwitz stability criterion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-theory, polynomials, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Routh–Hurwitz_stability_criterion
---

## Summary
The task asks the programmer to implement the Routh–Hurwitz stability criterion, a test that determines whether a linear time-invariant (LTI) system is stable by checking the roots of its characteristic polynomial without actually computing them. The key insight is that the system is stable if and only if every root has a negative real part, and this can be decided by building a triangular "Routh array" from the polynomial coefficients: the number of roots with positive real parts equals the number of sign changes in the array's first column.

## Task Requirements
- Given a real characteristic polynomial P(s) = a₀sⁿ + a₁sⁿ⁻¹ + … + aₙ with a₀ > 0, construct the Routh array.
- Compute each subsequent row from the two rows above it using the standard cross-multiplication formula (e.g. bᵢ = (a₁·a₂ᵢ − a₀·a₂ᵢ₊₁)/a₁).
- Count sign changes in the first column to report the number of right-half-plane roots; conclude the system is stable only if all first-column entries share the same sign.
- Ideally handle the special cases: a single zero in the first column (replace with a small ε) and an entirely zero row (form an auxiliary polynomial and use its derivative).

## Language Coverage
8 languages implement this task, a modest spread skewed toward numerically oriented and BASIC-family languages. Representative implementations include EasyLang, Fortran, FreeBASIC, Julia, Phix, Python, Raku, and Wren.

## Connections
- [[ControlTheory]] — the criterion is a foundational tool for analyzing feedback system stability
- [[CharacteristicPolynomial]] — the array is built directly from its coefficients
- [[PolynomialRootFinding]] — the criterion sidesteps explicit root computation while answering a question about root location
- [[NumericalStability]] — the ε-substitution special case addresses degenerate first-column zeros
- [[LinearTimeInvariantSystems]] — the class of systems the test applies to

## Contradictions
- None — reference task page.
