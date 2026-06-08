---
title: "Copy stdin to stdout (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, io, streams]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Copy_stdin_to_stdout
---

## Summary
This task asks the programmer to create an executable file (or a script run via an interpreter at the command line) that reads everything from standard input and writes it unchanged to standard output. The key insight is that this is the minimal pass-through filter: in many languages it reduces to copying a stream, and in some (like the Unix shell `cat`) it is essentially a no-op that already exists as a built-in tool.

## Task Requirements
- Produce an executable file or an interpretable script invoked from the command line.
- Read data from standard input (stdin).
- Write that data unchanged to standard output (stdout).

## Language Coverage
75 languages implement this task, spanning low-level assembly, classic languages, functional languages, scripting languages, and esolangs. Representative implementations include 8086 Assembly, C, C++, Haskell, Python, Perl, Ruby, Rust, Go, UNIX Shell, and Brainf***.

## Connections
- [[StandardStreams]] — stdin/stdout are the core I/O channels the task manipulates.
- [[PipesAndFilters]] — the program is the canonical Unix filter pattern.
- [[Buffering]] — efficient copying typically reads and writes in blocks rather than byte-by-byte.
- [[UnixCat]] — the `cat` utility is the archetypal implementation of this behavior.

## Contradictions
- None — reference task page.
