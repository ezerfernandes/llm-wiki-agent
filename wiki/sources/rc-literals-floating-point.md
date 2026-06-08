---
title: "Literals/Floating point (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, syntax, floating-point]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Literals/Floating_point
---

## Summary
This task asks the programmer to demonstrate the syntactic forms a language accepts for writing floating-point literals directly in source code. It is a syntax-survey task rather than an algorithmic one, covering decimal and alternative bases, exponential (scientific) notation, and any language-specific features such as digit separators or typed suffixes. Authors are encouraged to include a regular expression or BNF/ABNF/EBNF grammar defining the legal literal format.

## Task Requirements
- Show how floating-point literals are expressed in the language.
- Cover decimal notation and any other supported bases.
- Cover exponential / scientific notation (e.g. `1.5e-3`).
- Document any other special features (digit separators, type suffixes like `f`/`d`, hexadecimal floats, etc.).
- Optionally provide a regex or BNF/ABNF/EBNF grammar defining the allowable formats.

## Language Coverage
101 languages implement this task, spanning assembly, scripting, functional, and systems languages. Representative entries include C, C++, C#, Java, JavaScript, Python, Rust, Go, Haskell, Common Lisp, Fortran, and REXX.

## Connections
- [[FloatingPoint]] — the IEEE 754 numeric domain these literals denote
- [[LexicalAnalysis]] — literal recognition is a tokenizer concern
- [[FormalGrammar]] — BNF/ABNF/EBNF specifications requested by the task
- [[RegularExpression]] — alternative way to define allowable literal formats
- [[ScientificNotation]] — the exponential form of the literals

## Contradictions
- None — reference task page.
