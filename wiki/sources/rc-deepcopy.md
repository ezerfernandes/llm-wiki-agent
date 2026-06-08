---
title: "Deepcopy (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Deepcopy
---

## Summary
The task asks the programmer to demonstrate copying a data structure so that the copy is fully independent of the original, recursively duplicating every nested value rather than sharing references. The key challenge is handling heterogeneous structures and cyclic (self- or mutually-referential) graphs, which require tracking already-visited nodes to avoid infinite recursion. The demonstration must prove the copy and original are distinct objects.

## Task Requirements
- Copy data structures containing complex heterogeneous and cyclic semantics (deep copy).
- Show the relevant semantics of the structures: homogeneous vs. heterogeneous content, and presence of reference cycles.
- Use built-in facilities, a common library, or a hand-coded procedure if no built-in exists.
- State any limitations of the chosen method.
- Demonstrate that the structure and its copy are genuinely different (independent, no shared mutable state).
- Provide links to external documentation for any common libraries used.

## Language Coverage
54 languages implement this task, spanning low-level assembly through high-level dynamic and functional languages. Representative implementations include C, C++, C#, Java, Python, JavaScript, Ruby, Rust, Go, Common Lisp, OCaml, and even 6502 Assembly.

## Connections
- [[DeepCopy]] — the central technique the task demonstrates
- [[Recursion]] — deep copying traverses nested structures recursively
- [[Serialization]] — a common implementation strategy is serialize-then-deserialize
- [[CyclicGraphs]] — cycle detection is required to copy self-referential structures
- [[ReferenceSemantics]] — distinguishing shallow (shared reference) from deep (independent) copies

## Contradictions
- None — reference task page.
