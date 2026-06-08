---
title: "Sum of a series (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, summation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_of_a_series
---

## Summary
This task asks the programmer to compute the n-th partial sum of a series — the sum of the first n terms of a sequence. The concrete instance is S_n = sum over k from 1 to n of 1/k², evaluated at n = 1000. The key insight is that this partial sum approximates the Riemann zeta function at s=2, whose exact limit is π²/6, the answer to the famous Basel problem.

## Task Requirements
- Compute the n-th term (partial sum) of a series, i.e. accumulate the sum of the first n terms of a sequence.
- Specifically evaluate S_n = Σ (1/k²) for k = 1 to n.
- Compute S_1000 concretely.
- Note that this value approaches ζ(2) = π²/6 as n grows.

## Language Coverage
197 languages implement this task, making it one of the broadest entries on the site, spanning everything from assembly to modern functional languages. Representative implementations include C, Python, Haskell, Java, JavaScript, Rust, Go, Ruby, Lisp, and APL.

## Connections
- [[RiemannZetaFunction]] — the partial sum approximates ζ(2)
- [[BaselProblem]] — the exact limit π²/6 is the solution to this classic problem
- [[Summation]] — the core operation of accumulating sequence terms
- [[Series]] — the mathematical object being partially summed
- [[FloatingPointArithmetic]] — practical accumulation involves floating-point precision concerns

## Contradictions
- None — reference task page.
