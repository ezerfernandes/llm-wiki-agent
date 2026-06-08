---
title: "Parallel brute force (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing, concurrency]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parallel_brute_force
---

## Summary
The task asks the programmer to recover three five-letter, all-lowercase-ASCII passwords from their SHA-256 hashes by exhaustively iterating over the entire 26^5 (~11.9 million) candidate space. The key insight is that the search space is small enough to brute force directly, and that the independent per-candidate hashing makes it an ideal showcase for concurrent or parallel processing. Each matching password should be printed alongside its hash.

## Task Requirements
- Find the five-letter passwords matching three given SHA-256 hashes.
- Iterate naively through all passwords of exactly five lower-case ASCII English letters.
- Use concurrent or parallel processing where the language supports it.
- Compute SHA-256 via a library call or a custom implementation.
- Print each matching password together with its SHA-256 hash.

## Language Coverage
38 languages implement this task, spanning systems languages with native threading and functional languages with parallel combinators. Representative implementations include C, C++, C#, Rust, Go, Java, Haskell, Clojure, Julia, Python, Erlang, and Raku.

## Connections
- [[SHA256]] — the cryptographic hash function being inverted by search
- [[BruteForceSearch]] — exhaustive enumeration of the candidate space
- [[Cryptography]] — password hashing and preimage recovery context
- [[ParallelProcessing]] — concurrency across independent hash computations
- [[HashFunction]] — general one-way function being checked per candidate

## Contradictions
- None — reference task page.
