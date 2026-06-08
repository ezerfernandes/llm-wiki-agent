---
title: "Sorting algorithms/Bogosort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, randomness]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Bogosort
---

## Summary
The task is to implement Bogosort, a deliberately inefficient sorting algorithm used mainly as an in-joke. Bogosort repeatedly checks whether a list is in order and, if not, randomly shuffles it, looping until the shuffle happens to produce a sorted sequence. The key insight is that its average runtime is O(n!), since the probability that a random permutation is sorted is roughly 1/n!, and its worst case is unbounded because there is no guarantee a random shuffle ever yields order.

## Task Requirements
- Bogosort a list of numbers.
- Repeatedly: while the list is not in order, shuffle it; stop once sorted.
- The shuffle step may be implemented using a Knuth (Fisher-Yates) shuffle.

## Language Coverage
100 languages implement this task, spanning a very broad cross-section from assembly to scripting languages — including C, C++, C#, Java, Python, Haskell, Rust, Go, Ruby, Common Lisp, Prolog, and AArch64 Assembly.

## Connections
- [[SortingAlgorithms]] — Bogosort is a (joke) member of this family.
- [[KnuthShuffle]] — recommended technique for the random shuffle step.
- [[RandomPermutation]] — each iteration generates one to test for order.
- [[ComputationalComplexity]] — illustrates O(n!) average and unbounded worst-case behavior.

## Contradictions
- None — reference task page.
