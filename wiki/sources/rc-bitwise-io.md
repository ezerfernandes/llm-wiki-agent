---
title: "Bitwise IO (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bit-manipulation, compression, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitwise_IO
---

## Summary
The task asks the programmer to write functions (or a class) that read and write arbitrary-length sequences of bits, most-significant-bit first, even though real I/O is always quantized to whole bytes. The key insight is that an internal bit buffer must accumulate bits until a full byte is available, padding the final partial byte with zero bits on flush. This lets variable-width codes cross byte boundaries cleanly while delegating buffering and endianness to the underlying byte stream.

## Task Requirements
- Provide functions/methods to write a sequence of bits and to read a sequence of bits, MSB first.
- Perform actual I/O byte-by-byte; pad the trailing partial byte with zero bits (e.g. 13-bit `0101011101010` is emitted as bytes `0x57 0x50`).
- As a test, implement a rough compressor/decompressor for ASCII bytes (high bit unused): pack 8 input bytes into 7 output bytes by writing only 7 bits each, and reverse it.
- Limiting the maximum bits per single read/write operation is permitted; error handling is optional.

## Language Coverage
47 languages implement this task, spanning systems languages, functional languages, assembly, and scripting. Representative implementations include C, C++, Rust, Go, Java, Haskell, OCaml, Common Lisp, Python, Perl, and 6502 Assembly.

## Connections
- [[BitManipulation]] — shifting and masking to pack/unpack sub-byte fields
- [[DataCompression]] — the canonical use case driving variable-length bit I/O
- [[HuffmanCoding]] — variable-length codes that require bit-level streams
- [[LZWCompression]] — fixed/variable nine-bit words read and written via this mechanism
- [[Buffering]] — accumulating bits in a buffer before flushing whole bytes

## Contradictions
- None — reference task page.
