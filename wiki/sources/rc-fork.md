---
title: "Fork (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, operating-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fork
---

## Summary
This task asks the programmer to spawn a new process that runs simultaneously with, and independently of, the original parent process. The key insight is process creation at the OS level: on Unix-like systems this is the classic `fork()` system call, which duplicates the calling process, while other platforms and languages expose equivalent process-spawning primitives. The new process executes concurrently and does not block the parent.

## Task Requirements
- Spawn a new process from within a running program.
- The spawned process must be able to run simultaneously with the parent.
- The spawned process must run independently of the parent process.

## Language Coverage
70 languages implement this task, reflecting broad support across systems-level, scripting, and functional languages. Representative implementations include C, C++, Rust, Go, Python, Perl, Ruby, Java, Haskell, Erlang, Lua, and UNIX Shell, with several relying on the POSIX `fork()` call and others on higher-level process or threading abstractions.

## Connections
- [[ProcessManagement]] — spawning and managing OS-level processes
- [[Concurrency]] — running parent and child simultaneously
- [[ForkSystemCall]] — the POSIX primitive that duplicates a process
- [[OperatingSystem]] — the kernel facility providing process creation
- [[ParallelComputing]] — independent execution paths

## Contradictions
- None — reference task page.
