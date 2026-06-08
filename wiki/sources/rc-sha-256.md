---
title: "SHA-256 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/SHA-256
---

## Summary
This task asks the programmer to compute the SHA-256 cryptographic digest of a given string, either via a built-in/library function or by implementing the algorithm from scratch per FIPS PUB 180-4. SHA-256 is presented as the recommended stronger successor to SHA-1. The key insight is that the digest must be reproducible exactly, so the task supplies a known answer to verify against.

## Task Requirements
- Compute the SHA-256 digest of the string `"Rosetta code"`.
- The result must equal the hex string `764faf5c61ac315f1497f9dfa542713965b785e5cc2f707d6468d7d1124cdfcf`.
- Either a dedicated crypto library or a hand-rolled implementation of the algorithm is acceptable.

## Language Coverage
82 languages implement this task, spanning systems languages, scripting languages, and even hand-written assembly, reflecting how ubiquitous SHA-256 support is. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, JavaScript, and AArch64 Assembly.

## Connections
- [[CryptographicHashFunction]] — SHA-256 is a member of this family
- [[SHA2]] — SHA-256 is the 256-bit variant of the SHA-2 family
- [[SHA1]] — the weaker predecessor this task recommends replacing
- [[MerkleDamgardConstruction]] — the iterated compression-function design SHA-256 uses
- [[BitwiseOperations]] — the algorithm relies on rotations, shifts, and modular addition

## Contradictions
- None — reference task page.
