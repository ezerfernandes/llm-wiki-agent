---
title: "Hex dump (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, binary-data, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hex_dump
---

## Summary
The task is to implement a hexdump-like tool that renders the raw bytes of a file in the "canonical" format used by the Unix `hexdump` utility. Each output line shows a hexadecimal byte offset, up to 16 bytes in hex (with extra spacing between the 8th and 9th bytes), and the same bytes rendered as ASCII (non-printable bytes shown as `.`) between pipe characters, ending with a final total byte count. The key insight is mapping a linear byte stream into fixed-width, multi-column text while tracking offsets and substituting printable representations.

## Task Requirements
- Output bytes in the canonical hexdump format (offset, hex columns, ASCII gutter, trailing byte count).
- Accept an optional starting offset in bytes from which to begin dumping.
- Accept an optional length in bytes after which to stop.
- Demonstrate using the given UTF-16 little-endian sample string ("Rosetta Code is a programming chrestomathy site 😀.").
- Stretch goal: implement an `xxd`-style binary mode that prints each byte as 8 bits instead of hexadecimal, with 6 bytes per line.

## Language Coverage
33 languages implement this task, spanning systems and assembly languages through high-level and array languages. Representative implementations include AArch64 Assembly, ARM Assembly, C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, and the array language Uiua.

## Connections
- [[Hexadecimal]] — the primary numeric base used for offsets and byte values
- [[ASCII]] — printable-character mapping for the right-hand text gutter
- [[CharacterEncoding]] — the sample input is UTF-16 little-endian with a byte order mark
- [[BinaryData]] — the task operates on raw byte streams independent of text semantics
- [[StringFormatting]] — fixed-width column alignment drives the output layout

## Contradictions
- None — reference task page.
