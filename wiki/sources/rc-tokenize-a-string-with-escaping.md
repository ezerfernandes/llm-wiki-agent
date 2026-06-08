---
title: "Tokenize a string with escaping (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tokenize_a_string_with_escaping
---

## Summary
This task asks the programmer to write a function that splits a string into fields at each separator character, while respecting an escape character. The key insight is that a separator preceded by an unescaped escape character is treated as a literal character rather than a delimiter, and the escape characters that perform escaping are removed from the output. This is a stateful character-by-character scan rather than a naive split, since standard library split functions cannot honor escaping.

## Task Requirements
- Accept three inputs: the string, the separator character, and the escape character.
- Output a list of strings (the fields).
- Split only at separators that are not escaped.
- Preserve empty fields, including at the start and end of the input.
- "Escaped" means preceded by an escape character that is not itself already escaped.
- An escape character before a non-special character still consumes the escape but does nothing special.
- Escape characters used for escaping must not appear in the output.
- Test case: `one^|uno||three^^^^|four^^^|^cuatro|` with separator `|` and escape `^` yields `one|uno`, ``, `three^^`, `four^|cuatro`, ``.

## Language Coverage
62 languages implement this task, spanning systems languages, scripting languages, functional languages, and assembly. Representative implementations include C, C++, Rust, Go, Python, Haskell, OCaml, Common Lisp, Perl, Raku, Java, and 8080 Assembly.

## Connections
- [[StringProcessing]] — core domain of splitting and field extraction
- [[Tokenization]] — breaking input into discrete tokens
- [[FiniteStateMachine]] — the escape-aware scan is naturally modeled as a small state machine
- [[EscapeCharacter]] — the central mechanism distinguishing this from a plain split
- [[Lexing]] — closely related to lexical analysis in parsers

## Contradictions
- None — reference task page.
