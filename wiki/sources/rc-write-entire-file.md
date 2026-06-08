---
title: "Write entire file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-handling, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Write_entire_file
---

## Summary
This task asks the programmer to write (or overwrite) a file so that it contains a given string in a single operation. It is the inverse of the "Read entire file" task: rather than slurping a file's full contents in one pass, you create or replace a file's content wholesale. The key insight is that most languages offer a one-shot write idiom that opens the file in truncate/create mode, writes the buffer, and closes it.

## Task Requirements
- (Over)write a file so that it contains a specified string.
- Create the file if it does not already exist, and replace existing contents if it does.

## Language Coverage
94 languages implement this task, reflecting how universal whole-file I/O is across programming ecosystems — from systems languages to scripting and BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Haskell, Ruby, and Lua.

## Connections
- [[FileHandling]] — the core domain: opening, writing, and closing files
- [[InputOutput]] — file writing is a fundamental form of output
- [[ReadEntireFile]] — the inverse task this one mirrors
- [[FileTruncation]] — overwriting requires truncate/create-mode semantics

## Contradictions
- None — reference task page.
