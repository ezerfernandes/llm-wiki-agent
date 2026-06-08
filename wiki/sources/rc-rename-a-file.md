---
title: "Rename a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rename_a_file
---

## Summary
This task asks the programmer to rename a file (input.txt to output.txt) and a directory (docs to mydocs) using the language's filesystem facilities. The operation must be performed twice: once in the current working directory and once at the filesystem root. The exercise highlights how a single rename/move primitive typically handles both files and directories, and how absolute versus relative paths are expressed across platforms.

## Task Requirements
- Rename a file named input.txt into output.txt.
- Rename a directory named docs into mydocs.
- Perform each rename twice: once in the current working directory and once in the filesystem root.
- Assume the user holds sufficient permissions (root-level access for the filesystem-root case on unix-type systems).

## Language Coverage
125 languages implement this task, spanning a very broad range from systems and scripting languages to BASIC dialects and Lisps. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and Common Lisp.

## Connections
- [[FileSystemOperations]] — the task is categorized under file system operations.
- [[FilePath]] — distinguishing relative (current directory) from absolute (root) paths.
- [[StandardLibrary]] — rename is typically a thin wrapper over an OS/standard-library call.
- [[SystemCall]] — most implementations delegate to the underlying rename(2) syscall.

## Contradictions
- None — reference task page.
