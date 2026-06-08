---
title: "File size distribution (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, histogram]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/File_size_distribution
---

## Summary
This task asks the programmer to walk a directory hierarchy (starting from the current directory or one given as a command-line argument) and count how many files fall into each size bucket. The suggested approach is to bucket by the logarithm of the file size, since small absolute differences are insignificant; the goal is to reveal whether a filesystem holds mostly many small files or fewer large ones.

## Task Requirements
- Recursively traverse a directory tree from the current directory, or from a directory passed as a command-line argument.
- Determine the size of each file and tally counts across size ranges.
- Prefer bucketing by logarithm of file size rather than exact bytes.
- Account for empty (zero-byte) files, which may exist as markers.
- Summarize the distribution so the bias toward small or large files is visible.

## Language Coverage
31 languages implement this task, spanning systems languages, scripting languages, and shells. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Haskell, and UNIX Shell.

## Connections
- [[RecursiveDirectoryTraversal]] — the core walk over a directory hierarchy
- [[Histogram]] — counts grouped into size buckets form a distribution histogram
- [[Logarithm]] — log-scale bucketing of file sizes is the suggested technique
- [[FileSystem]] — the task probes the size profile of a filesystem

## Contradictions
- None — reference task page.
