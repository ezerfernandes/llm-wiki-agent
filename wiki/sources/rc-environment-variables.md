---
title: "Environment variables (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, operating-system, process-management]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Environment_variables
---

## Summary
This task asks the programmer to demonstrate how a running process can read one of its environment variables. Environment variables are key-value pairs inherited by a process from its parent (typically the shell), and the task highlights that the available variables differ across operating systems. The key insight is that nearly every language exposes a small standard-library facility for this, but the variable names themselves are platform-dependent.

## Task Requirements
- Show how to retrieve one of the current process's environment variables.
- Demonstrate reading a commonly available Unix variable such as PATH, HOME, or USER.
- Acknowledge that available variables vary by system.

## Language Coverage
134 languages implement this task, reflecting how universal process-environment access is across runtimes. Representative implementations include C, Python, Java, Go, Rust, Ruby, Perl, JavaScript, Haskell, and the UNIX Shell, spanning systems languages, scripting languages, and functional languages alike.

## Connections
- [[EnvironmentVariable]] — the OS-level key-value pairs being queried
- [[ProcessManagement]] — environment is part of a process's inherited context
- [[OperatingSystemInterface]] — standard-library APIs that expose system state
- [[StandardLibrary]] — most languages provide this via a built-in module or function

## Contradictions
- None — reference task page.
