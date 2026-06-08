---
title: "Equilibrium index (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arrays, prefix-sum]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Equilibrium_index
---

## Summary
An equilibrium index of a sequence is a position where the sum of all elements to its left equals the sum of all elements to its right (with an empty side summing to zero). The task is to write a function that returns all equilibrium indices of a given sequence. The key insight is that a single pass tracking a running prefix sum against the precomputed total avoids the naive O(n²) recomputation, yielding an O(n) solution suitable for very long sequences.

## Task Requirements
- Given a sequence, return all of its equilibrium indices (the result may be empty).
- An index i qualifies when the sum of elements before i equals the sum of elements after i.
- Treat the sum of zero elements (at the boundary) as zero, so index 0 and the last index can qualify.
- Out-of-range positions are not valid indices and must be excluded.
- Assume the sequence may be very long, motivating an efficient (linear) approach.

## Language Coverage
87 languages implement this task, reflecting very broad coverage across imperative, functional, and array-oriented paradigms. Representative implementations include Python, C, C++, Java, Go, Rust, Haskell, J, Julia, and Perl.

## Connections
- [[PrefixSum]] — the standard linear technique: compare a running left sum against total minus current element.
- [[ArrayProcessing]] — the task operates over a one-dimensional sequence of integers.
- [[TimeComplexity]] — distinguishes the naive O(n²) scan from the optimal O(n) single pass.
- [[RunningTotal]] — accumulating partial sums while iterating to test the equilibrium condition.

## Contradictions
- None — reference task page.
