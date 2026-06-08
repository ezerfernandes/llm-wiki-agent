---
title: "Constrained random points on a circle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability-statistics, random-sampling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Constrained_random_points_on_a_circle
---

## Summary
The task asks the programmer to generate 100 integer coordinate pairs <x,y> drawn uniformly at random subject to the constraint that the radius sqrt(x^2 + y^2) falls between 10 and 15 inclusive, then plot them to produce a "fuzzy" annulus (ring). Because duplicate pairs may be generated, the actual number of distinct plotted points can be fewer than 100. The key insight is that only 404 lattice points satisfy the constraint, so one can either reject-sample random pairs or precompute that finite set and draw from it directly.

## Task Requirements
- Generate 100 <x,y> pairs where x and y are integers sampled uniformly.
- Enforce the condition 10 <= sqrt(x^2 + y^2) <= 15.
- Display or plot the resulting points (expected to look like a fuzzy circle/ring).
- Accept that fewer than 100 distinct points may appear due to repeated pairs.
- Two suggested algorithms: (1) generate random integer pairs and filter by the constraint, or (2) precompute the 404 valid points and select randomly from that set.

## Language Coverage
78 languages implement this task, spanning systems languages, scripting languages, functional languages, and dedicated plotting/math tools. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, R, Mathematica / Wolfram Language, and gnuplot.

## Connections
- [[UniformDistribution]] — points are drawn from a uniform random distribution
- [[RejectionSampling]] — algorithm 1 filters random pairs that fail the radius constraint
- [[LatticePoints]] — the valid coordinates form a finite set of 404 integer grid points
- [[Annulus]] — the constraint defines a ring-shaped region between two radii
- [[RandomNumberGeneration]] — relies on a pseudorandom source for sampling

## Contradictions
- None — reference task page.
