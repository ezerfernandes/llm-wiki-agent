---
title: "Knuth's power tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, exponentiation, trees]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knuth's_power_tree
---

## Summary
This task asks the programmer to implement Knuth's power tree, a method for efficiently computing x^n for any real x and non-negative integer n. The power tree determines a short sequence of integers (an addition chain) whose corresponding intermediate powers are built by squaring or by multiplying an earlier power, minimizing the number of multiplications. The key insight is that for even exponents you square the previous value, and for odd exponents you multiply by an appropriate previously-computed odd power of x.

## Task Requirements
- Compute and show the list of Knuth's power tree integers needed to evaluate x^n for arbitrary real x and non-negative integer n.
- Using those integers, compute and show exact values of 2^n for n from 0 to 17 inclusive.
- Compute and show 3^191 and 1.1^81.
- Handle a zero power as a special case (x^0 = 1).
- Optionally support negative integer powers.

## Language Coverage
27 languages implement this task, spanning functional, imperative, and array-oriented styles. Representative implementations include Python, Haskell, Go, Java, JavaScript, Julia, Perl, Raku, Racket, REXX, and Wren.

## Connections
- [[AdditionChainExponentiation]] — the power tree is one strategy for building short addition chains.
- [[Exponentiation]] — the task computes integer powers x^n.
- [[ExponentiationBySquaring]] — squaring even powers is the core repeated step.
- [[Tree]] — the algorithm walks a tree of exponents to find the path to n.
- [[NumberTheory]] — optimal exponent sequences are a number-theoretic optimization.

## Contradictions
- None — reference task page.
