---
title: "Long multiplication (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arbitrary-precision, arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Long_multiplication
---

## Summary
The task asks the programmer to explicitly implement the schoolbook long-multiplication algorithm rather than relying on a language's built-in multiplication. This is one route to arbitrary-precision integer arithmetic, since the operands are represented as digit sequences and multiplied digit-by-digit with carry propagation. The key insight is that multiplying two n-digit numbers reduces to a grid of single-digit products plus positional shifts and summation.

## Task Requirements
- Explicitly implement long multiplication (the digit-by-digit algorithm), not the native `*` operator.
- Display the result of 2^64 * 2^64, which equals 2^128.
- Expected output: 2^64 = 18,446,744,073,709,551,616 and 2^64 * 2^64 = 340,282,366,920,938,463,463,374,607,431,768,211,456.
- Optionally verify the result against the language's built-in arbitrary-precision support.

## Language Coverage
95 languages implement this task, spanning low-level assembly, mainstream high-level languages, functional languages, and esoteric/specialty tools. Representative examples include C, C++, Java, Python, Go, Haskell, Common Lisp, REXX, Fortran, and several assembly variants such as AArch64 Assembly and RISC-V Assembly.

## Connections
- [[ArbitraryPrecisionArithmetic]] — long multiplication is a foundational building block for bignum integer support.
- [[Multiplication]] — implements the grade-school positional multiplication algorithm.
- [[CarryPropagation]] — digit products must accumulate carries across positions.
- [[BigNum]] — operands too large for native word sizes are stored as digit arrays.

## Contradictions
- None — reference task page.
