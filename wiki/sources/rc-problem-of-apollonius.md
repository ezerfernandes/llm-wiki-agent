---
title: "Problem of Apollonius (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, analytic-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Problem_of_Apollonius
---

## Summary
The task asks the programmer to find a circle that is tangent to three given circles, the classical Problem of Apollonius. The straightforward approach is the algebraic solution: set up equations expressing equal distances from the unknown circle's center to each given circle's edge, then solve the resulting system. The key insight is that the choice of internal versus external tangency for each given circle (encoded as +1/-1 signs) selects which of the up-to-eight distinct solution circles is returned.

## Task Requirements
- Compute the circle tangent to three specified circles, each defined by a center and radius.
- Support both tangency modes: an "internally tangent" solution (tangent to all three from inside) and an "externally tangent" solution.
- Demonstrate with the example circles, reproducing the red (internal) and green (external) solution circles shown in the reference diagram.

## Language Coverage
53 languages implement this task, spanning systems and functional languages, scripting languages, and many BASIC dialects. Representative implementations include C, C++, C#, Java, Python, Haskell, Go, Julia, Perl, Raku, Ruby, and Fortran.

## Connections
- [[ComputationalGeometry]] — constructing a circle tangent to other circles
- [[AnalyticGeometry]] — the algebraic solution via coordinate equations
- [[SystemOfLinearEquations]] — solving for the tangent circle's parameters
- [[QuadraticEquation]] — the radius is recovered by solving a quadratic

## Contradictions
- None — reference task page.
