---
title: "Unix/ls (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, filesystem, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Unix/ls
---

## Summary
This task asks the programmer to write a program that lists everything in the current working directory, mimicking the Unix `ls` utility or the Windows `DIR` command. The output must be sorted alphabetically, but extended file details and multi-column formatting are explicitly not required. The key insight is exercising each language's directory-enumeration API combined with a simple sort.

## Task Requirements
- List every entry contained in the current folder.
- Sort the output (alphabetical order, as in the worked example).
- Printing extended details (sizes, permissions, dates) is not required.
- Producing multi-column output is not required.
- Example: run in `/foo` prints `bar`; run in `/foo/bar` prints `1`, `2`, `a`, `b` on separate lines.

## Language Coverage
80 languages implement this task, spanning systems languages, scripting languages, and shells, reflecting that directory listing is a near-universal capability. Representative implementations include C, C++, Rust, Go, Python, Perl, Ruby, Haskell, Java, and UNIX Shell.

## Connections
- [[FileSystem]] — the task reads directory entries from the working directory
- [[DirectoryListing]] — core operation being demonstrated
- [[Sorting]] — entries must be returned in sorted order
- [[StandardLibrary]] — most solutions rely on built-in OS/filesystem APIs

## Contradictions
- None — reference task page.
