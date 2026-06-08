---
title: "Peaceful chess queen armies (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorial-search, backtracking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Peaceful_chess_queen_armies
---

## Summary
The task is to place two equal-sized "armies" of queens — m black and m white — on an n-by-n chessboard so that no queen attacks any queen of the opposite colour. Queens attack along rows, columns, and both diagonals, but only target pieces of the other colour, so same-colour queens may freely share lines of attack. The key insight is that this is a constraint-satisfaction/search problem distinct from the classic n-queens (where queens are mutually hostile), and the maximum achievable m for a given n is tracked by OEIS sequence A250000.

## Task Requirements
- Create a routine to represent two-colour queens on a 2-D board (visual embellishments optional).
- Create a routine to generate at least one valid placement of m black and m white queens on an n-by-n board such that no queen attacks one of the opposite colour.
- Display results for the m=4, n=5 case.

## Language Coverage
25 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, C#, D, Go, Java, Julia, Python, Perl, Raku, Scheme, and Uiua.

## Connections
- [[Backtracking]] — typical strategy for searching valid queen placements
- [[ConstraintSatisfaction]] — the no-opposite-colour-attack rule is a set of constraints
- [[CombinatorialSearch]] — exploring arrangements of pieces on a grid
- [[EightQueensPuzzle]] — related classic chessboard placement problem
- [[IntegerSequences]] — maxima recorded as OEIS A250000

## Contradictions
- None — reference task page.
