---
title: "Cycles of a permutation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, permutations, group-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cycles_of_a_permutation
---

## Summary
This task explores permutations and their cycle decomposition, framed through a story of a couple rearranging fifteen letters on a shelf. The programmer must implement a toolkit for working with permutations in both one-line notation and cycle notation, including conversion between them, inversion, application to a string, and composition (multiplication). The key insight is that any permutation factors uniquely into disjoint cycles, and that this representation makes operations like inversion, order, and signature computable directly from cycle structure.

## Task Requirements
- Build a permutation from two strings sharing the same unique characters, in one-line or cycle notation.
- Compute the inverse of a permutation in both notations (reverse each cycle; rotate smallest element first to keep convention).
- Apply a permutation (either notation) to a string of unique characters.
- Compose two permutations A and B in cycle notation, yielding the single permutation equivalent to applying A then B (i.e. A·B / function composition).
- Convert between one-line and cycle notation in both directions (decomposition).
- Return the order of a permutation: the least common multiple of its cycle lengths.
- Return the signature (sign/parity): +1 for an even number of even-length cycles, -1 otherwise.
- Demonstrate the full toolkit on the seven shelf arrangements; state notation and 0- vs 1-based choices.

## Language Coverage
20 languages implement this task, a moderate spread covering systems, scripting, JVM, and niche stack-based languages. Representative entries include C#, C++, Go, Java, JavaScript, Julia, Python, Rust, Raku, Swift, Wren, and Quackery.

## Connections
- [[Permutation]] — the core mathematical object the task manipulates.
- [[CycleNotation]] — the disjoint-cycle decomposition that names the task.
- [[GroupTheory]] — permutations form the symmetric group; composition is its operation.
- [[LeastCommonMultiple]] — used to compute the order of a permutation.
- [[PermutationParity]] — the signature is the parity of the permutation's transposition count.

## Contradictions
- None — reference task page.
