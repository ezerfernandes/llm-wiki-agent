---
title: "Honaker primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Honaker_primes
---

## Summary
A Honaker prime is a prime number whose digital sum (sum of its decimal digits) equals the digital sum of its position (1-based index) within the ordered sequence of primes. The task asks the programmer to write a routine that tests this property and to apply it to enumerate Honaker primes. For example, the prime 131 sits at position 32; both 1+3+1 and 3+2 equal 5, making 131 a Honaker prime, whereas the first prime 2 (position 1) is not.

## Task Requirements
- Write a routine that identifies whether a prime qualifies as a Honaker prime (its digit sum equals the digit sum of its prime-sequence position).
- Use that routine to find the first fifty Honaker primes, displaying both the position and value of each.
- Stretch goal: find and display the ten-thousandth Honaker prime, showing its position and value.

## Language Coverage
53 languages implement this task, reflecting broad coverage spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[PrimeNumbers]] — the task generates and indexes the sequence of primes
- [[DigitalRoot]] — built on repeated digit-sum operations over base-10 representations
- [[SieveOfEratosthenes]] — a common technique for enumerating the primes efficiently, especially for the stretch goal
- [[NumberTheory]] — the broader domain of integer properties this puzzle belongs to

## Contradictions
- None — reference task page.
