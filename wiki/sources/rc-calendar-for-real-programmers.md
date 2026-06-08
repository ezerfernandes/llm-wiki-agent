---
title: "Calendar - for \"REAL\" programmers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, text-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Calendar_-_for_%22REAL%22_programmers
---

## Summary
A humorous variant of the standard Calendar task: print a full twelve-month calendar formatted to fill a 132-character-wide line-printer page, but with the constraint that the entire program source contains no lowercase letters whatsoever. The constraint is a nod to 1960s hardware where uppercase-only character sets were common (6-bit characters packed into 36-bit or 60-bit words), satirized in Ed Post's "Real Programmers Don't Use PASCAL." A Snoopy ASCII-art header is replaced with a placeholder to keep output compact.

## Task Requirements
- Implement the same calendar-rendering algorithm as the standard [[Calendar]] task (lay out all 12 months of a year in a grid).
- Format the output to nicely fill a page exactly 132 characters wide, emulating a 1969-era line printer.
- Write the entire source code without any lowercase letters (all UPPERCASE).
- Do not include actual Snoopy ASCII art; emit a placeholder where it would appear.

## Language Coverage
47 languages implement this task, spanning low-level assembly, classic mainframe languages, and modern scripting languages. Representative entries include 360 Assembly, X86 Assembly, COBOL, Fortran, PL/I, REXX, Ada, C, D, Go, Rust, Julia, Perl, Raku, Ruby, Kotlin, and Common Lisp.

## Connections
- [[Calendar]] — the base task this variant extends.
- [[DateAndTime]] — computing weekday offsets and month lengths.
- [[ZellersCongruence]] — a common algorithm for finding the day-of-week a month starts on.
- [[TextFormatting]] — column-aligned grid layout within a fixed 132-character width.
- [[CaseSensitivity]] — the all-uppercase source constraint central to the task.

## Contradictions
- None — reference task page.
