---
title: "Ramer-Douglas-Peucker line simplification (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ramer-Douglas-Peucker_line_simplification
---

## Summary
The task asks the programmer to implement the Ramer-Douglas-Peucker algorithm, a recursive curve-simplification method that reduces the number of points in a polyline while preserving its overall shape. The key insight is to find the point farthest from the line segment connecting the two endpoints; if that maximum perpendicular distance exceeds a given threshold, the point is kept and the curve is split and processed recursively, otherwise all intermediate points are discarded.

## Task Requirements
- Implement the Ramer-Douglas-Peucker algorithm to simplify a 2D polyline.
- Simplify the specific line through the points (0,0), (1,0.1), (2,-0.1), (3,5), (4,6), (5,7), (6,8.1), (7,9), (8,9), (9,9).
- Use an error threshold (epsilon) of 1.0.
- Display the remaining points after simplification.

## Language Coverage
43 languages implement this task, showing broad coverage across systems, scripting, functional, and BASIC-family languages. Representative examples include C, C++, Rust, Go, Java, Python, JavaScript, Julia, Haskell-style functional approaches in J, and Perl/Raku.

## Connections
- [[ComputationalGeometry]] — the task operates on points and line segments in 2D space
- [[Recursion]] — the algorithm recursively subdivides the polyline at the farthest point
- [[PerpendicularDistance]] — each point's distance to the connecting segment drives the keep/discard decision
- [[CurveSimplification]] — the broader class of algorithms for reducing polyline complexity
- [[DivideAndConquer]] — the curve is split into independent subproblems at the retained point

## Contradictions
- None — reference task page.
