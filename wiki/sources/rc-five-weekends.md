---
title: "Five weekends (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Five_weekends
---

## Summary
The task asks the programmer to find every month between 1900 and 2100 (Gregorian calendar) that contains five full weekends — that is, five Fridays, five Saturdays, and five Sundays. The key insight is that this can only happen in a 31-day month whose first day falls on a Friday, which reduces the problem from counting weekdays to a simple day-of-week test on the first of each long month.

## Task Requirements
- Show all months from 1900 through 2100 that have five Fridays, five Saturdays, and five Sundays.
- Report the total count of such months (expected to be 201).
- Display at least the first five and last five qualifying dates, in chronological order.
- Extra credit: count and/or list the years that have no five-weekend month at all (expected to be 29).

## Language Coverage
102 languages implement this task, reflecting broad coverage across general-purpose, scripting, and esoteric languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Go, Rust, Ruby, Perl, and Wren.

## Connections
- [[CalendarArithmetic]] — relies on computing the day of the week for the first of each month.
- [[GregorianCalendar]] — the date range is bounded by Gregorian calendar rules.
- [[DayOfTheWeek]] — directly reuses day-of-week determination as a subroutine.
- [[ModularArithmetic]] — weekday cycling is naturally expressed with modulo 7.

## Contradictions
- None — reference task page.
