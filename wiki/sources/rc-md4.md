---
title: "MD4 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing, bitwise]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/MD4
---

## Summary
The task asks the programmer to compute the MD4 message digest of a string of octets, using the ASCII string "Rosetta Code" as the test input. Solutions may either call an existing MD4 library or implement the algorithm directly. MD4, specified in RFC 1320, is an obsolete cryptographic hash function that produces a 128-bit (16-byte) digest; RFC 6150 formally declares it obsolete, and it survives mainly in legacy protocols.

## Task Requirements
- Find the MD4 message digest of a string of octets.
- Use the ASCII-encoded string "Rosetta Code" (without quotes) as the input.
- Either call an MD4 library or implement MD4 from scratch in the chosen language.

## Language Coverage
41 languages implement this task. Coverage is broad across systems, scripting, and functional languages, including C, C++, C#, Go, Rust, Java, Python, Ruby, Perl, Haskell, and Common Lisp, with many relying on standard or third-party crypto libraries rather than a hand-rolled implementation.

## Connections
- [[CryptographicHashFunction]] — MD4 is an early member of this family.
- [[MessageDigest]] — the 128-bit fixed-length output produced.
- [[BitwiseOperations]] — the core rounds rely on rotations, AND/OR/XOR mixing.
- [[Checksums]] — the Rosetta Code category this task belongs to.
- [[MD5]] — the successor hash function derived from MD4's design.

## Contradictions
- None — reference task page.
