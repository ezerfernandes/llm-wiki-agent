---
title: "UTF-8 encode and decode (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, character-encoding, bit-manipulation, unicode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/UTF-8_encode_and_decode
---

## Summary
This task asks the programmer to implement both an encoder and a decoder for the UTF-8 character encoding. The encoder takes a Unicode code-point (an integer) and produces the corresponding sequence of 1–4 bytes; the decoder reverses the process, reconstructing the code-point from its UTF-8 byte sequence. The key insight is that UTF-8 is a variable-length scheme where the high bits of the leading byte signal how many continuation bytes (each prefixed with `10`) follow, allowing self-synchronizing, ASCII-compatible encoding.

## Task Requirements
- Write an encoder mapping a Unicode code-point integer to a sequence of 1–4 octets in UTF-8.
- Write the corresponding decoder mapping a 1–4 byte UTF-8 sequence back to the code-point.
- Demonstrate round-trip encode/decode on five sample characters: `A` (U+0041 → 41), `ö` (U+00F6 → C3 B6), `Ж` (U+0416 → D0 96), `€` (U+20AC → E2 82 AC), and `𝄞` (U+1D11E → F0 9D 84 9E), covering all four byte-length cases.

## Language Coverage
57 languages implement this task, spanning systems languages, scripting languages, and functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp (the reference), Perl, and Raku.

## Connections
- [[UTF-8]] — the encoding scheme being implemented
- [[Unicode]] — the code-point space being encoded
- [[CharacterEncoding]] — the broader category of byte/text mapping schemes
- [[BitManipulation]] — masking and shifting drive both encode and decode

## Contradictions
- None — reference task page.
