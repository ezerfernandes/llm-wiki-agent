---
title: "Kirkpatrick–Seidel algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, divide-and-conquer]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kirkpatrick–Seidel_algorithm
---

## Summary
The task asks the programmer to implement the Kirkpatrick–Seidel algorithm, an output-sensitive method for computing the convex hull of a set of planar points. Often called the "ultimate convex hull algorithm," it achieves an optimal time complexity of O(n log h), where n is the number of input points and h is the number of points actually on the hull. The key insight is its divide-and-conquer "bridge"-finding strategy, which lets it ignore interior points and run faster than O(n log n) algorithms like Graham scan or Jarvis march when h is small relative to n.

## Task Requirements
- Compute the convex hull of a set of points in the plane using the Kirkpatrick–Seidel approach.
- Split the points with a vertical line at the median x-coordinate into roughly equal left and right subsets.
- Find the "bridge": a segment joining one point from each subset that lies above all other points.
- Recurse on the subsets to find further bridges, building the upper and lower hulls separately.
- Merge the upper and lower hulls into the complete convex hull.

## Language Coverage
20 languages implement this task, spanning systems, functional, scripting, and statistical languages. Representative examples include C++, C#, Java, Go, Rust, Python, JavaScript, Julia, R, and Raku.

## Connections
- [[ConvexHull]] — the geometric structure the algorithm computes
- [[ComputationalGeometry]] — the field this algorithm belongs to
- [[DivideAndConquer]] — the algorithmic paradigm it relies on
- [[OutputSensitiveAlgorithm]] — its O(n log h) complexity depends on the output size h
- [[MedianSelection]] — finding the median x-coordinate to split the point set

## Contradictions
- None — reference task page.
