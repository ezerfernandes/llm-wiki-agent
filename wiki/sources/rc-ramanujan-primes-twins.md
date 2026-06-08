---
title: "Ramanujan primes/twins (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ramanujan_primes/twins
---

## Summary
This task asks the programmer to generate Ramanujan primes and then, by analogy with ordinary twin primes, count how many of the first million Ramanujan primes form "twins" — i.e. pairs of consecutive Ramanujan primes differing by exactly 2. A Ramanujan prime is the smallest integer R(n) such that for all x ≥ R(n) there are at least n primes in the interval (x/2, x]; the key challenge is generating them efficiently before scanning the sequence for adjacent values two apart.

## Task Requirements
- Generate the first one million Ramanujan primes.
- Determine how many of those are "twins" — consecutive Ramanujan primes whose difference is 2.
- Report the resulting count.

## Language Coverage
20 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C++, Go, Rust, Nim, Java, Julia, Python, Perl, Raku, J, and Wren.

## Connections
- [[RamanujanPrime]] — the central object the task generates and counts.
- [[TwinPrimes]] — the analogy and the explicitly named related task defining the "differ by 2" twin condition.
- [[PrimeNumbers]] — the underlying objects counted within the (x/2, x] intervals.
- [[SieveOfEratosthenes]] — common technique for generating the prime base needed to compute Ramanujan primes.
- [[NumberTheory]] — the mathematical domain of prime-counting and prime gaps.

## Contradictions
- None — reference task page.
