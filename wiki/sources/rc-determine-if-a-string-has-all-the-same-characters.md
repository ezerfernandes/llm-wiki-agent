---
title: "Determine if a string has all the same characters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_a_string_has_all_the_same_characters
---

## Summary
This task asks the programmer to write a routine that scans a string left-to-right and decides whether every character is identical. The key insight is that the result is more than a boolean: when the string is not uniform, the routine must report the first differing character, its 1-based position, and its hexadecimal code. An empty string is defined as trivially "all the same."

## Task Requirements
- Create a function that determines whether all characters in a string are the same.
- For each test string, display the string and its length as it is examined.
- Treat a zero-length (empty) string as all the same character(s).
- Process characters left-to-right.
- If all characters match, display a message saying so.
- If not, report that fact, the first character that differs, its position in the string, and the hexadecimal value of that character.
- Run at least seven test values: empty string, three blanks, "2", "333", ".55", "tttTTT", and "4444 444k".
- Show all output on the page.

## Language Coverage
82 languages implement this task, spanning systems languages, functional languages, scripting languages, and esoteric ones. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, REXX, and J.

## Connections
- [[StringProcessing]] — the core domain of scanning and comparing characters.
- [[CharacterEncoding]] — reporting the differing character's hexadecimal code point.
- [[LinearSearch]] — finding the first index whose character breaks uniformity.
- [[EdgeCaseHandling]] — defining the empty string as trivially uniform.

## Contradictions
- None — reference task page.
