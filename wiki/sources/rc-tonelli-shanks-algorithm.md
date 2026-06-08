---
title: "Tonelli-Shanks algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic, cryptography]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tonelli-Shanks_algorithm
---

## Summary
The task asks the programmer to implement the Tonelli-Shanks algorithm, which computes a modular square root: it solves x² ≡ n (mod p) for x, given an odd prime p and a quadratic residue n. The key idea is to factor p-1 as q·2ˢ with q odd, then iteratively refine a candidate root using a non-residue z and repeated squaring until the "tracking" value t collapses to 1. It is a standard primitive in cryptography (e.g. the Rabin cryptosystem and point decompression on elliptic curves).

## Task Requirements
- Use the Legendre symbol (a|p) = a^((p-1)/2) mod p to verify that n is a square mod p before proceeding.
- Factor p-1 = q·2ˢ with q odd; handle the p ≡ 3 (mod 4) shortcut (r ≡ ±n^((p+1)/4)).
- Select a quadratic non-residue z (Legendre symbol -1), set c ≡ zq, then iterate to find the lowest i with t^(2^i) ≡ 1 and update r, t, c, m accordingly.
- Output both solutions r and p - r.
- Solve the given cases, e.g. n=10 p=13, n=56 p=101, n=1030 p=10009, n=44402 p=100049.
- Extra credit: solve very large instances including a 50-digit-plus prime (10^50 + 577), requiring big-integer arithmetic.

## Language Coverage
41 languages implement this task, spanning systems and assembly languages through scripting and functional ones. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, Perl, and even ARM/AArch64 Assembly.

## Connections
- [[ModularExponentiation]] — the core operation (a^k mod p) used throughout the algorithm
- [[ModularArithmetic]] — the algebraic setting for all computations
- [[QuadraticResidue]] — Tonelli-Shanks finds square roots of quadratic residues
- [[LegendreSymbol]] — used to test residuosity and pick a non-residue
- [[CipollasAlgorithm]] — an alternative method for the same modular square root problem

## Contradictions
- None — reference task page.
