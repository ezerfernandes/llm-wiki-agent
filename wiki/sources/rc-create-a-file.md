---
title: "Create a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-system, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Create_a_file
---

## Summary
This task asks the programmer to create a new empty file named "output.txt" (0 bytes) and an empty directory named "docs". Each must be created twice: once in the current working directory and once in the filesystem root. The key insight is exercising a language's standard file-system API for both file and directory creation, and contrasting relative paths with absolute root-level paths.

## Task Requirements
- Create an empty file `output.txt` of size 0 bytes.
- Create an empty directory `docs`.
- Perform both operations in the current working directory ("here").
- Perform both operations again at the filesystem root.

## Language Coverage
152 languages implement this task, reflecting nearly universal support for basic file-system operations across general-purpose and scripting languages. Representative implementations include C, Python, Go, Rust, Java, Ruby, Perl, Haskell, UNIX Shell, and PowerShell.

## Connections
- [[FileSystem]] — the OS abstraction the task manipulates
- [[FileIO]] — creating and writing files is core I/O
- [[WorkingDirectory]] — distinguishes the "here" target from root
- [[AbsolutePath]] — the filesystem-root target requires an absolute path

## Contradictions
- None — reference task page.
