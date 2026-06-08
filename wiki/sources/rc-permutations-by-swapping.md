---
title: "Permutations by swapping (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Permutations_by_swapping
---

## Summary
This task asks the programmer to generate all permutations of n items such that each successive permutation differs from the previous one by swapping exactly two items. Along with each permutation, the program must report its sign (+1 for an even number of swaps from the initial state, -1 for an odd number). The key insight is that swapping any two elements always flips the parity, so signs simply alternate as permutations are generated. These ordered permutations-with-signs are precisely what is needed to compute the determinant of a square matrix.

## Task Requirements
- Generate the permutations of n items so each successive one differs from the prior by swapping two items.
- Output the sign of each permutation: +1 for an even swap count from the start, -1 for odd.
- Demonstrate by showing all permutations and signs of three items in order of generation.
- Note that adjacency of the swapped items is not required (the Steinhaus–Johnson–Trotter algorithm uses adjacent swaps, but that is not mandated).
- Keep determinant computation in mind when designing the function.

## Language Coverage
52 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[Permutations]] — the core combinatorial objects being enumerated.
- [[SteinhausJohnsonTrotterAlgorithm]] — generates permutations via adjacent transpositions.
- [[HeapsAlgorithm]] — alternative swap-based permutation generator.
- [[ParityOfAPermutation]] — the sign tracks even/odd swap parity.
- [[Determinant]] — signed permutations are summed to compute a matrix determinant.

## Contradictions
- None — reference task page.
