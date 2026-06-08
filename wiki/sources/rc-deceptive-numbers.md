---
title: "Deceptive numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Deceptive_numbers
---

## Summary
A repunit R_n is the number made up of n repeated ones (e.g. R_6 = 111111). Every prime p greater than 5 evenly divides the repunit R_{p-1}; this is a property derived from Fermat's little theorem. Some composite numbers share this property and are called deceptive numbers (or deceptive non-primes). The task is to find composite n such that n evenly divides R_{n-1}.

## Task Requirements
- Find and display at least the first 10 deceptive numbers.
- A deceptive number is a composite n that evenly divides the repunit R_{n-1}.
- The key insight: R_{n-1} = (10^{n-1} - 1) / 9, so divisibility can be tested with modular arithmetic rather than building huge integers.

## Language Coverage
50 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and J.

## Connections
- [[RepunitNumbers]] — the central object being divided
- [[FermatsLittleTheorem]] — explains why primes > 5 divide R_{p-1}
- [[ModularArithmetic]] — used to test divisibility without huge integers
- [[CompositeNumbers]] — deceptive numbers are composites mimicking a prime property
- [[OEIS]] — sequence A000864 catalogs deceptive nonprimes

## Contradictions
- None — reference task page.
