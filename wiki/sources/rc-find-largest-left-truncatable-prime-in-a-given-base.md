---
title: "Find largest left truncatable prime in a given base (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_largest_left_truncatable_prime_in_a_given_base
---

## Summary
The task asks the programmer to compute, for a given integer base greater than 2, the largest left-truncatable prime: a prime whose every right-aligned substring (the number and all numbers formed by repeatedly chopping digits from the left) is also prime when read in that base. The key insight is that candidates can be built incrementally from the rightmost digit outward — each step prepends a digit in the range 1 to base-1 to existing candidates and keeps only those that remain prime — so the search terminates naturally when no candidate can be extended. The goal is to reproduce as much of OEIS A103443 as possible.

## Task Requirements
- For each base, find the single largest left-truncatable prime expressible in that base.
- A valid number must have all of its right-substrings prime, with the leading digit never zero at any truncation step.
- Build candidates incrementally: start from prime last digits, then prepend digits 1..base-1, retaining only resulting primes, repeating until no extensions remain.
- Reconstruct (and ideally extend) the table of results found in OEIS A103443.

## Language Coverage
33 languages implement this task, spanning systems languages, functional languages, scripting languages, and computer-algebra systems. Representative implementations include C, C++, C#, Go, Rust, Java, Haskell, Python, Perl, Raku, Julia, and PARI/GP, with several relying on big-integer arithmetic and Miller-Rabin primality testing for larger bases.

## Connections
- [[PrimeNumber]] — the values sought and every truncation must satisfy primality
- [[MillerRabinPrimalityTest]] — the probabilistic test most solutions use to check large candidates
- [[NumberBases]] — digits and truncation are interpreted relative to an arbitrary base
- [[BreadthFirstSearch]] — the incremental digit-prepending candidate expansion is a level-by-level search
- [[BigInteger]] — larger bases produce primes far beyond native integer ranges

## Contradictions
- None — reference task page.
