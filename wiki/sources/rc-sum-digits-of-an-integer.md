---
title: "Sum digits of an integer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, radix]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sum_digits_of_an_integer
---

## Summary
The task asks the programmer to take a natural number expressed in a given base (radix) and return the sum of its digits. The key insight is that summing digits is base-dependent: the same value yields different digit sums in different bases, so the algorithm repeatedly extracts digits via integer division and modulo by the base.

## Task Requirements
- Accept a natural number and a base (radix) in which it is represented.
- Return the sum of the number's digits in that base.
- Support bases beyond 10 (hexadecimal examples given), so digit values can exceed 9.
- Worked examples: 1₁₀ → 1; 1234₁₀ → 10; fe₁₆ → 29; f0e₁₆ → 29.

## Language Coverage
129 languages implement this task, reflecting very broad coverage across assembly, functional, scripting, and esoteric language families. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Perl, Raku, and APL.

## Connections
- [[NumberBase]] — digit extraction depends entirely on the chosen radix.
- [[ModularArithmetic]] — digits are obtained via modulo and integer division by the base.
- [[DigitalRoot]] — repeated digit summing collapses to a related single-digit invariant.
- [[NumberTheory]] — digit sums underpin divisibility rules and casting out nines.

## Contradictions
- None — reference task page.
