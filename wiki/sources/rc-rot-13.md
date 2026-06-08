---
title: "Rot-13 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cryptography, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rot-13
---

## Summary
The task asks the programmer to implement a rot-13 function that shifts each ASCII letter 13 positions forward through the 26-letter alphabet, wrapping from z back to a. The key insight is that rot-13 is its own inverse: applying it twice restores the original text, because 13 is exactly half of 26. It is a trivially-keyed mono-alphabetic substitution cipher historically used on Usenet to obscure spoilers or offensive content rather than for real security.

## Task Requirements
- Implement rot-13 as a callable function, procedure, class, or subroutine appropriate to the language.
- Work on both upper- and lower-case letters and preserve the case of each letter.
- Pass all non-alphabetic characters through unchanged.
- Optionally wrap the function in a `tr`-like utility that rot-13-encodes input line-by-line from files named on the command line, or acts as a filter on standard input.

## Language Coverage
204 languages implement this task, making it one of Rosetta Code's most broadly covered entries, spanning systems languages, scripting languages, functional languages, and many BASIC dialects and assemblers. Representative implementations include C, C++, Python, Haskell, Ruby, Rust, Go, JavaScript, Perl, AWK, and sed.

## Connections
- [[SubstitutionCipher]] — rot-13 is the canonical trivially-keyed mono-alphabetic substitution cipher.
- [[CaesarCipher]] — rot-13 is the special case of a Caesar cipher with a fixed shift of 13.
- [[ModularArithmetic]] — the alphabet wrap-around is computed modulo 26.
- [[StringProcessing]] — the task is fundamentally a per-character string transformation.
- [[Involution]] — rot-13 is self-inverse, since two applications net a shift of 26 ≡ 0.

## Contradictions
- None — reference task page.
