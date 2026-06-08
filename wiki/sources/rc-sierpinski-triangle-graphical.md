---
title: "Sierpinski triangle/Graphical (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, recursion, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sierpinski_triangle/Graphical
---

## Summary
The task asks the programmer to produce a graphical (pixel/vector) rendering of a Sierpinski triangle of order N, in any orientation. The Sierpinski triangle is a self-similar fractal formed by recursively subdividing a triangle into four smaller triangles and removing the central one. The key insight is that the figure can be generated several equivalent ways: by explicit recursive subdivision, by the chaos-game random-point method, or by exploiting the bitwise/Pascal-triangle structure of the pattern.

## Task Requirements
- Generate a Sierpinski triangle of a given order N.
- Render it graphically (as an image or drawn output), not as ASCII art.
- Any orientation of the triangle is acceptable.

## Language Coverage
63 languages implement this task, spanning compiled, scripting, functional, and assembly families as well as dedicated graphics/plotting tools. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Racket, Processing, and gnuplot.

## Connections
- [[SierpinskiTriangle]] — the fractal being rendered
- [[Fractal]] — the broader class of self-similar geometric figures
- [[Recursion]] — the natural subdivision strategy for generating it
- [[ChaosGame]] — an alternative iterated-function-system method for plotting it
- [[ComputerGraphics]] — the rendering domain the task targets

## Contradictions
- None — reference task page.
