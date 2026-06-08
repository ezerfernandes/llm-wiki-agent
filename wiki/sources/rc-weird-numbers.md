---
title: "Weird numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Weird_numbers
---

## Summary
A weird number is a natural number that is abundant (the sum of its proper divisors exceeds the number) but not semiperfect (no subset of those proper divisors sums to the number itself). The task is to find and display the first 25 weird numbers. The key insight is combining a divisor-sum test for abundance with a subset-sum search to rule out semiperfectness.

## Task Requirements
- For each candidate number, compute its proper divisors (1 and other divisors, excluding the number itself).
- Confirm the number is abundant: the sum of proper divisors is strictly greater than the number.
- Confirm it is not semiperfect: no subset of the proper divisors sums exactly to the number.
- Find and display the first 25 numbers satisfying both conditions (e.g., 70, 836, 4030, ...).

## Language Coverage
43 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Go, Julia, Perl, Raku, and J.

## Connections
- [[NumberTheory]] — weird numbers are a classification within divisor theory
- [[AbundantNumbers]] — abundance is a prerequisite condition for being weird
- [[SubsetSum]] — testing for semiperfectness requires a subset-sum search over proper divisors
- [[Divisors]] — the task hinges on enumerating proper divisors

## Contradictions
- None — reference task page.
