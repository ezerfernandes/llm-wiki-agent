---
title: "Arithmetic/Rational (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic/Rational
---

## Summary
This task asks the programmer to build a reasonably complete rational-number (fraction) arithmetic library using the host language's idioms. The core abstraction is a `frac` type pairing a numerator and denominator, with a full suite of overloaded operators. The key insight is that exact rational arithmetic avoids floating-point rounding error, which the task showcases by detecting perfect numbers exactly via sums of unit reciprocals.

## Task Requirements
- Define a `frac` type via a binary `//` operator over two integers, yielding a numerator/denominator structure.
- Implement unary operators `abs` and negation `-`.
- Implement binary arithmetic: addition, subtraction, multiplication, division, integer division, and modulo.
- Implement comparison operators (`<`, `<=`, `>`, `>=`) and equality operators (`=`, `!=`).
- Provide coercion operators casting `int` to `frac`.
- If space allows, define increment/decrement operators (`+:=`, `-:=`).
- Test by finding all perfect numbers below 2^19 through summing the reciprocals of each number's factors.

## Language Coverage
79 languages implement this task, reflecting broad coverage that spans systems, functional, scripting, and computer-algebra languages. Representative implementations include C, C++, Rust, Haskell, OCaml, Python, Ruby, Perl, Raku, Scheme, Common Lisp, and Mathematica.

## Connections
- [[RationalNumbers]] — the mathematical type the task models exactly
- [[OperatorOverloading]] — the central language-idiom mechanism the task exercises
- [[PerfectNumbers]] — the validation problem solved via reciprocal sums
- [[GreatestCommonDivisor]] — needed to reduce fractions to lowest terms
- [[NumberTheory]] — the domain of perfect numbers and divisor sums

## Contradictions
- None — reference task page.
