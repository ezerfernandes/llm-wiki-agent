---
title: "Perlin noise (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, procedural-generation, gradient-noise]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Perlin_noise
---

## Summary
Perlin noise is a gradient noise invented by Ken Perlin, widely used in computer graphics to procedurally generate textures and heightmaps. It is a pseudo-random mapping from d-dimensional space into the reals (typically d = 2, 3, or 4). The task asks the programmer to implement (or use a library for) the classic 2002 Java reference algorithm and verify that the noise value at the 3D point (3.14, 42, 7) equals 0.13691995878400012.

## Task Requirements
- Implement the Perlin noise algorithm as defined in Ken Perlin's 2002 Java reference implementation, or use a dedicated library.
- Evaluate the noise function at the 3D point with coordinates (3.14, 42, 7).
- Show that the result equals 0.13691995878400012 (assuming 64-bit IEEE-754 floating point).
- If the language uses a different floating point representation, note it and report the value accurate to 15 decimal places (or the language's accuracy threshold); trailing zeros need not be displayed.

## Language Coverage
44 languages implement this task, spanning systems, scripting, functional, and graphics-shader languages. Representative examples include C, C++, Rust, Go, Java, JavaScript, Python, Julia, GLSL, and Common Lisp.

## Connections
- [[GradientNoise]] — Perlin noise is a specific kind of gradient noise
- [[ProceduralGeneration]] — primary application for textures and heightmaps
- [[Interpolation]] — uses a smoothstep fade curve and trilinear interpolation between gradients
- [[PseudorandomNumberGeneration]] — relies on a fixed permutation table for deterministic randomness
- [[ComputerGraphics]] — the dominant domain where the technique is used

## Contradictions
- None — reference task page.
