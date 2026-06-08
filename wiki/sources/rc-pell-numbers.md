---
title: "Pell numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequences, recurrence-relations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pell_numbers
---

## Summary
Pell numbers are an infinite integer sequence (0, 1, 2, 5, 12, 29, 70, ...) defined by the recurrence Pₙ = 2·Pₙ₋₁ + Pₙ₋₂, and they form the denominators of the best rational approximations to √2. The companion Pell-Lucas numbers (2, 2, 6, 14, 34, ...) share the same recurrence but with different seed values, and half of each supplies the matching numerators. The task explores how this one sequence interlinks with √2 convergents, prime detection, NSW numbers, and near-isosceles Pythagorean triples.

## Task Requirements
- Find and show at least the first 10 Pell numbers.
- Find and show at least the first 10 Pell-Lucas (companion) numbers.
- Use the Pell (and optionally Pell-Lucas) numbers to show at least the first 10 rational approximations to √2, in both rational and decimal form.
- Find and show at least the first 10 Pell primes (Pell numbers that are prime).
- Find and show at least the first 10 indices of Pell primes.
- Find and show at least the first 10 Newman-Shank-Williams (NSW) numbers, formed by sums P₂ₙ + P₂ₙ₊₁.
- Find and show at least the first 10 Pythagorean triples for near-isosceles right triangles (legs differing by exactly 1, e.g. (3,4,5), (20,21,29)).

## Language Coverage
24 languages implement this task, spanning systems, functional, array, and scripting paradigms. Representative implementations include ALGOL 68, Common Lisp, Go, Haskell, Java, Julia, Python, Perl, Raku, Wren, J, and Phix. Big-integer support is helpful since the sequences grow quickly.

## Connections
- [[RecurrenceRelations]] — Pell and Pell-Lucas are both linear second-order recurrences.
- [[ContinuedFractions]] — Pell numbers generate the convergents of √2's continued fraction expansion.
- [[IntegerSequences]] — registered in OEIS as A000129, A002203, A001333, and related.
- [[PrimalityTesting]] — required to identify Pell primes and their indices.
- [[PythagoreanTriples]] — Pell numbers enumerate near-isosceles right triangles.

## Contradictions
- None — reference task page.
