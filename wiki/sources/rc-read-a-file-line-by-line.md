---
title: "Read a file line by line (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Read_a_file_line_by_line
---

## Summary
This task asks the programmer to read a text file one line at a time, processing or emitting each line in turn, rather than slurping the entire file into memory at once. The key insight is streaming I/O: iterating over a file by line keeps memory usage bounded regardless of file size, which matters for large inputs and is the idiomatic way most languages expose file reading.

## Task Requirements
- Read a file one line at a time.
- Contrast with reading the entire file at once (the related "Read entire file" task).
- Related tasks: reading a file character by character, and the general input-loop pattern.

## Language Coverage
139 languages implement this task, spanning systems languages, scripting languages, functional languages, and assembly. Representative examples include C, C++, Rust, Go, Python, Perl, Ruby, Haskell, Java, and AWK.

## Connections
- [[FileIO]] — the core operating-system facility being exercised
- [[StreamProcessing]] — reading incrementally keeps memory bounded
- [[Buffering]] — line-buffered reads underpin most implementations
- [[InputLoop]] — the iterate-until-EOF control pattern

## Contradictions
- None — reference task page.
