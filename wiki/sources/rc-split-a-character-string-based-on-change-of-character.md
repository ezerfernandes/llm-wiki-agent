---
title: "Split a character string based on change of character (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Split_a_character_string_based_on_change_of_character
---

## Summary
The task asks the programmer to split a character string into runs of identical consecutive characters, joining the resulting segments with a comma-and-blank delimiter. A new segment begins wherever a character differs from the one immediately before it (scanning left to right). The key insight is that this is run-length grouping: blanks and commas count as ordinary characters, so the test string `gHHH5YY++///\` becomes `g, HHH, 5, YY, ++, ///, \`.

## Task Requirements
- Read a character string and scan it from left to right.
- Group together maximal runs of identical adjacent characters.
- Start a new group whenever the current character differs from the previous one.
- Join the groups with a comma plus a blank (`, `) as the delimiter.
- Treat blanks and commas as ordinary characters, not special.
- Demonstrate the output using the example string `gHHH5YY++///\`.

## Language Coverage
111 languages implement this task, reflecting its "Simple" string-manipulation classification and very broad reach across paradigms. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Ruby, Perl, APL, and several assembly dialects (8080, ARM, Z80).

## Connections
- [[StringProcessing]] — core domain of the task
- [[RunLengthEncoding]] — grouping consecutive identical characters is the same scan as RLE
- [[StringSplitting]] — produces delimited segments from a single string
- [[IterationVsRecursion]] — typically solved with a single left-to-right pass

## Contradictions
- None — reference task page.
