---
title: "Julia set (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, complex-numbers, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Julia_set
---

## Summary
The task is to generate and draw a Julia set, a fractal defined by iterating the complex map z → z² + c for a fixed complex constant c. Each pixel is mapped to a point in the complex plane, and the iteration is run until the magnitude escapes a bound or a maximum iteration count is reached; the escape time is then mapped to a color. The key insight is that, unlike the Mandelbrot set (which varies c per point), the Julia set holds c constant and varies the starting point z₀.

## Task Requirements
- Generate a Julia set for a chosen complex constant c.
- Map screen pixels to coordinates in the complex plane.
- Iterate z = z² + c per point, tracking escape time against an iteration limit and an escape radius.
- Draw / render the result as an image, coloring points by escape behavior.

## Language Coverage
51 languages implement this task, spanning systems, scripting, functional, and even database languages — reflecting how widely the escape-time fractal serves as a graphics benchmark. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, JavaScript, Julia, Lua, and even Transact-SQL.

## Connections
- [[ComplexNumbers]] — iteration occurs in the complex plane
- [[Fractals]] — the Julia set is a canonical fractal
- [[MandelbrotSet]] — closely related escape-time fractal sharing the z²+c map
- [[EscapeTimeAlgorithm]] — the rendering technique used
- [[Iteration]] — the core dynamical-systems mechanism

## Contradictions
- None — reference task page.
