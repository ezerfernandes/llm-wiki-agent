---
title: "Determine if a string is numeric (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_a_string_is_numeric
---

## Summary
The task asks for a boolean function that takes a string and reports whether it represents a valid number — including floating-point and negative values — according to the language's own syntax for numeric literals or string-to-number conversion. The key insight is that "numeric" is defined relative to each language's parsing rules, so most idiomatic solutions lean on the built-in conversion/parse machinery (catching failure) rather than hand-rolling a validator.

## Task Requirements
- Implement a function accepting a string and returning a boolean.
- Return true when the string is a numeric string, false otherwise.
- Accept floating-point notation and negative numbers.
- Judge validity using the language's native numeric-literal syntax or its string-to-number conversion.

## Language Coverage
170 languages implement this task, reflecting its status as a fundamental text-processing exercise spanning scripting, systems, and assembly languages. Representative implementations include Python, JavaScript, C, Java, Ruby, Haskell, Rust, Go, Perl, and even low-level entries like 6502 Assembly and MIPS Assembly.

## Connections
- [[StringProcessing]] — the task is fundamentally about classifying string content
- [[Parsing]] — validating numeric syntax is a parsing problem
- [[TypeConversion]] — most idiomatic solutions attempt string-to-number coercion and catch failures
- [[RegularExpressions]] — a common technique for matching numeric-literal patterns
- [[ExceptionHandling]] — "try to parse, catch the error" is a recurring implementation pattern

## Contradictions
- None — reference task page.
