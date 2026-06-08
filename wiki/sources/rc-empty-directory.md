---
title: "Empty directory (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Empty_directory
---

## Summary
Given a path to a directory, determine whether that directory is empty — meaning it contains no files and no subdirectories. The key subtlety is that on Unix and Windows systems most directories include the special entries "." (self) and ".." (parent), so an empty-directory check must ignore these and treat the directory as empty only when no other entries remain.

## Task Requirements
- Take a path to a directory as input.
- Report whether the directory is empty (contains no files nor subdirectories).
- Account for the "." and ".." pseudo-entries present on Unix/Windows, which do not count toward emptiness.

## Language Coverage
85 languages implement this task, spanning systems languages, scripting languages, and BASIC dialects. Representative implementations include C, C++, Rust, Go, Python, Ruby, Perl, Haskell, Java, and the UNIX Shell.

## Connections
- [[FileSystem]] — the task inspects directory contents through filesystem APIs.
- [[DirectoryTraversal]] — emptiness is decided by enumerating directory entries.
- [[StandardLibrary]] — most solutions rely on built-in directory/listing functions.

## Contradictions
- None — reference task page.
