---
title: "Even or odd (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, bitwise-operations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Even_or_odd
---

## Summary
The task is to test whether a given integer is even or odd. The core insight is that parity can be determined several equivalent ways, the cheapest being to inspect only the least significant bit: a number is even exactly when its lowest bit is 0. This reduces a seemingly arithmetic question to a single bitwise operation.

## Task Requirements
- Test whether an integer is even or odd.
- Acceptable approaches include any of the following:
  - Use built-in even/odd predicates if the language provides them.
  - Check the least significant bit via bitwise-AND with 1 (result 0 means even, 1 means odd for binary integers).
  - Divide by 2 and inspect the remainder (0 means even; +1 or -1 means odd).
  - Use modular congruences: i ≡ 0 (mod 2) is even, i ≡ 1 (mod 2) is odd.

## Language Coverage
224 languages implement this task, an exceptionally broad set reflecting its status as a beginner-level exercise. Representative implementations include C, Python, Java, Haskell, Rust, Go, Common Lisp, APL, Forth, and several assembly dialects such as x86-64 Assembly and Z80 Assembly.

## Connections
- [[Parity]] — the even/odd property being tested
- [[ModularArithmetic]] — the mod-2 congruence approach
- [[BitwiseOperations]] — the least-significant-bit AND technique
- [[NumberTheory]] — divisibility and remainder fundamentals

## Contradictions
- None — reference task page.
