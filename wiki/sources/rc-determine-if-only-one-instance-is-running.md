---
title: "Determine if only one instance is running (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, concurrency, operating-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_only_one_instance_is_running
---

## Summary
This task asks the programmer to ensure that only a single instance of an application can run at a time. When a program starts, it should detect whether another instance is already active; if so, it should print a message and exit. The common technique is a system-wide mutual-exclusion primitive — a named mutex, a lock file (often with flock or a PID file), or binding to a fixed network port — that the second instance fails to acquire.

## Task Requirements
- On startup, detect whether another instance of the same application is already running.
- If an existing instance is found, display a message stating the program is already running.
- Exit cleanly when a duplicate instance is detected, allowing only the first instance to continue.

## Language Coverage
49 languages implement this task, spanning systems languages, scripting languages, and several BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, C#, Python, Perl, Ruby, Tcl, and Haskell, each using platform-appropriate locking primitives.

## Connections
- [[Concurrency]] — the task guards against multiple concurrent processes of one program.
- [[MutualExclusion]] — a named mutex or lock is the canonical mechanism used.
- [[FileLocking]] — many solutions rely on lock files or flock to claim exclusivity.
- [[InterProcessCommunication]] — port binding and named kernel objects coordinate across processes.

## Contradictions
- None — reference task page.
