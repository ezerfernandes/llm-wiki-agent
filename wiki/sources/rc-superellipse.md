---
title: "Superellipse (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometry, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Superellipse
---

## Summary
The task is to draw a superellipse, a geometric curve defined as the set of all points (x, y) satisfying |x/a|^n + |y/b|^n = 1, where n, a, and b are positive numbers. The exponent n controls the shape: values below 2 produce pinched astroid-like figures, n = 2 gives an ordinary ellipse, and values above 2 produce rounded-rectangle "squircle" shapes. The specific instance to render uses n = 2.5 with a = b = 200.

## Task Requirements
- Draw a superellipse with the parameters n = 2.5 and a = b = 200.
- The figure follows the implicit equation |x/a|^n + |y/b|^n = 1.

## Language Coverage
43 languages implement this task, showing broad coverage across general-purpose, graphics-capable, and math-oriented languages. Representative implementations include C, Java, JavaScript, Python, Haskell, Go, Julia, Racket, Mathematica/Wolfram Language, and Processing.

## Connections
- [[ParametricEquations]] — superellipses are typically plotted via a parametric form using powers of sine and cosine.
- [[ComputerGraphics]] — the task centers on rendering a curve to a canvas or image.
- [[Lame Curve]] — the superellipse is the special case of the Lamé curve with equal positive exponents.
- [[Squircle]] — the rounded shape produced when the exponent n exceeds 2.

## Contradictions
- None — reference task page.
