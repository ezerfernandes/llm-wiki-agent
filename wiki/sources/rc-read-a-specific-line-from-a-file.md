---
title: "Read a specific line from a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Read_a_specific_line_from_a_file
---

## Summary
This task asks the programmer to retrieve the contents of a specific line (the seventh) from a file and store it in a variable or memory for later use. The key insight is that most languages lack random access by line number, so the line must be reached by reading sequentially while counting newlines. Empty lines still count, and the program must report an appropriate message if the file has fewer than seven lines, the target line is empty, or the line is too large to read.

## Task Requirements
- Obtain the contents of the seventh line of a file and store it in a variable or memory.
- Use any special line-access semantics the language offers; otherwise read line by line.
- Count empty lines as well; they are not skipped.
- Output an appropriate message if the file has fewer than seven lines, if the seventh line is empty, or if the line is too big to retrieve.
- Functional languages or those without variables may simply print the extracted line.

## Language Coverage
95 languages implement this task, spanning systems, scripting, functional, and text-processing tools. Representative examples include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and dedicated text utilities like AWK, sed, and ed.

## Connections
- [[FileIO]] — reading file contents from disk
- [[LineProcessing]] — splitting input into lines and counting them
- [[SequentialAccess]] — reaching a target line without random access
- [[ErrorHandling]] — reporting missing, empty, or oversized lines

## Contradictions
- None — reference task page.
