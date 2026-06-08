---
title: "Elementary cellular automaton/Random number generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, random-number-generation, bitwise]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Elementary_cellular_automaton/Random_number_generator
---

## Summary
This task demonstrates Stephen Wolfram's method of generating pseudo-random numbers from Rule 30, an elementary cellular automaton chaotic enough that Mathematica long used it as its default RNG. The key insight is that successive bits read from a single fixed cell position, as the automaton evolves, form a high-quality random bit stream. The task builds on the parent Elementary Cellular Automaton task rather than re-implementing the automaton itself.

## Task Requirements
- Use a Rule 30 elementary cellular automaton (code from the parent task may be reused).
- Initialize the cell array to all zeros except a single cell set to one.
- Track the evolving state of that one particular cell across successive generations.
- Group the extracted bits into packets of eight, building bytes with the first bit as the most significant bit.
- Output the first ten bytes produced this way.
- The chosen initial array length must be visible in the code so output is reproducible across languages.
- Extra credit: optimize for speed, e.g. via extensive bitwise logic.

## Language Coverage
33 languages implement this task, spanning systems languages, functional languages, and array/math-oriented languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, F#, Python, Julia, Mathematica/Wolfram Language, and J.

## Connections
- [[CellularAutomaton]] — the underlying computational model
- [[Rule30]] — the specific chaotic rule used as the entropy source
- [[PseudoRandomNumberGeneration]] — the practical goal of the task
- [[BitwiseOperations]] — the recommended optimization technique
- [[MostSignificantBit]] — bit ordering for byte reconstruction

## Contradictions
- None — reference task page.
