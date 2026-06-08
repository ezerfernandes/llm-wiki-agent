---
title: "Composite numbers k with no single digit factors whose factors are all substrings of k (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Composite_numbers_k_with_no_single_digit_factors_whose_factors_are_all_substrings_of_k
---

## Summary
This Rosetta Code task asks the programmer to find composite numbers k in base 10 that satisfy two conditions: none of their prime factors is a single-digit prime (so no factor of 2, 3, 5, or 7), and every prime factor, written in decimal, appears as a substring of k itself. The key insight is combining integer factorization with a textual substring search over the decimal representation, blending number theory with string handling.

## Task Requirements
- Find and display the first ten elements of the sequence on the page.
- A qualifying k must be composite.
- k must have no single-digit prime factors (i.e., not divisible by 2, 3, 5, or 7).
- Each prime factor of k, in base 10, must occur as a substring of k's decimal digits.
- Stretch goal: find and show the next ten elements.

## Language Coverage
31 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative entries include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, Nim, and Wren.

## Connections
- [[PrimeFactorization]] — each candidate must be factored to obtain its prime factors.
- [[NumberTheory]] — the task is built around composite numbers and prime divisibility.
- [[StringProcessing]] — factors are matched as substrings of the decimal representation.
- [[SubstringSearch]] — testing whether a factor's digits appear within k.
- [[IntegerSequences]] — the output forms an enumerated sequence of qualifying integers.

## Contradictions
- None — reference task page.
