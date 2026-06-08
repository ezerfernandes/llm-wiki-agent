---
title: "One-dimensional cellular automata (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/One-dimensional_cellular_automata
---

## Summary
The task asks the programmer to simulate a one-dimensional cellular automaton over an array of live (1) and dead (0) cells. Each cell's next-generation value is determined by its own state plus its immediate left and right neighbours, using a fixed transition table that mimics simple survival/birth/overcrowding rules. The key insight is that this particular rule set behaves like a "survival" automaton: a cell lives only when it has exactly one live neighbour, and dies from isolation or overcrowding.

## Task Requirements
- Maintain an array of cells, each either live (1) or dead (0), starting from a given initial distribution.
- Treat cells off the ends of the array as having fixed (boundary) values.
- Compute each next-generation cell from the triple of (left neighbour, self, right neighbour) using the specified 8-row truth table.
- Apply the rules so that a cell survives with exactly one live neighbour, is born from two live neighbours when itself dead, and dies otherwise (isolation or starvation/overcrowding).

## Language Coverage
105 languages implement this task, giving very broad coverage across paradigms from systems and scripting to array and functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, J, Common Lisp, Tcl, and Wolfram Language.

## Connections
- [[CellularAutomaton]] — this task is a concrete instance of a discrete cellular automaton.
- [[ElementaryCellularAutomaton]] — closely related Rosetta task; this rule is a specific case of nearest-neighbour binary CA.
- [[ConwaysGameOfLife]] — the survival/birth/overcrowding rules echo Life's logic in one dimension.
- [[BitwiseOperations]] — common implementation technique encodes neighbourhoods as 3-bit indices into a rule table.

## Contradictions
- None — reference task page.
