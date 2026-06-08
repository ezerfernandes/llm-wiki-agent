---
title: "Find the last Sunday of each month (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, calendar]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_the_last_Sunday_of_each_month
---

## Summary
The task is to write a program that, given a year as input, prints the date of the last Sunday in each of that year's twelve months. Output is formatted as `YYYY-MM-DD`, one line per month. The key insight is mapping each calendar month to its final occurrence of a given weekday, which most solutions handle either via date-library weekday lookups or by counting back from the last day of the month.

## Task Requirements
- Accept a year through any simple input method (command line, stdin, etc.).
- For each of the 12 months of that year, determine the date of the last Sunday.
- Print the 12 dates in chronological order, formatted as `YYYY-MM-DD`.

## Language Coverage
99 languages implement this task, giving very broad coverage across general-purpose, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, C#, Java, Python, Ruby, Perl, Go, Rust, Haskell, JavaScript, and REXX.

## Connections
- [[CalendarArithmetic]] — computing weekdays within months and month-end boundaries
- [[ZellersCongruence]] — a classic algorithm for finding the day of the week for a date
- [[DateAndTime]] — domain of date/time handling and formatting
- [[ModularArithmetic]] — underlies weekday-offset calculations from a known anchor day

## Contradictions
- None — reference task page.
