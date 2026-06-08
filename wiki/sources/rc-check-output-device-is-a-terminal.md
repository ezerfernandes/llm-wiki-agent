---
title: "Check output device is a terminal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, system-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Check_output_device_is_a_terminal
---

## Summary
This task asks the programmer to demonstrate how a program can determine whether its standard output is connected to an interactive terminal (TTY) versus being redirected to a file or pipe. The key insight is that programs often adapt behavior based on this distinction — for example enabling color or progress output only when a human is watching. On POSIX systems this is typically done via the `isatty()` system call on the output file descriptor.

## Task Requirements
- Demonstrate how to check whether the output device is a terminal or not.
- Relates to the companion task of checking whether the input device is a terminal.

## Language Coverage
52 languages implement this task, spanning systems languages, scripting languages, and shells, reflecting how nearly every runtime exposes some form of TTY detection. Representative implementations include C, C++, Rust, Go, Python, Perl, Ruby, Haskell, Java, and the UNIX Shell.

## Connections
- [[Isatty]] — the standard POSIX call most implementations rely on
- [[FileDescriptor]] — the abstraction (stdout / fd 1) being inspected
- [[TerminalControl]] — broader category of TTY-aware behavior
- [[StandardStreams]] — stdin/stdout/stderr whose nature is being queried

## Contradictions
- None — reference task page.
