---
title: "Percolation/Site percolation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, simulation, graph-traversal, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Percolation/Site_percolation
---

## Summary
This task simulates site percolation on an M×N grid where each cell is independently filled with probability p. The goal is to test whether a connected path of adjacent filled cells reaches from the top row to the bottom row, then repeat the trial many times to estimate the percolation probability as a function of p. The key insight is the emergence of a sharp percolation threshold: as p increases from 0.0 to 1.0, the fraction of grids that percolate rises steeply around a critical density.

## Task Requirements
- Build an M×N grid filling each cell independently with constant probability p (0.0 ≤ p ≤ 1.0).
- Test for a route of adjacent filled cells from any cell in row 0 to any cell in the bottom row (site percolation).
- For each p, repeat the simulation t ≥ 100 times to estimate the fraction of grids that percolate.
- Show how percolation probability varies with p stepping from 0.0 to 1.0 in 0.1 increments.
- Use a fixed M=15, N=15 grid for all cases.
- Optionally depict a percolating grid graphically; show all output on the page.

## Language Coverage
25 languages implement this task, spanning systems, functional, and scripting families. Representative implementations include C, C++, D, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[Percolation]] — the physical/statistical phenomenon being modeled
- [[MonteCarloSimulation]] — repeated random trials estimate the percolation fraction
- [[FloodFill]] — common technique for detecting a connected top-to-bottom path
- [[GraphConnectivity]] — percolation reduces to connectivity between top and bottom rows
- [[PercolationThreshold]] — the critical p at which large-scale connectivity emerges

## Contradictions
- None — reference task page.
