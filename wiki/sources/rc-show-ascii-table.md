---
title: "Show ASCII table (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, character-encoding, string-processing, formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Show_ASCII_table
---

## Summary
The task asks the programmer to display the printable ASCII character set — the characters whose decimal code points run from 32 (space) to 127 (DEL) — laid out as a table. The key insight is mapping each integer code point to its corresponding glyph (e.g. via a chr-style conversion) and arranging the 96 entries into aligned columns, typically grouping by code value modulo the number of columns.

## Task Requirements
- Show the ASCII character set for decimal values 32 through 127.
- Present the values and their characters in a table format.

## Language Coverage
114 languages implement this task, reflecting very broad coverage across assembly, scripting, functional, and BASIC dialects. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Perl, and REXX.

## Connections
- [[ASCII]] — the character encoding being displayed
- [[CharacterEncoding]] — the broader category of code-point-to-glyph mappings
- [[StringFormatting]] — aligning code points and glyphs into columns
- [[ControlCharacters]] — the non-printable codes adjacent to the printable range

## Contradictions
- None — reference task page.
