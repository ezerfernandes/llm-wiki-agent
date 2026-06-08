---
title: "Two's complement (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bitwise-operations, binary-representation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Two's_complement
---

## Summary
Two's complement is the standard scheme for representing signed integers in binary. The task asks the programmer to compute the two's complement of an integer using the canonical method: invert all the bits of a positive value and add one to produce its negative counterpart. The key insight is that this representation lets the same hardware addition logic handle both positive and negative numbers, and it need not be limited to a 32-bit width.

## Task Requirements
- Show how to calculate the two's complement of an integer.
- The width is not fixed — it does not have to be a 32-bit integer.
- Demonstrate the core operation: flip the bits and add one to negate a value.

## Language Coverage
46 languages implement this task, spanning a wide range from low-level assembly through high-level scripting. Because the operation maps directly to CPU instructions, many entries are assembly dialects (6502, 68000, 8080, 8086, AArch64, ARM, x86-64, Z80), alongside systems and general-purpose languages such as Ada, C, C++, Rust, Java, JavaScript, Python, Perl, Ruby, and Fortran.

## Connections
- [[TwosComplement]] — the signed-integer representation the task implements
- [[BitwiseOperations]] — bit inversion (NOT) is the first step of the algorithm
- [[BinaryRepresentation]] — the underlying encoding of integers in base 2
- [[SignedIntegers]] — the broader problem of representing negative numbers

## Contradictions
- None — reference task page.
