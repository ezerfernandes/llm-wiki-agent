---
title: "Delete a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-system, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Delete_a_file
---

## Summary
This task asks the programmer to delete a file named "input.txt" and a directory named "docs" using the language's standard library or operating system facilities. Each deletion must be performed twice: once relative to the current working directory and once at the filesystem root. The key insight is that files and directories are typically removed via distinct calls (e.g., `unlink`/`remove` versus `rmdir`), and that root-level operations expose differences in path conventions and permissions across platforms.

## Task Requirements
- Delete a file called "input.txt".
- Delete a directory called "docs".
- Perform both deletions in the current working directory ("here").
- Perform both deletions again at the filesystem root.

## Language Coverage
134 languages implement this task, reflecting that file-system manipulation is a near-universal capability across general-purpose languages, scripting languages, shells, and even assembly. Representative implementations include C, Python, Go, Rust, Java, Ruby, Perl, Haskell, Common Lisp, and UNIX Shell.

## Connections
- [[FileSystem]] — the OS subsystem whose entries the task manipulates
- [[FileSystemOperations]] — the broader Rosetta Code category of file/directory tasks
- [[WorkingDirectory]] — relative-path deletions depend on the process's current directory
- [[FilePermissions]] — root-level deletions surface privilege and access constraints

## Contradictions
- None — reference task page.
