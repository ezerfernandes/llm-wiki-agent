---
title: "Text processing/1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-processing, data-munging]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Text_processing/1
---

## Summary
A classic "data munging" task: parse a tab/space-delimited meteorological data file where each row holds a date followed by 24 value/flag pairs (hourly measurements). For each line the program must sum and average only the valid readings (those with flag > 0), and across the whole file it must find the "maximum data gap" — the longest run of consecutive invalid measurements (flag <= 0). The key insight is tracking a running streak of invalid records that can span line boundaries.

## Task Requirements
- Read a fixed-format file: `<date> <val1> <flag1> ... <val24> <flag24>` (24 hourly pairs per row).
- Treat a measurement as valid only when its flag is greater than 0.
- Per line, report statistics: count of valid values, their sum, and the mean.
- Across the entire file, report summary statistics including the maximum data gap (longest consecutive run of invalid readings, flag <= 0), which may cross line boundaries.
- Show a few sample line statistics plus the full end-of-file summary.

## Language Coverage
55 languages implement this task, spanning text-oriented scripting languages, systems languages, and functional languages — for example AWK, Perl, Python, Ruby, Raku, C, C++, Go, Haskell, Java, and Tcl. The breadth reflects how every general-purpose language has idioms for delimited-record parsing and aggregation.

## Connections
- [[DataMunging]] — the task is a canonical example of reformatting/cleaning raw data.
- [[TextProcessing]] — parsing delimited fixed-format records.
- [[StreamProcessing]] — accumulating per-line and cross-line state in a single pass.
- [[DescriptiveStatistics]] — computing sums and means of valid values.

## Contradictions
- None — reference task page.
