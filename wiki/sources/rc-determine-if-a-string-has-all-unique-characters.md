---
title: "Determine if a string has all unique characters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_a_string_has_all_unique_characters
---

## Summary
The task asks the programmer to write a routine that decides whether every character in a string is distinct. When a duplicate is found, the routine must report the first repeated character, the positions of both occurrences, and that character's hexadecimal value. An empty string counts as unique, and characters are processed left to right.

## Task Requirements
- Implement a function that determines whether all characters in a string are unique.
- Display each test string along with its length as it is examined.
- Treat a zero-length (empty) string as unique.
- Process characters from left to right.
- If unique, print a message saying so.
- If not unique, report which character is duplicated (only the first non-unique one), where both copies are located, and the hexadecimal value of that character.
- Test with at least five strings: empty, a single period, "abcABC", "XYZ ZYX" (blank in the middle), and a 36-character string lacking the letter "O".

## Language Coverage
66 languages implement this task, spanning systems, scripting, functional, and esoteric families. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, J, and Raku.

## Connections
- [[StringProcessing]] — the task centers on inspecting and comparing characters within a string.
- [[HashSet]] — a common O(n) approach tracks seen characters in a set or boolean array.
- [[CharacterEncoding]] — reporting the hexadecimal value ties to ASCII/Unicode code points.
- [[DuplicateDetection]] — detecting the first repeated element is the core algorithmic problem.

## Contradictions
- None — reference task page.
