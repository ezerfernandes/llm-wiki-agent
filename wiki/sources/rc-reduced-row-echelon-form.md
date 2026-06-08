---
title: "Reduced row echelon form (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Reduced_row_echelon_form
---

## Summary
The task asks the programmer to compute the reduced row echelon form (RREF, also called row canonical form) of a matrix, typically stored as a two-dimensional array. The standard approach is Gauss-Jordan elimination: locate a pivot in each column, normalize the pivot row, and eliminate that column's entries in all other rows. The key insight is tracking a "lead" column that advances as pivots are found, skipping columns that are entirely zero.

## Task Requirements
- Reduce an arbitrary matrix to reduced row echelon form.
- The matrix may be stored in any convenient datatype (commonly a 2D array).
- Built-in functions or the provided Wikipedia pseudocode may be used.
- The pseudocode iterates over rows, finds/swaps a nonzero pivot for the current lead column, divides the pivot row to make the pivot 1, then subtracts multiples of the pivot row from every other row.
- Verify against the given 3x4 test matrix, which reduces to a form with an identity block in the first three columns and the solution `[-8, 1, -2]` in the last.

## Language Coverage
72 languages implement this task, showing very broad coverage spanning systems, scripting, functional, and array/math-oriented languages. Representative implementations include C, C++, Java, Python, Haskell, Go, Rust, Julia, J, MATLAB, Mathematica, and REXX.

## Connections
- [[GaussianElimination]] — the elimination procedure RREF builds upon
- [[LinearAlgebra]] — RREF is a foundational matrix canonical form
- [[Matrix]] — the data structure operated on
- [[SystemsOfLinearEquations]] — RREF directly yields solutions to linear systems
- [[NumericalStability]] — pivot selection affects floating-point accuracy

## Contradictions
- None — reference task page.
