---
title: "Steffensen's method (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, root-finding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Steffensen's_method
---

## Summary
Steffensen's method is a derivative-free numerical technique for finding roots of functions, comparable to Newton's method in convergence behavior but, like Newton's, prone to failing to converge at all. The task uses the Aitken's-delta-squared-extrapolation variant, which finds a fixed point `p` of `f` (where `f(p) = p`); to solve `g(t) = 0` one finds a fixed point of `f(t) = g(t) + t`. The illustrative problem is locating the four intersection points of two quadratic Bézier parabolas via implicitization, evaluating the curve with de Casteljau's algorithm and plugging values into the implicit equation `5x² + y − 5 = 0`.

## Task Requirements
- Implement Steffensen's method using Aitken's extrapolation to find a fixed point of a function, iterating until a tolerance is met or a maximum iteration count is exceeded.
- Convert the root-finding problem `g(t) = 0` into a fixed-point problem via `f(t) = g(t) + t`.
- Define the two quadratic Bézier curves with control points (-1,0),(0,10),(1,0) and (2,1),(-8,2),(2,3).
- Evaluate the convex-leftward curve's x(t) and y(t) directly from control points using de Casteljau's algorithm (no need to expand the degree-4 polynomial in t).
- Use the implicit equation of the convex-upward parabola, `5x² + y − 5 = 0`, and search for the intersection points, demonstrating that the method finds only some (or none) of the four roots depending on the initial estimate.

## Language Coverage
27 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include ALGOL 68, ATS, C, C++, Go, Java, JavaScript, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[SteffensensMethod]] — the core derivative-free root-finding algorithm
- [[NewtonsMethod]] — closely related root-finder requiring derivatives
- [[AitkensDeltaSquaredProcess]] — convergence-acceleration scheme used by this variant
- [[FixedPointIteration]] — reframing root-finding as finding `f(p) = p`
- [[BezierCurve]] — the parametric curves whose intersections are sought
- [[DeCasteljausAlgorithm]] — evaluates the Bézier curve points without polynomial expansion

## Contradictions
- None — reference task page.
