---
title: "Last Friday of each month (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, calendar-computation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Last_Friday_of_each_month
---

## Summary
The task asks for a program that, given a year, prints the date of the last Friday in each of that year's twelve months. The year is supplied through any convenient input method (command line, stdin, etc.). The key insight is to walk backward from the last day of each month — or compute it via weekday arithmetic — until a Friday is found, handling month lengths and leap years correctly.

## Task Requirements
- Accept a year via any simple input method.
- For each of the 12 months, determine the date of the final Friday.
- Output the dates, typically in `YYYY-MM-DD` format, one per line (the example uses 2012).

## Language Coverage
104 languages implement this task, reflecting its appeal as a date-arithmetic exercise across nearly every major paradigm. Representative implementations include C, C++, Python, Java, Haskell, Perl, Ruby, Go, Rust, PowerShell, and REXX.

## Connections
- [[CalendarArithmetic]] — computing month lengths and iterating over months of a year.
- [[DayOfTheWeek]] — determining the weekday for a given date.
- [[ZellersCongruence]] — a classic formula for finding the day of the week of any date.
- [[LeapYear]] — February's length affects the last-Friday computation.

## Contradictions
- None — reference task page.
