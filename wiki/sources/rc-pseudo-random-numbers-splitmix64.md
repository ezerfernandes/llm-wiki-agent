---
title: "Pseudo-random numbers/Splitmix64 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, prng, bitwise-operations, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pseudo-random_numbers/Splitmix64
---

## Summary
This task asks the programmer to implement the Splitmix64 pseudo-random number generator, a fast and simple algorithm that maintains a single 64-bit state and emits 64 bits per call. Each step increments the state by the constant 0x9e3779b97f4a7c15 (derived from the golden ratio), then runs a fixed sequence of xor-shift-and-multiply mixing operations to scramble the output. The key insight is that all arithmetic wraps modulo 2^64, so languages lacking native unsigned 64-bit integers must apply bitmasks; Splitmix64 is too weak for cryptography but is widely used to seed more complex generators.

## Task Requirements
- Implement a class or set of functions generating pseudo-random numbers via Splitmix64.
- `next_int()`: add 0x9e3779b97f4a7c15 to state, then mix via two `(z ^ (z >> shift)) * constant` rounds (shifts 30 and 27) and a final `z ^ (z >> 31)`.
- `next_float()`: return `next_int() / 2^64` to yield a value in [0, 1).
- Show the first five integers for seed 1234567 (e.g. 6457827717110365317, ...).
- For seed 987654321, show the distribution of 100,000 repetitions of `floor(next_float() * 5)` (each bucket near 20,000).
- Display the output on the page.

## Language Coverage
39 languages implement this task, spanning systems, functional, scripting, and stack-based families. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Forth, and Wren.

## Connections
- [[PseudoRandomNumberGenerator]] — Splitmix64 is a concrete PRNG design.
- [[BitwiseOperations]] — relies on xor, right shifts, and modular multiplication.
- [[ModularArithmetic]] — all state and output arithmetic is modulo 2^64.
- [[GoldenRatio]] — the increment constant 0x9e3779b97f4a7c15 derives from the golden ratio.
- [[Xorshift]] — a related generator family that Splitmix64 is often used to seed.

## Contradictions
- None — reference task page.
