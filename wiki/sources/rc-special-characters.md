---
title: "Special characters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, lexical-syntax]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Special_characters
---

## Summary
This task asks the programmer to document a language's special characters — the symbols or character sequences that carry a built-in syntactic meaning and therefore cannot normally appear in identifiers. It also asks for the corresponding escape sequences, the mechanism each language provides to strip that special meaning and use the symbol as ordinary text. The key insight is that the answer is inherently language-specific: it is a survey of lexical and syntactic conventions rather than an algorithm.

## Task Requirements
- List the language's special characters (single characters or sequences with reserved/built-in meaning).
- Show the escape sequences the language uses to neutralize that special meaning.
- Cover cases where escaping is possible, and note where a character cannot be escaped.

## Language Coverage
87 languages implement this task, spanning high-level scripting languages, systems languages, assembly dialects, and markup/typesetting systems — reflecting that nearly every language has its own lexical conventions. Representative entries include C, C++, Java, Python, Perl, Ruby, Rust, Go, Haskell, Tcl, and even markup-oriented systems like HTML, LaTeX, and XSLT.

## Connections
- [[StringProcessing]] — the task is fundamentally about how strings and tokens are lexed
- [[EscapeSequence]] — the central mechanism for disabling special meaning
- [[LexicalAnalysis]] — special characters define token boundaries in a language's grammar
- [[CharacterEncoding]] — escapes often reference code points or control characters

## Contradictions
- None — reference task page.
