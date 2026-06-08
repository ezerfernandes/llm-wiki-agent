---
title: "Formatted numeric output (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Formatted_numeric_output
---

## Summary
This task asks the programmer to express a decimal number as a fixed-length string padded with leading zeros. The canonical example is rendering 7.125 as the 9-character string "00007.125". The key insight is that most languages expose this directly through a format specifier (e.g. printf-style width and zero-fill flags), so the challenge is mainly knowing the idiomatic formatting facility rather than implementing padding by hand.

## Task Requirements
- Take a decimal number (the example uses 7.125).
- Produce a fixed-length string representation of it.
- Pad the left side with leading zeros so the total field width is met.

## Language Coverage
124 languages implement this task, reflecting that numeric formatting is a near-universal feature touched early in learning a language. Representative implementations include C, C++, Java, Python, Perl, Ruby, Go, Rust, Common Lisp, Haskell, and COBOL.

## Connections
- [[StringFormatting]] — the task is a direct application of width-and-fill format specifiers.
- [[Printf]] — many solutions rely on C-style printf format strings (e.g. "%09.3f").
- [[StringPadding]] — leading-zero fill is a special case of left-padding a field to a fixed width.
- [[FloatingPointRepresentation]] — formatting a decimal fraction requires controlling the displayed precision.

## Contradictions
- None — reference task page.
