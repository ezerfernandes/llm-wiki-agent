---
title: "Super-Poulet numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Super-Poulet_numbers
---

## Summary
A super-Poulet number is a Poulet number (a Fermat pseudoprime to base 2, i.e. a composite n that divides 2^n − 2) with the stronger property that *every* divisor d of n itself divides 2^d − 2. The task asks the programmer to identify these numbers and recognize that the super-Poulet condition is a refinement applied across all divisors, not just n itself.

## Task Requirements
- Find and display the first 20 super-Poulet numbers.
- Stretch goal: find and display the index and value of the first super-Poulet number greater than one million.

## Language Coverage
23 languages implement this task, giving solid coverage across systems, functional, and scripting families. Representative implementations include Ada, ALGOL 68, C++, Java, Python, Julia, Perl, Raku, Ruby, Lua, Nim, and Wren.

## Connections
- [[FermatPseudoprime]] — super-Poulet numbers are a special class of base-2 Fermat pseudoprimes
- [[PouletNumber]] — the broader set from which these are filtered
- [[ModularExponentiation]] — efficient computation of 2^d mod d for the divisibility check
- [[NumberTheory]] — the task lives in divisibility and pseudoprime theory
- [[DivisorFunction]] — the defining test enumerates all divisors of each candidate

## Contradictions
- None — reference task page.
