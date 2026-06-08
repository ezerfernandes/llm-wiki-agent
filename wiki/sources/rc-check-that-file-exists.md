---
title: "Check that file exists (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-system, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Check_that_file_exists
---

## Summary
This task asks the programmer to verify the existence of a file named `input.txt` and a directory named `docs`, checking both in the current working directory and at the filesystem root. The key insight is distinguishing between a regular file and a directory, and handling filesystem path resolution (relative vs. absolute) — a common entry point into a language's filesystem API.

## Task Requirements
- Verify that a file called `input.txt` exists.
- Verify that a directory called `docs` exists.
- Perform each check twice: once relative to the current working directory, once at the filesystem root.
- Optional (May 2015): also handle zero-length files and an unusual filename such as `` `Abdu'l-Bahá.txt ``.

## Language Coverage
154 languages implement this task, spanning systems, scripting, functional, and assembly languages — reflecting how universal filesystem access is. Representative implementations include C, Python, Rust, Go, Java, Haskell, Perl, Ruby, Common Lisp, and UNIX Shell.

## Connections
- [[FileSystem]] — the task exercises filesystem existence queries
- [[FileIO]] — relates to the broader category of file input/output operations
- [[PathResolution]] — distinguishing relative working-directory paths from absolute root paths
- [[UnicodeHandling]] — the optional non-ASCII filename criterion stresses character encoding in paths

## Contradictions
- None — reference task page.
