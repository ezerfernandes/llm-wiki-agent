---
title: "Sutherland-Hodgman polygon clipping (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sutherland-Hodgman_polygon_clipping
---

## Summary
The task is to implement the Sutherland-Hodgman clipping algorithm, which computes the intersection of an arbitrary "subject" polygon with a convex "clip" polygon. The key insight is that clipping against a convex region can be decomposed into clipping the subject polygon successively against each edge of the clip polygon (treated as an infinite half-plane), feeding the output of one edge as input to the next. This is widely used in 2D computer graphics to discard parts of a scene that fall outside a viewport.

## Task Requirements
- Clip the closed subject polygon with vertices (50,150), (200,50), (350,150), (350,300), (250,300), (200,250), (150,350), (100,250), (100,200) by the rectangle (100,100), (300,100), (300,300), (100,300).
- Print the sequence of points defining the resulting clipped polygon.
- Extra credit: render all three polygons (subject, clip, result) on a graphical surface with distinct colors and fill the resulting polygon.

## Language Coverage
49 languages implement this task, spanning systems languages, functional languages, and BASIC dialects. Representative implementations include C, C++, C#, Rust, Go, Java, JavaScript/TypeScript, Python, Haskell, Common Lisp, OCaml, and Wren.

## Connections
- [[ComputationalGeometry]] — the algorithm is a foundational 2D geometry routine.
- [[PolygonClipping]] — the general problem class this task solves.
- [[ConvexPolygon]] — the clip region must be convex for the half-plane decomposition to be valid.
- [[LineIntersection]] — each edge step requires computing where subject edges cross a clip edge.
- [[ComputerGraphics]] — primary application domain (viewport/scene clipping).

## Contradictions
- None — reference task page.
