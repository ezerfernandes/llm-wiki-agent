---
title: "Knuth shuffle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, algorithms, randomization, arrays]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knuth_shuffle
---

## Summary
The task is to implement the Knuth shuffle (also known as the Fisher-Yates shuffle), an algorithm that randomly permutes the elements of an array. The key insight is that iterating from the last index down to 1 and swapping each element with a randomly chosen element at or below its index produces an unbiased permutation in linear time, where every ordering is equally likely.

## Task Requirements
- Implement the Knuth shuffle for an integer array, or ideally for an array of any type.
- Follow the in-place algorithm: for i from last downto 1, pick a random integer j with 0 ≤ j ≤ i, and swap items[i] with items[j].
- The shuffle should modify the array in place; if that is impractical in the language, returning a new shuffled array is acceptable.
- Iterating left-to-right instead of right-to-left is an allowed variant.

## Language Coverage
146 languages implement this task, reflecting very broad coverage across nearly every paradigm. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Ruby, Common Lisp, and Scala.

## Connections
- [[FisherYatesShuffle]] — the canonical name for this algorithm
- [[RandomPermutation]] — what the shuffle produces, with uniform probability
- [[InPlaceAlgorithm]] — the standard formulation mutates the array directly
- [[SattoloCycle]] — closely related variant that produces only single-cycle permutations
- [[RandomNumberGeneration]] — the quality of the shuffle depends on the underlying RNG

## Contradictions
- None — reference task page.
