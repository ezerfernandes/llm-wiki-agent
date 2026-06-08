---
title: "Write float arrays to a text file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-handling, floating-point, number-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Write_float_arrays_to_a_text_file
---

## Summary
This task asks the programmer to write two equal-sized numerical arrays, `x` and `y`, into a two-column text file, with each column formatted to an independently specified precision. The key insight is controlling floating-point output formatting: each value should be rendered using a "significant digits" style (like C's `%g`) so that compact values stay short while large or small magnitudes fall back to scientific notation (e.g. `1e+011`, `3.1623e+005`).

## Task Requirements
- Write arrays `x` and `y` (equal size) to a two-column text file named `filename`.
- Format the first column using a given `xprecision` and the second using a given `yprecision`.
- Match the worked example: `x = {1, 2, 3, 1e11}`, `y = sqrt(x)`, with `xprecision = 3` and `yprecision = 5`, producing rows such as `3   1.7321` and `1e+011   3.1623e+005`.
- This is intended as a subtask for measuring relative performance of sorting algorithm implementations.

## Language Coverage
82 languages implement this task, spanning systems languages, scripting languages, numeric/array languages, and many BASIC dialects. Representative examples include Ada, C, C++, Python, Java, Go, Haskell, Fortran, Perl, and MATLAB/Octave.

## Connections
- [[FileHandling]] — writing formatted data to a text file
- [[FloatingPointFormatting]] — rendering floats with controlled significant digits
- [[ScientificNotation]] — fallback representation for large/small magnitudes
- [[FormattedOutput]] — precision-controlled column output like C's `%g`

## Contradictions
- None — reference task page.
