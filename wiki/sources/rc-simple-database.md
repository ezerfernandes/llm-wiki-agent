---
title: "Simple database (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, serialization, cli]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Simple_database
---

## Summary
The task asks the programmer to build a small command-line tool that tracks a set of records, where each entry has at least a description, a category/tag, a date, and optional extra fields. The data must be persisted to disk in a human-readable, structured format, ideally a standard serialization format available natively rather than a hand-rolled one. The core challenge is combining argument parsing, an in-memory record structure, persistence, and a few query/report operations.

## Task Requirements
- Provide a command-line interface that lets the user enter at least two different values per entry.
- Track at minimum: a description (e.g. title/name), a category or tag, and a date (entered or auto-generated); other optional fields are allowed.
- Store entries in a structured format saved to disk that is human-readable (no custom format if an existing one like JSON, YAML, or S-Expressions can be used).
- Support CLI subcommands to: add a new entry, print the latest entry, print the latest entry for each category, and print all entries sorted by date.

## Language Coverage
38 languages implement this task, spanning system languages, scripting languages, and Lisp-family languages, reflecting how broadly serialization plus CLI handling is supported. Representative examples include C, C++, C#, Java, Python, Ruby, Perl, Go, Haskell, Common Lisp, and Tcl.

## Connections
- [[Serialization]] — persisting structured records to disk in a readable form.
- [[JSON]] — a recommended native, human-readable storage format.
- [[CommandLineArguments]] — parsing subcommands and field values from argv.
- [[Sorting]] — printing all entries ordered by date.
- [[DataStructures]] — modeling each entry as a record with named fields.

## Contradictions
- None — reference task page.
