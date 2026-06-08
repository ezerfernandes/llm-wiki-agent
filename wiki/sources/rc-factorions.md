---
title: "Factorions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Factorions
---

## Summary
A factorion is a natural number that equals the sum of the factorials of its digits (for example, 145 = 1! + 4! + 5!). The task asks the programmer to find and print all factorions in several number bases. The key insight is that for base 10 no factorion can exceed 1,499,999, which bounds the search to a finite, tractable range rather than an open-ended scan.

## Task Requirements
- Compute the digit-factorial sum of a number in a given base and test whether it equals the original number.
- Demonstrate there are 3 factorions in base 9.
- Demonstrate there are 4 factorions in base 10.
- Demonstrate there are 5 factorions in base 11.
- Demonstrate there are 2 factorions in base 12 (using the same upper bound as base 10).
- Print out the factorions found for each base.

## Language Coverage
55 languages implement this task, spanning systems languages, scripting languages, functional languages, and array/stack languages — for example C, C++, Go, Rust-style BASIC dialects, Java, JavaScript, Python, Haskell, Julia, Raku, and J.

## Connections
- [[Factorial]] — each digit's factorial is summed
- [[NumberTheory]] — factorions are a number-theoretic curiosity
- [[RadixConversion]] — digits are extracted relative to an arbitrary base
- [[DigitManipulation]] — the core operation decomposes a number into its digits
- [[NarcissisticNumbers]] — a related family of self-referential number definitions

## Contradictions
- None — reference task page.
