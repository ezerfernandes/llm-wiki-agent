---
title: "Hofstadter Figure-Figure sequences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hofstadter_Figure-Figure_sequences
---

## Summary
The task asks for an implementation of the two interleaving Hofstadter Figure-Figure sequences R and S, where R(1)=1, S(1)=2, and each subsequent R(n) = R(n-1) + S(n-1). The defining insight is that S is the strictly increasing sequence of positive integers absent from R, so the two sequences together form a complementary partition of the positive integers. Computing R therefore requires generating S on the fly by tracking which integers have not yet appeared in R.

## Task Requirements
- Write two functions `ffr` and `ffs` returning R(n) and S(n) respectively (1-indexed: R(1)=1, S(1)=2).
- Assume no maximum value for n.
- Show the first ten values of R: 1, 3, 7, 12, 18, 26, 35, 45, 56, 69.
- Demonstrate that the first 40 values of ffr plus the first 960 values of ffs together contain every integer from 1 to 1000 exactly once.

## Language Coverage
61 languages implement this task, spanning functional, imperative, and array-oriented paradigms. Representative implementations include Python, Haskell, C, C++, Java, Go, Rust, J, APL, Racket, Raku, and Common Lisp.

## Connections
- [[IntegerSequences]] — R and S are integer sequences (OEIS A005228 and A030124).
- [[ComplementarySequences]] — S consists exactly of the positive integers not in R, a complementary partition.
- [[Recursion]] — R is defined recursively in terms of prior R and S values.
- [[SieveTechnique]] — generating S requires sieving out integers already claimed by R.
- [[NumberTheory]] — the construction is a classic self-referential number-theoretic sequence.

## Contradictions
- None — reference task page.
