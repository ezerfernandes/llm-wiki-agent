---
title: "Elementary cellular automaton/Infinite length (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Elementary_cellular_automaton/Infinite_length
---

## Summary
This task extends an elementary cellular automaton so the row of cells is conceptually infinite, limited only by available memory. The key insight is that any state can be represented by a finite window of "interesting" cells, with every cell beyond that window defined as the negation of the nearest in-window cell. This lets the automaton grow its support outward each generation without ever truly storing infinite data.

## Task Requirements
- Implement an elementary cellular automaton whose cell count is bounded only by memory, not a fixed width.
- Model the state as an infinite tape with bounded support: a finite list of adjacent cells, plus the convention that all cells outside that list equal the negation of the closest in-list cell.
- Reproduce the given encoding examples (e.g. `1` -> `...,0,0,1,0,0,...`; `0,1` -> `...,1,1,0,1,0,0,...`; `1,0,1` -> `...,0,0,1,0,1,0,0,...`).
- Stick to this simple negation-based encoding rather than more elaborate schemes.

## Language Coverage
25 languages implement this task. Coverage spans systems and functional languages alongside scripting and array-oriented ones, including C++, D, Go, Haskell, Java, Julia, Python, Perl, Raku, Ruby, J, and Wolfram Language.

## Connections
- [[CellularAutomaton]] — the underlying simulation model being extended
- [[ElementaryCellularAutomaton]] — the 1D, two-state, nearest-neighbor base rule set
- [[BoundedSupport]] — finite representation enabling an unbounded tape
- [[Simulation]] — discrete time-step state evolution

## Contradictions
- None — reference task page.
