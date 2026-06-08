---
title: "Factorial base numbers indexing permutations of a collection (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Factorial_base_numbers_indexing_permutations_of_a_collection
---

## Summary
The task asks the programmer to build a one-to-one mapping between factorial base numbers (mixed-radix numbers where the least significant digit is base 2, the next base 3, and an n-digit number has digits in bases 2 through n+1) and the permutations of a collection. The key insight is the decoding algorithm: scanning digits from most to least significant, each non-zero digit g triggers a rotation of the elements from position m to m+g, producing the corresponding permutation deterministically. This gives an efficient, lossless index into the n! permutations of n elements.

## Task Requirements
- Implement a function that converts a factorial base number into the matching permutation via the rotate-from-m-to-m+g algorithm.
- Reproduce the example table mapping the first 24 three-digit factorial base numbers (0.0.0 through 3.2.1) to permutations of 0123.
- Generate all permutations of 11 digits (counting rather than displaying) and compare the approach with Rosetta Code's general permutations task.
- Apply the function to two provided 51-digit factorial base numbers to permute a 52-card shoe.
- Construct one's own 51-digit factorial base number and produce its corresponding permutation of the shoe.

## Language Coverage
20 languages implement this task, spanning systems, functional, array, and scripting paradigms. Representative implementations include ALGOL 68, C++, Go, Haskell, J, Java, JavaScript, Julia, Python, Raku, and Wren.

## Connections
- [[FactorialNumberSystem]] — the mixed-radix numeral system underlying the digit-to-permutation index
- [[Permutations]] — the combinatorial structures the numbers index
- [[Combinatorics]] — the broader field of counting and enumerating arrangements
- [[LehmerCode]] — the closely related bijection between integers and permutations
- [[Factorial]] — the n! count of permutations these indices enumerate

## Contradictions
- None — reference task page.
