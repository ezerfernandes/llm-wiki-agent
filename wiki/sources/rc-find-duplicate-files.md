---
title: "Find duplicate files (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_duplicate_files
---

## Summary
The task asks for a program that, given a minimum file size and a directory, finds all files of at least that size whose contents are duplicated elsewhere under the directory, then reports the sets of duplicates ordered by decreasing size. The key insight is that duplicates can be detected either by direct byte comparison or by computing a content hash (the typical fast approach: group candidates by size, then compare hashes within each group).

## Task Requirements
- Accept a minimum size (bytes) and a folder/directory as input.
- Recursively find all files of at least the given size with duplicate contents.
- Output the sets of duplicate files in order of decreasing size.
- May be command-line or graphical; duplicates may be found by direct comparison or by hashing.
- Specify any filesystem- or OS-specific requirements.
- Identify hard links (filenames referencing the same content) in the output where applicable.
- Extra credit: detect identical whole directory sub-trees, and optionally remove or link identical files.

## Language Coverage
27 languages implement this task, spanning systems, scripting, and functional styles. Representative implementations include Python, Go, Rust, C++, Haskell, OCaml, Perl, Ruby, Julia, and Tcl.

## Connections
- [[HashFunction]] — content hashing (e.g. MD5/SHA) is the common technique for fast duplicate detection
- [[FileSystem]] — recursive directory traversal and handling of hard links
- [[DirectoryTraversal]] — walking the folder tree to enumerate candidate files
- [[HashTable]] — grouping files by size and hash to cluster duplicates

## Contradictions
- None — reference task page.
