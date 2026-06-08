---
title: "Twelve statements (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, logic-puzzle, constraint-satisfaction, brute-force]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Twelve_statements
---

## Summary
This puzzle presents twelve self-referential statements that make claims about how many of the other statements (or themselves) are true, and asks the programmer to determine which assignment of truth values is self-consistent. The key insight is that there are only 2^12 = 4096 possible true/false assignments, so the cleanest solution is to brute-force every combination and keep those where each statement's asserted condition matches its assigned truth value.

## Task Requirements
- Encode the twelve interlocking, self-referential statements (e.g. "Exactly 3 of the last 6 statements are true", "If statement 5 is true, then 6 and 7 are both true").
- Search for and print every truth-value assignment that is fully consistent (each statement is true exactly when its claim holds).
- Extra credit: print a table of "near misses" — assignments contradicted by exactly one statement.

## Language Coverage
55 languages implement this task, spanning logic/constraint languages, functional, and mainstream imperative styles. Representative implementations include Prolog, Picat, Haskell, Python, C++, Java, Go, Julia, Raku, and Mathematica/Wolfram Language.

## Connections
- [[ConstraintSatisfactionProblem]] — the puzzle is naturally expressed as constraints over twelve boolean variables.
- [[BruteForceSearch]] — enumerating all 4096 assignments is the standard solution strategy.
- [[BooleanLogic]] — each statement is a propositional condition over the truth-value vector.
- [[SelfReference]] — statements reference the truth of the statement set, including themselves.
- [[LogicProgramming]] — Prolog and Picat express the solution declaratively.

## Contradictions
- None — reference task page.
