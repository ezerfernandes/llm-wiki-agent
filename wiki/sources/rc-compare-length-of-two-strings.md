---
title: "Compare length of two strings (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compare_length_of_two_strings
---

## Summary
Given two strings of differing length, determine which is longer or shorter, then print each string with its length on its own line, longest first. The key nuance is that "length" may be measured in bytes or in characters depending on what is natural for the language, which matters for multi-byte or Unicode-aware encodings.

## Task Requirements
- Take two strings of different length and compare their lengths.
- Print both strings together with their respective lengths, one per line.
- Print the longer string first.
- Measure length in bytes or characters as appropriate; note if the language lacks a length operator.
- Extra credit: given a list of more than two strings (e.g. `["abcd","123456789","abcdef","1234567"]`), output them sorted in descending length order.

## Language Coverage
74 languages implement this task, spanning systems and assembly languages through high-level scripting and functional languages. Representative implementations include C, C++, Rust, Go, Python, JavaScript, Haskell, Perl, Raku, and AArch64 Assembly.

## Connections
- [[StringLength]] — the core operation of measuring a string's size
- [[StringProcessing]] — the broader category this task belongs to
- [[Sorting]] — the extra credit requires ordering strings by length
- [[CharacterEncoding]] — byte-vs-character length depends on the encoding model

## Contradictions
- None — reference task page.
