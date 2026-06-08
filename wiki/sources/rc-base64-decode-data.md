---
title: "Base64 decode data (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, encoding, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Base64_decode_data
---

## Summary
This task is the inverse of "Base64 encode data": write a program that takes Base64-encoded output and reconstructs the original byte stream, regenerating the source file exactly. The key insight emphasized by the task is that correct padding (`=` characters) is essential — without it the four-character-to-three-byte grouping cannot be reversed faithfully, a mistake the author observed in several widely-circulated implementations.

## Task Requirements
- Take the output of the Base64 encode task as input.
- Decode it back into the original binary data, regenerating the original file byte-for-byte.
- Handle padding correctly so the round trip is lossless.

## Language Coverage
80 languages implement this task, spanning systems languages, scripting languages, functional languages, and data/query tools. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, Lua, and even SQL-flavored tools like DuckDB and jq.

## Connections
- [[Base64]] — the encoding scheme being reversed
- [[BinaryToTextEncoding]] — the broader family this technique belongs to
- [[DataDecoding]] — mapping the 4-character groups back to 3 bytes
- [[BitManipulation]] — extracting 6-bit sextets and repacking into 8-bit octets

## Contradictions
- None — reference task page.
