---
title: "Read entire file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Read_entire_file
---

## Summary
This task asks the programmer to load the complete contents of a text file into a single string variable in one operation, rather than reading it line by line. The key insight is that many languages offer a dedicated "slurp" idiom for this, and the task invites discussion of encoding selection and the possibility of memory-mapping the file. It explicitly notes this is appropriate only when having the whole file in memory is genuinely needed, not for large files processable incrementally.

## Task Requirements
- Load the entire contents of a text file into a single string variable.
- If applicable, discuss encoding selection (e.g., choosing a character encoding when decoding bytes to text).
- If applicable, discuss the possibility of memory-mapping the file.
- The task is meant for cases where the whole file is wanted at once; incremental reading belongs to the separate File IO task.

## Language Coverage
157 languages implement this task, reflecting that whole-file reads are a near-universal capability across general-purpose languages, scripting languages, and even specialized tools. Representative implementations include C, C++, Python, Java, Rust, Go, Ruby, Perl, Haskell, Lua, and the UNIX Shell.

## Connections
- [[FileIO]] — companion task for incremental/streaming reads instead of whole-file slurping
- [[CharacterEncoding]] — decoding raw bytes into a string requires choosing an encoding
- [[MemoryMappedFile]] — an alternative mechanism for accessing file contents as if in memory
- [[StringProcessing]] — the loaded contents are held as a single string for further manipulation

## Contradictions
- None — reference task page.
