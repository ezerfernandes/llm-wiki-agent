---
title: "Vector products (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Vector_products
---

## Summary
This task asks the programmer to implement the four common products of 3-dimensional vectors: the dot (scalar) product, the cross (vector) product, the scalar triple product, and the vector triple product. The key insight is that the scalar and vector triple products are simply compositions of the dot and cross products, so implementing those two primitives well lets the higher-order products be expressed by combining them.

## Task Requirements
- Define a named function to compute the dot product of two vectors (yields a scalar).
- Define a function to compute the cross product of two vectors (yields a vector).
- Optionally define functions for the scalar triple product `A • (B x C)` and the vector triple product `A x (B x C)`.
- Using a = (3, 4, 5), b = (4, 3, 5), c = (-5, -12, -13), compute and display: `a • b`, `a x b`, `a • (b x c)`, and `a x (b x c)`.

## Language Coverage
119 languages implement this task, reflecting broad coverage across functional, imperative, array-oriented, and scientific-computing languages. Representative implementations include Python, C, C++, Haskell, J, APL, MATLAB / Octave, Julia, Rust, and Common Lisp.

## Connections
- [[DotProduct]] — the scalar product underlying the task
- [[CrossProduct]] — the vector product and basis for triple products
- [[LinearAlgebra]] — the mathematical domain of vector operations
- [[Vector]] — the 3-tuple data structure being operated on
- [[TripleProduct]] — scalar and vector triple products defined here

## Contradictions
- None — reference task page.
