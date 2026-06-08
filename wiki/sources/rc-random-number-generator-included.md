---
title: "Random number generator (included) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, random-number-generation, cryptography]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Random_number_generator_(included)
---

## Summary
This is a reporting (not implementation) task: state which pseudo-random number generator algorithm a language's built-in RNG uses, and link to a wider explanation where possible. The goal is to survey what generators ship with each language rather than to build one. The key insight is that built-in RNGs fall into a few well-known families with very different statistical and security properties.

## Task Requirements
- State the type of RNG algorithm used by the language's built-in random number generator.
- If the language or its standard libraries provide no RNG, skip the task.
- Where possible, link to a broader explanation of the algorithm used.
- Note: do NOT implement an RNG — report on the most likely in-built one.

## Language Coverage
104 languages document their built-in RNGs, reflecting near-universal language support and a broad spread of underlying algorithms. Representative entries include C, C++, Java, Python, Ruby, Rust, Go, Haskell, Common Lisp, and JavaScript. The task notes the main PRNG families: the Linear Congruential Generator (LCG), the Generalized Feedback Shift Register (GFSR, with the Mersenne Twister as a subclass), and constructions that pass a generator's output through a cryptographic hash for unpredictability — with a warning that LCGs and GFSRs alone are unsuitable for cryptography.

## Connections
- [[PseudorandomNumberGenerator]] — the general category this task surveys.
- [[LinearCongruentialGenerator]] — one of the two main PRNG families named.
- [[MersenneTwister]] — the dominant GFSR-subclass generator in many standard libraries.
- [[CryptographicHashFunction]] — used to harden RNG output for unpredictability.
- [[Cryptography]] — the demanding application for which plain LCGs/GFSRs are inadequate.

## Contradictions
- None — reference task page.
