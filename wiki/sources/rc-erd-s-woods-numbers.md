---
title: "Erdős–Woods numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, gcd]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Erdős–Woods_numbers
---

## Summary
A positive integer k is an Erdős–Woods number if some positive integer a exists such that every element of the consecutive sequence (a, a+1, ..., a+k) shares a non-trivial common factor with at least one of the two endpoints a or a+k. The task is to find these numbers and, for each, the smallest qualifying starting value a. The key insight is checking, for each interior integer, whether gcd with either endpoint exceeds 1.

## Task Requirements
- Compute and display the first 20 Erdős–Woods numbers together with the smallest corresponding value of a.
- For each candidate k, search for an a where every i in [0, k] satisfies gcd(a, a+i) > 1 or gcd(a+i, a+k) > 1.
- If the language lacks arbitrary-precision arithmetic, show as many as feasible.
- Extra credit: do the same for the next 20 Erdős–Woods numbers.
- Note: the first example is k = 16 with smallest a = 2184; all task-relevant numbers are even, though odd ones (first being 903) exist.

## Language Coverage
13 languages implement this task, a moderate spread across compiled, scripting, and CAS environments. Representative implementations include Go, Java, JavaScript, Julia, Python, Perl, Raku, Phix, Scala, Mathematica/Wolfram Language, and Wren.

## Connections
- [[NumberTheory]] — the task is rooted in divisibility and prime-factor structure of integer sequences.
- [[GreatestCommonDivisor]] — the core test relies on computing gcd against the endpoints.
- [[PrimeFactorization]] — endpoint factorizations determine which interior integers are covered.
- [[BruteForceSearch]] — finding the smallest a involves scanning candidate starting points.

## Contradictions
- None — reference task page.
