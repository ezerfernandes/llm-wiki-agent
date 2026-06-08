---
title: "Character codes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, character-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Character_codes
---

## Summary
This task asks the programmer to convert between a character and its numeric code in whichever encoding the language uses (ASCII, Unicode, etc.), in both directions. The key insight is that ASCII forms the prefix of Unicode, so a character like 'a' maps to code 97 under both schemes. It exercises a language's built-in primitives for the character-to-ordinal and ordinal-to-character mappings.

## Task Requirements
- Given a character value, print its numeric code (ASCII, Unicode code point, or whatever the language uses).
- Conversely, given a numeric code, print the corresponding character.
- Example: the character 'a' has code 97.

## Language Coverage
205 languages implement this task, reflecting that it is a fundamental, near-universal operation present in essentially every language. Representative implementations include Python, C, Java, JavaScript, Haskell, Ruby, Rust, Go, Lisp, and Forth.

## Connections
- [[ASCII]] — the classic character-to-code mapping the task references
- [[Unicode]] — modern superset of ASCII for code points
- [[CharacterEncoding]] — the general scheme mapping characters to integers
- [[StringProcessing]] — broader domain of manipulating textual data

## Contradictions
- None — reference task page.
