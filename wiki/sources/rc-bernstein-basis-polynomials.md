---
title: "Bernstein basis polynomials (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, polynomials, computer-graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bernstein_basis_polynomials
---

## Summary
The Bernstein basis polynomials of degree n are b_{k,n}(t) = C(n,k) t^k (1-t)^(n-k), and any real polynomial can be written as a linear combination of them whose coefficients are the Bernstein coefficients. This task asks the programmer to build a small toolkit for converting between ordinary monomial coefficients and degree-2/degree-3 Bernstein coefficients, and for evaluating Bernstein-form polynomials via de Casteljau's algorithm. The motivating insight is that OpenType fonts store glyph outlines exactly as degree-2 or degree-3 Bernstein (Bezier) coefficients, so these conversions are a practical font/graphics operation.

## Task Requirements
- Subprogram (1): convert monomial coefficients of a degree-2-or-less polynomial to degree-2 Bernstein coefficients.
- Subprogram (2): evaluate a degree-2 Bernstein polynomial at a given point using de Casteljau's algorithm.
- Subprogram (3): convert monomial coefficients of a degree-3-or-less polynomial to degree-3 Bernstein coefficients.
- Subprogram (4): evaluate a degree-3 Bernstein polynomial at a point via de Casteljau's algorithm.
- Subprogram (5): elevate degree-2 Bernstein coefficients to degree-3 Bernstein coefficients.
- Demonstrate all subprograms on p(x)=1, q(x)=1+2x+3x^2, and r(x)=1+2x+3x^2+4x^3, evaluating at x=0.25 and x=7.50; optionally also evaluate in the monomial basis using Horner's scheme.

## Language Coverage
25 languages implement this task, spanning historic and modern systems languages. Representative entries include ALGOL 60 (the reference implementation), ALGOL 68, C, C++, C#, Go, Java, JavaScript, Julia, Python, Rust, and Wren.

## Connections
- [[BernsteinPolynomial]] — the basis functions central to the task.
- [[DeCasteljausAlgorithm]] — the numerically stable evaluation method required.
- [[BezierCurve]] — Bernstein coefficients are exactly the control points of Bezier curves.
- [[HornersMethod]] — used for the optional monomial-basis evaluation.
- [[BinomialCoefficient]] — appears in the definition of each basis polynomial.

## Contradictions
- None — reference task page.
