---
title: "Harriss Spiral (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractal, geometry, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Harriss_Spiral
---

## Summary
The Harriss Spiral, discovered by mathematician Edmund Harriss around 2015, is a fractal nest of spirals built by recursively decomposing a rectangle into a similar rotated rectangle, a square, and another similar rectangle, then drawing circular arcs across the squares. Unlike the golden spiral (which uses the golden ratio), it requires the rectangle's aspect ratio to equal the plastic ratio (~1:1.3247), the real root of x^3 - x - 1 = 0. Because each square spawns two smaller similar regions, the arcs form a branching structure rather than a single spiral.

## Task Requirements
- Construct the recursive rectangle/square decomposition using the plastic-ratio aspect ratio.
- Draw the circular arcs across each square to form the branching nest of spirals.
- Create and display (render) the resulting Harriss Spiral image in your language.

## Language Coverage
14 languages implement this task, spanning graphics-capable and turtle/canvas-style environments rather than purely numeric ones. Representative implementations include Java, Python, Julia, Nim, Raku, Processing, Wren, Phix, Red, and ALGOL 68.

## Connections
- [[PlasticRatio]] — the aspect ratio governing the decomposition
- [[GoldenRatio]] — the analogous constant for the related golden spiral
- [[FractalGeometry]] — the self-similar recursive structure produced
- [[RecursiveSubdivision]] — the rectangle decomposition technique
- [[ComputerGraphics]] — rendering arcs and squares to display the figure

## Contradictions
- None — reference task page.
