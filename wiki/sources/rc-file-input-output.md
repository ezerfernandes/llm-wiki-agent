---
title: "File input/output (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, streams]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/File_input/output
---

## Summary
This task asks the programmer to copy the contents of an existing file "input.txt" into a new file "output.txt", routing the data through an intermediate variable rather than relying on the operating system's native copy command. The point is to demonstrate the two fundamental file operations together: reading a file's contents into program memory and then writing that in-memory value back out to a different file.

## Task Requirements
- Read the contents of "input.txt" into a variable.
- Write that variable's contents into a newly created file "output.txt".
- Use an intermediate variable; oneliners that bypass it (or shell copy commands) are of only secondary interest.

## Language Coverage
151 languages implement this task, making it one of the most broadly covered file-handling exercises across systems, scripting, and assembly languages. Representative implementations include C, C++, Python, Java, Go, Rust, Haskell, Perl, Ruby, and AArch64 Assembly.

## Connections
- [[FileIO]] — the core capability being demonstrated
- [[StreamProcessing]] — reading and writing via file streams or handles
- [[Buffering]] — in-memory intermediate variable holding the file contents
- [[ResourceManagement]] — opening and closing file handles correctly

## Contradictions
- None — reference task page.
