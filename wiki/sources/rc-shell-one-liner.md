---
title: "Shell one-liner (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, command-line, scripting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Shell_one-liner
---

## Summary
This task asks the programmer to show how to specify and run a short program written in the target language directly from a command shell, supplying the entire program as a single line of input. The key insight is that most languages expose a command-line flag (commonly `-e` for "evaluate") that accepts inline source code, letting the interpreter run code without a separate script file.

## Task Requirements
- Demonstrate executing a short program in the language from a command shell using only one line of input.
- Avoid depending on a particular shell or operating system as much as is reasonable.
- If a language has implementations with different command-argument syntax, or runs on systems with different shell styles, show multiple examples.

## Language Coverage
111 languages implement this task, reflecting how broadly inline/command-line execution is supported across scripting languages, compiled languages, and shells. Representative examples include Perl, Python, Ruby, Raku, AWK, sed, Tcl, Haskell, Go, and PowerShell.

## Connections
- [[CommandLineInterface]] — the shell context in which the one-liner is invoked
- [[ReadEvalPrintLoop]] — inline evaluation flags relate closely to interactive interpreters
- [[Interpreter]] — most one-liners rely on an interpreter's evaluate-from-string capability
- [[ShellScripting]] — the broader practice this task is a minimal case of

## Contradictions
- None — reference task page.
