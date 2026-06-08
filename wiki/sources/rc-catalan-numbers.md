---
title: "Catalan numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Catalan_numbers
---

## Summary
The task asks the programmer to compute and print the first 15 Catalan numbers, a sequence arising frequently in combinatorial counting problems. Three equivalent formulas are offered: a direct closed form using a binomial coefficient, a convolution-style recursion summing products of earlier terms, and a simpler linear recurrence relating each term to its predecessor. The key insight is that the same sequence can be reached through markedly different algorithms with very different cost profiles.

## Task Requirements
- Implement at least one of the three given algorithms (closed-form binomial, convolution recurrence, or the linear recurrence Cn = 2(2n-1)/(n+1) * Cn-1).
- Print the first 15 Catalan numbers (C0 through C14) using the chosen method.
- Memoization is optional but suggested as worthwhile for the convolution recurrence.

## Language Coverage
127 languages implement this task, reflecting very broad coverage across functional, imperative, array, and assembly families. Representative examples include Python, Haskell, C, Rust, Java, J, APL, Mathematica, Forth, and REXX.

## Connections
- [[CatalanNumber]] — the integer sequence the task computes
- [[BinomialCoefficient]] — basis of the closed-form definition
- [[Recursion]] — underlies two of the three algorithms
- [[Memoization]] — optimization suggested for the convolution recurrence
- [[Combinatorics]] — the broader field where these counts appear

## Contradictions
- None — reference task page.
