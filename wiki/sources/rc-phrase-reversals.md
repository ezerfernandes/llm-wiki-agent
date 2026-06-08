---
title: "Phrase reversals (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Phrase_reversals
---

## Summary
Starting from the fixed phrase "rosetta code phrase reversal", the programmer must produce three distinct transformations of the space-separated string. The key insight is distinguishing reversal at three granularities: the entire character sequence, the characters within each word, and the order of the words themselves.

## Task Requirements
- Begin with the string `rosetta code phrase reversal`.
- Reverse the characters of the entire string.
- Reverse the characters of each individual word while preserving the original word order.
- Reverse the order of the words while preserving the character order within each word.
- Display all three resulting outputs.

## Language Coverage
91 languages implement this task, reflecting broad coverage typical of basic string-manipulation exercises. Representative implementations include C, C++, Java, Python, JavaScript, Haskell, Ruby, Go, Rust, and Perl.

## Connections
- [[StringProcessing]] — the core domain of splitting, reversing, and rejoining text
- [[StringReversal]] — the underlying primitive applied at character and word levels
- [[Tokenization]] — splitting on whitespace to operate on individual words
- [[ArrayReversal]] — reversing the sequence of word tokens

## Contradictions
- None — reference task page.
