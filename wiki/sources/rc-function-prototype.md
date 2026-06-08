---
title: "Function prototype (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-features, functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Function_prototype
---

## Summary
This task asks the programmer to demonstrate how a given language declares function prototypes — forward declarations of a function's name, parameters, and (sometimes) return type that are separate from its body. The key insight is that prototyping is a language-specific facility: it lets a compiler know a function's signature before its full definition is seen, and languages that lack any such mechanism are explicitly excluded from the task.

## Task Requirements
- Explain any placement restrictions on where prototype declarations may appear.
- Show a prototype for a function taking no arguments.
- Show a prototype for a function taking two arguments.
- Show a prototype for a function using varargs (variadic arguments).
- Show a prototype for a function using optional arguments.
- Show a prototype for a function using named parameters.
- Show prototypes for subroutines/procedures if they differ from functions.
- Explain and exemplify any special forms of prototyping not covered above.

## Language Coverage
45 languages implement this task, spanning low-level compiled languages with mandatory forward declarations through dynamic and functional languages that emulate the concept. Representative entries include C, C++, C#, Ada, ALGOL 68, COBOL, PL/I, D, Go, Haskell, OCaml, Common Lisp, Perl, and Raku.

## Connections
- [[FunctionPrototype]] — the central declaration mechanism this task demonstrates
- [[ForwardDeclaration]] — declaring a name before its full definition
- [[TypeSignature]] — the parameter and return-type information a prototype encodes
- [[VariadicFunction]] — varargs prototypes required by the task
- [[NamedParameters]] — named/optional argument declarations required by the task

## Contradictions
- None — reference task page.
