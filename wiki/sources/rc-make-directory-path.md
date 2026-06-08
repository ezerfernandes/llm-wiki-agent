---
title: "Make directory path (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Make_directory_path
---

## Summary
The task asks the programmer to implement a function that takes a single path string (e.g. `./path/to/dir`) and creates that directory along with any missing parent directories, mirroring the POSIX `mkdir -p` command. If the target directory already exists, the function should still return successfully rather than error. The key insight is that the operation must be idempotent and recursively create the full chain of intermediate directories.

## Task Requirements
- Implement a function accepting one path string argument.
- Create the requested directory and any missing parent directories along the path.
- Return successfully (no error) if the directory already exists.
- Ideally work cross-platform (Windows, Linux, OS X).
- If the standard library provides such a function, show how it would be implemented as well.

## Language Coverage
55 languages implement this task. Coverage is broad across systems, scripting, and functional languages, since nearly every standard library exposes a recursive-directory primitive. Representative implementations include C, C++, Go, Rust, Java, Python, Ruby, Perl, Haskell, and UNIX Shell.

## Connections
- [[FileSystem]] — the task operates on directory structures
- [[POSIX]] — modeled directly on the `mkdir -p` command
- [[Idempotence]] — succeeding when the directory already exists
- [[Recursion]] — parent directories are created recursively along the path

## Contradictions
- None — reference task page.
