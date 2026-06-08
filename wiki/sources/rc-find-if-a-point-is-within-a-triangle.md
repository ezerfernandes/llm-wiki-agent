---
title: "Find if a point is within a triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, collision-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_if_a_point_is_within_a_triangle
---

## Summary
This task asks the programmer to determine whether a point P(x, y) lies inside a triangle defined by three vertices A, B, and C on the real-number plane. Any algorithm is permitted, with a bonus for explaining why the chosen method works. The common approaches are the sign-of-cross-product (orientation) test, which checks that P falls on the same side of all three directed edges, and barycentric coordinates, which express P as a weighted combination of the vertices and test that all weights are non-negative.

## Task Requirements
- Assume points lie on a plane with (x, y) real-number coordinates.
- Given a point P and a triangle formed by points A, B, and C, determine if P is within triangle ABC.
- Any algorithm may be used.
- Bonus: explain why the chosen algorithm works.

## Language Coverage
46 languages implement this task, spanning systems languages, functional languages, BASIC dialects, and math-oriented tools — representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, Raku, and Mathematica/Wolfram Language.

## Connections
- [[ComputationalGeometry]] — the task is a foundational point-in-shape primitive
- [[BarycentricCoordinates]] — one standard method expresses P relative to the triangle vertices
- [[CrossProduct]] — the orientation/sign test relies on the 2D cross product to determine side
- [[CollisionDetection]] — point-in-triangle is a building block for hit testing
- [[PointInPolygon]] — the general case this task specializes

## Contradictions
- None — reference task page.
