---
title: "Cuban primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cuban_primes
---

## Summary
A cuban prime is a prime that equals the difference of two consecutive cubes, i.e. a prime of the form (n+1)³ − n³, which simplifies to 3n² + 3n + 1. The name (coined by A. J. C. Cunningham in 1923) refers to cubes, not the country Cuba. The key insight is that candidates can be generated directly from this closed form rather than scanning every integer, leaving only a primality test to apply.

## Task Requirements
- Show the first 200 cuban primes in a multi-line horizontal format.
- Show the 100,000th cuban prime.
- Display the primes with thousands-separator commas where appropriate.
- Show all output on the page.

## Language Coverage
57 languages implement this task, spanning systems, functional, and scripting families. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Ruby, Perl, Julia, and Wren.

## Connections
- [[PrimeNumbers]] — each candidate must pass a primality test
- [[NumberTheory]] — the task is a classic recreational number-theory exercise
- [[FigurateNumbers]] — values follow the centered hexagonal number form 3n² + 3n + 1
- [[OEIS]] — sequence A002407 catalogs the cuban primes

## Contradictions
- None — reference task page.
