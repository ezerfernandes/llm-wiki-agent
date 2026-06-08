---
title: "Sum of elements below main diagonal of matrix (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrix]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_of_elements_below_main_diagonal_of_matrix
---

## Summary
The task asks the programmer to compute and display the sum of all elements that lie strictly below the main diagonal of a square matrix. The key insight is that an element at row i, column j is below the main diagonal exactly when j < i, so the solution simply iterates over those positions and accumulates their values.

## Task Requirements
- Operate on a square matrix (the task supplies a fixed 5x5 example matrix).
- Sum only the elements strictly below the main diagonal (where column index < row index).
- Find and display that sum.

## Language Coverage
53 languages implement this task, spanning systems languages, scripting languages, array-oriented and functional languages. Representative implementations include C, C++, Java, Python, JavaScript, Haskell, Julia, APL, J, and Wren.

## Connections
- [[Matrix]] — the data structure being summed.
- [[MainDiagonal]] — the reference line that partitions elements above, on, and below it.
- [[TriangularMatrix]] — the strictly-lower-triangular region defines exactly which elements are summed.
- [[NestedIteration]] — the common imperative technique of looping over rows and columns to accumulate the result.

## Contradictions
- None — reference task page.
