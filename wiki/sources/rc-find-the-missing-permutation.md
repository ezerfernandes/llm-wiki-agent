---
title: "Find the missing permutation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, permutations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_the_missing_permutation
---

## Summary
Given 23 of the 24 permutations of the symbols A, B, C, and D, the task is to identify the single missing permutation. The clever insight is that a brute-force enumeration is unnecessary: because each letter appears an equal (even) number of times in every column when all permutations are present, the missing letter for each position can be recovered by computing the parity or column-sum of the listed permutations.

## Task Requirements
- Take the supplied list of 23 four-letter permutations of A, B, C, D.
- Determine the one permutation that is absent from the list.
- The obvious method is to enumerate all 24 permutations and find which one is not present.
- An alternate method exploits parity: each letter appears an even number of times per column across all permutations, so the missing letter in a column is the one whose count is odd (or recoverable via XOR / column-sum).

## Language Coverage
91 languages implement this task, giving very broad coverage across functional, imperative, array, and assembly families. Representative implementations include Python, Haskell, C, Java, JavaScript, Ruby, Rust, J, APL, and REXX.

## Connections
- [[Permutations]] — the task operates over the full set of permutations of a four-element alphabet.
- [[Combinatorics]] — counting and enumerating arrangements underlies both solution methods.
- [[Parity]] — the elegant solution recovers each missing letter from the parity of per-column letter counts.
- [[XOR]] — a common implementation trick is to XOR all values in a column to isolate the odd-one-out.

## Contradictions
- None — reference task page.
