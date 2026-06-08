---
title: "Element-wise operations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Element-wise_operations
---

## Summary
This task asks the programmer to implement basic element-wise operations on matrices, covering both matrix-matrix and scalar-matrix variants. The required operations are addition, subtraction, multiplication, division, and exponentiation, each applied position-by-position rather than via conventional linear-algebra rules. The key insight is that element-wise operations are simple componentwise applications of a scalar operator across aligned positions, distinct from matrix multiplication or other algebraic products.

## Task Requirements
- Implement element-wise matrix-matrix operations and scalar-matrix operations.
- Support addition, subtraction, multiplication, division, and exponentiation.
- These primitives are meant to be reusable building blocks for higher-order tasks.
- Optionally extend with additional basic operations that do not warrant their own task.

## Language Coverage
54 languages implement this task, spanning array-oriented, functional, imperative, and mathematical-DSL ecosystems. Representative implementations include C, C++, C#, Java, Python, Haskell, J, Julia, MATLAB, Fortran, Rust, and Wren, with array languages like J and K expressing the operations especially tersely.

## Connections
- [[MatrixMultiplication]] — a related but distinct matrix operation referenced by this task
- [[MatrixTransposition]] — a sibling basic matrix manipulation task
- [[LinearAlgebra]] — the broader domain these matrix primitives belong to
- [[Broadcasting]] — the scalar-matrix variants generalize to the broadcasting pattern in array programming
- [[HigherOrderFunctions]] — element-wise ops are naturally implemented by mapping an operator over aligned elements

## Contradictions
- None — reference task page.
