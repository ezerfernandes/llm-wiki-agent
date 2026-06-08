---
title: "Random Latin squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, randomization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Random_Latin_squares
---

## Summary
A Latin square of size n is an n-by-n grid filled with n symbols so that every symbol appears exactly once in each row and each column. This task asks for a routine that, given n, generates a randomized Latin square such that any valid square has non-zero probability of being produced. The key relaxation is that strict uniform sampling (an unsolved hard problem) is explicitly not required, so simple randomized construction-with-backtracking or shuffling approaches are acceptable.

## Task Requirements
- Write a function that, given n, generates a randomized Latin square of size n.
- The generation must be probabilistic: every valid Latin square of size n must have a non-zero chance of being produced.
- Use the function to generate and display two randomly generated squares of size 5.
- Strict uniformity is not required.

## Language Coverage
38 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include C, C++, C#, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[LatinSquare]] — the core combinatorial object the task constructs
- [[Combinatorics]] — Latin squares are a classic combinatorial design
- [[Randomization]] — probabilistic generation is central to the task
- [[Backtracking]] — common technique for filling rows while preserving constraints
- [[ConstraintSatisfaction]] — each cell must satisfy row and column uniqueness constraints

## Contradictions
- None — reference task page.
