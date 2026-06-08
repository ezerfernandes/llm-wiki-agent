---
title: "Wieferich primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wieferich_primes
---

## Summary
A Wieferich prime is a prime p whose square p² evenly divides 2^(p−1) − 1. The task is to write a routine that detects such primes and use it to list all Wieferich primes below 5000. The key insight is that this is a strengthening of Fermat's little theorem (which guarantees p divides 2^(p−1) − 1) to divisibility by p², making these primes extremely rare — only two are known below 10^17.

## Task Requirements
- Write a routine (function/procedure) that identifies Wieferich primes.
- A prime p qualifies when p² evenly divides 2^(p−1) − 1.
- Use the routine to find and display all Wieferich primes less than 5000.

## Language Coverage
47 languages implement this task, spanning systems and functional languages plus several BASIC and Lisp dialects. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, and Raku.

## Connections
- [[FermatsLittleTheorem]] — Wieferich primes are exactly the primes where this congruence holds modulo p² rather than p.
- [[ModularExponentiation]] — practical implementations compute 2^(p−1) mod p² rather than the full power.
- [[PrimeNumbers]] — candidates must first be prime before the square-divisibility test applies.
- [[NumberTheory]] — the broader field connecting these primes to Fermat quotients and the abc conjecture.

## Contradictions
- None — reference task page.
