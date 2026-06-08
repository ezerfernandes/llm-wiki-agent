---
title: "Terminal control/Display an extended character (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, text-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Terminal_control/Display_an_extended_character
---

## Summary
This task asks the programmer to print a single non-ASCII character to the terminal — specifically the British pound sign (£, GBP currency sign). The core challenge is character encoding: emitting a character beyond the 7-bit ASCII range requires knowing the terminal's encoding (UTF-8, Latin-1, etc.) and writing the correct byte sequence so the glyph renders correctly.

## Task Requirements
- Display an extended (non-ASCII) character onto the terminal.
- The specific character to output is the pound sign £ (GBP currency sign).

## Language Coverage
70 languages implement this task, spanning systems languages, scripting languages, BASIC dialects, and Lisp variants. Representative implementations include C, C++, C#, Java, Python, Perl, Raku, Ruby, Go, Haskell, Lua, and Common Lisp.

## Connections
- [[CharacterEncoding]] — selecting the right byte representation for the glyph
- [[Unicode]] — code point U+00A3 for the pound sign
- [[UTF8]] — common multi-byte encoding used by modern terminals
- [[TerminalControl]] — writing output to a console device

## Contradictions
- None — reference task page.
