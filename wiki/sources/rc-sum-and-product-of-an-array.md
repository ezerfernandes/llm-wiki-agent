---
title: "Sum and product of an array (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arrays, reduction, arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_and_product_of_an_array
---

## Summary
This task asks the programmer to compute both the sum and the product of an array (or list) of integers. The key insight is that both operations are simple folds (reductions) over a sequence: the sum accumulates with addition starting from 0, while the product accumulates with multiplication starting from 1. Many languages express this in one line via built-in reduce/fold functions or vectorized aggregate operations.

## Task Requirements
- Compute the sum of an array of integers.
- Compute the product of an array of integers.

## Language Coverage
207 languages implement this task, making it one of the most broadly covered entries on Rosetta Code, spanning everything from assembly to functional and array-oriented languages. Representative implementations include C, Python, Haskell, Java, JavaScript, Ruby, Rust, Lisp, APL, and J.

## Connections
- [[Fold]] — sum and product are textbook left/right folds over a sequence
- [[Reduction]] — both results are reductions of an array with an accumulator
- [[IdentityElement]] — 0 is the additive identity, 1 is the multiplicative identity used as fold seeds
- [[ArrayProcessing]] — iterating or aggregating over a collection of elements

## Contradictions
- None — reference task page.
