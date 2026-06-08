---
title: "Call a function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functions, language-semantics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Call_a_function
---

## Summary
This task asks the programmer to demonstrate the full range of syntax and semantics a language offers for *calling* (invoking) a function — explicitly not for defining one. The key insight is that calling conventions vary widely across languages, so the task is really a survey of each language's parameter-passing and invocation model rather than an algorithm.

## Task Requirements
- Call a function that takes no arguments.
- Call a function with a fixed number of arguments.
- Call a function with optional arguments.
- Call a function with a variable number of arguments (variadic).
- Call a function with named arguments.
- Use a function in statement context (discarding its result).
- Use a function in first-class context within an expression.
- Obtain the return value of a function.
- Distinguish built-in functions from user-defined ones.
- Distinguish subroutines from functions.
- State whether arguments are passed by value or by reference.
- Note whether partial application is possible and how.

## Language Coverage
126 languages implement this task, making it one of the broadest entries on the site since nearly every language has a way to invoke a function. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Common Lisp, Rust, Ruby, Go, and several assembly dialects (x86, ARM, 68000).

## Connections
- [[FirstClassFunctions]] — passing and using functions as values within expressions.
- [[VariadicFunction]] — calling with a variable number of arguments.
- [[NamedParameters]] — invoking with named/keyword arguments.
- [[PartialApplication]] — fixing some arguments to produce a new callable.
- [[ParameterPassing]] — by-value versus by-reference argument semantics.

## Contradictions
- None — reference task page.
