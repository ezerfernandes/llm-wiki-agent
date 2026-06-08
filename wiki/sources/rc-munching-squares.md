---
title: "Munching squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, bitwise]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Munching_squares
---

## Summary
This task asks the programmer to render a raster image in which each pixel at coordinates (x, y) is colored according to the value of the bitwise expression `x XOR y`, mapped through an arbitrary color table. The result is the classic "munching squares" pattern, an early computer-graphics demo whose self-similar, fractal-like structure emerges purely from the XOR operation rather than from any explicit geometric drawing.

## Task Requirements
- For every pixel, compute the value `x xor y` (bitwise exclusive-or of its coordinates).
- Use that value as an index into an arbitrary color table to pick the pixel's color.
- Render the resulting pattern as graphical raster output.

## Language Coverage
61 languages implement this task, reflecting broad participation across both graphics-capable and text/ASCII-based environments. Representative implementations include C, C++, C#, Java, Python, Haskell, Rust, Go, Lua, Processing, GLSL, and Mathematica.

## Connections
- [[BitwiseOperations]] — the pattern is generated directly by the XOR operator on coordinates
- [[ExclusiveOr]] — the core function `x xor y` driving every pixel's color
- [[RasterGraphics]] — output is a pixel grid colored per a color table
- [[ColorTable]] — indexed palette mapping XOR values to colors

## Contradictions
- None — reference task page.
