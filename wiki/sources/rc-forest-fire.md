---
title: "Forest fire (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Forest_fire
---

## Summary
The task is to implement the Drossel and Schwabl forest-fire model, a 2D cellular automaton in which each cell is empty, a tree, or burning. The grid evolves in discrete steps under four simple probabilistic rules, producing emergent self-organized criticality from purely local interactions. The key insight is that complex large-scale fire dynamics arise from trivial per-cell update rules combined with two tunable probabilities.

## Task Requirements
- Each cell holds one of three states: empty, tree, or burning.
- Apply the update rules synchronously: a burning cell becomes empty; a tree burns if any neighbor is burning; a tree ignites spontaneously with probability *f*; an empty cell grows a tree with probability *p*.
- Use the Moore neighborhood (8 surrounding cells) with fixed boundary conditions (boundary cells treated as always empty).
- Initialize the lattice randomly with empty and tree cells (e.g. probability 0.5 of being a tree), then let the system evolve.
- No graphical display or parameter-tuning interface is required.

## Language Coverage
63 languages implement this task, spanning systems and assembly languages, functional languages, and scripting languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Ruby, Common Lisp, and 6502 Assembly.

## Connections
- [[CellularAutomaton]] — the model is a 2D cellular automaton
- [[MooreNeighborhood]] — defines each cell's eight neighbors
- [[SelfOrganizedCriticality]] — emergent behavior the model exhibits
- [[ConwaysGameOfLife]] — related grid-based cellular automaton task
- [[Wireworld]] — related cellular automaton task

## Contradictions
- None — reference task page.
