---
title: "Arithmetic derivative (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic_derivative
---

## Summary
The task asks the programmer to implement the Lagarias arithmetic derivative D(n), a number-theoretic function defined by analogy with the calculus product (Leibniz) rule but built on prime factorization. The base cases are D(0) = D(1) = 0 and D(p) = 1 for any prime p, while composites follow D(mn) = D(m)n + mD(n); negatives are handled as -D(-n). The key insight is that recursively decomposing n into prime factors and applying the Leibniz rule yields a well-defined derivative for every integer.

## Task Requirements
- Implement the arithmetic derivative D(n) using the three defining rules (D(0)=D(1)=0, D(prime)=1, Leibniz product rule).
- Extend the definition to negative integers via D(n) = -D(-n) for n < 0.
- Find and display the arithmetic derivatives for all integers from -99 through 100.
- Stretch goal: compute the arithmetic derivative of 10^m for m from 1 to 20, then divide each result by 7.

## Language Coverage
57 languages implement this task, spanning mainstream, functional, array, and historical/esoteric families. Representative implementations include Python, C, C++, Rust, Go, Java, Haskell, Julia, Perl, Raku, J, and APL.

## Connections
- [[NumberTheory]] — the arithmetic derivative is a function studied within number theory.
- [[PrimeFactorization]] — the derivative is computed by decomposing integers into their prime factors.
- [[LeibnizRule]] — the product rule for derivatives is reused as the defining recurrence D(mn) = D(m)n + mD(n).
- [[Recursion]] — typical implementations recurse over factor decompositions to evaluate D(n).
- [[RosettaCode]] — this is a programming task from the Rosetta Code chrestomathy.

## Contradictions
- None — reference task page.
