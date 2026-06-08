---
title: "Literals/String (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, syntax-elements]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Literals/String
---

## Summary
This task asks the programmer to show how character and string literals are written in a given language. The key insight is that languages differ widely in their quoting conventions: which delimiters denote a string, whether escape sequences are interpreted, whether variables are interpolated, and what special literal forms exist for multi-line or unescaped text.

## Task Requirements
- Show the literal specification of characters and strings in the language.
- If supported, demonstrate verbatim strings (quotes where escape sequences are kept literal rather than interpreted).
- If supported, demonstrate here-strings (here-documents / multi-line block literals).
- Discuss which kinds of quotes expand or interpolate variables.

## Language Coverage
144 languages implement this task, spanning scripting languages, systems languages, assembly, and markup/data formats — reflecting how universally relevant string syntax is. Representative entries include Python, Perl, Ruby, C, C++, Java, JavaScript, Go, Rust, Haskell, Tcl, and the UNIX Shell, several of which show distinct quote styles (single vs. double) with differing interpolation and escaping rules.

## Connections
- [[StringLiteral]] — the core syntactic construct the task demonstrates.
- [[EscapeSequence]] — interpreted vs. verbatim handling of backslash escapes.
- [[StringInterpolation]] — variable expansion inside certain quote styles.
- [[HereDocument]] — multi-line here-string literal form.
- [[LexicalSyntax]] — string literals as a feature of a language's lexer/tokenizer.

## Contradictions
- None — reference task page.
