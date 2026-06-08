---
title: "Program name (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, system-introspection, command-line]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Program_name
---

## Summary
This task asks the programmer to programmatically obtain the name used to invoke the running program, distinguishing for example between running a script directly versus running another program that imports it. The key insight is that languages expose this differently: some via an argument vector entry (argv[0]), others through dedicated runtime globals or environment introspection, and sometimes a multiline shebang is needed to surface the script name to the interpreter's ARGV.

## Task Requirements
- Determine, at runtime, the name used to invoke the program.
- Distinguish the directly-run script from one that merely imports or includes its code.
- Where applicable, use a multiline shebang so the language's internal ARGV receives the script name.

## Language Coverage
123 languages implement this task, spanning systems languages, scripting languages, functional languages, and several assembly dialects. Representative implementations include C, C++, Rust, Go, Python, Perl, Ruby, Java, Haskell, Common Lisp, and UNIX Shell.

## Connections
- [[CommandLineArguments]] — program name is typically the zeroth command-line argument.
- [[Shebang]] — multiline shebangs are sometimes required to pass the script name into ARGV.
- [[RuntimeReflection]] — obtaining invocation metadata is a form of program self-introspection.
- [[ProcessEnvironment]] — some languages derive the name from environment or process state rather than argv.

## Contradictions
- None — reference task page.
