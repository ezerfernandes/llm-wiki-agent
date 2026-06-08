---
title: "Kernighans large earthquake problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-processing, file-io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kernighans_large_earthquake_problem
---

## Summary
Based on a problem Brian Kernighan described in a University of Nottingham lecture, this task processes a whitespace-delimited data file whose lines each hold a date, a one-word name, and an earthquake magnitude. The goal is to filter and report every event whose magnitude exceeds 6. The key insight is that this is the canonical "filter rows by a numeric field" exercise — trivially solved by line-oriented tools like AWK or grep, which is precisely Kernighan's pedagogical point about choosing the right tool.

## Task Requirements
- Read a data file of thousands of lines, each with three whitespace-separated fields: date, single-word name, and magnitude.
- Find and report all events with a magnitude greater than 6.
- Either show how the program is invoked on a named file (e.g. "data.txt"), or hard-code the filename into a single-use program.

## Language Coverage
70 languages implement this task, spanning shell and text-processing tools, classic systems languages, scripting languages, and esoteric/assembly entries. Representative implementations include AWK, Bash, C, Python, Perl, Go, Haskell, Ruby, jq, and Wren.

## Connections
- [[TextProcessing]] — the core activity of parsing delimited lines and filtering rows
- [[FieldDelimitedData]] — whitespace-separated columnar records
- [[AWK]] — the archetypal one-liner tool for this class of problem
- [[Filtering]] — selecting records that satisfy a numeric predicate
- [[FileIO]] — reading an input file line by line

## Contradictions
- None — reference task page.
