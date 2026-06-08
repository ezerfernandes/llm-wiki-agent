---
title: "Substring/Top and tail (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, unicode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Substring/Top_and_tail
---

## Summary
This task asks the programmer to demonstrate removing the first and last characters from a string. Three results must be shown: the string with the first character removed, with the last character removed, and with both removed. The key insight is correctness under Unicode — when a program uses UTF-8 or UTF-16, it must operate on logical characters (code points), not on raw 8-bit or 16-bit code units, so it works for any valid code point including those above the Basic Multilingual Plane.

## Task Requirements
- Produce the string with its first character removed.
- Produce the string with its last character removed.
- Produce the string with both the first and last characters removed.
- For UTF-8/UTF-16 programs, operate on logical characters (code points), not code units, and handle code points above the BMP.
- Programs for other encodings (8-bit ASCII, EUC-JP, etc.) need not handle all Unicode characters.

## Language Coverage
131 languages implement this task, reflecting broad coverage typical of fundamental string-manipulation exercises. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Perl, and Raku.

## Connections
- [[StringManipulation]] — the task category, slicing characters off a string
- [[Substring]] — extracting a contiguous range of characters
- [[UnicodeCodePoint]] — the correctness requirement for UTF-8/UTF-16 programs
- [[CharacterEncoding]] — distinguishing code points from code units

## Contradictions
- None — reference task page.
