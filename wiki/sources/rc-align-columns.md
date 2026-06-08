---
title: "Align columns (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Align_columns
---

## Summary
The task asks the programmer to read a text file whose lines contain dollar-delimited fields and produce output where each column is padded so that all entries in a column line up vertically in a mono-spaced display. The program must support left, right, and center justification (the same choice applied to every column). The central insight is that column widths must be derived from the data: each column's width is the length of its longest field, plus a minimum separating gap, never hard-coded.

## Task Requirements
- Split each line into fields on a single `$` separator; tolerate lines with or without a trailing `$`.
- Compute each column's width from the longest field in that column (do not hard-code widths).
- Pad fields so columns are separated by at least one space; the minimum inter-column gap is computed from the text.
- Offer left-, right-, and center-justified output modes, with all columns sharing the same alignment.
- Trailing spaces at the end of output lines are insignificant; output is assumed to be viewed in a mono-spaced font.

## Language Coverage
141 languages implement this task, reflecting very broad coverage typical of a fundamental text-processing exercise. Representative implementations include Python, C, C++, Java, Haskell, Ruby, Perl, Go, Rust, Common Lisp, AWK, and Tcl.

## Connections
- [[StringProcessing]] — splitting, padding, and justifying delimited fields
- [[TextFormatting]] — aligning tabular output for mono-spaced display
- [[StringPadding]] — left/right/center justification within a fixed width
- [[Tokenization]] — parsing fields on a delimiter character

## Contradictions
- None — reference task page.
