---
title: "Arithmetic numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic_numbers
---

## Summary
An arithmetic number is a positive integer `n` whose positive divisors have an integer average — that is, the sum of its divisors is divisible by the count of its divisors. The task asks the programmer to identify these numbers efficiently. The key insight is that all odd primes qualify (divisors 1 and p sum to an even number), while 2 does not, since the average of {1, 2} is 1.5.

## Task Requirements
- Compute and display the first 100 arithmetic numbers.
- Find the xth arithmetic number for x = 1,000 and x = 10,000.
- Count how many of the first x arithmetic numbers are composite (noting that 1 is neither prime nor composite).
- Stretch goal: repeat steps 2 and 3 for x = 100,000 and x = 1,000,000.

## Language Coverage
61 languages implement this task, spanning systems languages, scripting languages, functional languages, and assembly. Representative implementations include C, C++, Rust, Go, Python, Haskell, Julia, Raku, Java, and ARM Assembly.

## Connections
- [[NumberTheory]] — the task is rooted in divisor properties of integers
- [[Divisors]] — requires enumerating and summing the divisors of each candidate
- [[SumOfDivisors]] — the sigma function determines arithmetic-ness when divisible by the divisor count
- [[PrimeNumbers]] — odd primes are always arithmetic, and primality classifies composites for the count
- [[OEIS]] — corresponds to sequence A003601

## Contradictions
- None — reference task page.
