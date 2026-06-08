---
title: "Identity matrix (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, matrices]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Identity_matrix
---

## Summary
The task asks the programmer to build an identity matrix of a size `n` that is known only at run-time. An identity matrix is the square `n × n` matrix whose diagonal entries are all 1 and whose off-diagonal entries are all 0. The key insight is that each element can be produced directly from a comparison of its row and column indices (1 when they are equal, 0 otherwise), so no general matrix machinery is required.

## Task Requirements
- Construct a square matrix of size `n × n` where `n` is determined at run-time.
- Set every element on the main diagonal to 1 (one).
- Set every off-diagonal element to 0 (zero).

## Language Coverage
132 languages implement this task, reflecting very broad coverage that spans general-purpose, array-oriented, and math-focused languages. Representative implementations include Python, C, C++, Java, Haskell, J, APL, MATLAB / Octave, Mathematica, Julia, and Rust, with many BASIC and Lisp dialects also present.

## Connections
- [[IdentityMatrix]] — the mathematical object the task constructs.
- [[LinearAlgebra]] — domain where the identity matrix serves as the multiplicative identity.
- [[Matrix]] — the underlying square 2D data structure being built.
- [[NestedLoops]] — common imperative technique for filling rows and columns by index comparison.

## Contradictions
- None — reference task page.
