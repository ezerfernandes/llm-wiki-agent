---
title: "CSV to HTML translation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/CSV_to_HTML_translation
---

## Summary
The task asks the programmer to write a function that takes a simplified CSV string (rows separated by newlines, columns by commas, with no commas inside fields) and returns an HTML table representing that data. The central insight is that field contents must be HTML-escaped — characters such as `<`, `>`, and `&` have to be converted to entities like `&lt;`, `&gt;`, and `&amp;` so that embedded markup renders as literal text rather than as HTML.

## Task Requirements
- Accept a string representation of CSV data (rows newline-delimited, columns comma-delimited).
- Emit a text string containing an HTML `<table>` with one `<tr>` per row and one `<td>` per field.
- HTML-escape special characters in field data so they display literally rather than as markup.
- Use the provided Monty Python sample data and show the produced output.
- Extra credit: optionally treat the first row as a header row, ideally using `<thead>`/`<th>` (or CSS).

## Language Coverage
95 languages implement this task, reflecting very broad coverage across general-purpose, scripting, and esoteric languages. Representative implementations include Python, C, C++, Java, JavaScript, Go, Rust, Haskell, Perl, Ruby, and Tcl.

## Connections
- [[StringProcessing]] — splitting rows and fields by delimiters
- [[HtmlEscaping]] — converting reserved characters to entities
- [[CommaSeparatedValues]] — the simplified CSV input format
- [[TextTemplating]] — assembling structured HTML output

## Contradictions
- None — reference task page.
