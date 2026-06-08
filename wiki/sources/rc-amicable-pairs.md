---
title: "Amicable pairs (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Amicable_pairs
---

## Summary
The task asks the programmer to find all amicable pairs of integers below 20,000. Two distinct integers N and M form an amicable pair when the sum of the proper divisors of N equals M, and the sum of the proper divisors of M equals N. The key insight is that this reduces to computing a proper-divisor-sum function once per number and then matching numbers whose sums point back at each other (e.g., 1184 and 1210).

## Task Requirements
- For integers below 20,000, compute the sum of proper divisors (all divisors excluding the number itself) for each candidate.
- Identify pairs N != M where sum(propDivs(N)) = M and sum(propDivs(M)) = N.
- Output the eight amicable pairs that exist in this range.

## Language Coverage
119 languages implement this task, giving very broad coverage from low-level assembly through functional and scripting languages. Representative implementations include C, C++, Java, Python, Rust, Go, Haskell, Common Lisp, Perl, Ruby, Julia, and several BASIC and Assembly dialects.

## Connections
- [[NumberTheory]] — amicable pairs are a classical number-theory topic
- [[ProperDivisors]] — the core subroutine the task depends on
- [[DivisorSumFunction]] — sum-of-divisors (sigma/aliquot) computation drives the matching
- [[PerfectNumbers]] — related divisor-sum classification (where the sum equals the number itself)
- [[AliquotSequences]] — amicable pairs are length-2 cycles of the aliquot map

## Contradictions
- None — reference task page.
