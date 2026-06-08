---
title: "Non-decimal radices/Input (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-parsing, radix]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Non-decimal_radices/Input
---

## Summary
This task asks the programmer to parse a string containing a number written in a non-decimal base (most commonly binary, octal, hexadecimal, or decimal) into a numeric value, preferring the language's built-in parsing facilities. Decimal parsing is mandatory and other bases are encouraged where supported, including base-detection from a prefix such as "0x". The key insight is that most languages already expose radix-aware string-to-integer conversion, so the task is largely about discovering the idiomatic built-in.

## Task Requirements
- Parse a string assumed to contain only a number into a numeric value.
- Decimal parsing is required; other radices (binary, octal, hex, or arbitrary bases like base-19) are optional but should be demonstrated if the language supports them.
- The base may be assumed known.
- If the language can auto-detect the base from a prefix (e.g. "0x" for hex) or other syntax, that should be illustrated.

## Language Coverage
71 languages implement this task, spanning systems, scripting, and functional ecosystems. Representative implementations include C, C++, Rust, Go, Java, C#, Python, Ruby, Perl, Haskell, Common Lisp, and REXX.

## Connections
- [[RadixConversion]] — converting numbers between number bases
- [[PositionalNotation]] — the underlying representation parsed here
- [[StringParsing]] — converting textual representations to values
- [[NumberBase]] — binary, octal, hexadecimal, and arbitrary radices

## Contradictions
- None — reference task page.
