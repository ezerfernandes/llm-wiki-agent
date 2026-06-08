---
title: "Program termination (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, process-management]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Program_termination
---

## Summary
This task asks the programmer to show the syntax for a complete, immediate stoppage of a program from inside a conditional, including the termination of all threads and processes that belong to the program. The key insight is that abrupt termination often skips language-level cleanup (object finalizers, destructors, run-on-exit hooks) and relies instead on the operating system to reclaim resources.

## Task Requirements
- Show the syntax for a complete stoppage of a program triggered inside a conditional structure.
- Ensure the termination covers all threads and processes that are part of the program.
- Explain the cleanup (or lack thereof) the termination causes regarding allocated memory, database connections, open files, object finalizers/destructors, and run-on-exit hooks.
- Note that, unless otherwise described, no cleanup beyond what the operating system provides is performed.

## Language Coverage
149 languages implement this task, reflecting very broad coverage across systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Erlang, and assembly variants such as Z80 Assembly and 6502 Assembly.

## Connections
- [[ConditionalStructures]] — termination is invoked from within a conditional branch
- [[ProcessManagement]] — stopping all threads and processes of the program
- [[ResourceCleanup]] — handling of memory, files, and database connections at exit
- [[Destructors]] — object finalizers that may or may not run during abrupt termination

## Contradictions
- None — reference task page.
