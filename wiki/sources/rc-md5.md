---
title: "MD5 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/MD5
---

## Summary
The task is to encode (hash) a string using the MD5 algorithm, producing the familiar 128-bit message digest. MD5 works by padding the message, processing it in 512-bit blocks through four rounds of nonlinear functions, modular additions, and bitwise rotations against four 32-bit state registers. The task notes that solutions may call a library or implement the algorithm from scratch, and warns that MD5 is cryptographically broken (collisions and forged signatures) and should not be used for production security.

## Task Requirements
- Encode a given string using the MD5 algorithm.
- Optionally validate the implementation against the test vectors in IETF RFC 1321.
- RFC 1321 is cited as the authoritative, more precise specification of the algorithm than the Wikipedia description.
- A separate page, MD5/Implementation, is reserved for from-scratch (non-library) implementations.

## Language Coverage
105 languages implement this task, an exceptionally broad spread that reflects MD5's ubiquity across general-purpose, scripting, and assembly languages. Representative entries include C, C++, C#, Java, Python, Go, Rust, Haskell, Perl, Ruby, JavaScript, and AArch64 Assembly.

## Connections
- [[CryptographicHashFunction]] — MD5 is a member of this family
- [[MessageDigest]] — the 128-bit fixed-length output it produces
- [[BitwiseOperations]] — relies on rotations, XOR, AND/OR for its round functions
- [[ModularArithmetic]] — state updates use 32-bit modular addition
- [[HashCollision]] — the known weakness that renders MD5 insecure

## Contradictions
- None — reference task page.
