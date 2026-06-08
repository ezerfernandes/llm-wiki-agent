---
title: "Get system command output (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, process-management, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Get_system_command_output
---

## Summary
This task asks the programmer to execute an external system command from within a program and capture its standard output back into the program. The captured output may be held in any kind of collection (array, list, string, etc.). The key insight is that this goes beyond merely launching a command — it requires redirecting and reading the child process's output stream rather than letting it print directly to the terminal.

## Task Requirements
- Execute a system (shell/external) command from inside the program.
- Capture the command's output into the program rather than letting it stream to the console.
- Store the captured output in any suitable collection type (array, list, string, etc.).

## Language Coverage
80 languages implement this task, spanning systems languages, scripting languages, BASIC dialects, and functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and PowerShell.

## Connections
- [[ProcessManagement]] — spawning and controlling child processes
- [[StandardStreams]] — capturing stdout from a subprocess
- [[InterProcessCommunication]] — piping data back from an external program
- [[ShellCommands]] — invoking the operating system shell

## Contradictions
- None — reference task page.
