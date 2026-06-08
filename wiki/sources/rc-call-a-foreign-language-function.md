---
title: "Call a foreign-language function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, foreign-function-interface, interop, memory-management]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Call_a_foreign-language_function
---

## Summary
This task demonstrates how a program written in one language can invoke a function implemented in another language, using C as the canonical example. The reference exercise builds a native string containing "Hello World!", passes its contents to C's `strdup` (which heap-allocates a duplicate), retrieves and prints the result, then frees the allocation. The key insight is bridging differing data representations and memory ownership conventions across the language boundary.

## Task Requirements
- Show how a foreign-language function can be called from the host language.
- Create a native string holding "Hello World!" of the type idiomatic to the language.
- Pass the string's contents to C's `strdup`, copying the data if necessary.
- Retrieve the result returned by `strdup` and print it using the host language's facilities.
- Free the heap-allocated result of `strdup` to avoid a memory leak.
- The C runtime may be linked statically or dynamically; using `strdup` specifically is not mandatory if it would be uninformative for the FFI being shown.

## Language Coverage
87 languages implement this task, spanning compiled systems languages, scripting languages, functional languages, and several assembly variants — reflecting how universal cross-language interop is. Representative implementations include C, C++, Rust, Go, Python, Haskell, OCaml, Java, Lua, and Common Lisp.

## Connections
- [[ForeignFunctionInterface]] — the core mechanism the task exercises
- [[LanguageInteroperability]] — calling across language boundaries
- [[MemoryManagement]] — explicit heap allocation and freeing of the duplicated string
- [[DynamicLinking]] — loading the C runtime at link or load time
- [[CStringHandling]] — null-terminated string representation passed to `strdup`

## Contradictions
- None — reference task page.
