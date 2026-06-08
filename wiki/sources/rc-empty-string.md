---
title: "Empty string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Empty_string
---

## Summary
This task demonstrates how each language handles strings that contain no characters. The programmer must show three idioms: assigning an empty string to a variable, testing whether a string is empty, and testing whether a string is not empty. The key insight is that languages differ in their canonical emptiness check — some compare against a literal `""`, others inspect length, and many provide a dedicated predicate or property such as `isEmpty`, `empty?`, or `len() == 0`.

## Task Requirements
- Demonstrate how to assign an empty string to a variable.
- Demonstrate how to check that a string is empty.
- Demonstrate how to check that a string is not empty.

## Language Coverage
195 languages implement this task, reflecting how universal the concept of an empty string is across paradigms — from assembly and BASIC dialects to functional and scripting languages. Representative implementations include C, Python, Java, Haskell, Ruby, JavaScript, Rust, Go, Perl, and Lua.

## Connections
- [[StringProcessing]] — empty strings are the boundary case of string manipulation.
- [[StringLength]] — emptiness is commonly tested via a zero length check.
- [[BooleanPredicate]] — many languages expose a dedicated emptiness predicate or truthiness test.
- [[SentinelValue]] — the empty string often serves as a default or sentinel for "no value".

## Contradictions
- None — reference task page.
