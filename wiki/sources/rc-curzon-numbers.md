---
title: "Curzon numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisibility, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Curzon_numbers
---

## Summary
A Curzon number is a positive integer n such that 2^n + 1 is evenly divisible by 2n + 1. The task generalizes this to a base integer k: n is a generalized Curzon number for base k when k^n + 1 is divisible by k·n + 1. The key insight is that such numbers only exist for even base integers, and the divisibility test can be computed efficiently with modular exponentiation rather than forming the huge power k^n directly.

## Task Requirements
- Find and show the first 50 generalized Curzon numbers for each even base integer k from 2 through 10.
- Note that "base" here means the integer the equation is built on, not the radix; all calculations are done in base 10.
- Stretch goal: find and show the one-thousandth generalized Curzon number for each base.

## Language Coverage
44 languages implement this task, spanning systems, functional, scripting, and array paradigms — including C, C++, Rust, Go, Java, Haskell, Python, Ruby, Perl, Raku, Julia, J, and Wren.

## Connections
- [[NumberTheory]] — the task is a divisibility property of integers
- [[ModularExponentiation]] — efficient implementations compute k^n mod (k·n+1) instead of forming k^n
- [[Divisibility]] — the core condition tests even divisibility
- [[OEIS]] — Curzon numbers are catalogued as OEIS A224486

## Contradictions
- None — reference task page.
