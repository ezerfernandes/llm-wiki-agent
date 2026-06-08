---
title: "Chinese remainder theorem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Chinese_remainder_theorem
---

## Summary
The task asks the programmer to solve a system of simultaneous linear congruences whose moduli are pairwise co-prime, using the Chinese Remainder Theorem. Given moduli n_i and residues a_i, the program must return the unique solution x in the range 0 ≤ x < N where N is the product of all moduli. The key insight is that for each i, n_i and N/n_i are co-prime, so the extended Euclidean algorithm yields a modular inverse, and the solution is the weighted sum x = Σ a_i · s_i · (N/n_i) reduced modulo N.

## Task Requirements
- Solve a system of linear congruences x ≡ a_i (mod n_i) for pairwise co-prime moduli.
- Indicate failure when the system cannot be solved (throw an exception or return a special false value).
- Return the unique minimal solution s with 0 ≤ s < N, where N = n_1·n_2·…·n_k.
- Demonstrate the program with n = [3, 5, 7] and a = [2, 3, 2] (the answer is 23).

## Language Coverage
82 languages implement this task, spanning systems and assembly languages through functional and scripting languages — for example C, C++, Rust, Go, Java, Haskell, Python, Perl, Ruby, Common Lisp, and several assembly dialects (AArch64, ARM, 360).

## Connections
- [[ChineseRemainderTheorem]] — the central result being implemented
- [[ModularArithmetic]] — congruences and reduction modulo N
- [[ExtendedEuclideanAlgorithm]] — used to compute modular inverses
- [[ModularMultiplicativeInverse]] — finds s_i such that s_i·(N/n_i) ≡ 1 (mod n_i)
- [[NumberTheory]] — the mathematical domain of the task

## Contradictions
- None — reference task page.
