---
title: "Dive into Systems — Appendix 2.6 grep and find"
type: source
tags: [unix, search, regex, command-line]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/grep.html
---

## Summary
Sixth subchapter of [[DiveIntoSystems]] Appendix 2. Codifies the **content-search vs. file-search** split: [[Grep|`grep`]] searches *inside* files, [[Find|`find`]] searches *for* files. Both accept regular expressions.

## Key Claims
- **`grep <pattern> <files>`** *"outputs every line in the file (or set of files) that has a matching occurrence of the pattern."* Key flags: `-n` line numbers, `-i` ignore case, `-r` recurse into directories, `-H` show filenames.
- **`find <path> -name "<pattern>"`** recursively searches the filesystem for files whose names match. `*` is the zero-or-more wildcard: `find ./ -name "*.c"`.
- Both support **regex** primitives — character classes `[A-Z]`, word boundaries `\b`, quantifiers like `*` (zero-or-more).
- **Composition**: `grep main *.c` searches every C file for `main`; `find` and `grep` are routinely piped together to grep through a discovered file set.

## Connections
- [[Grep]] — content search.
- [[Find]] — file-name search.
- [[RegularExpression|Regex]] — the common pattern language.
- [[UnixCommandLine]] — the shell context.
- [[DiveIntoSystems]] — 157th ingested chapter.

## Contradictions
- None.
