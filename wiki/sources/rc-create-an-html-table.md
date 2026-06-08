---
title: "Create an HTML table (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, markup-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Create_an_HTML_table
---

## Summary
This task asks the programmer to programmatically emit a well-formed HTML table as text output. The body must contain at least three rows by three columns headed "X", "Y", and "Z", plus an unlabeled extra column on the far left or right holding sequential row numbers. The key insight is that this is fundamentally a structured string/markup generation exercise — assembling nested `<table>`, `<tr>`, `<th>`, and `<td>` tags — rather than an algorithmic one.

## Task Requirements
- The table body should have at least three rows of three columns.
- The three columns should be labelled "X", "Y", and "Z".
- An extra unlabeled column at the extreme left or right should be filled with sequential row numbers.
- The X, Y, Z cells should hold random or sequential integers of 4 digits or fewer.
- The numbers should be aligned the same way across all columns.

## Language Coverage
108 languages implement this task, giving very broad coverage spanning systems languages, scripting languages, functional languages, and even assembly. Representative implementations include C, C++, Java, Python, JavaScript, Perl, PHP, Haskell, Lua, and XSLT.

## Connections
- [[StringFormatting]] — building the markup via concatenation, interpolation, or templating
- [[MarkupGeneration]] — programmatic emission of structured HTML/XML
- [[RandomNumberGeneration]] — populating cells with random integers
- [[TextTemplating]] — many solutions use loops or template strings to repeat rows

## Contradictions
- None — reference task page.
