---
title: "File extension is in extensions list (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, file-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/File_extension_is_in_extensions_list
---

## Summary
Given an arbitrary filename and a list of allowed extensions, determine whether the filename ends with one of those extensions. The key insight is that this is a membership check (does the file belong to a known category?) rather than extension extraction: the matching extension must appear at the very end of the name, immediately preceded by a dot, and the comparison is case-insensitive.

## Task Requirements
- Take a filename plus a list of extensions and return whether the filename carries one of them.
- Matching must be case-insensitive (e.g. `MyData.tar.Gz` matches `gz`).
- The extension must sit at the very end of the name and be immediately preceded by a dot; trailing dots (`MyData...`) and bare names (`MyData`) match nothing.
- Assume no extension in the list is empty or contains a dot (in the base task).
- Extra credit: allow extensions that themselves contain dots (e.g. `tar.gz`, `tar.bz2`), and state clearly whether the solution supports this.

## Language Coverage
56 languages implement this task, spanning systems, scripting, functional, and array languages. Representative entries include C, C++, Rust, Go, Java, C#, Python, Ruby, Perl, Raku, Haskell, J, and AWK.

## Connections
- [[StringProcessing]] — core operation is suffix/substring matching with case folding
- [[CaseInsensitiveComparison]] — required normalization before matching
- [[FilenameExtension]] — the file-system concept being tested
- [[ExtractFileExtension]] — sibling Rosetta Code task that parses out an extension rather than checking membership
- [[StringMatching]] — related suffix-matching technique

## Contradictions
- None — reference task page.
