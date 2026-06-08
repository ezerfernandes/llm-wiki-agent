---
title: "Return multiple values (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-semantics, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Return_multiple_values
---

## Summary
This task asks the programmer to show how a function can return more than one value to its caller. The key insight is that most languages lack a literal "multiple return" primitive, so the idiom is to bundle results into a composite — a tuple, list, array, record/struct, object, or map — or to use out-parameters/references; some languages (Go, Python, Lua, Common Lisp) offer native multiple-value return or tuple unpacking.

## Task Requirements
- Demonstrate returning more than one value from a single function.
- Use whatever mechanism the language provides (tuple, list, array, struct/record, object, by-reference/out parameters, multiple-value return, etc.).

## Language Coverage
140 languages implement this task, spanning everything from low-level assembly (where values come back in multiple registers) to functional and scripting languages with first-class tuples. Representative entries include Python, Go, Lua, Common Lisp, Haskell, Rust, C, C++, Java, JavaScript, and Perl.

## Connections
- [[Tuple]] — the canonical container for grouping return values
- [[DataStructures]] — arrays, records, and maps used to bundle results
- [[Functions]] — the calling/return convention being exercised
- [[PassByReference]] — out-parameters as an alternative to a single return value
- [[Destructuring]] — unpacking a composite return back into named variables

## Contradictions
- None — reference task page.
