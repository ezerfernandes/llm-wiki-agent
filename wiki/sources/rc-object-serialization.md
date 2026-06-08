---
title: "Object serialization (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, serialization, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Object_serialization
---

## Summary
This task asks the programmer to build a small class hierarchy using inheritance, where each class can print an instance's contents to standard output. Instances of every class are created, displayed, then written in binary form to a file named `objects.dat` via serialization (marshalling). The file is then read back and each reconstructed object is printed, demonstrating round-trip persistence of object state.

## Task Requirements
- Create a set of data types/classes based on inheritance.
- Give each class a print command that displays an instance's contents to standard output.
- Instantiate each class in the hierarchy and print them.
- Write each object to a binary file named `objects.dat` using serialization or marshalling.
- Read `objects.dat` back and print the contents of each deserialized object.

## Language Coverage
42 languages implement this task, spanning object-oriented, functional, and systems languages. Representative implementations include Java, C#, C++, Python, Ruby, Perl, Haskell, OCaml, Common Lisp, Go, and Rust.

## Connections
- [[Serialization]] — the core technique of converting object state to a byte stream
- [[Inheritance]] — the class hierarchy the task requires
- [[ObjectOrientedProgramming]] — the paradigm underlying the data types
- [[Marshalling]] — equivalent encoding mechanism named in the task
- [[BinaryFileIO]] — reading/writing the binary `objects.dat` file

## Contradictions
- None — reference task page.
