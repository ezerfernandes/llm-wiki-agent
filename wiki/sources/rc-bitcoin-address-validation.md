---
title: "Bitcoin/address validation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, checksums, encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitcoin/address_validation
---

## Summary
The task asks the programmer to validate a Bitcoin address by decoding it and verifying its embedded checksum. A Bitcoin address is a Base58 string that decodes to 25 bytes: a 1-byte version, a 20-byte payload (a RIPEMD-160 digest), and a 4-byte checksum. Validation means recomputing the checksum as the first four bytes of a double SHA-256 over the leading 21 bytes and confirming it matches the trailing four bytes. The key insight is that no key cryptography is needed — only Base58 decoding plus a SHA-256 digest library.

## Task Requirements
- Take a Bitcoin address string as input and return a boolean (or raise on invalid).
- Decode using Base58: the alphabet is 0-9, A-Z, a-z minus the four ambiguous characters `0` (zero), `O` (uppercase oh), `I` (uppercase eye), and `l` (lowercase ell).
- Interpret the decoded 25 bytes as version (1, must be zero for this task), payload (20 bytes), checksum (4 bytes).
- Compute the checksum as the first four bytes of `SHA-256(SHA-256(first 21 bytes))`.
- Confirm the computed checksum equals the address's last four bytes.
- Verify against the known-good test address `1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i`, which should validate; altering characters should make it fail.

## Language Coverage
39 languages implement this task, spanning systems and functional languages alongside scripting and BASIC dialects. Representative implementations include C, C++, Rust, Go, Haskell, Python, Ruby, Perl, Java, and JavaScript.

## Connections
- [[Base58]] — the encoding scheme used for the address string
- [[SHA256]] — the digest applied twice to derive the checksum
- [[Checksum]] — the integrity mechanism being verified
- [[RIPEMD160]] — produces the 20-byte payload (treated as opaque here)
- [[Cryptography]] — the broader domain of Bitcoin address construction

## Contradictions
- None — reference task page.
