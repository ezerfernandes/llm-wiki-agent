---
title: "RIPEMD-160 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/RIPEMD-160
---

## Summary
RIPEMD-160 is a cryptographic hash function that produces a 160-bit message digest. The task asks the programmer to compute the RIPEMD-160 digest of a string of octets, using the ASCII-encoded string "Rosetta Code" as the test input. Implementations may either call an existing RIPEMD-160 library or implement the algorithm from scratch. A key detail is that, for message padding, RIPEMD-160 follows the same scheme as MD4 (RFC 1320).

## Task Requirements
- Compute the RIPEMD-160 message digest (160-bit / 20-byte output) of a string of octets.
- Use the ASCII-encoded string "Rosetta Code" as the input.
- Either call an RIPEMD-160 library or implement the algorithm directly.
- Pad the message the same way MD4 does (per RFC 1320).

## Language Coverage
42 languages implement this task, spanning systems languages, scripting languages, and functional languages. Representative implementations include C, C++, C#, Go, Rust, Java, Python, Perl, Ruby, Haskell, and Common Lisp.

## Connections
- [[RIPEMD]] — the family of hash functions this digest belongs to
- [[CryptographicHashFunction]] — the broader class of algorithms
- [[MessageDigest]] — the fixed-length output produced
- [[MerkleDamgardConstruction]] — the iterated compression structure underlying it
- [[MD4]] — shares the same message-padding scheme (RFC 1320)

## Contradictions
- None — reference task page.
