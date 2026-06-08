---
title: "Respond to an unknown method call (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented, metaprogramming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Respond_to_an_unknown_method_call
---

## Summary
This task asks the programmer to make an object respond sensibly when a method that the class never defined is invoked on it. The key distinction is that this is not dynamic dispatch by a runtime-chosen name to an existing method — the called method genuinely does not exist, and the object must intercept the failed lookup. This is only meaningful in object systems that use dynamic dispatch without static type checking.

## Task Requirements
- Demonstrate intercepting an invocation of a method that is not defined in the object's class definitions.
- The handling must produce a sensible or useful response rather than a hard error.
- The method named at the call site must genuinely be undefined — not merely chosen dynamically among existing methods.
- Applicable only to object systems with dynamic dispatch and no static checking.

## Language Coverage
53 languages implement this task, spanning dynamic and scripting languages along with a few systems languages. Representative implementations include Python, Ruby, Perl, Raku, JavaScript, Smalltalk, Common Lisp, Objective-C, Lua, and Tcl.

## Connections
- [[DynamicDispatch]] — the runtime method-resolution mechanism this task hooks into
- [[Metaprogramming]] — intercepting and handling unknown calls at runtime
- [[MethodMissing]] — the hook (e.g. Ruby's `method_missing`, Python's `__getattr__`) used to catch undefined calls
- [[DuckTyping]] — the dynamic-typing philosophy that makes this pattern possible

## Contradictions
- None — reference task page.
