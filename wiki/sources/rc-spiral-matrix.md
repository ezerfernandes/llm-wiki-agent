---
title: "Spiral matrix (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, matrix, array-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Spiral_matrix
---

## Summary
The task is to build a square spiral array: an N×N grid filled with the first N² natural numbers (starting at 0), placed so the values increase sequentially while walking around the edges and spiraling inward toward the center. The key insight is to simulate movement in four directions (right, down, left, up), turning whenever the next cell is out of bounds or already filled.

## Task Requirements
- Produce an N×N square matrix.
- Fill it with the integers 0 through N²−1 in order.
- Place numbers along a path that traces the outer edge and spirals inward.
- For N=5 the result matches the given reference layout (0..4 across the top row, continuing clockwise inward).

## Language Coverage
94 languages implement this task, reflecting broad coverage from systems and functional languages to BASIC dialects and array-oriented languages. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, J, and Common Lisp.

## Connections
- [[Matrix]] — the task constructs and fills a square matrix.
- [[ArrayTraversal]] — the core challenge is traversing the grid in a spiral order.
- [[ZigZagMatrix]] — a related Rosetta Code task with a different fill pattern.
- [[UlamSpiral]] — another spiral-arrangement task, used for visualizing primes.
- [[Simulation]] — directional movement with boundary/visited checks drives the fill.

## Contradictions
- None — reference task page.
