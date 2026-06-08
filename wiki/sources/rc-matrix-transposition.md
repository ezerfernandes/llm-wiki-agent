---
title: "Matrix transposition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, arrays]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Matrix_transposition
---

## Summary
The task asks the programmer to transpose an arbitrarily sized rectangular matrix, swapping its rows and columns so that element at position (i, j) moves to (j, i). The key insight is handling non-square (m×n becoming n×m) matrices generically rather than assuming square input. Array-oriented languages can often do this with a single built-in primitive.

## Task Requirements
- Transpose an arbitrarily sized rectangular matrix.
- The solution must work for non-square dimensions (an m×n matrix yields an n×m result).

## Language Coverage
141 languages implement this task, spanning systems, scripting, functional, and array-oriented paradigms. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, J, APL, MATLAB, Julia, and Fortran.

## Connections
- [[Matrix]] — the data structure being operated on
- [[Transpose]] — the core mathematical operation
- [[LinearAlgebra]] — the mathematical domain
- [[TwoDimensionalArrays]] — the typical underlying representation

## Contradictions
- None — reference task page.
