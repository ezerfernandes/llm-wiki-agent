---
title: "Bitcoin/public point to address (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, hashing, encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitcoin/public_point_to_address
---

## Summary
This task asks the programmer to convert an elliptic-curve public point (its X and Y coordinates) into a Bitcoin address string. The conversion chains together a fixed prefix byte, two cryptographic hash functions, a checksum, and a custom Base-58 alphabet. The key insight is that a Bitcoin address is essentially a double-hashed, version-prefixed, checksummed, Base-58Check-encoded form of the public key.

## Task Requirements
- Concatenate the 32-byte X and 32-byte Y coordinates into a 64-byte string.
- Prepend a single byte equal to 4 (the uncompressed-point convention).
- Compute the SHA-256 digest of that 65-byte string.
- Compute the RIPEMD-160 of the SHA-256 digest.
- Prepend a version byte (a single zero byte) and compute a checksum over that concatenation (per the bitcoin/address validation task).
- Base-58 encode the version byte, the RIPEMD-160 digest, and the checksum. The Base-58 alphabet is alphanumeric (digits, uppercase, lowercase) minus the ambiguous characters 0, O, l, and I.
- Verify against the worked example, which maps to address `16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM` (the leading '1' is optional since 1 = zero in Base-58).
- Extra credit: validate that the public point actually lies on the secp256k1 curve.

## Language Coverage
27 languages implement this task, spanning systems, scripting, and functional families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Ruby, and the Wolfram Language.

## Connections
- [[SHA256]] — first hash applied to the prefixed public point.
- [[RIPEMD160]] — second hash that shortens the digest to 160 bits.
- [[Base58Check]] — version + payload + checksum encoding scheme used for the address.
- [[EllipticCurveCryptography]] — secp256k1 is the curve the public point belongs to.
- [[Bitcoin]] — the cryptocurrency whose address format this task reproduces.

## Contradictions
- None — reference task page.
