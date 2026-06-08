---
title: "Unicode variable names (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, unicode, identifiers, language-design]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Unicode_variable_names
---

## Summary
This task explores whether and how a programming language allows non-ASCII Unicode characters in identifier names. The programmer must document the language's rules for naming variables with characters beyond ASCII, then demonstrate by declaring a variable whose name includes the Greek delta character 'Δ', setting it to 1, incrementing it, and printing the result. The key insight is that identifier rules vary widely: many modern languages permit Unicode letters per the Unicode identifier standard (UAX #31), while older or ASCII-bound languages reject them entirely.

## Task Requirements
- Describe and link to documentation on the language's use of characters beyond ASCII in variable naming.
- Set a variable whose name includes the 'Δ' (delta) character to 1.
- Increment that variable.
- Print its value.

## Language Coverage
90 languages implement this task, spanning Unicode-friendly modern languages, classic Lisps, and assorted scripting and BASIC dialects. Representative examples include Python, JavaScript, Java, C#, Go, Rust, Swift, Julia, Haskell, Raku, Ruby, and Common Lisp.

## Connections
- [[Unicode]] — the character-encoding standard whose code points are used in identifiers.
- [[Identifiers]] — language-defined rules for naming variables and symbols.
- [[CaseSensitivity]] — closely related task on how letter case affects identifier equality.
- [[Lexical Analysis]] — the tokenizer stage that decides which characters are valid in a name.

## Contradictions
- None — reference task page.
