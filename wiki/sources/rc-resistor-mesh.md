---
title: "Resistor mesh (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, linear-algebra]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Resistor_mesh
---

## Summary
The task asks the programmer to compute the equivalent electrical resistance between two designated nodes (A and B) of a 10×10 grid of nodes interconnected by 1-ohm resistors along each grid edge. The key insight is that the mesh forms a linear system: applying Kirchhoff's current law at each node (with a unit current injected at A and drawn at B) yields a sparse system of linear equations whose solution gives the node potentials, from which the resistance V/I follows.

## Task Requirements
- Model a 10×10 grid of nodes, each interconnected to its orthogonal neighbors by 1Ω resistors.
- Find the effective resistance between two specified points A and B.
- (Optional extra credit) Solve the related xkcd "nerd sniping" infinite-grid problem.

## Language Coverage
40 languages implement this task, spanning systems and numeric-computing languages well-suited to solving linear systems. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Fortran, Octave, and Mathematica/Wolfram Language.

## Connections
- [[KirchhoffsLaws]] — node equations come from current conservation at each grid node
- [[LinearSystem]] — the mesh reduces to solving a system of linear equations
- [[GaussianElimination]] — a common direct method for solving the resulting matrix
- [[EffectiveResistance]] — the quantity being computed across the network
- [[SparseMatrix]] — the grid adjacency yields a sparse coefficient matrix

## Contradictions
- None — reference task page.
