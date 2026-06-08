---
title: "Named parameters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-features, function-calls]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Named_parameters
---

## Summary
This task asks the programmer to create a function whose arguments are supplied by name rather than (necessarily) by position, and to demonstrate calling it. The key idea is that a call can explicitly bind each parameter name to its argument — e.g. `func1(paramname2=argument2, paramname1=argument1)` — making the binding independent of argument order. Where the language allows it, the solution should also show argument reordering and optionally omitting some arguments.

## Task Requirements
- Define a function accepting several arguments identified by name, not just position.
- Show calling it normally with positional arguments.
- Show calling it with each argument explicitly bound to its parameter name.
- Demonstrate that named binding works irrespective of argument order.
- If supported, note reordering of arguments and optional omission of some arguments.

## Language Coverage
76 languages implement this task, spanning mainstream languages with first-class keyword-argument support and others that emulate the feature via maps, records, or option records. Representative implementations include Python, Ruby, C#, Kotlin, Swift, Common Lisp, Scala, Perl, PowerShell, and Tcl.

## Connections
- [[KeywordArguments]] — the language feature this task showcases
- [[OptionalParameters]] — closely related, often combined with named arguments
- [[Varargs]] — variadic argument handling, a sibling Rosetta Code task
- [[FunctionCallConventions]] — how arguments are bound to parameters at call time

## Contradictions
- None — reference task page.
