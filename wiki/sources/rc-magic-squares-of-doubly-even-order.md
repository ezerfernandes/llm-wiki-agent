---
title: "Magic squares of doubly even order (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, matrix]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magic_squares_of_doubly_even_order
---

## Summary
The task is to construct a magic square whose order N is a multiple of four (doubly even — e.g. 4, 8, 12). A magic square is an N×N matrix filled with the consecutive integers 1..N² such that every row, every column, and both main diagonals sum to the same magic constant. The key construction insight is that for doubly even orders, every N×N sub-block is also even, allowing a simple pattern-based fill rather than a search.

## Task Requirements
- Build a magic square of doubly even order, concretely demonstrating an 8×8 square.
- Fill it with consecutive integers 1..N² so all rows, columns, and both diagonals share the same magic constant.
- The standard method: number the cells 1..N² left-to-right, top-to-bottom, then in marked diagonal-pattern cells replace each value v with N²+1−v (complement), leaving the rest in place.

## Language Coverage
49 languages implement this task, spanning systems, scripting, functional, and historical/assembly dialects. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and even EDSAC order code and 360 Assembly.

## Connections
- [[MagicSquare]] — the central combinatorial structure being built
- [[NumberTheory]] — properties of the magic constant N(N²+1)/2
- [[Matrix]] — the square is represented and manipulated as a 2D grid
- [[MagicSquaresOfOddOrder]] — sibling task using a different (Siamese) construction
- [[MagicSquaresOfSinglyEvenOrder]] — sibling task for orders ≡ 2 (mod 4)

## Contradictions
- None — reference task page.
