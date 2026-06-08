---
title: "Check if a polygon overlaps with a rectangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, collision-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Check_if_a_polygon_overlaps_with_a_rectangle
---

## Summary
The task asks the programmer to determine whether a given polygon and an axis-aligned rectangle intersect. The polygon is supplied as an ordered list of its vertices, while the rectangle is given in (x, y, width, height) form. The key insight is that a rectangle is just a special four-vertex polygon, so the problem reduces to general polygon-polygon overlap testing — typically via the Separating Axis Theorem or edge-intersection plus containment checks.

## Task Requirements
- Accept a polygon as an array/vector/list of its vertices.
- Accept a rectangle expressed as x, y, width, and height.
- Return whether the two shapes intersect (overlap).

## Language Coverage
21 languages implement this task, giving broad coverage across systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Perl, Raku, Julia, and Wren.

## Connections
- [[ComputationalGeometry]] — the domain this overlap test belongs to
- [[SeparatingAxisTheorem]] — common technique for convex shape overlap
- [[CollisionDetection]] — practical application of shape-intersection tests
- [[PolygonOverlap]] — generalization of which a rectangle is a special case
- [[LineSegmentIntersection]] — underlying primitive for edge-crossing checks

## Contradictions
- None — reference task page.
