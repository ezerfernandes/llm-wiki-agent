---
title: "Forward difference (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Forward_difference
---

## Summary
The task asks the programmer to compute the nth-order forward difference of a list of numbers, given a non-negative integer order and the list. The first-order forward difference replaces each element with the difference between it and its successor (B[i] = A[i+1] - A[i]), yielding a list with one fewer element; applying this repeatedly n times gives the nth-order difference. The key insight is that the operation can be implemented either iteratively (recomputing a shorter list each pass) or in closed form via the binomial-coefficient formula.

## Task Requirements
- Accept a non-negative integer n (the order) and a list of numbers.
- Produce the nth-order forward difference list.
- The first-order difference of list A is list B where B[i] = A[i+1] - A[i].
- Each successive order reduces the list length by one, so the nth-order result has n fewer elements than the input.
- Order 0 returns the original list unchanged.

## Language Coverage
105 languages implement this task, reflecting very broad coverage across paradigms. Representative implementations include C, C++, Python, Haskell, Java, JavaScript, Ruby, Rust, Lisp dialects, and array languages such as APL, J, and BQN where the operation is especially concise.

## Connections
- [[FiniteDifference]] — the forward difference is the discrete analogue of differentiation.
- [[BinomialCoefficient]] — the closed-form nth-order difference sums terms weighted by binomial coefficients.
- [[PascalsTriangle]] — supplies the alternating binomial weights used in the formula option.
- [[NumericalDifferentiation]] — forward differences approximate derivatives on discrete data.
- [[Recursion]] — repeated application naturally expresses as a recursive reduction over the list.

## Contradictions
- None — reference task page.
