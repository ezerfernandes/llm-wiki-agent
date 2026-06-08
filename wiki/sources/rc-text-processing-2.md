---
title: "Text processing/2 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, data-validation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Text_processing/2
---

## Summary
This task processes the same pollution-monitoring data file used in Text processing/1: each line holds a datestamp followed by 24 (value, flag) pairs separated by arbitrary whitespace (spaces and/or tabs), where a flag >= 1 marks a working instrument. The goal is to validate the file's structure and produce three reports rather than compute averages. The key insight is distinguishing structural validation (49 fields per record) from semantic quality checks (duplicate dates and fully-good records).

## Task Requirements
- Confirm the general field format of the file: every record is a datestamp plus 24 value/flag pairs (49 whitespace-separated fields).
- Identify any DATESTAMPs that are duplicated across records.
- Report the number of records whose 24 instrument readings all have good flags (flag >= 1).

## Language Coverage
59 languages implement this task, giving broad coverage across systems, scripting, and functional families. Representative implementations include C, C++, Go, Java, Python, Perl, Raku, AWK, Haskell, Tcl, and REXX.

## Connections
- [[TextProcessing1]] — the companion task that averages readings from the same file
- [[Tokenization]] — splitting each line on runs of whitespace into fields
- [[DataValidation]] — confirming field count and flag-based record quality
- [[DuplicateDetection]] — finding repeated datestamps

## Contradictions
- None — reference task page.
