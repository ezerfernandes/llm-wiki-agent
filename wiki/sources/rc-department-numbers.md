---
title: "Department numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, constraint-satisfaction, brute-force]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Department_numbers
---

## Summary
Assign a distinct number from 1 to 7 to each of three departments (police, sanitation, fire) such that the three numbers are unique and sum to 12, with the additional constraint that the police number must be even. The task is to enumerate and print every valid combination. The key insight is that this is a small finite constraint-satisfaction problem solvable by exhaustively iterating over the three values and filtering on the constraints.

## Task Requirements
- Each department number is an integer between 1 and 7 inclusive.
- The three numbers must be unique (all different from one another).
- The three numbers must add up to 12.
- The police department number must be even.
- Output all valid combinations (in a police/sanitation/fire layout).

## Language Coverage
105 languages implement this task, spanning assembly, classic, functional, and scripting families. Representative solutions include C, C++, Python, Java, Haskell, Rust, Go, Perl, Ruby, and REXX.

## Connections
- [[Combinatorics]] — enumerating ordered selections under constraints
- [[ConstraintSatisfaction]] — filtering candidate tuples by rules
- [[BruteForceSearch]] — exhaustive iteration over the small search space
- [[NestedLoops]] — typical triple-loop implementation strategy

## Contradictions
- None — reference task page.
