---
title: "Sierpinski pentagon (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractal, recursion, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sierpinski_pentagon
---

## Summary
The task asks the programmer to render a Sierpinski pentagon (also called a pentaflake) of order 5, while also handling lower orders 1 through 4. A pentaflake is a self-similar fractal built by recursively replacing each pentagon with five (or six) smaller scaled-down pentagons, so the natural implementation is a recursive subdivision that scales positions by the golden-ratio-related factor between levels.

## Task Requirements
- Produce a graphical or ASCII-art representation of a Sierpinski pentagon (pentaflake).
- Render order 5 as the primary target.
- Also correctly generate the lower orders 1 through 4.

## Language Coverage
36 languages implement this task, spanning systems, scripting, functional, and graphics-oriented ecosystems. Representative implementations include C, C++, D, Rust, Go, Java, JavaScript, Python, Haskell, Racket, Julia, and Processing.

## Connections
- [[Fractal]] — the pentaflake is a self-similar fractal figure.
- [[SierpinskiTriangle]] — sibling construction applying the same recursive removal/replacement idea to a different polygon.
- [[Recursion]] — each order is built by recursively subdividing pentagons.
- [[GoldenRatio]] — the scaling factor between successive pentagon levels derives from the golden ratio.
- [[TurtleGraphics]] — a common approach for emitting the pentagon outlines.

## Contradictions
- None — reference task page.
