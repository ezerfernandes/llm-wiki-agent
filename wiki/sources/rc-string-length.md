---
title: "String length (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, unicode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/String_length
---

## Summary
The task asks the programmer to compute both the character length and the byte length of a string, correctly handling encodings where bytes and characters do not map one-to-one. The key insight is that "character" means an individual Unicode code point (not a byte, not a UTF-16 code unit, and not a user-visible grapheme), so multi-byte UTF-8 sequences and non-BMP code points must be counted accurately. As an optional extension, languages able to report grapheme length (combining characters merged into one visible unit) should demonstrate that too.

## Task Requirements
- Find the character length of a string, counting Unicode code points.
- Find the byte length of a string, accounting for the encoding (e.g., UTF-8 vs UTF-16).
- Handle non-BMP code points (U+10000 to U+10FFFF) as single characters, not as UTF-16 surrogate pairs.
- Mark examples with `===Character Length===` or `===Byte Length===`.
- Optionally provide `===Grapheme Length===` for languages that can count user-visible graphemes (combining-character clusters).

## Language Coverage
202 languages implement this task, an exceptionally broad set spanning assembly, scripting, and functional languages. Representative implementations include C, Python, JavaScript, Rust, Go, Haskell, Perl, Ruby, Java, and Raku.

## Connections
- [[UnicodeEncoding]] — distinguishes code points from bytes and code units
- [[UTF8]] — variable-width byte encoding central to the byte-vs-character distinction
- [[StringProcessing]] — fundamental string measurement operation
- [[GraphemeCluster]] — user-visible character unit for the optional grapheme count

## Contradictions
- None — reference task page.
