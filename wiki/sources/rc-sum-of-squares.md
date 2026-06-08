---
title: "Sum of squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arithmetic, reduction]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_of_squares
---

## Summary
This task asks the programmer to compute the sum of the squares of the elements of a numeric vector. The key edge case is that a zero-length (empty) vector must yield 0, which falls out naturally from initializing the accumulator to the additive identity. It is a canonical map-then-reduce exercise that maps each element to its square and folds the results with addition.

## Task Requirements
- Write a program that finds the sum of squares of a numeric vector.
- The program must handle a zero-length vector, returning an answer of 0.

## Language Coverage
186 languages implement this task, making it one of Rosetta Code's broadest entries, spanning systems, functional, scripting, and stack-based languages. Representative implementations include C, C++, Java, Python, Haskell, Ruby, Rust, Go, Common Lisp, and APL.

## Connections
- [[Reduce]] — folding the squared elements with addition is a classic reduction.
- [[MapReduce]] — the task is the map (squaring) followed by reduce (summing) pattern.
- [[VectorArithmetic]] — operates element-wise over a numeric vector.
- [[IdentityElement]] — the empty-vector case relies on 0 being the additive identity.

## Contradictions
- None — reference task page.
