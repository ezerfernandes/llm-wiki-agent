---
title: "Introspection (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reflection, runtime-environment]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Introspection
---

## Summary
This task asks the programmer to use a language's introspection (reflection) facilities to examine its own running environment. Specifically, it must verify the version of the active compiler/interpreter/runtime and exit if it is too old, then check at runtime whether a variable named `bloop` and a math function `abs()` exist, computing `abs(bloop)` only if both are present. The key insight is that programs can query their own state, available bindings, and host version rather than assuming them.

## Task Requirements
- Verify the version/revision of the currently running compiler, interpreter, byte-compiler, or runtime, and exit if it is too old.
- Check at runtime whether the variable `bloop` exists.
- Check at runtime whether the math function `abs()` is available.
- If both exist, compute `abs(bloop)`.
- Extra credit: report the number of integer variables in global scope and their sum.

## Language Coverage
88 languages implement this task, spanning interpreted scripting languages, compiled systems languages, Lisps, and BASIC dialects, since introspection support varies widely. Representative implementations include Python, Ruby, Perl, JavaScript, Common Lisp, Java, C#, Go, Rust, Tcl, and Racket.

## Connections
- [[Reflection]] — querying and acting on program structure at runtime
- [[RuntimeEnvironment]] — inspecting the host interpreter/compiler version
- [[DynamicTyping]] — checking existence of variables and functions at runtime
- [[Metaprogramming]] — programs that examine and reason about themselves

## Contradictions
- None — reference task page.
