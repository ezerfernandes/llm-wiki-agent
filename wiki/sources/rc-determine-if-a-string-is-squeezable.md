---
title: "Determine if a string is squeezable (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_a_string_is_squeezable
---

## Summary
The task asks the programmer to "squeeze" a string by removing immediate repetitions of a single *specified* character, keeping only the first occurrence of each run of that character. It differs from the closely related collapsible-string task in that only one named character is deduplicated rather than every immediately repeated character. The key insight is that the squeeze applies solely to consecutive duplicates of the target character; other characters and non-adjacent occurrences of the target are left untouched.

## Task Requirements
- Write a routine that takes a string plus a specified character and deletes any immediately repeated copies of that character (preserving the primary/first one).
- Process the string from either direction; runs of two or more of the target character collapse to one.
- For each test, display the specified character, the original string with its length, and the resulting string with its length.
- Bracket the strings with `<<<`/`>>>` (or guillemets) to make leading/trailing blanks visible.
- Use the five provided test strings (including a length-zero string and Truman's signature line), running the 5th string three times with the characters blank, minus, and lowercase `r`, for seven total results.

## Language Coverage
63 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, APL, J, Perl, Raku, and REXX.

## Connections
- [[StringProcessing]] — core domain of the task
- [[RunLengthEncoding]] — squeezing a run to one character is a degenerate RLE
- [[Deduplication]] — removing adjacent duplicates of a key
- [[FiniteStateMachine]] — single-pass scan tracking the previous character

## Contradictions
- None — reference task page.
