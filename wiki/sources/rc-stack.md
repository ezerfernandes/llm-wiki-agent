---
title: "Stack (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stack
---

## Summary
The task asks the programmer to implement a stack: a container with last-in, first-out (LIFO) access through a single end called the "top." The key insight is that all access is restricted to that one end, which makes stacks the natural mechanism for managing nested scopes, recursion, and other LIFO resource patterns. Stacks underpin everything from CPU call frames to recursive-descent parsers.

## Task Requirements
- Create a stack supporting the basic operations:
  - `push` — store a new element onto the top of the stack.
  - `pop` — return the last pushed element and remove it from the stack.
  - `empty` — test whether the stack contains no elements.
- Optionally support `top`/`peek` to read (or write) the topmost element without removing it.

## Language Coverage
164 languages implement this task, reflecting that the stack is a foundational data structure available almost everywhere. Representative implementations span systems languages (C, C++, Rust, Go), managed languages (Java, C#, Python, Kotlin), functional languages (Haskell, OCaml, Erlang, Scheme), and low-level assembly (x86-64 Assembly, MIPS Assembly, 6502 Assembly).

## Connections
- [[DataStructures]] — the stack is one of the canonical abstract data types.
- [[LIFO]] — last-in, first-out is the defining access policy.
- [[Recursion]] — call stacks and re-entrant subprograms are implemented via stacks.
- [[StackMachine]] — a formal computational model built on stack operations.
- [[RecursiveDescentParser]] — compiler construction technique with a natural stack representation.

## Contradictions
- None — reference task page.
