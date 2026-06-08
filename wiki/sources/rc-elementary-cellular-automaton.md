---
title: "Elementary cellular automaton (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation, bit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Elementary_cellular_automaton
---

## Summary
The task asks the programmer to implement and visualize an elementary cellular automaton: a one-dimensional grid of binary cells whose next-generation state depends only on each cell and its two immediate neighbors. The key insight is that each of the 256 possible rules is itself encoded as an 8-bit number, where each bit gives the output for one of the eight possible 3-cell neighborhood patterns (111 down to 000). The space must wrap toroidally, so the leftmost cell is the right neighbor of the rightmost and vice versa.

## Task Requirements
- Create a subroutine, program, or function to evolve any of the 256 possible elementary cellular automata.
- Support arbitrary space length and any given initial state.
- Treat the cell space as wrapping (toroidal): leftmost cell neighbors the rightmost.
- Visualize the evolution across generations, demonstrating with any chosen rule.

## Language Coverage
55 languages implement this task, spanning systems, scripting, and functional paradigms broadly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Ruby, and Mathematica/Wolfram Language.

## Connections
- [[CellularAutomata]] — the broader class of discrete spatial simulation systems this task instantiates
- [[WolframRuleNumbering]] — the 8-bit rule encoding scheme that names all 256 automata
- [[BitManipulation]] — extracting the relevant rule bit from the 3-cell neighborhood index
- [[ToroidalBoundary]] — the wrap-around neighbor logic the task mandates
- [[Rule110]] — a notable elementary automaton proven Turing complete

## Contradictions
- None — reference task page.
