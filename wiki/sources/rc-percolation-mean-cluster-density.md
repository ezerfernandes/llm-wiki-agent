---
title: "Percolation/Mean cluster density (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, monte-carlo, percolation, graph-algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Percolation/Mean_cluster_density
---

## Summary
The task asks the programmer to estimate the mean cluster density K(p) of a randomly filled n×n boolean grid, where each cell is 1 with probability p. Clusters are connected groups of 1-cells joined vertically or horizontally (Von Neumann neighborhood), and K(p) is approximated by counting clusters C_n and dividing by n². The key insight is that percolation theory predicts K(p) converges to a fixed value (≈0.065770 for p=0.5) as n grows, so larger grids and averaging over several Monte Carlo runs yield more accurate estimates.

## Task Requirements
- Build an n×n matrix where each cell is 1 with probability p (else 0).
- Count the number of clusters C_n, where a cluster is a maximal group of 1-cells connected horizontally or vertically.
- Compute K(p) = C_n / n².
- For p = 0.5, show how varying n (up to at least 1000) affects the accuracy of the simulated K(p), comparing against the reference value ≈0.065770.
- Average each estimate over t ≥ 5 runs to reduce randomness.
- Extra credit: graphically display the clusters in a 15×15, p=0.5 grid.

## Language Coverage
25 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include C, C++, D, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[MonteCarloMethod]] — accuracy improves by averaging many random trials
- [[PercolationTheory]] — the statistical-physics model the task simulates
- [[ConnectedComponents]] — cluster counting is connected-component labeling on a grid
- [[FloodFill]] — a common technique for identifying each cluster
- [[VonNeumannNeighborhood]] — defines which cells are adjacent

## Contradictions
- None — reference task page.
