---
title: "Calendar (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, text-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Calendar
---

## Summary
This task asks the programmer to write a routine that generates a full text calendar for any given year, laying out all twelve months in a grid that fits a fixed page width. The reference test is a 1969 calendar formatted for period devices: a 132-character line printer or an 80x43 IBM 3278 terminal. The key challenge is weekday computation for each month combined with multi-column text layout that adapts to the available width.

## Task Requirements
- Generate a text calendar for any year.
- Test by producing a 1969 calendar sized for one of: a 132-character line printer, or an 80x43 IBM 3278 terminal (months arranged across 80 columns, output capped at 43 lines).
- Ideally support any page width from 20 characters upward.
- Output a placeholder rather than generating the actual Snoopy artwork.
- Bonus (kudos) for handling the Julian-to-Gregorian calendar transition.

## Language Coverage
84 languages implement this task, showing very broad coverage across systems, scripting, functional, and legacy mainframe languages. Representative implementations include C, C++, Python, Java, Go, Rust, Haskell, COBOL, REXX, and 360 Assembly.

## Connections
- [[DateAndTime]] — computing weekdays and month lengths
- [[ZellersCongruence]] — common algorithm for day-of-week from a date
- [[GregorianCalendar]] — the standard calendar system being rendered
- [[TextFormatting]] — multi-column layout fitting a fixed page width
- [[LeapYear]] — February length depends on leap-year rules

## Contradictions
- None — reference task page.
