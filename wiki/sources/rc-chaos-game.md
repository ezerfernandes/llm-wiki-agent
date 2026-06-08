---
title: "Chaos game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Chaos_game
---

## Summary
The chaos game is a method for generating the attractor of an iterated function system (IFS). The task asks the programmer to plot a fractal by repeatedly jumping halfway from a current point toward a randomly chosen vertex of an equilateral triangle. The key insight is that despite the randomness of each step, the cumulative set of plotted points converges to a deterministic, self-similar Sierpinski Triangle.

## Task Requirements
- Use the three corners of an equilateral triangle as fixed reference points.
- Choose a random starting point, preferably inside the triangle.
- Repeatedly pick a reference point at random and place the next point halfway between the current point and that reference point.
- Plot the points; after sufficient iterations the image of a Sierpinski Triangle should emerge.

## Language Coverage
61 languages implement this task, showing broad coverage across general-purpose, functional, and graphics-oriented environments. Representative implementations include C, C++, Java, Python, JavaScript, Haskell, Rust, Go, Lua, Processing, and Mathematica/Wolfram Language.

## Connections
- [[IteratedFunctionSystem]] — the chaos game is a stochastic algorithm for rendering an IFS attractor.
- [[SierpinskiTriangle]] — the fractal that emerges as the limiting image.
- [[Fractal]] — the self-similar geometric structure produced.
- [[RandomNumberGeneration]] — random vertex selection drives each iteration.
- [[Attractor]] — the point set the iteration converges toward.

## Contradictions
- None — reference task page.
