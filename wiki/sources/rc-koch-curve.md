---
title: "Koch curve (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractal, recursion, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Koch_curve
---

## Summary
This task asks the programmer to draw a Koch curve, a classic self-similar fractal. The construction starts with a straight line segment and repeatedly replaces the middle third of every segment with two sides of an outward-pointing equilateral triangle. The key insight is that the curve is naturally expressed by recursion (or by an L-system / turtle-graphics rewrite rule), where each level of recursion quadruples the number of segments.

## Task Requirements
- Render a Koch curve as graphical or textual/turtle output.
- Apply the subdivision rule: split each segment into thirds and bump the middle third outward at 60 degrees to form a triangular spike.
- Recurse to a chosen depth (order) of the fractal.

## Language Coverage
47 languages implement this task, spanning compiled, scripting, functional, and BASIC-family ecosystems. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Logo, and Processing.

## Connections
- [[Fractal]] — the Koch curve is a canonical self-similar fractal of dimension log4/log3.
- [[Recursion]] — the standard generation strategy subdivides each segment recursively.
- [[LSystem]] — the curve can be defined by the rewrite rule F → F+F--F+F.
- [[TurtleGraphics]] — many implementations draw it via forward/turn turtle commands.
- [[KochSnowflake]] — three Koch curves joined into a triangle form the snowflake.

## Contradictions
- None — reference task page.
