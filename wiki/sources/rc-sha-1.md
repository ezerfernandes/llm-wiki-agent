---
title: "SHA-1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/SHA-1
---

## Summary
SHA-1 is a one-way cryptographic hash function that computes a 160-bit message digest from an input string of octets. The task asks the programmer to produce the SHA-1 digest for a given byte string, either by calling a library or implementing the algorithm (defined by US standard FIPS 180-1) directly. The page notes that SHA-1 has known collision weaknesses and is deprecated for production cryptography in favor of SHA-2 or SHA-3.

## Task Requirements
- Compute the SHA-1 message digest for a string of octets (bytes).
- Either invoke an existing SHA-1 library or implement the algorithm from scratch — both approaches are accepted.
- Output the resulting 160-bit digest (typically as 40 hexadecimal characters).

## Language Coverage
86 languages implement this task, spanning systems languages, scripting languages, and assembly. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Ruby, JavaScript, and AArch64 Assembly.

## Connections
- [[HashFunction]] — SHA-1 is a member of this family.
- [[Cryptography]] — the task lives in the security/checksums domain.
- [[MessageDigest]] — the 160-bit fixed-length output SHA-1 produces.
- [[SHA-2]] — recommended stronger successor referenced by the task.
- [[BitwiseOperations]] — the algorithm relies on rotations, XOR, and modular addition.

## Contradictions
- None — reference task page.
