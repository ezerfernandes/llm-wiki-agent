---
title: "Read a file character by character/UTF8 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, text-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Read_a_file_character_by_character/UTF8
---

## Summary
This task asks the programmer to read a file one character at a time rather than loading the whole file at once. The reader should behave like a procedure that returns the next character on each call and signals EOF at the end. The crucial wrinkle is UTF-8 support: because a single character may span multiple bytes, each read must return a complete Unicode character rather than a raw byte.

## Task Requirements
- Read a file incrementally, one character per call (not the entire file at once).
- Return EOF when the end of the file is reached.
- Correctly handle UTF-8 encoded files, returning whole multi-byte wide characters per read rather than individual bytes.

## Language Coverage
49 languages implement this task, spanning systems languages, scripting languages, and functional languages. Representative implementations include C, C++, C#, Rust, Go, Java, Python, Haskell, Perl, Ruby, Julia, and Common Lisp.

## Connections
- [[UTF8]] — the variable-width encoding the task centers on
- [[CharacterEncoding]] — distinguishing bytes from decoded characters
- [[FileIO]] — incremental/streaming reads versus whole-file reads
- [[Unicode]] — the character set being decoded from the byte stream

## Contradictions
- None — reference task page.
