---
title: "Variable size/Get (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, type-system, introspection, memory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Variable_size/Get
---

## Summary
This task asks the programmer to demonstrate how to determine the size of a variable, typically measured in bytes occupied in memory. The key insight is that "size" is language-dependent: in low-level languages it reflects the storage footprint of a fixed-width type, while in high-level dynamic languages it may require runtime introspection or be only loosely defined. It is presented as a companion to host introspection.

## Task Requirements
- Demonstrate how to obtain the size of a variable.
- Express the size in the language's natural unit (usually bytes).

## Language Coverage
73 languages implement this task, spanning systems languages with explicit memory layout, scripting languages, and functional languages. Representative implementations include C (sizeof), C++, Rust, Go, D, Ada, Fortran, Python, Perl, Ruby, Java, and Haskell.

## Connections
- [[TypeSystem]] — variable size is governed by the type's storage representation
- [[MemoryLayout]] — byte size reflects how a value is laid out in memory
- [[Introspection]] — dynamic languages discover size via runtime reflection
- [[PrimitiveDataTypes]] — fixed-width primitives have well-defined sizes

## Contradictions
- None — reference task page.
