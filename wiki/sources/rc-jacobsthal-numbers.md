---
title: "Jacobsthal numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequences, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jacobsthal_numbers
---

## Summary
The task asks the programmer to generate Jacobsthal numbers, an integer sequence akin to Fibonacci but where each term equals the previous term plus twice the term before that (J0=0, J1=1, Jn = Jn-1 + 2*Jn-2). The key insight is that, like Fibonacci, terms can be computed directly via a closed-form formula — Jn = (2^n - (-1)^n) / 3 — rather than only by recurrence. The task also covers three related variants: Jacobsthal-Lucas numbers (same recurrence, starting value J0=2, closed form 2^n + (-1)^n), Jacobsthal oblong numbers (each term times its successor), and Jacobsthal primes.

## Task Requirements
- Find and display the first 30 Jacobsthal numbers.
- Find and display the first 30 Jacobsthal-Lucas numbers.
- Find and display the first 20 Jacobsthal oblong numbers (Jn * Jn+1).
- Find and display at least the first 10 Jacobsthal primes (Jacobsthal numbers that are prime).

## Language Coverage
54 languages implement this task, spanning systems, scripting, functional, and array-oriented paradigms. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wren.

## Connections
- [[IntegerSequences]] — Jacobsthal numbers are a named OEIS sequence (A001045)
- [[FibonacciSequence]] — directly analogous recurrence-defined sequence
- [[Recursion]] — the sequence is naturally defined by a two-term linear recurrence
- [[PrimeNumbers]] — the Jacobsthal primes subtask requires primality testing
- [[ClosedFormExpression]] — terms admit a direct non-recursive formula

## Contradictions
- None — reference task page.
