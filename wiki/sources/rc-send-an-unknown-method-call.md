---
title: "Send an unknown method call (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reflection, metaprogramming, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Send_an_unknown_method_call
---

## Summary
This task asks the programmer to invoke an object method when the method's name is not known until run time — that is, the name is computed or supplied dynamically (e.g. as a string) rather than hard-coded in the source. The key insight is that this requires language support for dynamic dispatch or reflection, so the method can be resolved and called from a runtime value rather than a compile-time identifier.

## Task Requirements
- Invoke an object method where the name of the method to be invoked can be generated at run time.

## Language Coverage
53 languages implement this task, spanning dynamic, reflective, and statically-typed-with-reflection languages. Representative implementations include Python, Ruby, JavaScript, Java, C#, Common Lisp, Smalltalk, Perl, Tcl, and Go.

## Connections
- [[Reflection]] — resolving and calling methods by name at run time
- [[Metaprogramming]] — programs that manipulate their own dispatch behavior
- [[DynamicDispatch]] — selecting the method to run based on a runtime value
- [[RespondToUnknownMethodCall]] — the complementary receiving-side task
- [[RuntimeEvaluation]] — related task on evaluating code at run time

## Contradictions
- None — reference task page.
