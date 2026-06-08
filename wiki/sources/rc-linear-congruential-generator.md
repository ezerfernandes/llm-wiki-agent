---
title: "Linear congruential generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, random-number-generation, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Linear_congruential_generator
---

## Summary
The task asks the programmer to implement a linear congruential generator (LCG), the simplest class of pseudo-random number generators, defined by the recurrence `r(n+1) = (a * r(n) + c) mod m`. Specifically, it requires replicating two historic `rand()` implementations — BSD libc and the Microsoft C Runtime — so each yields the exact same integer sequence as the original when given the same seed. The key insight is that an LCG is fully deterministic and reproducible across languages because the formula is trivial, though its output is low quality and not cryptographically secure (knowing one value predicts the next).

## Task Requirements
- Implement the general LCG recurrence `state(n+1) = (a * state(n) + c) mod m`, starting from a seed `state(0)`.
- Replicate the BSD formula: `a = 1103515245`, `c = 12345`, `m = 2^31`, with `rand(n) = state(n)`, producing values in 0..2147483647.
- Replicate the Microsoft formula: `a = 214013`, `c = 2531011`, `m = 2^31`, with `rand(n) = state(n) / 2^16`, producing values in 0..32767.
- Each replica must produce the same sequence of integers as the original generator for a matching seed.

## Language Coverage
86 languages implement this task, spanning systems, scripting, functional, and assembly families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Forth, REXX, and X86 Assembly.

## Connections
- [[LinearCongruentialGenerator]] — the named algorithm this task implements
- [[PseudoRandomNumberGenerator]] — the broader category of deterministic generators
- [[ModularArithmetic]] — the modulo operation at the core of the recurrence
- [[NumberTheory]] — the field governing the choice of constants a, c, m for full-period output
- [[BitShifting]] — the Microsoft variant discards low bits via division by 2^16

## Contradictions
- None — reference task page.
