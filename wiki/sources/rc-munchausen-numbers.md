---
title: "Munchausen numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Munchausen_numbers
---

## Summary
A Munchausen number is a natural number that equals the sum of each of its base-10 digits raised to the power of itself (e.g. 3435 = 3³ + 4⁴ + 3³ + 5⁵). The task is to find all such numbers between 1 and 5000. The key insight is that digit-power values (00 conventionally treated as 0) can be precomputed in a small lookup table to avoid repeated exponentiation while scanning candidates.

## Task Requirements
- For each number n, decompose it into its base-10 digits and compute the sum of each digit d raised to the power d (d^d).
- Identify n as Munchausen when that self-powered digit sum equals n itself.
- Find and report all Munchausen numbers in the range 1 to 5000.

## Language Coverage
101 languages implement this task, reflecting very broad coverage across mainstream, functional, and assembly languages. Representative implementations include Python, C, C++, Java, Go, Rust, Haskell, JavaScript, Ruby, and 8080 Assembly.

## Connections
- [[NumberTheory]] — the task is a classic recreational-mathematics digit problem
- [[DigitManipulation]] — requires extracting and processing individual base-10 digits
- [[Exponentiation]] — each digit is raised to the power of itself
- [[NarcissisticNumbers]] — a closely related family of self-referential digit-power numbers
- [[LookupTable]] — precomputing d^d for digits 0–9 is the standard optimization

## Contradictions
- None — reference task page.
