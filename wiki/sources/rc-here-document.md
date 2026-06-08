---
title: "Here document (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, syntax]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Here_document
---

## Summary
A here document (or "heredoc") is a syntactic construct for embedding a multi-line block of text directly in source code while preserving line breaks, indentation, and other whitespace. It is typically introduced by an operator such as `<<` followed by a delimiter token; the literal text begins on the next line and ends when the delimiter token reappears at the start of a line. The task asks the programmer to demonstrate the language's here document facility.

## Task Requirements
- Demonstrate the use of here documents within the chosen language.
- Show how a block of text is delimited, started, and terminated, with whitespace and line breaks preserved.

## Language Coverage
95 languages implement this task, spanning shells, scripting languages, and general-purpose languages where multi-line string literals are common. Representative implementations include UNIX Shell, Perl, Python, Ruby, PHP, Tcl, Go, Lua, Haskell, and Raku.

## Connections
- [[StringLiteral]] — a here document is a form of multi-line string literal.
- [[StringInterpolation]] — many heredocs support variable interpolation inside the block.
- [[Lexing]] — delimiter tokens are recognized during the lexical/tokenizing phase.
- [[ShellScripting]] — heredocs originate from and are heavily used in UNIX shells.

## Contradictions
- None — reference task page.
