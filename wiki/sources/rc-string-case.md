---
title: "String case (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/String_case
---

## Summary
This task asks the programmer to take the string "alphaBETA" and convert it to both upper-case and lower-case, using the language's default string encoding (or plain ASCII when there is no string literal). The key insight is that case conversion is not always reversible across alphabets, so applying toLower then toUpper need not round-trip to the original. Implementations are also encouraged to show any extra case helpers their standard library offers.

## Task Requirements
- Convert "alphaBETA" to upper-case ("ALPHABETA").
- Convert "alphaBETA" to lower-case ("alphabeta").
- Use the language's default string-literal encoding, or plain ASCII if it has no string literal.
- Optionally demonstrate additional case functions such as swap-case or capitalizing the first letter.

## Language Coverage
194 languages implement this task, reflecting that case folding is a near-universal string-library primitive. Representative implementations include Python, C, C++, Java, JavaScript, Rust, Go, Haskell, Ruby, and Perl.

## Connections
- [[StringProcessing]] — case conversion is a core string-manipulation operation
- [[CharacterEncoding]] — default encoding determines how characters map between cases
- [[ASCII]] — the fallback encoding when a language lacks string literals
- [[CaseFolding]] — the general technique of normalizing letter case, which is not always reversible

## Contradictions
- None — reference task page.
