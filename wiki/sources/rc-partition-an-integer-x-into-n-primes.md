---
title: "Partition an integer x into n primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Partition_an_integer_x_into_n_primes
---

## Summary
The task is to express a positive integer X as a sum of exactly N distinct prime numbers, returning the unique primes in ascending order. When multiple decompositions exist, the lowest primes possible should be chosen (e.g. 18 = 5+13, not 7+11). The core insight is a combinatorial search over distinct primes — a recursive/backtracking selection of N primes whose sum equals X — which is closely related to integer factoring.

## Task Requirements
- Partition a positive integer X into N distinct primes that sum to X.
- Show the sum X and the N primes in ascending order, separated by plus signs.
- Compute the required examples: 99809 (1 prime), 18 (2), 19 (3), 20 (4), 2017 (24), 22699 (with 1, 2, 3, and 4 primes), and 40355 (3 primes).
- Prefer the lowest primes possible; only one solution per case needs to be shown.
- Input validation is not required.

## Language Coverage
52 languages implement this task, giving broad coverage across systems, functional, scripting, and array-oriented paradigms. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, J, and APL.

## Connections
- [[PrimeNumbers]] — the partition elements must all be prime.
- [[Backtracking]] — the distinct-prime selection is a recursive backtracking search.
- [[Combinatorics]] — choosing N distinct primes summing to X is a subset-sum / combinatorial problem.
- [[SubsetSum]] — finding a subset of primes with a target sum.
- [[SieveOfEratosthenes]] — a common way to generate the candidate primes.

## Contradictions
- None — reference task page.
