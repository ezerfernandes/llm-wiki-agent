---
title: "Latin Squares in reduced form (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, enumeration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Latin_Squares_in_reduced_form
---

## Summary
A Latin Square of order n is an n×n grid filled with n symbols such that each symbol appears exactly once in every row and every column; it is in reduced form when its first row and first column are in natural order (1 to n). The task is to enumerate the complete set of reduced Latin Squares of a given order and to index any element by a number g. The key insight is that each row beyond the first is a derangement-style permutation that must not clash (share a symbol in any column) with the rows already placed, so the set is built by constrained row-by-row backtracking.

## Task Requirements
- Construct the set of all reduced Latin Squares of a given order n, where row 1 is fixed as 1..n and each subsequent row k starts with k and clashes with no earlier row.
- Provide a means by which a number g selects a unique element from the set.
- Display the four reduced Latin Squares of order 4.
- For n = 1 to 6 (or more), produce a table of set sizes and verify that size × n! × (n-1)! matches the total Latin Square counts in OEIS A002860.

## Language Coverage
26 languages implement this task, spanning systems, functional, scripting, and constraint-solving styles. Representative implementations include C++, D, Go, Haskell, Java, Julia, Python, Raku, Rust, Wren, MiniZinc, and Phix.

## Connections
- [[LatinSquare]] — the combinatorial object being enumerated
- [[Permutation]] — each row is a permutation of the symbol set
- [[Derangement]] — second row and constrained later rows are derangements of the natural order
- [[Backtracking]] — the row-by-row clash-checking search strategy
- [[Combinatorics]] — counting and indexing the set, cross-checked against OEIS A002860

## Contradictions
- None — reference task page.
