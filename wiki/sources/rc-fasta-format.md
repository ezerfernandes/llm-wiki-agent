---
title: "FASTA format (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, file-parsing, bioinformatics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/FASTA_format
---

## Summary
FASTA is a text format from bioinformatics used to store one or more named character sequences (DNA, RNA, or protein). Each record begins with a `>` line giving the sequence name, followed by one or more lines of sequence data that must be concatenated into a single string. The task is to parse such a file and print each name with its joined sequence. The key insight is that a high-quality implementation should stream the file line by line rather than loading it all into memory, since real FASTA files can be many gigabytes.

## Task Requirements
- Read a FASTA file in which each record's header line starts with `>` followed by the sequence name.
- Treat all subsequent lines (until the next `>` or end of file) as fragments of one sequence and concatenate them with no spaces.
- Output each record as `name: sequence`.
- Prefer a streaming approach that does not hold the entire file in memory at once.

## Language Coverage
70 languages implement this task, spanning systems, scripting, and functional families. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Haskell, AWK, and Tcl.

## Connections
- [[StringConcatenation]] — joining multiline sequence fragments into one string
- [[FileParsing]] — reading and tokenizing a structured text file
- [[Streaming]] — processing input line by line to bound memory usage
- [[Bioinformatics]] — the domain that originated the FASTA format

## Contradictions
- None — reference task page.
