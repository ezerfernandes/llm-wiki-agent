---
title: "Prime numbers whose neighboring pairs are tetraprimes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, integer-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Prime_numbers_whose_neighboring_pairs_are_tetraprimes
---

## Summary
This task asks the programmer to find primes whose adjacent pair of consecutive integers are both tetraprimes — integers equal to the product of four distinct primes (e.g. 1155 = 3·5·7·11). A neighboring pair is the two consecutive numbers immediately preceding or following a prime; the key work is an efficient factorization/sieve routine that detects exactly-four-distinct-prime-factor numbers and scans large ranges.

## Task Requirements
- Define a tetraprime as a positive integer that is the product of four distinct primes.
- Find primes below 100,000 whose two preceding consecutive numbers are both tetraprimes.
- Find primes below 100,000 whose two following consecutive numbers are both tetraprimes.
- Count how many of those primes have a neighboring-pair member with a prime factor of 7.
- For those primes, report the minimum, median, and maximum gaps between consecutive primes.
- Repeat the calculations below 1 million (showing only counts for parts 1 and 2).
- Stretch goal: repeat for all primes below 10 million.

## Language Coverage
23 languages implement this task, spanning systems languages, scripting languages, and array/functional languages. Representative entries include C, C++, C#, Go, Java, Julia, Python, Perl, Raku, J, and Wren.

## Connections
- [[PrimeNumbers]] — the task centers on primality and prime neighbors.
- [[IntegerFactorization]] — detecting tetraprimes requires factoring into distinct primes.
- [[SieveOfEratosthenes]] — an efficient sieve underlies scanning ranges up to 10 million.
- [[NumberTheory]] — the broader domain of the multiplicative structure of integers.

## Contradictions
- None — reference task page.
