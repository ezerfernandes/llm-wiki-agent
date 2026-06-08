---
title: "Wireworld (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wireworld
---

## Summary
The task is to implement Wireworld, a four-state cellular automaton designed for simulating digital logic. Each cell is empty, an electron head, an electron tail, or a conductor, and all cells transition simultaneously each generation according to fixed rules. The defining insight is that a conductor turns into an electron head only when 1 or 2 of its 8 Moore neighbors are electron heads, which lets electrons propagate one-way along wires and makes the system Turing complete.

## Task Requirements
- Read a Wireworld pattern from a file (e.g. "H" = electron head, "t" = tail, "." = conductor, space = empty).
- Apply the four transition rules synchronously: empty stays empty; head becomes tail; tail becomes conductor; conductor becomes a head if 1 or 2 Moore neighbors are heads, otherwise stays conductor.
- Display an animation of the simulation advancing generation by generation.
- Text output is acceptable, though pixel-based rendering is suggested for large designs.

## Language Coverage
62 languages implement this task, reflecting broad coverage across systems, scripting, and functional families. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Common Lisp, and REXX.

## Connections
- [[CellularAutomaton]] — Wireworld is a specific 4-state cellular automaton.
- [[ConwaysGameOfLife]] — the canonical related automaton it is compared against.
- [[MooreNeighborhood]] — the 8-cell neighborhood used in the transition rule.
- [[TuringCompleteness]] — Wireworld can compute anything a Turing machine can.
- [[DigitalLogicSimulation]] — its electrons model wires, gates, and circuits.

## Contradictions
- None — reference task page.
