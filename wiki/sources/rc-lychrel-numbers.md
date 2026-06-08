---
title: "Lychrel numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Lychrel_numbers
---

## Summary
The task asks the programmer to detect Lychrel number candidates: starting integers that never produce a palindrome under the "reverse-and-add" recurrence (repeatedly add a number to its digit-reversal, checking for a palindrome after each addition). Within a 500-iteration cap over the range 1..10000, candidates must be further classified into true *seed* Lychrels and *related* numbers whose sequences merge into a lower seed's sequence. The key insight is that any number appearing in a Lychrel sequence is itself Lychrel, so deduplicating against seen sequence values separates seeds from relateds.

## Task Requirements
- Implement the reverse-and-add step: n_next = n + reverse(n), testing for a palindrome *after* each addition.
- Treat any n not reaching a palindrome within 500 (or more) iterations as a Lychrel candidate.
- For n in 1..10000 inclusive, find the count of seed Lychrel candidates and the count of related numbers.
- Print the number of seeds, the actual seed values, and just the count of relateds.
- Print any seed or related number that is itself a palindrome.
- Requires arbitrary-precision integers since sequence values grow very large.

## Language Coverage
46 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C++, Rust, Go, Haskell, Java, Python, Julia, Common Lisp, Perl, Raku, and J.

## Connections
- [[Palindrome]] — the termination condition for each sequence.
- [[ReverseAndAdd]] — the core recurrence relation driving the iteration.
- [[NumberTheory]] — Lychrel numbers are an open problem (the 196 conjecture) in this field.
- [[BigInteger]] — arbitrary-precision arithmetic needed as sums grow unbounded.
- [[OEIS]] — sequence A023108 catalogs these candidates.

## Contradictions
- None — reference task page.
