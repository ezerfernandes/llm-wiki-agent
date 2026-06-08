---
title: "CSV data manipulation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-io, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/CSV_data_manipulation
---

## Summary
This task asks the programmer to read a CSV (comma-separated values) file, modify some of its values, and write the result back to a file. The concrete demonstration is to load a small numeric table, append a new "SUM" column containing the per-row sums, and save it. The key insight is exercising round-trip parsing and serialization of tabular data, ideally via built-in or standard CSV libraries that handle the format's quirks rather than naive string splitting.

## Task Requirements
- Read a given CSV file containing a header row (C1–C5) and four rows of integers.
- Change/transform some values, specifically: add a new column headed "SUM" holding the sum of each row's values.
- Write the modified table back out as a CSV file.
- Where possible, use built-in or standard functions, methods, or libraries that handle generic CSV files.

## Language Coverage
100 languages implement this task, spanning system languages, scripting languages, functional languages, and data/spreadsheet-oriented tools. Representative implementations include C, C++, Rust, Go, Java, Python, Ruby, Perl, Haskell, R, and AWK.

## Connections
- [[CSV]] — the tabular file format being read and written
- [[FileIO]] — reading from and writing to files on disk
- [[Serialization]] — converting in-memory tabular data to and from text
- [[StringProcessing]] — parsing delimited fields and reassembling rows
- [[Convert CSV records to TSV]] — related Rosetta Code task on the same data format

## Contradictions
- None — reference task page.
