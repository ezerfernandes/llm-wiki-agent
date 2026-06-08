---
title: "Date manipulation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-time, string-parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Date_manipulation
---

## Summary
The task asks the programmer to parse the date string "March 7 2009 7:30pm EST", add 12 hours to it, and output the resulting time in any human-readable format. The key insight is correctly interpreting the named month, 12-hour clock with am/pm, and the time zone abbreviation, then performing time arithmetic that respects calendar and zone rules. Extra credit is to display the result in a different time zone from one's own.

## Task Requirements
- Parse the literal date string "March 7 2009 7:30pm EST" into a date/time value.
- Add 12 hours to that moment.
- Output the result in any human-readable format.
- Extra credit: also render the result in a time zone different from the local one.

## Language Coverage
87 languages implement this task, showing broad coverage across general-purpose and scripting languages with diverse date/time library maturity. Representative implementations include C, C++, Java, Python, Perl, Ruby, Go, Rust, JavaScript, Haskell, Tcl, and PowerShell.

## Connections
- [[DateTimeParsing]] — converting the textual date into a structured value
- [[TimeZones]] — interpreting EST and rendering in another zone
- [[CalendarArithmetic]] — adding a 12-hour offset while honoring date/time rules
- [[StringProcessing]] — reading the named month and am/pm token

## Contradictions
- None — reference task page.
