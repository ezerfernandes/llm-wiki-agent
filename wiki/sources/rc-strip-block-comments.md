---
title: "Strip block comments (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strip_block_comments
---

## Summary
The task is to remove block comments from program text written in a C-like language, where a comment begins with a beginning delimiter and ends with an ending delimiter (by default the two-character sequences `/*` and `*/`), inclusive. The key insight is to scan for the opening delimiter and then discard everything up to and including the next closing delimiter, handling multi-line spans and tricky cases like `/*/ ... */` where the slash that could close also opens.

## Task Requirements
- Strip simple, non-nested, multi-line block comments from sample program text.
- Use `/*` as the beginning delimiter and `*/` as the ending delimiter.
- Correctly handle the tricky case `/*/ <-- tricky comments */`.
- Extra credit: do not hard-code the delimiters; let the caller specify the beginning and ending sequences (optionally via optional parameters).

## Language Coverage
65 languages implement this task, spanning systems languages, scripting languages, and assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Haskell, and AArch64 Assembly.

## Connections
- [[StringProcessing]] — the core operation is scanning and rewriting a character stream
- [[Parsing]] — recognizing delimiter-bounded regions resembles a minimal tokenizer/lexer
- [[Lexer]] — comment stripping is a preprocessing step real lexers perform
- [[RegularExpressions]] — many solutions match the comment span with a non-greedy regex

## Contradictions
- None — reference task page.
