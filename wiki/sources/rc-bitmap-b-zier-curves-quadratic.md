---
title: "Bitmap/Bézier curves/Quadratic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Bézier_curves/Quadratic
---

## Summary
The task asks the programmer to draw a quadratic Bézier curve onto a raster image, building on the bitmap storage type and the `draw_line` routine defined in companion tasks. A quadratic Bézier is defined by three control points (start, control, end), and the practical approach is to sample the curve's parametric equation at many values of t between 0 and 1, then connect the resulting points with straight line segments — approximating the smooth curve with a polyline.

## Task Requirements
- Reuse the raster image data storage type from the Basic bitmap storage task.
- Reuse the `draw_line` function from the Bresenham's line algorithm task.
- Draw a quadratic Bézier curve, as defined on Wikipedia, given its control points.

## Language Coverage
42 languages implement this task, showing broad coverage across systems, functional, scripting, and BASIC-family languages. Representative implementations include C, D, Go, Haskell, Java, Python, Ruby, OCaml, Racket, Lua, Fortran, and Wren.

## Connections
- [[BezierCurve]] — the parametric curve being rendered
- [[BresenhamLineAlgorithm]] — supplies the `draw_line` primitive used to connect sampled points
- [[RasterGraphics]] — the bitmap target the curve is drawn onto
- [[LinearInterpolation]] — De Casteljau-style evaluation underlying the quadratic Bézier
- [[ParametricEquation]] — the t-parameterized form sampled to approximate the curve

## Contradictions
- None — reference task page.
