---
title: "Circles of given radius through two points (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometry, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Circles_of_given_radius_through_two_points
---

## Summary
Given two points on a plane and a radius, this task asks the programmer to find the (usually two) circles of that radius whose circumference passes through both points. The key geometric insight is that each circle's center lies on the perpendicular bisector of the segment joining the two points, offset from the midpoint by a distance derived from the radius and half the inter-point distance via the Pythagorean theorem.

## Task Requirements
- Write a function taking two points and a radius that returns the two circles through those points (or an indication of a special case).
- Handle r == 0.0: never describes circles, except when the points are coincident (then it collapses to a single point).
- Handle coincident points: infinitely many circles unless r == 0.0.
- Handle a diameter case (points exactly 2r apart): return two identical circles or a single circle.
- Handle points too far apart (distance > 2r): no circles can be drawn.
- Demonstrate output for the five given test inputs.

## Language Coverage
72 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Haskell, Python, Julia, Java, Perl, Raku, and Wren.

## Connections
- [[ComputationalGeometry]] — the task is a classic planar geometry construction problem.
- [[PerpendicularBisector]] — each candidate circle center lies on the perpendicular bisector of the two points.
- [[PythagoreanTheorem]] — used to compute the center offset from the midpoint.
- [[FloatingPointArithmetic]] — edge cases (coincident points, exact diameter) require careful float handling.

## Contradictions
- None — reference task page.
