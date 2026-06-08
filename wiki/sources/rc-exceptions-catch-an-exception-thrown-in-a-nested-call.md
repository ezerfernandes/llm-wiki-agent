---
title: "Exceptions/Catch an exception thrown in a nested call (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, exception-handling, control-flow]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Exceptions/Catch_an_exception_thrown_in_a_nested_call
---

## Summary
This task asks the programmer to demonstrate user-defined exceptions and selective exception handling across a call stack. The key insight is that an exception thrown deep in nested function calls can propagate upward and be caught by a handler several frames away, and that a handler can be made to catch only specific exception types while letting others continue propagating.

## Task Requirements
- Create two user-defined exceptions, U0 and U1.
- Have function foo call function bar twice.
- Have function bar call function baz.
- Arrange for baz to throw U0 on its first call and U1 on its second.
- Function foo should catch only U0, not U1.
- Show or describe what happens when the program runs (U1 should escape foo and remain uncaught/terminate).

## Language Coverage
79 languages implement this task, spanning mainstream object-oriented and functional languages as well as scripting and BASIC dialects. Representative implementations include Java, C#, C++, Python, Ruby, Haskell, Erlang, Common Lisp, Rust, and Scala.

## Connections
- [[ExceptionHandling]] — the core mechanism the task exercises
- [[StackUnwinding]] — how a thrown exception propagates up through nested frames
- [[ControlFlow]] — exceptions as a non-local control-transfer construct
- [[CustomExceptionTypes]] — defining U0 and U1 as distinct user types enables selective catching

## Contradictions
- None — reference task page.
