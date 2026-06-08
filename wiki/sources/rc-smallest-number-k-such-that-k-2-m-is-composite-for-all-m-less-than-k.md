---
title: "Smallest number k such that k+2^m is composite for all m less than k (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Smallest_number_k_such_that_k+2^m_is_composite_for_all_m_less_than_k
---

## Summary
This task asks for the sequence of integers k where, for every positive integer m less than k, the value k + 2^m is composite (never prime). The key insight is that only odd k need to be tested, since any even number plus a positive power of 2 is always even and therefore composite. The sequence corresponds to OEIS A033919.

## Task Requirements
- For each candidate k, test every positive integer m with m < k.
- A candidate qualifies only if k + 2^m is composite for all such m (if any k + 2^m is prime, the candidate fails).
- Only odd k need to be checked (even k trivially yield composites).
- Find and display the first 5 elements of the sequence.

## Language Coverage
17 languages implement this task, a moderate breadth spanning compiled, scripting, and mathematical languages. Representative implementations include Ada, ALGOL 68, Go, Java, Julia, Mathematica/Wolfram Language, Nim, Perl, Python, Raku, and Wren.

## Connections
- [[NumberTheory]] — the task is grounded in properties of integers and powers of two.
- [[PrimalityTesting]] — each candidate requires testing whether k + 2^m is prime or composite.
- [[CompositeNumbers]] — the qualifying condition is universal compositeness across the tested range.
- [[IntegerSequences]] — the output is the OEIS A033919 sequence.

## Contradictions
- None — reference task page.
