---
title: "Commatizing numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Commatizing_numbers
---

## Summary
This task asks the programmer to write a function that inserts grouping separators (commas by default) into the first numeric part it finds inside an arbitrary string, leaving the rest of the string untouched. The key insight is that the numeric portion must be detected and isolated within surrounding text (e.g. "US$1744 millions"), and only its integer digits before any decimal point or exponent are grouped — many edge cases (signs, leading zeroes, exponents, whitespace, subscripts) must be preserved exactly.

## Task Requirements
- Take a string plus optional parameters; commatize the first commatizable numeric run and return the modified string.
- If no suitable number exists, return the string unchanged with no error (quiet, non-failing execution); invalid options also cause no change.
- Never commatize the exponent part (e.g. `9.7e+12000`) nor leading zeroes (`0000000005714.882` becomes `0000000005,714.882`); treat any `.` as a decimal point.
- Preserve leading signs (even superfluous), all whitespace, exponent-indicator case, and any non-digit terminator including super/subscripts; support many exponent forms (`e`, `D`, `^`, `**`, `↑`, `²`, `<sup>`).
- Make the separator character(s) configurable (may be blanks/tabs/multiple chars), the period (group) length configurable (default 3), and the scan start position configurable (default 1).
- Correctly handle the prescribed test strings (pi to many digits grouped by 5 with blanks, Zimbabwe notes, the Eddington proton count, etc.).

## Language Coverage
33 languages implement this task, a moderate spread spanning systems, scripting, functional, and BASIC-family languages. Representative entries include C++, Go, Rust, Java, Python, Haskell, Perl, Raku, Julia, Kotlin, REXX, and Fortran.

## Connections
- [[StringProcessing]] — the core work is parsing and rewriting substrings within a larger string.
- [[RegularExpressions]] — a common technique for locating the numeric field and its boundaries.
- [[NumberFormatting]] — grouping digits with thousands separators is a formatting/localization concern.
- [[FiniteStateMachine]] — scanning sign, digits, decimal point, and exponent can be modeled as a small parser/state machine.

## Contradictions
- None — reference task page.
