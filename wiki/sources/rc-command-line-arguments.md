---
title: "Command-line arguments (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, command-line, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Command-line_arguments
---

## Summary
This task asks the programmer to retrieve and access the list of command-line arguments passed to a program at invocation. The key insight is that nearly every language exposes these arguments through some standard mechanism (an `argv`-style array, a special variable, or a library call), though they differ on whether the program name itself is included as the first element.

## Task Requirements
- Retrieve the list of arguments given to the program on the command line.
- Demonstrate access against an example invocation such as `myprogram -c "alpha beta" -h "gamma"`.
- This is raw retrieval only — intelligent option parsing is covered by the separate "Parsing command-line arguments" task.

## Language Coverage
166 languages implement this task, making it one of the most broadly covered entries on Rosetta Code and a near-universal capability across programming environments. Representative implementations include C, C++, Java, Python, Ruby, Rust, Go, Haskell, Perl, and several assembly variants (x86-64, ARM, MMIX).

## Connections
- [[CommandLineInterface]] — the runtime context that supplies these arguments
- [[StandardLibrary]] — most languages expose argv via built-in runtime facilities
- [[ParsingCommandLineArguments]] — the follow-on task for structured option parsing
- [[ProgramEntryPoint]] — where argv is typically received (e.g. `main(argc, argv)`)

## Contradictions
- None — reference task page.
