---
title: "Ordered partitions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ordered_partitions
---

## Summary
The task asks the programmer to implement a function `partitions(arg_1, ..., arg_n)` that distributes the consecutive integers `{1, ..., sum(args)}` into `n` ordered blocks whose sizes are exactly the given arguments. Because the blocks are ordered and distinguishable, the output enumerates every way to assign elements to sized slots — equivalent to choosing successive combinations for each block from the remaining elements. The key insight is that the count of results equals the multinomial coefficient, the product of binomial coefficients for each block in sequence.

## Task Requirements
- Generate all ordered distributions of `{1, ..., arg_1+...+arg_n}` into `n` blocks of sizes `arg_1, ..., arg_n`.
- A block of size 0 is valid and appears as an empty set in the output.
- Total number of results is the multinomial coefficient `C(s, arg_1) * C(s - arg_1, arg_2) * ...`.
- Use only the language's standard library (no external combinatorics helpers).
- The program must be runnable from the command line and default to printing `partitions(2, 0, 2)`.
- If the language lacks polyvariadic functions, accept a list argument instead.

## Language Coverage
38 languages implement this task, spanning functional, imperative, and array styles — including Haskell, Python, C, C++, Java, JavaScript, Julia, Racket, Common Lisp, and J. The breadth reflects that combinatorial enumeration maps naturally onto recursion or list-comprehension idioms in nearly every paradigm.

## Connections
- [[Combinations]] — each block is chosen as a combination from the remaining elements
- [[MultinomialCoefficient]] — gives the exact count of ordered partitions
- [[BinomialCoefficient]] — the multinomial count is a product of these
- [[Recursion]] — the natural strategy: fix one block, recurse on the rest
- [[DiscreteMathematics]] — the broader domain of the task

## Contradictions
- None — reference task page.
