---
title: "Gray code (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, binary-encoding, bit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gray_code
---

## Summary
Gray code is a binary encoding in which consecutive integers differ by exactly one bit, making it useful for reducing hardware data hazards and for ordering inputs in Karnaugh maps. The task is to implement functions that encode an integer into binary-reflected Gray code and decode it back. The key insight is that encoding is simply `g = b XOR (b >> 1)`, while decoding requires XOR-folding each bit with the running accumulation of higher bits.

## Task Requirements
- Write a function to encode a number into binary-reflected Gray code.
- Write a function to decode a Gray code value back to its normal binary value.
- Use the encoding rule `g = b xor (b >> 1)` (or the per-bit form using the previous binary bit).
- Use the decoding rule `b[0] = g[0]` and `b[i] = g[i] xor b[i-1]` for subsequent bits.
- Display the normal binary, Gray code, and decoded values for all 5-bit numbers (0-31 inclusive).

## Language Coverage
105 languages implement this task, spanning systems and assembly languages through high-level scripting and functional languages, plus hardware description languages reflecting the encoding's circuit-design origins. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, Ada, Verilog, and VHDL.

## Connections
- [[GrayCode]] — the binary-reflected encoding scheme this task implements
- [[BitwiseOperations]] — XOR and bit-shift operations are the core mechanism
- [[BinaryNumberSystem]] — the underlying representation being transformed
- [[KarnaughMap]] — a primary application motivating ordered single-bit-change sequences

## Contradictions
- None — reference task page.
