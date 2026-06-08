---
title: "Magic squares of singly even order (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magic_squares_of_singly_even_order
---

## Summary
A magic square is an NxN matrix filled with consecutive integers so that every row, every column, and both main diagonals sum to the same magic constant. A square is "singly even" when its order is congruent to 2 mod 4 (i.e. 6, 10, 14, ...), which is the trickiest case to construct because the order is even yet not divisible by 4. The standard construction (the LUX / Conway method) splits the square into four odd-order subsquares, fills each with a shifted odd-order magic square, then swaps selected columns to fix the diagonals.

## Task Requirements
- Construct and display a 6x6 magic square (a singly even square).
- All rows, all columns, and both diagonals must sum to the same magic constant.

## Language Coverage
32 languages implement this task, spanning systems languages, scripting languages, and assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Ruby, Perl, and even 360 Assembly and EDSAC order code.

## Connections
- [[MagicSquare]] — the matrix structure this task builds
- [[NumberTheory]] — order classification by residue mod 4
- [[LUXMethod]] — the standard singly-even construction technique
- [[MatrixConstruction]] — assembling the result from odd-order subsquares

## Contradictions
- None — reference task page.
