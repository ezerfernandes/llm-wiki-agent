---
title: "Pseudo-random numbers/PCG32 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, pseudo-random, bitwise-operations, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pseudo-random_numbers/PCG32
---

## Summary
This task asks the programmer to implement the PCG32 (Permuted Congruential Generator) pseudo-random number generator. PCG32 keeps two 64-bit unsigned integers of internal state — a `state` value advanced by a linear congruential step, and a constant `sequence`/`inc` that selects one of 2**63 distinct streams. Each step advances the LCG state, then applies an xorshift permutation and an output rotation to produce a well-distributed 32-bit result, which the unsigned arithmetic and bit manipulation must implement exactly.

## Task Requirements
- Implement a class/set of functions generating pseudo-random numbers via the PCG32 algorithm (LCG multiplier `N = 6364136223846793005`, increment `inc = (seed_sequence << 1) | 1`).
- The output step computes `xs = ((state>>18)^state)>>27`, `rot = state>>59`, and outputs `(xs>>rot)|(xs<<((-rot)&31))`, then advances `state = state*N + inc`.
- Show the first five integers from seed `42, 54` equal `2707161783 2068313097 3122475824 2211639955 3215226955`.
- For seed `987654321, 1`, bin 100,000 repetitions of `floor(next_float() * 5)` and show counts approximately `0: 20049, 1: 20022, 2: 20115, 3: 19809, 4: 20005`.
- Display output on the task page.

## Language Coverage
41 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, C#, Haskell, OCaml, Python, Julia, Raku, and FreeBASIC.

## Connections
- [[PseudoRandomNumberGeneration]] — the general problem class this task belongs to
- [[LinearCongruentialGenerator]] — the LCG state-advance step at PCG32's core
- [[BitwiseOperations]] — xorshift, logical shifts, and bit rotation used in the output permutation
- [[ModularArithmetic]] — 64-bit unsigned wraparound arithmetic required for correctness
- [[Anamorphism]] — the unfold structure the task notes as dual to fold/reduce

## Contradictions
- None — reference task page.
