---
title: "Sierpinski arrowhead curve (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, recursion, l-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sierpinski_arrowhead_curve
---

## Summary
The task asks the programmer to produce a graphical or ASCII-art rendering of a Sierpinski arrowhead curve of at least order 3. The arrowhead curve is a space-filling fractal that, in the limit, traces out the same shape as the Sierpinski triangle while remaining a single continuous, non-self-intersecting line. The key insight is that the curve is naturally expressed as a recursive (or L-system) construction of turtle-graphics moves and 60-degree turns.

## Task Requirements
- Generate a representation of a Sierpinski arrowhead curve.
- Output may be graphical or ASCII-art.
- The curve must be at least order (recursion depth) 3.

## Language Coverage
38 languages implement this task, giving broad coverage across compiled, scripting, BASIC-family, and functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, Ruby, and Wren.

## Connections
- [[Fractal]] — the arrowhead curve is a self-similar fractal figure.
- [[SierpinskiTriangle]] — the curve fills the same region as this fractal in the limit.
- [[LSystem]] — a common way to specify the curve via rewriting rules.
- [[TurtleGraphics]] — typical drawing model using forward moves and fixed-angle turns.
- [[Recursion]] — the order-n curve is defined recursively from lower orders.

## Contradictions
- None — reference task page.
