---
title: "Zsigmondy numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zsigmondy_numbers
---

## Summary
The Zsigmondy number Zs(n, a, b) is the greatest divisor of aⁿ − bⁿ that is coprime to aᵐ − bᵐ for every positive integer m < n. The task asks for a routine that computes this sequence for arbitrary radix pairs (a, b). The key insight is that Zs(n, a, b) captures the "new" prime factors first appearing at exponent n; when aⁿ − bⁿ is prime the Zsigmondy number equals that prime, and it can collapse to 1 when no new coprime divisor exists (e.g. Zs(6, 2, 1) = 1).

## Task Requirements
- Write a general function to compute the Zsigmondy number sequence given a radix set (a, b).
- For each n, take aⁿ − bⁿ, enumerate its divisors, and return the largest divisor coprime to all aᵐ − bᵐ for m = 1..n−1 (1 is always a valid divisor).
- Generate at least the first 10 elements for each of the radix sets: (2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (3,2), (5,3), (7,3), and (7,5).

## Language Coverage
27 languages implement this task, spanning systems, scripting, functional, and array-oriented styles. Representative implementations include C, C++, C#, Rust, Zig, Java, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[NumberTheory]] — the task is rooted in the theory of divisors and integer factorization.
- [[GreatestCommonDivisor]] — the coprimality test relies on computing GCDs against earlier terms.
- [[ZsigmondysTheorem]] — guarantees a primitive prime divisor exists for almost all n.
- [[Coprime]] — the defining condition selects divisors sharing no common factor with prior terms.

## Contradictions
- None — reference task page.
