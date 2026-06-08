---
title: "Globally replace text in several files (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, file-io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Globally_replace_text_in_several_files
---

## Summary
This task asks the programmer to perform a search-and-replace across a group of text files, substituting every occurrence of one literal string with another. The concrete example replaces "Goodbye London!" with "Hello New York!" in a supplied list of files. The key practical insight is iterating over multiple files while doing in-place rewriting of each file's contents.

## Task Requirements
- Replace every occurring instance of a given piece of text with a different piece of text.
- Apply the replacement across a group (list) of text files, not just one.
- Use the specific example replacement of "Goodbye London!" → "Hello New York!".

## Language Coverage
72 languages implement this task, reflecting broad coverage spanning systems languages, scripting languages, and shell tools. Representative implementations include C, C++, Rust, Go, Python, Ruby, Perl, Haskell, AWK, and the UNIX Shell (often delegating to Sed).

## Connections
- [[StringReplacement]] — the core substitution operation on text contents
- [[FileIO]] — reading and writing each target file
- [[BatchProcessing]] — applying one operation uniformly over a list of files
- [[StreamEditing]] — the Sed/AWK style line-by-line transformation idiom

## Contradictions
- None — reference task page.
