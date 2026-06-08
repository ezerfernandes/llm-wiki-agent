---
title: "Variable-length quantity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, encoding, bit-manipulation, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Variable-length_quantity
---

## Summary
The task asks the programmer to implement operations on variable-length quantities (VLQ), a way of encoding an arbitrary-size integer into a sequence of octets where each byte carries 7 bits of payload and 1 continuation flag. At minimum, a solution must convert a native integer to its VLQ octet sequence and back. The key insight is that the high bit of each byte signals whether more bytes follow, so big values use more bytes while small values stay compact.

## Task Requirements
- Implement conversion from a normal number to the binary VLQ representation, and the inverse conversion back to a number (any VLQ variant is acceptable).
- Convert the two numbers 0x200000 (2097152) and 0x1FFFFF (2097151) into sequences of octets.
- Display these octet sequences.
- Convert the sequences back to numbers and verify they equal the originals.

## Language Coverage
49 languages implement this task, spanning systems, functional, and scripting families. Representative examples include C, C++, C#, Go, Haskell, Java, JavaScript, Python, Perl, Raku, Ruby, and Tcl.

## Connections
- [[VariableLengthQuantity]] — the encoding scheme this task implements
- [[BitManipulation]] — masking 7-bit groups and setting continuation bits
- [[Base128Encoding]] — VLQ encodes integers in base 128 with a high-bit flag
- [[IntegerEncoding]] — broader family of compact integer serialization formats

## Contradictions
- None — reference task page.
