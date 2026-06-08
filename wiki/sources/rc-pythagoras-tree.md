---
title: "Pythagoras tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, graphics, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pythagoras_tree
---

## Summary
The Pythagoras tree is a plane fractal built from squares, where each square spawns two smaller squares tilted so that the three touching squares enclose a right triangle (echoing the Pythagorean theorem). The task is to draw such a tree to order 7. The key constraint is that the construction must be done using only vector arithmetic — no rotation matrices or trigonometric functions — so each child square is derived by adding/subtracting and scaling the parent's edge vectors.

## Task Requirements
- Construct a Pythagoras tree of order 7.
- Use only vectors to position and size the squares.
- Do not use rotation operations or trigonometric functions.

## Language Coverage
48 languages implement this task, showing broad adoption across general-purpose, graphics-capable, and BASIC-family languages. Representative implementations include C, C++, Java, JavaScript, Python, Haskell, Go, Rust, Julia, Processing, and Racket.

## Connections
- [[Fractal]] — the tree is a self-similar fractal figure
- [[Recursion]] — natural recursive subdivision down to a given order
- [[PythagoreanTheorem]] — each triple of squares frames a right triangle
- [[VectorArithmetic]] — squares are placed via vector addition/scaling, no trig
- [[ComputerGraphics]] — task output is a rendered 2D image

## Contradictions
- None — reference task page.
