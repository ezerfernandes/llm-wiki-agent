---
title: "Abundant, deficient and perfect number classifications (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abundant,_deficient_and_perfect_number_classifications
---

## Summary
This task asks the programmer to classify positive integers by comparing each number to the sum of its proper divisors P(n) — the divisors of n excluding n itself. A number is deficient when P(n) < n, perfect when P(n) == n, and abundant when P(n) > n. The key insight is that all three classifications derive from a single quantity, the aliquot sum, so one divisor-sum routine handles every case.

## Task Requirements
- Define P(n) as the sum of all positive proper divisors of n (every divisor except n itself).
- Classify n as deficient (P(n) < n), perfect (P(n) == n), or abundant (P(n) > n).
- Count how many integers from 1 to 20,000 inclusive fall into each of the three classes.
- Display the three counts.

## Language Coverage
115 languages implement this task, reflecting very broad coverage typical of introductory number-theory exercises. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Ruby, Common Lisp, and REXX.

## Connections
- [[NumberTheory]] — classification depends on divisor structure of integers
- [[ProperDivisors]] — P(n) is the sum of a number's proper divisors
- [[AliquotSum]] — the quantity P(n) is precisely the aliquot sum
- [[PerfectNumber]] — the boundary case where P(n) equals n
- [[DivisorFunction]] — relates to sigma(n) minus n

## Contradictions
- None — reference task page.
