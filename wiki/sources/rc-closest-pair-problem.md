---
title: "Closest-pair problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, divide-and-conquer]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Closest-pair_problem
---

## Summary
The task asks for a function that, given a set of points in the 2D plane, finds the two points separated by the smallest Euclidean distance. The naive approach compares every pair in O(n²) time, but the key insight is a divide-and-conquer strategy that achieves O(n log n): split the points by a vertical median line, solve each half recursively, then only check points within a narrow vertical strip around the boundary where a closer cross-pair could exist.

## Task Requirements
- Provide a function that returns the closest pair (and ideally their distance) among N planar points.
- Implement at minimum the brute-force O(n²) algorithm; for N < 2 the distance is infinity.
- The recommended better solution is the recursive divide-and-conquer algorithm running in O(n log n), working over points pre-sorted by x and by y coordinate.
- In the divide step, only points whose x-distance to the median is less than the current minimum need cross-strip comparison, and within the strip only a bounded number of y-neighbors per point.

## Language Coverage
74 languages implement this task, spanning systems languages, functional languages, scripting languages, and many BASIC dialects. Representative examples include C, C++, C#, Java, Python, Haskell, OCaml, Go, Rust, Common Lisp, and Prolog.

## Connections
- [[ComputationalGeometry]] — the problem is a foundational planar geometry algorithm.
- [[DivideAndConquer]] — the optimal O(n log n) solution recursively splits the point set.
- [[EuclideanDistance]] — the metric minimized between the chosen pair of points.
- [[AlgorithmicComplexity]] — contrasts the O(n²) brute force with the O(n log n) recursive approach.

## Contradictions
- None — reference task page.
