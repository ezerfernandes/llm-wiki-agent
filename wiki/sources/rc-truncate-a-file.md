---
title: "Truncate a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-system, io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Truncate_a_file
---

## Summary
The task asks the programmer to write a routine that truncates a file to a specified byte length, taking the filename and target length as parameters. The key insight is to prefer a native truncation system or library call (such as POSIX `truncate`/`ftruncate`) when available, and otherwise fall back to copying the head of the file into a temporary file and renaming it. The operation must be binary-safe, leaving the surviving bytes byte-for-byte unchanged.

## Task Requirements
- Implement a routine taking two parameters: filename and required length in bytes.
- Use system/library truncation calls if they exist; otherwise build a smaller temp file, delete the original, and rename.
- Be binary-safe: do not alter the contents of the untruncated portion.
- Raise an appropriate error if the file does not exist or the requested length is not less than the current file length.
- Note (or warn about) platform behavior where truncation may extend or fail to shrink a file when the target length exceeds the current length.

## Language Coverage
68 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and the UNIX Shell.

## Connections
- [[FileSystemOperations]] — truncation is a core file-system manipulation
- [[POSIX]] — `truncate`/`ftruncate` are the canonical native calls
- [[BinarySafeIO]] — surviving bytes must be preserved exactly
- [[AtomicFileReplace]] — the temp-file-and-rename fallback strategy
- [[ErrorHandling]] — required for missing files and invalid lengths

## Contradictions
- None — reference task page.
