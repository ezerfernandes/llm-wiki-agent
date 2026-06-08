---
title: "Archimedean spiral (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Archimedean_spiral
---

## Summary
The task is to draw an Archimedean spiral, the curve named after the Greek mathematician Archimedes. It is defined in polar coordinates by the equation r = a + b·θ, where a and b are real constants. The key property is that successive turns of the spiral are separated by a constant distance (controlled by b), distinguishing it from logarithmic spirals where spacing grows geometrically.

## Task Requirements
- Draw an Archimedean spiral.
- The spiral is described by the polar equation r = a + b·θ for real numbers a and b.
- Typically rendered by sweeping θ and converting polar coordinates to Cartesian (x = r·cos θ, y = r·sin θ) for plotting.

## Language Coverage
70 languages implement this task, reflecting broad coverage across general-purpose, scientific, and graphics-oriented languages. Representative implementations include C, C++, Java, Python, Rust, Go, Haskell, JavaScript, MATLAB, and Mathematica/Wolfram Language.

## Connections
- [[PolarCoordinates]] — the spiral is most naturally expressed in polar form r = a + b·θ.
- [[ParametricEquations]] — drawing requires converting polar to Cartesian via x = r·cos θ, y = r·sin θ.
- [[ComputerGraphics]] — the task is fundamentally a 2D plotting/rendering exercise.
- [[Spiral]] — the Archimedean spiral is one family within the broader class of spiral curves.

## Contradictions
- None — reference task page.
