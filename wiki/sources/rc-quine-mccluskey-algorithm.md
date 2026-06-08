---
title: "Quine–McCluskey algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, boolean-logic, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Quine–McCluskey_algorithm
---

## Summary
The task is to implement the Quine–McCluskey algorithm, an exact method for minimizing a Boolean function given as a set of minterms. Unlike Karnaugh maps it scales beyond a handful of variables and produces a guaranteed-minimal sum-of-products expression. The key insight is a two-stage process: tabular combination of adjacent minterms to find prime implicants, followed by chart-based selection of essential prime implicants for full coverage.

## Task Requirements
- Accept a Boolean function specified via truth table, minterm set, or Karnaugh map.
- Stage 1: group minterms by the number of 1-bits, then repeatedly combine pairs differing in exactly one bit, replacing the differing bit with a dash ("don't care"), until no more combinations are possible, yielding the prime implicants.
- Stage 2: build a prime-implicant chart (implicants as rows, minterms as columns) and identify essential prime implicants that uniquely cover some minterm.
- Select additional implicants as needed so every minterm is covered, minimizing the total number of terms.
- Output the minimal sum-of-products representation.

## Language Coverage
16 languages implement this task, a moderate spread spanning systems, scripting, and academic languages. Representative entries include C#, C++, Go, Java, JavaScript, Python, Julia, Rust, Raku, and R.

## Connections
- [[BooleanAlgebra]] — the algebraic structure the function is minimized within
- [[LogicMinimization]] — the broader problem class the algorithm solves
- [[KarnaughMap]] — the visual heuristic this algorithm generalizes and replaces
- [[PrimeImplicant]] — the central combinatorial object produced in stage one
- [[EspressoAlgorithm]] — the heuristic alternative used when variable count is large

## Contradictions
- None — reference task page.
