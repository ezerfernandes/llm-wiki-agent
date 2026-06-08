---
title: "Pascal's triangle/Puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, constraint-solving, linear-algebra]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pascal's_triangle/Puzzle
---

## Summary
This task presents a five-row "pyramid of numbers" where each brick equals the sum of the two bricks directly beneath it. Several cells are pre-filled (apex 151, others 40, 11, 4) and three base cells X, Y, Z are unknown, with the added constraint that the middle base value equals the sum of the outer two (Y = X + Z). The programmer must find the values that satisfy all the additive relationships. The key insight is that the whole pyramid is a system of linear equations in the unknown base cells, solvable by algebra, constraint propagation, or a constraint/SAT solver.

## Task Requirements
- Reconstruct the pyramid where every brick is the sum of the two bricks below it.
- Honor the given fixed values (apex 151; cell 40; base cells 11 and 4).
- Enforce the extra constraint Y = X + Z on the three missing base numbers.
- Write a program that finds a solution satisfying all constraints.

## Language Coverage
53 languages implement this task, spanning general-purpose, functional, and dedicated constraint/logic languages. Representative entries include C, C++, Java, Python, Haskell, Prolog, MiniZinc, Picat, Julia, and Raku — notably several use declarative constraint solvers (MiniZinc, Picat, Prolog) rather than hand-derived algebra.

## Connections
- [[ConstraintSatisfaction]] — the puzzle is naturally modeled as a CSP over the base cells
- [[SystemOfLinearEquations]] — the additive brick rules form a solvable linear system
- [[PascalsTriangle]] — the pyramid structure echoes the binomial coefficient triangle
- [[ConstraintPropagation]] — fixed values can be propagated upward/downward to deduce unknowns

## Contradictions
- None — reference task page.
