---
title: "Zig-zag matrix (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, matrices, array-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zig-zag_matrix
---

## Summary
The task asks the programmer to build an N×N "zig-zag" array filled with the first N² natural numbers (0 through N²−1), where values increase sequentially as you sweep back and forth along the matrix's anti-diagonals. The key insight is that all cells on a given anti-diagonal share the same index sum (row + col), and the sweep direction alternates between diagonals, which is the same ordering JPEG uses to serialize DCT coefficients for image compression.

## Task Requirements
- Produce a square N×N array containing the integers 0 .. N²−1.
- Fill it so the numbers increase along the anti-diagonals in zig-zag (alternating) traversal order.
- For N=5, reproduce the canonical example array (0,1,5,6,14 across the top row, etc.).

## Language Coverage
122 languages implement this task, giving very broad coverage across imperative, functional, array, and esoteric paradigms. Representative implementations include C, C++, Python, Java, Haskell, J, APL, Rust, Go, Common Lisp, and Forth.

## Connections
- [[Matrix]] — the core data structure being constructed and traversed.
- [[AntiDiagonalTraversal]] — the ordering principle driving the fill.
- [[JPEG]] — uses this exact zig-zag scan to encode image coefficient blocks.
- [[SpiralMatrix]] — closely related matrix-filling traversal task.

## Contradictions
- None — reference task page.
