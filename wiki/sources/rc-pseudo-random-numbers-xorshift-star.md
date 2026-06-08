---
title: "Pseudo-random numbers/Xorshift star (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, prng, bitwise-operations, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pseudo-random_numbers/Xorshift_star
---

## Summary
The task asks the programmer to implement the Xorshift* pseudo-random number generator, a variant of Marsaglia's xorshift family that scrambles the output with a final multiplication step to improve statistical quality. The generator holds a 64-bit state, advances it through three xor-shift mixing steps (right 12, left 25, right 27), then multiplies by the constant 0x2545F4914F6CDD1D and returns the high 32 bits as the result. The key insight is that the non-linear multiplication ("star") significantly improves randomness over a plain xorshift while remaining extremely fast.

## Task Requirements
- Implement a class or set of functions producing the Xorshift* sequence as specified.
- Seeded with 1234567, verify the first five `next_int()` outputs are 3540625527, 2750739987, 4037983143, 1993361440, 3809424708.
- Implement `next_float()` returning `next_int() / (1 << 32)`.
- With seed 987654321, run 100000 repetitions of `floor(next_float() * 5)` and confirm the bucket counts: 0: 20103, 1: 19922, 2: 19937, 3: 20031, 4: 20007.
- Show the output on the page.

## Language Coverage
33 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, and Perl.

## Connections
- [[PseudorandomNumberGenerator]] — the broader class of algorithms this belongs to.
- [[Xorshift]] — the base PRNG family that Xorshift* extends.
- [[BitwiseOperations]] — relies on logical shifts and exclusive-or.
- [[ModularArithmetic]] — the 64-bit multiplication wraps modulo 2^64.

## Contradictions
- None — reference task page.
