---
title: "Permutations/Rank of a permutation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Permutations/Rank_of_a_permutation
---

## Summary
This task defines a bijective ranking between the integers `0 .. n!-1` and the orderings of all permutations of `0 .. n-1`. The programmer must build a function that turns a rank into a permutation (unranking) and its inverse that turns a permutation into its rank. The key insight is that such pairs of functions let you sample large numbers of distinct random permutations of many items without ever enumerating the factorially many permutations, which quickly exceeds the range of 32-bit (`12!`) and 64-bit (`20!`) integers.

## Task Requirements
- Create a function to generate a permutation from a given rank (unrank).
- Create the inverse function that, given a permutation, generates its rank.
- Demonstrate for `n=3` that the two functions are inverses of each other.
- Compute and show 4 random, individual sample permutations of 12 objects.
- Stretch goal: comment on whether the program could feasibly generate one million distinct random permutations of 144 items (the motivating Stack Overflow problem).

## Language Coverage
29 languages implement this task, spanning systems languages, functional languages, and array/CAS environments. Representative implementations include C, C++, D, Go, Haskell, Java, Julia, Python, Perl, Raku, J, and Wren.

## Connections
- [[Permutation]] — the combinatorial object being ranked and unranked
- [[Factorial]] — `n!` bounds the rank space and drives the factorial-base decomposition
- [[FactorialNumberSystem]] — the Lehmer-code/factoradic representation underlying lexicographic ranking
- [[CombinatorialEnumeration]] — ranking/unranking as a way to index a combinatorial set
- [[RandomSampling]] — using ranks to draw distinct random permutations without full enumeration

## Contradictions
- None — reference task page.
