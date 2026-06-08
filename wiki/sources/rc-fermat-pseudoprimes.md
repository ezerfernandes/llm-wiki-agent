---
title: "Fermat pseudoprimes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fermat_pseudoprimes
---

## Summary
A Fermat pseudoprime is a composite integer that nonetheless passes the Fermat primality test for some base, meaning it falsely "looks prime." For a base a > 1, a composite x is a Fermat pseudoprime to base a when x evenly divides a^(x−1) − 1, the divisibility relation that Fermat's little theorem guarantees for genuine primes. The task asks the programmer to enumerate these counterexamples across multiple bases, exposing the limits of probabilistic primality testing.

## Task Requirements
- For each base integer a from 1 through 20: count the Fermat pseudoprimes up to and including 12,000.
- For each base, also display the first 20 pseudoprimes found.
- Note: base a = 1 degenerates to returning all composite numbers.
- Stretch goal: extend the count threshold to 25,000, 50,000, or higher.

## Language Coverage
30 languages implement this task, spanning systems languages, functional languages, and array/CAS tools. Representative implementations include Ada, ALGOL 68, C++, Go, Java, Julia, Python, Perl, Raku, Wren, J, and Mathematica/Wolfram Language.

## Connections
- [[FermatsLittleTheorem]] — the congruence whose failure for composites defines these numbers
- [[PrimalityTesting]] — the broader problem the Fermat test addresses
- [[ModularExponentiation]] — required to compute a^(x−1) mod x efficiently
- [[NumberTheory]] — the mathematical domain of the task
- [[CarmichaelNumbers]] — composites that are Fermat pseudoprimes to every coprime base

## Contradictions
- None — reference task page.
