---
title: "Break OO privacy (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented, reflection, metaprogramming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Break_OO_privacy
---

## Summary
This task asks the programmer to access private or protected members of a class from outside an instance, without going through any public or protected accessor as a proxy. The point is to demonstrate the escape hatch — reflection, introspection, or some other intentional mechanism — that a debugger, serializer, or meta-programming tool would use to read normally-encapsulated state. Crucially, raw memory peeking/poking is explicitly disallowed; the access must stay within the language's own facilities.

## Task Requirements
- Read or otherwise access a private/protected member of a class instance from outside that instance.
- Do not call any non-private/non-protected member of the class as an intermediary proxy.
- Use a language-provided escape hatch (reflection, introspection, metaprogramming) rather than heroic measures like raw memory access.
- The task acknowledges this is generally unidiomatic and considered poor practice; languages that intentionally permit it can show it off.

## Language Coverage
46 languages implement this task, spanning statically-typed OO languages with formal reflection APIs and dynamic languages where encapsulation is largely a convention. Representative examples include Java, C#, C++, Python, Ruby, Go, Swift, Kotlin, Scala, Perl, and Common Lisp.

## Connections
- [[Reflection]] — the primary mechanism most languages use to bypass access modifiers
- [[Encapsulation]] — the OO principle this task deliberately circumvents
- [[Metaprogramming]] — debuggers and serializers rely on this kind of access
- [[ObjectOrientedProgramming]] — the paradigm whose privacy guarantees are at issue
- [[AccessModifiers]] — private/protected visibility is what is being broken

## Contradictions
- None — reference task page.
