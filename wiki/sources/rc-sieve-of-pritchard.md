---
title: "Sieve of Pritchard (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sieve_of_Pritchard
---

## Summary
The task is to implement the Sieve of Pritchard, a 1981 algorithm for finding all primes up to a limit N. It works by iteratively building "wheels" — repeating patterns of numbers coprime to the first k primes — increasing k until the k-th prime squared reaches N. The key insight is that it examines far fewer composite numbers than the Sieve of Eratosthenes and has better asymptotic time complexity, though its space requirement cannot be reduced, making it impractical for very large limits.

## Task Requirements
- Write a program or subprogram that uses the Sieve of Pritchard algorithm to find all primes up to a specified limit.
- Show the result of running it with a limit of 150.

## Language Coverage
20 languages implement this task, spanning systems, scripting, functional, and array-oriented styles. Representative implementations include C++, C#, Java, Python, Julia, Perl, Raku, Fortran, Pascal, J, and Wren.

## Connections
- [[PrimeNumbers]] — the algorithm enumerates all primes up to N
- [[SieveOfEratosthenes]] — the classic alternative this algorithm improves on asymptotically
- [[WheelFactorization]] — wheels of coprime residues are the core data structure
- [[NumberTheory]] — coprimality and prime-product circumferences underpin the method
- [[AsymptoticComplexity]] — its better time complexity is the main selling point

## Contradictions
- None — reference task page.
