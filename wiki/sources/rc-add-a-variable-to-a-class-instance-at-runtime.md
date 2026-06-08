---
title: "Add a variable to a class instance at runtime (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Add_a_variable_to_a_class_instance_at_runtime
---

## Summary
This task asks the programmer to dynamically attach new instance variables (attributes) to an already-created object at runtime, rather than declaring them statically in the class definition. The key insight is that this capability — sometimes called "monkeypatching" — is trivial in dynamic languages with open or dictionary-backed objects, but requires workarounds (maps, expando wrappers, or reflection) in statically typed languages. It is useful when an instance's shape depends on data not known until runtime, such as building an object-oriented CSV parser whose fields come from the file header.

## Task Requirements
- Demonstrate adding one or more variables to an existing class instance after the object has been created.
- The addition must happen at runtime, not via a fixed/static field declaration.

## Language Coverage
69 languages implement this task, spanning highly dynamic scripting languages where it is built-in and stricter statically typed languages where it must be emulated. Representative examples include Python, Ruby, JavaScript, Perl, PHP, Lua, Common Lisp, Java, C#, and Go.

## Connections
- [[Metaprogramming]] — adding members at runtime is a core metaprogramming technique
- [[MonkeyPatching]] — the common name for runtime modification of objects/classes
- [[Reflection]] — statically typed languages reach this via reflective or dynamic-object APIs
- [[ObjectOrientedProgramming]] — the task concerns mutable object/class instances
- [[DynamicTyping]] — open objects and dictionary-backed instances enable the feature directly

## Contradictions
- None — reference task page.
