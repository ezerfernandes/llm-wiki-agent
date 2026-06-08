---
title: "Yin and yang (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Yin_and_yang
---

## Summary
This Rosetta Code task asks the programmer to draw the taijitu, the familiar yin-and-yang symbol from the philosophy of duality. The core challenge is constructing the figure parametrically: an outer circle split by two opposing semicircular arcs into the interlocking light and dark halves, each containing a small contrasting "eye" dot. The key insight is that the entire glyph must scale cleanly from a single size parameter, so all radii and offsets are expressed as fractions of that input.

## Task Requirements
- Create a function that, given a parameter representing size, generates a taijitu symbol scaled to the requested size.
- Generate and display the symbol for two different (small) sizes.

## Language Coverage
79 languages implement this task, reflecting broad coverage across both raster/vector graphics libraries and text/ASCII rendering approaches. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Go, Rust, Ruby, PostScript, and SVG.

## Connections
- [[ComputerGraphics]] — the task is fundamentally a drawing/rendering exercise.
- [[Circle]] — the symbol is built from full and half circles and dots.
- [[VectorGraphics]] — many solutions emit SVG or PostScript scalable output.
- [[ParametricScaling]] — all geometry is derived from a single size parameter.
- [[Symmetry]] — the taijitu exhibits 180-degree rotational symmetry between its halves.

## Contradictions
- None — reference task page.
