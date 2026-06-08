---
title: "Bézier curves/Intersections (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, curves, root-finding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bézier_curves/Intersections
---

## Summary
The task gives two planar quadratic Bézier curves, each defined by three control points, that happen to trace parabolas crossing at four points. The goal is to compute and print the (x,y) coordinates of all four intersections. The key challenge is that intersecting two quadratic curves reduces to solving a polynomial system, so implementations typically use subdivision/clipping or resultant-based root finding rather than a closed-form shortcut.

## Task Requirements
- Take the two fixed quadratic Bézier curves with control points (-1,0),(0,10),(1,0) and (2,1),(-8,2),(2,3).
- Find all four points where the curves intersect.
- Print the (x,y) coordinates of each intersection point.
- Any correct algorithm is acceptable (subdivision, Bézier clipping, resultants, numerical root finding, etc.).

## Language Coverage
25 languages implement this task, a moderate breadth weighted toward systems and numeric languages. Representative examples include Ada, C, C++, C#, D, Fortran, Go, Java, JavaScript, Julia, Nim, Python, Raku, Rust, Phix, and Wren.

## Connections
- [[BezierCurve]] — the parametric curve type whose intersections are sought
- [[ComputationalGeometry]] — the broader field of curve/shape intersection problems
- [[RootFinding]] — solving the resulting polynomial system numerically
- [[Resultants]] — algebraic elimination technique used to reduce two curves to one polynomial
- [[ParametricEquations]] — Bézier curves are defined parametrically over t in [0,1]

## Contradictions
- None — reference task page.
