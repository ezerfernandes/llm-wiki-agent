---
title: "Determine if two triangles overlap (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, collision-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_two_triangles_overlap
---

## Summary
Given two triangles lying in the same 2D plane, decide whether their interiors overlap. This is a foundational primitive in collision detection. The standard approach uses the Separating Axis Theorem: two convex shapes are disjoint if and only if some edge of one acts as a separating line with the other shape entirely on the opposite side. The task also notes the ambiguous edge case where the triangles only touch at a single corner.

## Task Requirements
- Determine, for each given pair of triangles, whether they overlap in 2D.
- Evaluate a fixed set of six test pairs (overlapping, identical, disjoint, and edge-sharing configurations).
- Optionally handle the boundary case where only a single corner is in contact, where there is no single agreed-upon correct answer (touching may count as overlap or not).

## Language Coverage
47 languages implement this task, spanning systems languages, functional languages, scripting languages, and array/BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, and Fortran.

## Connections
- [[SeparatingAxisTheorem]] — the canonical algorithm for testing convex-shape overlap
- [[CollisionDetection]] — the broader problem domain this primitive serves
- [[ComputationalGeometry]] — field covering point-in-triangle and orientation tests
- [[CrossProduct]] — signed-area/orientation sign used to find a separating edge
- [[ConvexPolygon]] — triangles are the simplest convex polygons, enabling the convexity-based test

## Contradictions
- None — reference task page.
