---
title: "Search in paragraph's text (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-parsing, regular-expressions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Search_in_paragraph's_text
---

## Summary
The task asks the programmer to scan a multi-paragraph text file (e.g. a log of Python tracebacks) and find paragraphs that contain a given keyword or regular expression. The example splits the input on a recurring marker line ("Traceback (most recent call last):") to define paragraph boundaries, then keeps only those paragraphs in which the keyword "SystemError" appears. The key insight is recognizing that "paragraphs" are delimited by a domain-specific separator rather than blank lines, so the matching and re-formatting must respect that custom boundary.

## Task Requirements
- Read a structured-or-unstructured text containing several paragraphs.
- Verify the presence of a word or regular expression (here, "SystemError") within each paragraph.
- Treat each block beginning with "Traceback (most recent call last):" as one paragraph.
- Print only the relevant matching paragraphs to standard output.
- Format the output with a `----------------` line as the separator between paragraphs, keeping the marker line at the start of each retained paragraph.

## Language Coverage
18 languages implement this task, spanning systems and scripting languages alongside dedicated text-processing tools. Representative implementations include C, C++, Java, Python, Perl, Raku, Julia, Nim, AWK, sed, jq, and Wren.

## Connections
- [[RegularExpressions]] — keyword/pattern matching against paragraph text
- [[StringProcessing]] — splitting, scanning, and reformatting text blocks
- [[TextParsing]] — delimiting paragraphs by a custom marker line
- [[LogAnalysis]] — practical motivation of filtering traceback/error logs

## Contradictions
- None — reference task page.
