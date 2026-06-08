---
title: "Fractran (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, esoteric-language, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fractran
---

## Summary
FRACTRAN is a Turing-complete esoteric language invented by John Horton Conway in which a program is just an ordered list of positive fractions plus a starting integer n. At each step, n is multiplied by the first fraction in the list that yields an integer, and that product becomes the new n; execution halts when no fraction produces an integer. The task is to parse a list of fractions and run this simple register-machine-like interpreter, with a step limit. The key insight is that prime factorizations of n act as registers, so multiplying by fractions adds and removes prime exponents to perform arithmetic.

## Task Requirements
- Read a list of fractions in a natural format (keyboard or string) and parse each into two integers (numerator/denominator).
- Run the FRACTRAN program starting from a provided integer, printing n at each step.
- Limit the number of steps via an easily-tunable parameter.
- Extra credit: use Conway's 14-fraction PRIMEGAME program (starting at n=2) to derive the first ~20 prime numbers, which appear as the powers of 2 in the generated sequence.

## Language Coverage
66 languages implement this task, spanning low-level assembly through esoteric and functional styles. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, Julia, and Befunge.

## Connections
- [[EsotericProgrammingLanguage]] — FRACTRAN is a minimal esoteric language.
- [[TuringCompleteness]] — the language is provably Turing-complete.
- [[PrimeFactorization]] — prime exponents of n serve as the machine's registers.
- [[RegisterMachine]] — fraction multiplication models register increment/decrement.
- [[PrimeNumbers]] — Conway's PRIMEGAME emits primes as powers of 2.

## Contradictions
- None — reference task page.
