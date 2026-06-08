---
title: "Execute a system command (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, system-programming, shell]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Execute_a_system_command
---

## Summary
This task asks the programmer to invoke an external operating-system command from within a program — running `ls` (or `dir` on Windows), or `pause`. The key insight is that each language exposes the host shell differently: some provide a one-call convenience function while others require spawning a subprocess and managing its lifecycle, but in all cases control is handed off to the OS command interpreter.

## Task Requirements
- Run either the `ls` system command (`dir` on Windows) or the `pause` system command.
- The command is executed via the host operating system's shell or process facilities.

## Language Coverage
165 languages implement this task, making it one of the broadest entries on the site and reflecting that nearly every language offers some path to the underlying OS. Representative implementations include C, C++, Python, Perl, Ruby, Go, Rust, Java, Haskell, and shell-oriented languages like UNIX Shell, Tcl, and PowerShell.

## Connections
- [[ProcessSpawning]] — launching an external process is the core mechanism
- [[ShellCommand]] — commands are dispatched through the OS command interpreter
- [[StandardLibrary]] — most languages expose this via a system/exec library call
- [[InterProcessCommunication]] — related to capturing or piping subprocess output

## Contradictions
- None — reference task page.
