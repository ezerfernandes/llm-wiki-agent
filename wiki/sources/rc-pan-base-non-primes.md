---
title: "Pan base non-primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pan_base_non-primes
---

## Summary
A decimal numeric string can be reinterpreted as a number in many different radices, and in most cases it will be prime in at least one of those bases. A "pan-base non-prime" is a decimal numeric string that is composite (never prime) in every base in which it is a valid number. The key insight is that you only need to test bases up to N: if a string N is composite in every base up to base N, it is composite in all bases, which makes the search finite. Strings ending in 0 (except "10"), and strings whose digits share a GCD greater than 1, are always composite.

## Task Requirements
- Find and display the first 40 pan-base non-prime decimal numeric strings.
- Find and display the first 20 odd pan-base non-prime decimal numeric strings.
- Count pan-base non-prime decimal numeric strings up to at least the string "1000".
- Report what percentage of those are odd versus even (even ones are far more prevalent).
- Treat the digit "1" as a special case (neither prime nor composite); excluding it is conventional.

## Language Coverage
20 languages implement this task, a moderate spread across systems, scripting, and array/math-oriented languages. Representative implementations include C, C++, Java, Python, Julia, Perl, Raku, Ruby, Nim, J, PARI/GP, and Wren.

## Connections
- [[PrimeNumbers]] — primality testing of strings reinterpreted across radices
- [[RadixRepresentation]] — interpreting the same digit string in multiple bases
- [[GreatestCommonDivisor]] — shared-digit GCD test forces compositeness
- [[NumberTheory]] — the underlying domain of the task
- [[OEIS]] — sequence A121719 catalogs these strings

## Contradictions
- None — reference task page.
