---
title: "Remove lines from a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-handling, text-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Remove_lines_from_a_file
---

## Summary
The task asks the programmer to write a routine that deletes a contiguous block of lines from a text file, given the filename, a starting line number, and the count of lines to remove. Line numbering is 1-based, empty lines count toward the total, and the routine must emit an appropriate message when the requested range extends past the end of the file. The key insight is that most implementations read the file into memory (or stream it), skip the targeted lines, and rewrite the remainder back to disk.

## Task Requirements
- Implement a routine taking three parameters: filename, starting line, and number of lines to remove.
- Use 1-based indexing for both line numbers and the line count (e.g. `foobar.txt, 1, 2` removes the first two lines).
- Count empty lines as real lines; an empty line within the range should still be removed.
- Print an appropriate message if removal is requested beyond the end of the file.

## Language Coverage
71 languages implement this task, spanning systems languages, scripting languages, and shell/text tools. Representative entries include C, C++, Rust, Go, Java, Python, Ruby, Perl, Haskell, AWK, and the UNIX Shell.

## Connections
- [[FileHandling]] — reading, rewriting, and truncating files on disk
- [[TextProcessing]] — line-oriented manipulation of text content
- [[OffByOneError]] — 1-based indexing and end-of-file boundary checks are common pitfalls
- [[InPlaceEditing]] — many solutions emulate stream-editor style in-place modification

## Contradictions
- None — reference task page.
