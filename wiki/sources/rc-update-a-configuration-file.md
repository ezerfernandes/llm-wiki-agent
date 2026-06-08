---
title: "Update a configuration file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-handling, string-processing, configuration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Update_a_configuration_file
---

## Summary
This task asks the programmer to read a standard hash/semicolon-commented configuration file and rewrite it after applying a set of edits to specific options. The challenge lies in the normalization rules: option names are case-insensitive but parameter data is case-sensitive, options are disabled with a leading semicolon and enabled by stripping it, and the rewritten file must clean up whitespace, duplicate semicolons, and stray non-ASCII characters. It is a companion to the "Read a configuration file" task, focused on the write/modify half of the workflow.

## Task Requirements
- Disable the `needspeeling` option by prefixing it with a semicolon.
- Enable `seedsremoved` by removing the semicolon and any leading whitespace.
- Change the `numberofbananas` parameter to 1024.
- Enable or create `numberofstrawberries` with a value of 62000.
- Treat option names case-insensitively but rewrite them in uppercase; preserve parameter data lettercase.
- Leave hash-comment lines unchanged; add any missing option; remove duplicate option entries keeping only the first.
- Replace double semicolon prefixes with a single one (or remove all when uncommenting); drop semicolon-only lines.
- Strip leading/trailing whitespace, collapse option-to-parameter spacing to a single space, and remove tabs, control codes, and non-ASCII characters.

## Language Coverage
35 languages implement this task, spanning systems, scripting, and functional styles. Representative entries include C, C++, D, Go, Rust-adjacent assembly (ARM and AArch64 Assembly), Haskell, Python, Perl, Raku, Ruby, Java, Kotlin, and Tcl.

## Connections
- [[StringProcessing]] — the core work is line-by-line parsing and rewriting.
- [[FileIO]] — reading and atomically rewriting a config file.
- [[RegularExpressions]] — common tool for matching options, comments, and whitespace.
- [[ConfigurationFileFormats]] — the INI-like key/value-with-comments format being manipulated.
- [[CaseInsensitiveMatching]] — option names compared without regard to lettercase.

## Contradictions
- None — reference task page.
