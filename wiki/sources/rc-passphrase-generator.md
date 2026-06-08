---
title: "Passphrase generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, random-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Passphrase_generator
---

## Summary
The task asks the programmer to generate a passphrase composed of n words, where each word is formatted according to a fixed pattern. The core work is selecting words (typically from a dictionary or a hardcoded list), capitalizing them, appending a random number, and joining them with separators. The interesting bit is composing several small transformations into a single formatted output string.

## Task Requirements
- Generate a passphrase made of n words.
- Every word must start with an uppercase letter.
- Every word must have a number appended after its last letter.
- Every word except the last must be followed by a hyphen separator (-).
- Example output for n = 5: `Hello92-Butterfly89-Elephant55-Rainbow44-Sunshine38`.

## Language Coverage
20 languages implement this task, with broad coverage across BASIC dialects, scripting languages, and functional languages. Representative implementations include Python, Perl, Raku, Ruby, Julia, Racket, Scheme, R, FreeBASIC, and Wren.

## Connections
- [[RandomNumberGeneration]] — appending a random number to each word
- [[StringFormatting]] — capitalization, concatenation, and separator joining
- [[PasswordSecurity]] — passphrases as a usability-oriented authentication scheme
- [[Tokenization]] — composing output from discrete word units

## Contradictions
- None — reference task page.
