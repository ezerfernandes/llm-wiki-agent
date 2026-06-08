---
title: "Perfect shuffle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, permutations, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Perfect_shuffle
---

## Summary
A perfect shuffle (also called a faro or weave shuffle) splits an even-sized deck into two equal halves and perfectly interleaves them, taking one card from the left half, then one from the right, and so on. Repeating the shuffle eventually returns the deck to its original order, and the task is to count how many shuffles that takes for various deck sizes. The key insight is that this count is the multiplicative order of 2 modulo (n−1) for the "out-shuffle" variant, so the answer depends only on the deck size, not the card contents.

## Task Requirements
- Write a function that performs a perfect shuffle on an even-sized list of unique values.
- Repeatedly apply the function and count the shuffles needed to restore the original order.
- Run this for the listed deck sizes and print the resulting counts.
- Test cases: 8→3, 24→11, 52→8, 100→30, 1020→1018, 1024→10, 10000→300.

## Language Coverage
65 languages implement this task, spanning systems languages, scripting languages, functional languages, and array languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, J, APL, and Raku.

## Connections
- [[Permutations]] — each shuffle is a fixed permutation of deck positions.
- [[MultiplicativeOrder]] — shuffle count equals the order of 2 modulo (n−1).
- [[ModularArithmetic]] — position mapping is computed mod (n−1).
- [[Combinatorics]] — broader field of the faro/weave shuffle problem.
- [[ArrayManipulation]] — the core operation is interleaving two list halves.

## Contradictions
- None — reference task page.
