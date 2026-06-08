---
title: "Draw a sphere (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, 3d-rendering, ascii-art]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Draw_a_sphere
---

## Summary
This task asks the programmer to render a sphere, either as true graphics or as ASCII art depending on the language's capabilities. The defining insight is that a convincing sphere comes mostly from shading: computing surface normals and applying a simple lighting model (e.g. Lambertian diffuse reflection toward a light source) produces the illusion of curvature on what is otherwise a flat circle.

## Task Requirements
- Draw a sphere.
- It may be represented graphically or in ASCII art, depending on language capability.
- Either a static image or a rotational projection is acceptable.

## Language Coverage
85 languages implement this task, spanning native 3D/graphics toolkits, 2D rasterizers, and pure text output. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, JavaScript, POV-Ray, and SVG, with several ASCII-only renderings in languages such as AWK, REXX, and BASIC.

## Connections
- [[RayTracing]] — sphere-ray intersection is the canonical way to render a shaded sphere
- [[LambertianShading]] — diffuse lighting via the dot product of surface normal and light direction
- [[SurfaceNormal]] — per-pixel normals drive the shading that conveys curvature
- [[OrthographicProjection]] — mapping the 3D hemisphere onto a 2D circle of pixels or characters
- [[ASCIIArt]] — character-density gradients used for non-graphical renderings

## Contradictions
- None — reference task page.
