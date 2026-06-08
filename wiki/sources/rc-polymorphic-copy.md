---
title: "Polymorphic copy (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-oriented, polymorphism]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Polymorphic_copy
---

## Summary
This task explores how to duplicate a polymorphic object whose concrete (dynamic) type is unknown until run time. Given a value statically typed as a base type T but actually holding an instance of some derived type S, the goal is to produce an exact deep copy that preserves S — not merely a reference or pointer. The key insight is that ordinary copying based on the static type would slice the object down to T, so languages must rely on a virtual clone mechanism, run-time type information, or built-in deep-copy facilities to recover the true dynamic type.

## Task Requirements
- Hold an instance of a specific type S (derived from a known base type T) inside a polymorphic object/variable typed as T.
- The concrete type S may be unknown until run time.
- Create an exact copy of the object, preserving its dynamic type — not a reference and not a pointer.
- Type T must declare a method that S overrides.
- Call that overridden method on the copy to prove the copy's dynamic type is genuinely S.

## Language Coverage
53 languages implement this task, spanning statically typed OO languages that need explicit virtual-clone idioms, dynamically typed languages where copying is type-agnostic, and functional/Lisp dialects with structural copy primitives. Representative entries include Ada, C++, C#, Java, Python, Ruby, Common Lisp, OCaml, Go, Scala, Swift, and Perl.

## Connections
- [[Polymorphism]] — the core concept the task demonstrates
- [[ObjectOrientedProgramming]] — base/derived types and overridden methods
- [[VirtualMethodDispatch]] — how the overridden method resolves at run time
- [[DeepCopy]] — producing an independent duplicate rather than a reference
- [[RunTimeTypeInformation]] — recovering the dynamic type S at run time

## Contradictions
- None — reference task page.
