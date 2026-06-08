---
title: "Ray-casting algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, point-in-polygon]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ray-casting_algorithm
---

## Summary
The task asks the programmer to determine whether a given point lies inside or outside a polygon using the ray-casting algorithm. A horizontal ray is shot from the point toward infinity and the number of polygon edges it crosses is counted: an odd count means the point is inside, an even count means it is outside. The key insight is that each border crossing toggles between inside and outside, and since the ray ultimately ends outside the finite polygon, parity of crossings uniquely decides containment.

## Task Requirements
- Implement a function that returns true/false for whether a point is inside a polygon.
- For each side of the polygon, test whether the horizontal ray from point P intersects that segment.
- Count intersections; return "inside" if the count is odd, "outside" if even.
- Implement `ray_intersects_segment(P, A, B)` where A is the endpoint with the smaller y coordinate and B the larger.
- Handle the degenerate "ray on vertex" case by nudging the point's y coordinate by a small epsilon.
- Use slope comparison (m_red of segment vs m_blue of the point-to-A line, treating vertical lines as infinite slope) to resolve points falling inside the segment's bounding box.

## Language Coverage
43 languages implement this task, giving broad coverage across imperative, functional, and array-oriented paradigms. Representative implementations include C, C++, C#, Java, Python, JavaScript, Haskell, Common Lisp, Rust, Go, Julia, and J.

## Connections
- [[PointInPolygon]] — the geometric containment problem this task solves
- [[ComputationalGeometry]] — the field these segment-intersection tests belong to
- [[LineSegmentIntersection]] — the core primitive `ray_intersects_segment` computes
- [[ParityArgument]] — the odd/even crossing count that yields the inside/outside answer

## Contradictions
- None — reference task page.
