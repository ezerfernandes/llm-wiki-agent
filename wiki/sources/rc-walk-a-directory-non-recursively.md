---
title: "Walk a directory/Non-recursively (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, pattern-matching]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Walk_a_directory/Non-recursively
---

## Summary
This task asks the programmer to list the entries of a single directory and print the names of those files whose names match a given pattern. The key constraint is that the listing must be non-recursive: it reads one directory level only and does not descend into subdirectories. The task deliberately leaves "pattern" loosely defined, so solutions vary between substring matching, shell glob patterns, and full regular expressions depending on the language's idioms.

## Task Requirements
- Read the contents of a single given directory (no recursion into subdirectories).
- Filter entries by a given pattern (substring, glob, or regex — definition is language-dependent).
- Print the names of the matching files.

## Language Coverage
105 languages implement this task, spanning systems languages, scripting languages, assembly, and shells, reflecting how universal directory iteration is. Representative implementations include C, C++, Rust, Go, Python, Ruby, Perl, Haskell, Java, and the UNIX Shell.

## Connections
- [[FileSystemOperations]] — the task is a basic directory enumeration operation.
- [[PatternMatching]] — filtering filenames by a supplied pattern.
- [[Globbing]] — many solutions use shell-style wildcard expansion.
- [[RegularExpressions]] — alternative pattern definition used by several languages.
- [[WalkDirectoryTree]] — the recursive counterpart task.

## Contradictions
- None — reference task page.
