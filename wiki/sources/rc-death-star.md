---
title: "Death Star (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, constructive-solid-geometry, ray-tracing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Death_Star
---

## Summary
The task asks the programmer to render a large sphere with a chunk carved out of it by geometrically subtracting a smaller, offset sphere — producing the iconic "Death Star" silhouette. The key insight is constructive solid geometry (CSG): the difference of two solids, which for a rendered image is most simply realized by ray casting each pixel and shading the nearest visible surface point that lies inside the big sphere but outside the small one.

## Task Requirements
- Display a region consisting of one large sphere with part of a smaller sphere removed from it.
- The removal is performed via geometric subtraction (set difference of the two solid spheres).
- The result is the recognizable concave-dish "Death Star" shape.

## Language Coverage
43 languages implement this task, spanning low-level graphics, scripting, functional, and dedicated CAD/ray-tracing tools. Representative implementations include C, Python, Java, JavaScript, Haskell, Lua, Go, Perl, Raku, and the domain-specific renderers POV-Ray, Brlcad, and Openscad.

## Connections
- [[ConstructiveSolidGeometry]] — the difference operation between two solids defines the shape
- [[RayTracing]] — common technique to render the lit, shaded surface per pixel
- [[Sphere]] — the two primitive solids being combined
- [[GeometricSubtraction]] — the set-difference operation removing one volume from another
- [[ComputerGraphics]] — the broader domain of producing the displayed image

## Contradictions
- None — reference task page.
