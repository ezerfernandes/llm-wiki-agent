---
title: "Miller-Rabin primality test (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Miller-Rabin_primality_test
---

## Summary
The task asks the programmer to implement the Miller-Rabin primality test, a probabilistic algorithm (as modified by Michael O. Rabin to avoid relying on the generalized Riemann hypothesis) that decides whether a given odd integer n > 2 is composite or probably prime. The key insight is to write n − 1 as 2^s · d with d odd, then repeatedly pick a random witness a and check whether modular exponentiation a^d mod n and its successive squarings ever reveal a nontrivial square root of 1, which would prove n composite.

## Task Requirements
- Implement the probabilistic Miller-Rabin test taking n (odd, > 2) and an accuracy parameter k (number of rounds).
- Factor n − 1 into 2^s · d with d odd.
- For each of k rounds: pick a random witness a in [2, n − 1], compute x = a^d mod n, and through up to s − 1 squarings determine "composite" or continue to the next round.
- Return "composite" or "probably prime" accordingly.
- Use of big-number libraries is suggested but not mandatory; deterministic variants are an optional extra.

## Language Coverage
77 languages implement this task, spanning systems languages, functional languages, scripting languages, and even raw assembly. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Perl, Raku, Julia, and AArch64 Assembly.

## Connections
- [[PrimalityTest]] — Miller-Rabin is one of the most widely used primality tests.
- [[ModularExponentiation]] — the core operation computing a^d mod n efficiently.
- [[ProbabilisticAlgorithm]] — the test is randomized, returning "probably prime" with bounded error.
- [[FermatLittleTheorem]] — the test refines Fermat's primality test by checking nontrivial square roots of unity.
- [[BigInteger]] — arbitrary-precision arithmetic is suggested for the large numbers involved.

## Contradictions
- None — reference task page.
