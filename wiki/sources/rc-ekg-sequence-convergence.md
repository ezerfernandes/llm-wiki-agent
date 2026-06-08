---
title: "EKG sequence convergence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/EKG_sequence_convergence
---

## Summary
The EKG sequence (OEIS A064740) starts with a(1)=1, a(2)=N, and for each subsequent term picks the smallest unused natural number that shares at least one prime factor with the previous term. The task asks the programmer to generate these sequences for several starting values and to detect when two differently-seeded variants converge. The key insight is that two EKG generators with different starts (e.g. EKG(5) and EKG(7)) eventually produce identical tails once their internal state — the set of used numbers — coincides.

## Task Requirements
- Generate and show the first 10 members of EKG(2), EKG(5), EKG(7), EKG(9), and EKG(10).
- For each new term (n > 2), pick the smallest natural number not already used that shares a prime factor with the previous term.
- As a stretch goal, determine the term index at which EKG(5) and EKG(7) converge — i.e. where their generator states become equal.

## Language Coverage
35 languages implement this task, spanning systems, functional, scripting, and array styles. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, and J.

## Connections
- [[GreatestCommonDivisor]] — shared-prime-factor test is naturally expressed via GCD > 1.
- [[PrimeFactorization]] — each term is chosen by comparing prime factors with the predecessor.
- [[SieveOfEratosthenes]] — an efficient way to obtain prime factors for candidate numbers.
- [[IntegerSequences]] — the EKG sequence is a defined OEIS integer sequence (A064740).
- [[YellowstoneSequence]] — a closely related greedy prime-factor-driven integer sequence.

## Contradictions
- None — reference task page.
