---
title: "Read a configuration file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, file-handling, parsing, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Read_a_configuration_file
---

## Summary
The task is to parse a plain-text configuration file in a "standard" INI-like format and populate program variables from its contents. The key insight is handling the format's conventions: comment lines starting with `#` or `;`, blank lines to ignore, case-insensitive option names but case-sensitive data, an optional `=` separator, bare option names that act as boolean flags, and comma-separated multi-value parameters with surrounding whitespace trimmed.

## Task Requirements
- Ignore blank lines and lines beginning with `#` (hash) or `;` (semicolon).
- Treat option names as case-insensitive; preserve case of parameter data.
- Allow an optional equals sign to separate the option name from its data.
- Set string variables (e.g. fullname = "Foo Barber", favouritefruit = "banana").
- Treat a bare option name with no data as a boolean set to true (needspeeling = true); options not present default to false (seedsremoved = false).
- Split a multi-parameter option on commas into an array, trimming leading/trailing whitespace (otherfamily = ["Rhu Barber", "Harry Barber"]).

## Language Coverage
86 languages implement this task, spanning systems languages, scripting languages, and assembly. Representative entries include C, C++, Rust, Go, Java, Python, Perl, Ruby, Haskell, and AWK.

## Connections
- [[StringParsing]] — tokenizing lines and splitting on delimiters
- [[FileHandling]] — reading and iterating over a text file
- [[ConfigurationFormats]] — INI-style key/value config conventions
- [[Tokenization]] — separating option names from parameter data

## Contradictions
- None — reference task page.
