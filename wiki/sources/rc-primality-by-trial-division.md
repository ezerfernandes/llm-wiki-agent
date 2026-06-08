---
title: "Primality by trial division (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Primality_by_trial_division
---

## Summary
This Rosetta Code task asks the programmer to write a boolean function that reports whether a given integer is prime, using trial division. The key insight is that you only need to test candidate divisors up to the square root of n, and even numbers above 2 can be rejected immediately, which keeps the algorithm simple while bounding its work.

## Task Requirements
- Return a boolean indicating whether the input integer is prime.
- Treat 1 and all non-positive numbers as not prime.
- Use trial division as the method.
- Eliminate even numbers greater than 2 right away.
- Looping divisors from 3 up to √n suffices (other loop bounds are allowed).

## Language Coverage
166 languages implement this task, making it one of the most broadly covered entries on the site and spanning everything from assembly to modern functional languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Ada, Lisp, and Fortran.

## Connections
- [[PrimeNumber]] — the property being tested
- [[TrialDivision]] — the algorithm specified by the task
- [[SquareRootBound]] — the optimization limiting divisors to √n
- [[SieveOfEratosthenes]] — an alternative bulk primality method (related task)
- [[PrimeDecomposition]] — a closely related factoring task

## Contradictions
- None — reference task page.
