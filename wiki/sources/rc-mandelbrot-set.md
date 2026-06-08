---
title: "Mandelbrot set (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, complex-numbers, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mandelbrot_set
---

## Summary
The task asks the programmer to generate and draw the Mandelbrot set, the canonical fractal defined over the complex plane. The core insight is simple: for each point c in the complex plane, iterate z → z² + c starting from z = 0, and color the pixel by how many iterations pass before |z| escapes a fixed radius (2). Points that never escape within the iteration cap belong to the set. The page deliberately leaves the rendering method open, noting many algorithms and generating functions exist.

## Task Requirements
- Compute the escape-time iteration z → z² + c for each point of a sampled region of the complex plane.
- Determine membership / divergence speed using an escape radius (|z| > 2) and a maximum iteration count.
- Draw or output the resulting image (raster image, ASCII art, or other visual rendering are all acceptable).

## Language Coverage
150 languages implement this task, an exceptionally broad coverage spanning compiled, scripting, functional, esoteric, and even shader/database languages. Representative implementations include C, C++, Rust, Python, Haskell, Java, JavaScript, Forth, GLSL (shader-based), MySQL, and Brainf***.

## Connections
- [[MandelbrotSet]] — the fractal object this task renders
- [[ComplexNumbers]] — the iteration z² + c operates over the complex plane
- [[EscapeTimeAlgorithm]] — the standard divergence-counting rendering method
- [[Fractals]] — the broader class of self-similar structures this belongs to
- [[RasterGraphics]] — the typical pixel-buffer output target

## Contradictions
- None — reference task page.
