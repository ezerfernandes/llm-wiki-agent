---
title: "Longest string challenge (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Longest_string_challenge
---

## Summary
This task asks the programmer to read lines from standard input and, on end of file, print the longest line — or all lines if several tie for longest length. The twist is a set of artificial restrictions (no comparison operators, no arithmetic, only integer and string datatypes with no lists, and no re-reading input) that force creative, non-pedestrian solutions. The key insight is that the restrictions push implementers to compare and accumulate lengths implicitly, showcasing idiosyncratic language features rather than the obvious approach.

## Task Requirements
- Read lines from standard input; on EOF, write the longest line to standard output.
- If multiple lines tie for the longest, output all of the tied lines (order may vary).
- Produce no output if there is no input.
- Honor the spirit of the restrictions: no comparison operators, no arithmetic, only integer and string types (no lists), and do not re-read the input.
- Describe how the solution circumvents or works around the restrictions while meeting their intent.

## Language Coverage
61 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative examples include Ada, C, C++, Haskell, J, Java, Python, Perl, Raku, Rust, Tcl, and Wren.

## Connections
- [[StringProcessing]] — the core operation is comparing string lengths
- [[StandardInputOutput]] — reading from stdin and writing to stdout
- [[ComparisonOperators]] — restriction targets avoiding explicit length comparison
- [[ProgrammingParadigms]] — solutions vary widely by language paradigm

## Contradictions
- None — reference task page.
