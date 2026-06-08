---
title: "Sierpinski triangle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sierpinski_triangle
---

## Summary
The task asks the programmer to produce an ASCII-art representation of a Sierpinski triangle of order N, a self-similar fractal built from a triangle whose central sub-triangle is recursively removed. The key insight is that the pattern can be generated without explicit recursion: row i of an order-N triangle prints an asterisk at column j exactly when the bitwise AND of i and j is zero, which is also the rule that produces Pascal's triangle modulo 2.

## Task Requirements
- Output an ASCII Sierpinski triangle for a given order N.
- For order 4, the triangle must span 16 rows, each progressively wider, with asterisks separated by spaces matching the example layout.

## Language Coverage
129 languages implement this task, spanning low-level assembly, classic structured languages, functional languages, and esoteric languages. Representative solutions include C, C++, Python, Haskell, Java, Rust, Lisp, Forth, and esoteric entries such as Befunge and Unlambda.

## Connections
- [[Fractals]] — the Sierpinski triangle is a canonical self-similar fractal
- [[Recursion]] — the classic generation strategy subdivides triangles recursively
- [[PascalsTriangle]] — odd entries of Pascal's triangle mod 2 trace the same pattern
- [[BitwiseOperations]] — the `(i & j) == 0` test produces each row directly
- [[CellularAutomata]] — Rule 90 generates the same fractal from a single seed cell

## Contradictions
- None — reference task page.
