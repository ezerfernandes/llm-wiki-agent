---
title: "Count in factors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Count_in_factors
---

## Summary
The task asks the programmer to count upward from 1 and display each integer as the product of its prime factors (e.g. 6 shown as 2×3, 2144 shown as 2×2×2×2×2×67). Primes are displayed as themselves, and 1 (unity) may be shown as itself. The core insight is that every integer above 1 has a unique prime factorization, so the program repeatedly extracts prime factors of each successive number.

## Task Requirements
- Count up starting from 1.
- For each number, display it as the multiplication of its prime factors.
- A prime number is shown as itself; 1 may be shown as itself.

## Language Coverage
97 languages implement this task, giving very broad coverage across paradigms from low-level assembly to functional and scripting languages. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Ruby, Common Lisp, and REXX.

## Connections
- [[PrimeFactorization]] — the central operation each number undergoes
- [[PrimeNumber]] — primes are the building blocks and the base display case
- [[TrialDivision]] — common algorithm for extracting prime factors
- [[NumberTheory]] — domain grounding the fundamental theorem of arithmetic

## Contradictions
- None — reference task page.
