---
title: "Check if two polygons overlap (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, collision-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Check_if_two_polygons_overlap
---

## Summary
Given two polygons, each described as a list of vertices, determine whether the two shapes overlap. The task is intentionally open-ended; the canonical approach is the Separating Axis Theorem, which tests whether a line (axis) exists that separates the two convex shapes, but solutions must also account for edge intersections and containment cases.

## Task Requirements
- Accept two polygons, each represented as an ordered list of vertices.
- Return whether the two polygons overlap.

## Language Coverage
22 languages implement this task, giving solid coverage across systems, scripting, and array-oriented languages. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Julia, Perl, Raku, and Fortran.

## Connections
- [[SeparatingAxisTheorem]] — standard convex-overlap test by projecting onto candidate separating axes
- [[ComputationalGeometry]] — the broader field this task belongs to
- [[CollisionDetection]] — practical application of polygon overlap testing
- [[LineSegmentIntersection]] — checking whether polygon edges cross
- [[ConvexPolygon]] — the shape class most overlap algorithms assume

## Contradictions
- None — reference task page.
