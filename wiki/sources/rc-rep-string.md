---
title: "Rep-string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rep-string
---

## Summary
The task asks the programmer to detect whether a binary string is a "rep-string": a string formed by repeating some prefix substring at least twice and then truncating on the right to the original length. The function must report whether the string qualifies and identify the repeating unit (or its length). The key insight is that because the unit must repeat two or more times, no candidate period can exceed half the input length, bounding the search.

## Task Requirements
- Write a function that takes a string and indicates whether it is a rep-string, returning the repeated substring or the count of repeated characters.
- When multiple valid substrings exist, reporting all, the longest, or the shortest is acceptable.
- Apply the function to a fixed list of test strings (e.g. `1001110011`, `1110111011`, `0010010010`, `1010101010`, `1111111111`, `0100101101`, `0100100`, `101`, `11`, `00`, `1`).
- Show the output on the page.

## Language Coverage
90 languages implement this task, spanning systems, scripting, and functional families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Ruby, and Common Lisp.

## Connections
- [[StringProcessing]] — core domain of substring and prefix manipulation
- [[StringPeriodicity]] — a rep-string is exactly a string with a period dividing into the prefix repetition
- [[PatternMatching]] — detecting repeated structure within a sequence
- [[BinaryString]] — inputs are series of ones and zeroes

## Contradictions
- None — reference task page.
