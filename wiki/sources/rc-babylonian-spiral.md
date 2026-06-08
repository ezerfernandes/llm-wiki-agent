---
title: "Babylonian spiral (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Babylonian_spiral
---

## Summary
The Babylonian spiral is a sequence of points on strictly integer coordinates, where each successive vector minimally increases in length and minimally bends clockwise from the previous vector, with length taking priority over angle. The key insight is that the allowed squared vector lengths are exactly the sorted set of sums of two integer squares (including zero), so each step picks the next-larger such length and, among ties, the candidate that turns clockwise by the smallest positive angle.

## Task Requirements
- Start with P(1) = (0,0) and P(2) = (0,1), giving an initial vertical vector of length 1.
- For each new point, choose the shortest vector strictly longer than the previous vector, whose squared length is a sum of two integer squares.
- Among candidates of that length, pick the one that bends clockwise by more than zero radians but by the least amount.
- Find and display the first 40 (x, y) coordinates of the spiral.
- Stretch task: compute and plot the first 10000 points, matching the OEIS reference graph.

## Language Coverage
20 languages implement this task, spanning systems and scripting languages alongside math-oriented and BASIC dialects. Representative implementations include C++, Java, JavaScript, Python, Julia, Perl, Raku, Nim, Zig, and J.

## Connections
- [[NumberTheory]] — vector lengths are sums of two integer squares
- [[SumOfTwoSquares]] — the squared-length sequence drives candidate selection
- [[ComputationalGeometry]] — clockwise bending and vector angles on a lattice
- [[Atan2]] — typically used to compare turn angles between vectors
- [[IntegerLattice]] — all points lie on strictly integral coordinates

## Contradictions
- None — reference task page.
