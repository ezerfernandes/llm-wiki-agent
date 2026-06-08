---
title: "Sphenic numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sphenic_numbers
---

## Summary
The task asks the programmer to identify sphenic numbers — positive integers that are the product of exactly three distinct prime numbers (e.g. 30 = 2 x 3 x 5), making them square-free 3-almost primes. It also introduces sphenic triplets, runs of three consecutive sphenic numbers (e.g. 1309, 1310, 1311). A key insight is that sphenic quadruplets are impossible, since every fourth consecutive integer is divisible by 4 and thus cannot have distinct prime factors.

## Task Requirements
- List all sphenic numbers less than 1,000.
- List all sphenic triplets less than 10,000.
- Stretch: count sphenic numbers below 1 million.
- Stretch: count sphenic triplets below 1 million.
- Stretch: find the 200,000th sphenic number and its three prime factors.
- Stretch: find the 5,000th sphenic triplet.

## Language Coverage
28 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, C#, Java, Python, Go, Julia, Perl, Raku, Ruby, J, and Wren.

## Connections
- [[PrimeFactorization]] — each candidate must be decomposed into its prime factors
- [[SquareFreeIntegers]] — sphenic numbers are a subset of square-free integers
- [[AlmostPrime]] — sphenic numbers are exactly the square-free 3-almost primes
- [[SieveOfEratosthenes]] — efficient factor counting over a range typically uses a sieve
- [[NumberTheory]] — the task is rooted in multiplicative structure of integers

## Contradictions
- None — reference task page.
