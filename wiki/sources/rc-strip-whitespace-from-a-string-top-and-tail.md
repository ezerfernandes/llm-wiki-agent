---
title: "Strip whitespace from a string/Top and tail (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strip_whitespace_from_a_string/Top_and_tail
---

## Summary
This task asks the programmer to remove whitespace from the ends of a string, demonstrating three distinct operations: stripping only leading whitespace, only trailing whitespace, and both. The key nuance is that "whitespace" is defined broadly to include any non-printing character without a graphical representation (spaces, tabs, newlines, and similar control characters), not just the literal space character.

## Task Requirements
- Strip leading whitespace from a string (left-trim).
- Strip trailing whitespace from a string (right-trim).
- Strip both leading and trailing whitespace from a string (full trim).
- Treat whitespace inclusively: spaces, tabs, and other non-printable/non-graphical characters all count.

## Language Coverage
128 languages implement this task, reflecting that trimming is a near-universal string operation with dedicated library support in most ecosystems. Representative implementations include Python, Java, C, C++, JavaScript, Ruby, Go, Rust, Haskell, Perl, and Common Lisp, ranging from one-line standard-library calls to manual character-scanning in assembly.

## Connections
- [[StringProcessing]] — the broader category of text manipulation this task belongs to
- [[Whitespace]] — the class of non-printing characters being stripped
- [[StringTrimming]] — the specific left/right/both trim operations demonstrated
- [[CharacterClassification]] — distinguishing printable from non-printable characters

## Contradictions
- None — reference task page.
