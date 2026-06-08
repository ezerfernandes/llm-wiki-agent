---
title: "Convex hull (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Convex_hull
---

## Summary
This task asks the programmer to compute the convex hull of an arbitrary set of two-dimensional points: the smallest convex polygon that encloses all of them, defined by the subset of points that form its boundary vertices. The key insight is that interior points and points lying on hull edges are discarded, leaving only the extreme "corner" points, typically found by sorting and testing the turn direction (cross product) at each candidate vertex.

## Task Requirements
- Given a set of arbitrary 2D points, find the points that form their convex hull.
- A worked example with 20 input points is provided whose hull is the 7 points (-9,-3), (-3,-9), (19,-8), (17,5), (12,17), (5,19), (-3,15).

## Language Coverage
58 languages implement this task, showing broad coverage across functional, imperative, and array-oriented paradigms. Representative implementations include C, C++, Java, Python, Go, Rust, Haskell, OCaml, Julia, Common Lisp, J, and Wren.

## Connections
- [[ConvexHull]] — the geometric structure being computed
- [[ComputationalGeometry]] — the field this problem belongs to
- [[GrahamScan]] — a standard algorithm (referenced via the task's see-also link) for the construction
- [[CrossProduct]] — used to determine orientation/turn direction of point triples
- [[Sorting]] — most hull algorithms sort points by angle or coordinate as a first step

## Contradictions
- None — reference task page.
