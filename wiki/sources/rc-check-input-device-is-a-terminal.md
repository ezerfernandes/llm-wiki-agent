---
title: "Check input device is a terminal (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, terminal-control, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Check_input_device_is_a_terminal
---

## Summary
The task asks the programmer to determine at runtime whether the program's standard input is connected to an interactive terminal (a TTY) rather than to a redirected file or a pipe. The key insight is that most platforms expose this through a single system call—`isatty()` on the file descriptor for stdin (descriptor 0)—which higher-level languages wrap in library helpers. This distinction lets a program adapt its behavior, for example prompting interactively only when a human is present.

## Task Requirements
- Demonstrate how to check whether the input device (standard input) is a terminal or not.
- Report or act on the boolean result distinguishing an interactive TTY from redirected/piped input.

## Language Coverage
45 languages implement this task, spanning systems languages, scripting languages, and shells, since terminal detection is a thin wrapper over the OS. Representative implementations include C, Rust, Go, Python, Haskell, OCaml, Ruby, Perl, Lua, and the UNIX Shell.

## Connections
- [[FileDescriptor]] — stdin is checked via descriptor 0
- [[Isatty]] — the POSIX system call underlying most solutions
- [[TerminalControl]] — broader category of TTY-aware behavior
- [[StandardStreams]] — distinguishing interactive vs redirected stdin
- [[CheckOutputDeviceIsATerminal]] — the related stdout-side task

## Contradictions
- None — reference task page.
