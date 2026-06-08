---
title: "Walk a directory/Recursively (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, file-system]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Walk_a_directory/Recursively
---

## Summary
This task asks the programmer to traverse an entire directory tree and print every file whose name matches a given pattern. The defining requirement is recursion: unlike the sibling "non-recursive" task, the solution must descend into every subdirectory rather than listing only the top level. The key insight is that file systems form a tree, so each subdirectory is handled by reapplying the same walk procedure.

## Task Requirements
- Walk a given directory tree (not just a single directory).
- Match files against a given name pattern (e.g. a glob or regular expression).
- Print the files that match.
- Use a recursive method that reads the entire tree by descending into subdirectories.

## Language Coverage
91 languages implement this task, spanning systems languages, scripting languages, and functional languages, since directory traversal is a near-universal capability. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, Common Lisp, and the UNIX Shell.

## Connections
- [[Recursion]] — the tree is walked by reapplying the procedure to each subdirectory.
- [[TreeTraversal]] — the directory hierarchy is a tree to be visited depth-first.
- [[FileSystemOperations]] — listing directories and reading file metadata.
- [[PatternMatching]] — filtering filenames via globs or regular expressions.

## Contradictions
- None — reference task page.
