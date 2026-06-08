---
title: "Proper divisors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Proper_divisors
---

## Summary
The proper divisors of a positive integer N are all the numbers other than N itself that divide N evenly. For N greater than 1 they always include 1, while N == 1 has none. The task is to write a routine that generates these divisors and then apply it to two reporting problems. A practical insight is that divisors come in pairs around the square root, so a count can be found efficiently by iterating only up to sqrt(N).

## Task Requirements
- Create a routine that generates all proper divisors of a number.
- Use it to show the proper divisors of each number from 1 to 10 inclusive.
- Find the number in the range 1 to 20,000 that has the most proper divisors, showing both the number and the count of its proper divisors.
- Show all output.

## Language Coverage
95 languages implement this task, spanning systems, scripting, functional, array, and assembly families. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, J, Julia, and REXX.

## Connections
- [[Divisor]] — proper divisors are all divisors of N excluding N itself.
- [[NumberTheory]] — the task is a foundational divisor-counting exercise.
- [[HighlyCompositeNumber]] — finding the integer with the most divisors in a range relates to highly composite numbers.
- [[PerfectNumber]] — proper-divisor sums underlie perfect, abundant, and deficient classifications.
- [[Factorization]] — generating divisors is closely tied to integer factorization.

## Contradictions
- None — reference task page.
