---
title: "GSTrans string conversion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, encoding, text-escaping]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/GSTrans_string_conversion
---

## Summary
GSTrans is a text encoding from Acorn/RISC OS that represents any 8-bit byte value (0-255) using only printable characters, so non-printable characters can be passed on a command line. The scheme uses the `|` pipe character as an escape: control codes 0-31 become `|@`, `|A`, ... (the letter offset by 64), the pipe and quote characters self-escape (`||`, `|"`), 127 becomes `|?`, and high bytes 128-255 are written as `|!` followed by the encoding of the low 7 bits. Strings may be wrapped in double quotes. The key insight is a reversible, fully printable byte-to-text mapping.

## Task Requirements
- Write an encode function that converts an arbitrary string of byte values into a GSTrans string.
- Write a decode function that converts a GSTrans string back into the original bytes.
- Handle the control-code (`|@`..`|_`), literal (`||`, `|"`), DEL (`|?`), and high-byte (`|!`) escape rules.
- Support optional surrounding double quotes.
- Indicate what error checking is performed and how errors are reported.

## Language Coverage
16 languages implement this task, spanning systems, scripting, and functional styles. Representative implementations include ALGOL 68, BBC BASIC, Java, Rust, Python, Perl, Raku, Julia, Nim, and Wren.

## Connections
- [[StringProcessing]] — core text transformation work
- [[CharacterEncoding]] — mapping bytes to a printable representation
- [[EscapeSequences]] — the `|`-prefixed escape grammar
- [[ControlCharacters]] — handling of bytes 0-31 and DEL (127)

## Contradictions
- None — reference task page.
