---
title: "Dinesman's multiple-dwelling problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-satisfaction, logic-puzzle, search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dinesman's_multiple-dwelling_problem
---

## Summary
This classic logic puzzle (from SICP) asks the programmer to determine which of five people — Baker, Cooper, Fletcher, Miller, and Smith — lives on each of the five floors of an apartment building, given a set of constraints on their positions. The key challenge is not just solving the puzzle but expressing it naturally: solutions should follow the plain-English problem statement closely and make it easy to modify constraints, valuing flexibility and clarity over brute speed.

## Task Requirements
- Assign each of the five named tenants to a distinct floor (1–5).
- Honor all constraints: Baker not on the top floor; Cooper not on the bottom; Fletcher on neither top nor bottom; Miller above Cooper; Smith not adjacent to Fletcher; Fletcher not adjacent to Cooper.
- Solve in a way that follows the problem statement naturally; parsing/interpreting the problem text is allowed but optional.
- State which changes to the problem are easy to make, and show example output.
- Optionally split the solution into "setup", "problem statement", and "output" sections.

## Language Coverage
69 languages implement this task, spanning constraint-logic, functional, and imperative styles. Representative implementations include Python, Prolog, Common Lisp, Haskell, Racket, MiniZinc, Picat, J, Ruby, and C++.

## Connections
- [[ConstraintSatisfactionProblem]] — the puzzle is a textbook finite-domain CSP.
- [[Permutations]] — the brute-force approach enumerates all orderings of tenants over floors.
- [[BacktrackingSearch]] — a common solving strategy that prunes invalid partial assignments.
- [[LogicProgramming]] — declarative languages like Prolog and MiniZinc express the constraints directly.
- [[StructureAndInterpretationOfComputerPrograms]] — the original source of this problem.

## Contradictions
- None — reference task page.
