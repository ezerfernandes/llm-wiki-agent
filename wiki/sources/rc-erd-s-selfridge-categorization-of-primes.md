---
title: "Erdös-Selfridge categorization of primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Erdös-Selfridge_categorization_of_primes
---

## Summary
This task implements the Erdös-Selfridge categorization of prime numbers, a recursive classification based on the prime factors of p+1. A prime p is category 1 if every prime factor of p+1 is 2 or 3; more generally p is in category g when all prime factors of p+1 belong to categories 1 through g-1. The key insight is that each prime's category is defined recursively in terms of the categories already assigned to smaller primes, so categories can be computed incrementally while sieving.

## Task Requirements
- Categorize a prime p by the categories of the prime factors of p+1 (category 1 = factors only 2 and/or 3; category g = all factors in categories 1..g-1).
- Display the first 200 primes grouped under their assigned category.
- Assign the first one million primes to their categories.
- For each category, report the smallest prime, the largest prime, and the count of primes allocated to that category.

## Language Coverage
20 languages implement this task, giving moderate breadth across systems, functional, and scripting families. Representative implementations include C++, Go, Rust, Nim, Java, JavaScript, Python, Julia, Perl, Raku, F#, Factor, and Wren.

## Connections
- [[PrimeNumbers]] — the objects being categorized
- [[IntegerFactorization]] — categorization depends on the prime factors of p+1
- [[SieveOfEratosthenes]] — efficient generation of the first million primes
- [[Recursion]] — categories are defined recursively over smaller primes
- [[NumberTheory]] — the broader field this classification belongs to

## Contradictions
- None — reference task page.
