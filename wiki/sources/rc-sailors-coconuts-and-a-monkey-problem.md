---
title: "Sailors, coconuts and a monkey problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, brute-force]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sailors,_coconuts_and_a_monkey_problem
---

## Summary
A classic recreational number-theory puzzle: five shipwrecked sailors each secretly wake at night, divide a coconut pile into five equal parts with exactly one coconut left over (given to a monkey), hide their fifth, and recombine the rest. In the morning the remaining pile divides evenly into five with no remainder. The task is to find the minimum starting pile size that satisfies this chain of divide-by-N-remainder-1 operations followed by a final clean division.

## Task Requirements
- Compute the minimum initial pile size for the 5-sailor version.
- Solve it by searching candidate answers and applying the story's constraints (integer division, remainder, and remainder tests), not by plugging into a closed-form formula. Constraint solvers are permitted.
- Repeat the calculation for the 6-sailor variant.
- Show the results.
- Extra credit: report how many coconuts each sailor hides during the night.
- Note: this is the version where the monkey gets nothing in the morning (distinct from the variant where it does).

## Language Coverage
51 languages implement this task, spanning systems and scripting languages alike: C, C++, C#, Java, Go, Rust-adjacent Nim, Python, Ruby, Perl, Raku, Haskell, Julia, Clojure, and esoteric entries such as Befunge and Uiua. Most solutions iterate candidate pile sizes and verify the modular constraints.

## Connections
- [[NumberTheory]] — the puzzle is a system of modular divisibility constraints.
- [[ModularArithmetic]] — each night's step requires remainder 1 on division by the sailor count.
- [[BruteForceSearch]] — the mandated approach iterates and tests candidate answers.
- [[DiophantineEquations]] — the underlying analytical solution is an integer-valued linear recurrence.

## Contradictions
- None — reference task page.
