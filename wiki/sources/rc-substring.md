---
title: "Substring (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, unicode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Substring
---

## Summary
This task asks the programmer to extract and display substrings from a larger string using five different addressing schemes. The key subtlety is that when a language uses UTF-8 or UTF-16, the extraction must operate on logical characters (Unicode code points) rather than raw 8-bit or 16-bit code units, so it works correctly for characters outside the Basic Multilingual Plane.

## Task Requirements
- Display a substring starting at offset `n` characters in, of length `m`.
- Display a substring starting at offset `n` characters in, up to the end of the string.
- Display the whole string minus its last character.
- Display a substring starting from a known character within the string, of length `m`.
- Display a substring starting from a known substring within the string, of length `m`.
- For UTF-8/UTF-16 programs, all positions must be measured in code points, not code units, and must handle code points above the BMP.

## Language Coverage
150 languages implement this task, reflecting its status as a basic string-manipulation exercise present across nearly every language family. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Perl, Ruby, Go, and Rust, alongside niche and assembly entries like ARM Assembly and RISC-V Assembly.

## Connections
- [[StringProcessing]] — core string slicing and extraction operations
- [[Unicode]] — code-point-aware indexing requirement
- [[StringSearch]] — locating a known character or substring before slicing
- [[CharacterEncoding]] — UTF-8/UTF-16 code unit vs. code point distinction

## Contradictions
- None — reference task page.
