---
title: "Delegates (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, design-patterns, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Delegates
---

## Summary
This task asks the programmer to implement the delegation design pattern, in which one object (the delegator) hands off a responsibility to an optional helper object (the delegate). The key insight is graceful fallback: the delegator calls a method on its delegate only if the delegate exists and responds to that message, otherwise it supplies a default implementation. This pattern is central to Apple's Cocoa frameworks.

## Task Requirements
- The delegator keeps an optional reference to a delegate instance.
- The delegator implements an "operation" method that returns the delegate's "thing" result if the delegate responds to "thing", otherwise returns the string "default implementation".
- The delegate implements "thing", returning the string "delegate implementation".
- Demonstrate three cases: no delegate at all, a delegate that does not implement "thing", and a delegate that does implement "thing".

## Language Coverage
61 languages implement this task, spanning classic OO languages, dynamic scripting languages, and functional languages. Representative implementations include Java, C#, C++, Objective-C, Python, Ruby, Smalltalk, Swift, Go, and Common Lisp.

## Connections
- [[DelegationPattern]] — the core design pattern being demonstrated
- [[ObjectOrientedProgramming]] — paradigm underlying the task
- [[Duck Typing|DuckTyping]] — responding-to-message checks rely on runtime capability detection
- [[Composition Over Inheritance|CompositionOverInheritance]] — delegation favors object composition for reuse
- [[Cocoa]] — Apple framework that heavily uses this pattern

## Contradictions
- None — reference task page.
