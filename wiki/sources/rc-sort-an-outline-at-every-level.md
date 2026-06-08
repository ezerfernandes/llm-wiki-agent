---
title: "Sort an outline at every level (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, sorting, tree]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_an_outline_at_every_level
---

## Summary
The task asks for a function over an indented plain-text outline that recursively sorts the sibling sub-lists at every level of indentation, while either preserving the original indent style or reporting that the indentation is too inconsistent to interpret. The core insight is that an indented outline is really a tree: you must first infer the indent unit (tabs vs. spaces, and its width) directly from the text, parse the lines into a nested structure, sort each node's children, then re-emit using the original indentation.

## Task Requirements
- Sort the sub-lists at every indentation level, or report inconsistent/ambiguous indentation.
- Detect at least two kinds of inconsistency: mixed whitespace characters (tabs vs. spaces) and irregular indent widths (e.g. an odd indent where the unit is 2 or 4 spaces).
- Handle both tab-indented and space-indented outlines without being told in advance which character or unit width is used.
- Support multiple sort orders, at minimum ascending and descending lexical sorts.
- Preserve the type and size of the indentation units present in the input.

## Language Coverage
17 languages implement this task, giving moderate coverage across functional, imperative, and array paradigms. Representative entries include C++, Go, Haskell, Java, J, Julia, Nim, Perl, Python, Raku, and Wren.

## Connections
- [[TreeDataStructure]] — an indented outline maps directly onto a nested tree of siblings
- [[Sorting]] — children at each level are reordered by a comparison key
- [[RecursiveAlgorithms]] — the sort is applied depth-first across every level
- [[Parsing]] — indentation must be tokenized and validated before structuring
- [[Serialization]] — the sorted tree is re-rendered back to indented text

## Contradictions
- None — reference task page.
