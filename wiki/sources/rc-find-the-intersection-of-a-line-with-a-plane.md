---
title: "Find the intersection of a line with a plane (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, linear-algebra, collision-detection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_the_intersection_of_a_line_with_a_plane
---

## Summary
The task asks the programmer to compute the point where an infinite ray (line) intersects an infinite plane in 3D space. The key insight is that the intersection is found by parameterizing the ray as origin + t·direction and solving for the scalar t where the point lies on the plane, using vector dot products against the plane's normal.

## Task Requirements
- Given a ray with direction (0, -1, -1) passing through point (0, 0, 10).
- Given a plane with normal vector (0, 0, 1) passing through point [0, 0, 5].
- Find and report the point of intersection of the ray with the plane.

## Language Coverage
49 languages implement this task, showing broad coverage across systems, functional, scientific, and scripting families. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Fortran, MATLAB, and Wren.

## Connections
- [[VectorAlgebra]] — uses vector addition, subtraction, and scaling
- [[DotProduct]] — projects vectors onto the plane normal to solve for the parameter
- [[PlaneGeometry]] — the plane is defined by a point and a normal vector
- [[CollisionDetection]] — ray-plane intersection is a core primitive
- [[ParametricEquation]] — the ray is expressed as a parametric line

## Contradictions
- None — reference task page.
