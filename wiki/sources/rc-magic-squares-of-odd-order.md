---
title: "Magic squares of odd order (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, matrix]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magic_squares_of_odd_order
---

## Summary
The task asks the programmer to generate an NxN magic square for any odd N, filling it with the integers 1 through N², such that every row, every column, and both main diagonals sum to the same value (the "magic constant"). The standard approach is the Siamese (de la Loubère) method: place 1 in the middle of the top row, then move diagonally up-and-right for each successive number, wrapping around the edges, and dropping straight down one cell whenever the target cell is already occupied.

## Task Requirements
- Generate a magic square of odd order N using consecutive integers 1 through N².
- Every row, column, and both main diagonals must share the same sum.
- Demonstrate the generator with at least the case N = 5.
- Optionally display the magic number (magic constant), which equals N(N²+1)/2.

## Language Coverage
76 languages implement this task, giving very broad coverage across paradigms — from low-level assembly and array-oriented languages to functional and scripting languages. Representative implementations include C, C++, Python, Java, Haskell, J, APL, Rust, Go, and Common Lisp.

## Connections
- [[MagicSquare]] — the combinatorial object the task constructs.
- [[SiameseMethod]] — the de la Loubère diagonal-placement algorithm for odd orders.
- [[NumberTheory]] — the magic constant formula N(N²+1)/2 derives from arithmetic series.
- [[Matrix]] — the square is represented and manipulated as a 2D grid.
- [[ModularArithmetic]] — edge wrapping during placement relies on index modulo N.

## Contradictions
- None — reference task page.
