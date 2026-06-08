---
title: "CRC-32 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksums, error-detection, bit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/CRC-32
---

## Summary
The task asks the programmer to compute a CRC-32 cyclic redundancy check from within the language, producing a result consistent with the widely-used standard adopted by ISO 3309, ITU-T V.42, Gzip, and PNG. The key insight is that this specific variant processes bits in LSB-first order, initializes the running CRC register to 0xFFFFFFFF, and complements (bitwise-inverts) the final value. Implementations may either call a library routine or build the checksum directly, typically via a precomputed 256-entry lookup table.

## Task Requirements
- Demonstrate a method of deriving the CRC-32 checksum within the language (library call or hand-rolled).
- Conform to the ISO 3309 / ITU-T V.42 / Gzip / PNG variant: LSB-first bit order, initial CRC = 0xFFFFFFFF, final CRC complemented.
- Generate and display the CRC-32 checksum for the ASCII string `The quick brown fox jumps over the lazy dog`.

## Language Coverage
97 languages implement this task, spanning low-level assembly through high-level functional and scripting languages — many leverage built-in zlib/CRC libraries while others construct the lookup table manually. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Erlang, Common Lisp, Forth, and 6502 Assembly.

## Connections
- [[CyclicRedundancyCheck]] — the error-detecting code this task computes
- [[Checksum]] — the broader class of integrity-verification techniques
- [[PolynomialDivision]] — CRC is the remainder of binary polynomial division over GF(2)
- [[BitManipulation]] — relies on shifts, XORs, and bit-order handling
- [[LookupTable]] — common optimization precomputing per-byte CRC contributions

## Contradictions
- None — reference task page.
