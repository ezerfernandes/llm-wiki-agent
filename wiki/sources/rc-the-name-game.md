---
title: "The Name Game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/The_Name_Game
---

## Summary
The task asks the programmer to generate the lyrics of Shirley Ellis's song "The Name Game" for a given input name. The core insight is that the rhyming verse is built by stripping the name's first letter to form a suffix and prepending fixed consonant prefixes (b-, f-, m-), with three special cases that adjust how the truncation and prefixing are applied.

## Task Requirements
- Accept a name as input and print the four-line verse.
- Default rule: drop the name's first letter to make the rhyming stem, then build "(X), (X), bo-b(Y) / Banana-fana fo-f(Y) / Fee-fi-mo-m(Y) / (X)!".
- Vowel first letter (A, E, I, O, U): do not truncate the name when forming the stem.
- 'B', 'F', or 'M' first letter: the line whose prefix matches that letter is sung without the leading prefix (avoiding a doubled consonant).

## Language Coverage
60 languages implement this task, showing broad coverage across general-purpose and niche languages. Representative examples include Python, C, C++, Java, JavaScript, Go, Rust, Haskell, Ruby, Perl, and REXX.

## Connections
- [[StringManipulation]] — slicing and concatenation of name fragments
- [[CaseInsensitivity]] — first-letter classification ignores letter case
- [[ConditionalLogic]] — branching for vowel and B/F/M special cases
- [[TextGeneration]] — templated lyric output

## Contradictions
- None — reference task page.
