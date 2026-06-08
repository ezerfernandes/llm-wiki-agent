---
title: "Zebra puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, logic-puzzle, constraint-satisfaction]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zebra_puzzle
---

## Summary
The Zebra puzzle (a.k.a. Einstein's Riddle) is a logic puzzle to be solved programmatically. Five houses, each with a distinct color, nationality, pet, beverage, and cigarette brand, are constrained by 15 clues, and the task is to determine who owns the zebra. The key insight is that the puzzle reduces to a constraint-satisfaction problem solvable by exhaustive search over permutations or by logic-programming/constraint solvers.

## Task Requirements
- Model five houses, each with a unique color, nationality, pet, drink, and cigarette brand.
- Encode the 15 given clues (e.g., the Englishman lives in the red house; the Norwegian lives in the first house; milk is drunk in the middle house; the green house is immediately left of the white house).
- Determine who owns the zebra and list the full solution for all five houses.
- Optionally, demonstrate that the solution is unique.

## Language Coverage
62 languages implement this task, spanning imperative, functional, logic, and dedicated constraint-solving paradigms. Representative implementations include Prolog, MiniZinc, Picat, and Curry (constraint/logic styles) alongside Python, C, Haskell, Go, Rust, and Java (general-purpose search-based solutions).

## Connections
- [[ConstraintSatisfactionProblem]] — the puzzle is a canonical CSP instance.
- [[LogicProgramming]] — Prolog/Mercury/Curry solve it declaratively.
- [[BacktrackingSearch]] — common brute-force strategy over candidate assignments.
- [[Permutations]] — many solutions enumerate permutations of the five attributes.

## Contradictions
- None — reference task page.
