---
title: "Find limit of recursion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, stack]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_limit_of_recursion
---

## Summary
This task asks the programmer to determine how deeply a function can call itself before the language runtime fails. The usual approach is a function that recurses while incrementing a depth counter and reports the count reached when the program hits a stack overflow or interpreter-imposed recursion limit. The key insight is that the limit reflects the call stack size (or a configured guard), so it varies by language, platform, and stack settings rather than being a universal constant.

## Task Requirements
- Write code that recurses (typically a self-calling function carrying a depth counter).
- Trigger and observe the failure point — stack overflow, segfault, or an interpreter-enforced recursion ceiling.
- Report the recursion depth reached at the limit.

## Language Coverage
131 languages implement this task, spanning low-level assembly, systems, scripting, and functional languages — illustrating how stack behavior differs across runtimes. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Lisp, Lua, and Perl.

## Connections
- [[Recursion]] — the core mechanism the task exercises.
- [[CallStack]] — the limit is governed by available stack frames.
- [[StackOverflow]] — the failure condition that defines the limit.
- [[TailCallOptimization]] — languages with it may recurse without bound, sidestepping the limit.

## Contradictions
- None — reference task page.
