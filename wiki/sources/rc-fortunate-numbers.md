---
title: "Fortunate numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fortunate_numbers
---

## Summary
A Fortunate number is the smallest integer m > 1 such that primorial(n) + m is prime, where primorial(n) is the product of the first n primes. The task is to compute Fortunate numbers across successive n, then sort the results and remove duplicates. The key insight is that the search reduces to primality testing of large primorial-plus-offset candidates, which favors languages with big-integer support.

## Task Requirements
- For each positive integer n, compute primorial(n) = product of the first n prime numbers.
- Find the smallest m > 1 for which primorial(n) + m is prime; that m is the Fortunate number for n.
- Sort all computed Fortunate numbers and remove duplicates.
- Show the first 8 Fortunate numbers, or the first 50 if the language supports big integers.

## Language Coverage
26 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, C#, Go, Java, Haskell, Julia, Python, Perl, Raku, and Wren.

## Connections
- [[Primorial]] — the core quantity each candidate is built from
- [[PrimeNumbers]] — Fortunate numbers are defined via primality
- [[PrimalityTest]] — finding the smallest m requires testing many candidates
- [[BigIntegerArithmetic]] — primorials grow rapidly, needing arbitrary precision for n=50
- [[NumberTheory]] — the broader mathematical domain of the task

## Contradictions
- None — reference task page.
