---
title: "Date format (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-time, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Date_format
---

## Summary
This task asks the programmer to obtain the current system date and render it in two distinct textual formats: the ISO-8601 numeric form (e.g. `2007-11-23`) and a long, human-readable form including the weekday and spelled-out month name (e.g. `Friday, November 23, 2007`). The key insight is exercising a language's date/time facilities to both query the system clock and apply locale-aware formatting templates.

## Task Requirements
- Display the current date in the numeric format `YYYY-MM-DD` (e.g. `2007-11-23`).
- Display the current date in the long format `Weekday, Month DD, YYYY` (e.g. `Friday, November 23, 2007`).

## Language Coverage
148 languages implement this task, reflecting that nearly every general-purpose language ships date/time formatting in its standard library. Representative implementations include Python, C, C#, Java, JavaScript, Go, Rust, Ruby, Haskell, Perl, and PowerShell.

## Connections
- [[DateAndTime]] — core domain of obtaining and representing calendar dates
- [[ISO8601]] — the standard behind the `YYYY-MM-DD` numeric format
- [[StringFormatting]] — applying format templates to produce textual output
- [[Localization]] — weekday and month names are locale-dependent

## Contradictions
- None — reference task page.
