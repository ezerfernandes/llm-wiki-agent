---
title: "Xiaolin Wu's line algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, anti-aliasing, rasterization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Xiaolin_Wu's_line_algorithm
---

## Summary
The task is to implement Xiaolin Wu's line algorithm, which draws anti-aliased straight lines on a raster grid. Unlike a hard-edged rasterizer, it distributes each pixel's intensity according to how much of the ideal line passes through it, producing smooth, blurred-looking edges. The key insight is that the line's coverage of each pair of vertical (or horizontal) neighboring pixels can be computed from the fractional part of its position, weighting the two pixels' brightness so they sum to full intensity.

## Task Requirements
- Implement the Xiaolin Wu line algorithm as described in Wikipedia.
- The algorithm must produce anti-aliased lines (smoothly shaded edges), not aliased ones.
- Output the drawn line to some raster surface or image representation.

## Language Coverage
46 languages implement this task, spanning low-level assembly through high-level functional and scripting languages. Representative implementations include ARM Assembly, C, C++, C#, Java, Haskell, Python, Rust, Go, Racket, and Wren.

## Connections
- [[AntiAliasing]] — the core visual goal of the algorithm
- [[RasterGraphics]] — the surface model the line is drawn onto
- [[BresenhamsLineAlgorithm]] — the related task for non-anti-aliased lines
- [[LineDrawing]] — the general class of rasterization techniques
- [[FixedPointArithmetic]] — used in several implementations to avoid floating point

## Contradictions
- None — reference task page.
