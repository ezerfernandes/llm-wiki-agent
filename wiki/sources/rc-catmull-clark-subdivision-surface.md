---
title: "Catmull–Clark subdivision surface (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computer-graphics, geometry, mesh-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Catmull–Clark_subdivision_surface
---

## Summary
The task is to implement the Catmull-Clark surface subdivision algorithm, which refines a 3D polygon mesh (a set of points plus polygons) into a smoother mesh made entirely of quadrilaterals. The key insight is that each subdivision step computes new face points, edge points, and repositioned vertex points using weighted averages, and repeated application converges toward a smooth limit surface (e.g. a cube approaching a sphere).

## Task Requirements
- For each face, create a *face point* equal to the average of all the face's vertices.
- For each edge, create an *edge point* equal to the average of the edge midpoint and the face points of the two adjacent faces.
- Reposition each original vertex using the formula with weights m1=(n-3)/n, m2=1/n, m3=2/n applied to old coords, average of adjacent face points, and average of adjacent edge midpoints (n = number of faces touching the vertex).
- Replace each face with new quad faces connecting original vertices, edge points, and the face point.
- Handle holes: an edge bordering a hole belongs to only one face; a boundary vertex has n_faces != n_edges. Hole-border edge points are the plain edge midpoint, and boundary vertices are repositioned using only hole-boundary edge midpoints and old coordinates.

## Language Coverage
18 languages implement this task, spanning systems and graphics-oriented languages as well as functional and array languages. Representative implementations include C, C++, Go, Rust, Haskell, OCaml, J, Java, JavaScript, Python, Julia, and Wren.

## Connections
- [[SubdivisionSurface]] — the general family of mesh-refinement schemes this task belongs to.
- [[PolygonMesh]] — the vertex/edge/face data structure being refined.
- [[ComputerGraphics]] — the broader domain of 3D surface modeling.
- [[LinearInterpolation]] — the weighted-average barycentric computations at the core of each step.
- [[ComputationalGeometry]] — the geometric reasoning over points, edges, and faces.

## Contradictions
- None — reference task page.
