---
title: "Bitmap/Bézier curves/Cubic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computer-graphics, curves, raster-graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Bézier_curves/Cubic
---

## Summary
This task asks the programmer to draw a cubic Bézier curve onto a raster image. A cubic Bézier is defined by four control points: two endpoints and two intermediate handles that shape the curve. The standard approach is to evaluate the parametric cubic formula at many values of t between 0 and 1, then connect the resulting sample points with straight line segments. The key insight is that a smooth curve is approximated well enough by sampling it densely and drawing the points as a connected polyline.

## Task Requirements
- Use the raster image storage type from the Basic bitmap storage task.
- Use the `draw_line` function from the Bresenham's line algorithm task.
- Draw a cubic Bézier curve, which is defined by four control points.
- Approximate the curve by sampling parametric points and joining them with line segments.

## Language Coverage
43 languages implement this task, showing broad coverage across systems, scripting, functional, and BASIC-family languages. Representative implementations include C, D, Go, Java, JavaScript, Python, OCaml, Racket, Ruby, Lua, and Wren.

## Connections
- [[BezierCurve]] — the parametric curve this task renders
- [[BernsteinPolynomial]] — the cubic blending functions that weight the four control points
- [[BresenhamLineAlgorithm]] — used to draw each line segment of the approximation
- [[RasterGraphics]] — the bitmap storage and pixel-plotting context
- [[CurveSubdivision]] — an alternative recursive technique for rendering Bézier curves

## Contradictions
- None — reference task page.
