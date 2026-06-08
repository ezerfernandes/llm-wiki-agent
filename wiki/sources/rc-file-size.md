---
title: "File size (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-system, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/File_size
---

## Summary
This Rosetta Code task asks the programmer to determine the size of a file named `input.txt` in two locations: the current working directory and the file system root. The key point is exercising each language's standard mechanism for querying file metadata and handling both a relative path and an absolute (root) path.

## Task Requirements
- Verify the size of a file called `input.txt` located in the current working directory.
- Verify the size of another file `input.txt` located in the file system root.

## Language Coverage
135 languages implement this task, reflecting very broad coverage since file-size queries are a fundamental file-system operation available almost everywhere. Representative implementations include C, C++, Python, Java, Go, Rust, Ruby, Perl, Haskell, and the UNIX Shell.

## Connections
- [[FileSystemOperations]] — querying file metadata is a core filesystem operation
- [[FileMetadata]] — file size is one attribute of a file's stat/metadata record
- [[StandardLibrary]] — most solutions rely on built-in stat or file-info functions
- [[AbsoluteVsRelativePaths]] — the task contrasts a working-directory path with a root path

## Contradictions
- None — reference task page.
