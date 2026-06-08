---
title: "Camel case and snake case (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, naming-conventions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Camel_case_and_snake_case
---

## Summary
The task asks for two functions that convert between the two dominant variable-naming styles: snake_case (lowercase words joined by underscores) and camelCase (lowercase first word, subsequent words capitalized). The key generalization is to treat spaces and hyphens as word separators equivalent to the underscore, so arbitrary strings can be re-tokenized into either convention. Leading or trailing whitespace may be trimmed.

## Task Requirements
- Write a function converting snake case to camel case, and a function converting camel case to snake case.
- Generalize each so that space- or hyphen-delimited words also work, treating ` ` and `-` as separators like `_`.
- Leading/trailing whitespace may be ignored; no whitespace is allowed inside the resulting variable names.
- Show both conversions applied to a fixed test set: `"snakeCase"`, `"snake_case"`, `"variable_10_case"`, `"variable10Case"`, `"ɛrgo rE tHis"`, `"hurry-up-joe!"`, `"c://my-docs/happy_Flag-Day/12.doc"`, and `"  spaces  "`.

## Language Coverage
41 languages implement this task, spanning systems, scripting, and functional families. Representative solutions include Python, Rust, Go, Java, C++, JavaScript, Perl, Raku, Julia, and Wren.

## Connections
- [[StringProcessing]] — tokenizing and rejoining words under different delimiter rules
- [[NamingConventions]] — the broader topic of identifier styling this task formalizes
- [[Tokenization]] — splitting input on multiple separator characters before recasing
- [[RegularExpressions]] — a common technique for detecting word boundaries and separators

## Contradictions
- None — reference task page.
