---
title: "Bitmap/Midpoint circle algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computer-graphics, rasterization, integer-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Midpoint_circle_algorithm
---

## Summary
This task asks the programmer to implement the midpoint circle algorithm (also called Bresenham's circle algorithm) to draw a circle outline into a raster image using the basic bitmap storage type defined in a companion task. The key insight is that the circle can be rasterized using only integer addition, subtraction, and bit shifts by tracking a decision variable, exploiting the eight-way symmetry of a circle so that one computed octant fills in all eight.

## Task Requirements
- Build on the raster image storage type from the Basic bitmap storage task.
- Implement the midpoint/Bresenham circle algorithm to plot a circle given a center and radius.
- Produce the circle outline as pixels written into the bitmap.

## Language Coverage
54 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects. Representative implementations include C, C#, Java, Python, Go, Haskell, Ruby, Lua, OCaml, and Racket.

## Connections
- [[MidpointCircleAlgorithm]] — the rasterization technique this task implements
- [[BresenhamsLineAlgorithm]] — sibling integer-only rasterization method by the same author
- [[Rasterization]] — converting geometric shapes into pixels on a grid
- [[IntegerArithmetic]] — the algorithm avoids floating point by using a decision variable
- [[RasterGraphics]] — the bitmap storage domain this task operates on

## Contradictions
- None — reference task page.
