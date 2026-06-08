---
title: "Doomsday rule (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Doomsday_rule
---

## Summary
This task asks the programmer to implement John Conway's Doomsday rule, a mental-arithmetic algorithm for finding the day of the week for any given date. The key insight is that within any year a set of "doomsday" dates (e.g., 4/4, 6/6, 8/8, the last day of February) all fall on the same weekday, the year's "anchor day"; once that anchor is computed, the weekday of any date is found by counting days to the nearest doomsday and reducing modulo 7.

## Task Requirements
- Compute a year's doomsday (anchor weekday) via `doomsday = (2 + 5(y mod 4) + 4(y mod 100) + 6(y mod 400)) % 7`, with Sunday = 0 through Saturday = 6.
- Use the per-month doomsday-date table (with separate January/February rules for common vs leap years) to count the offset from the date to a nearby doomsday.
- Add the year's doomsday to that offset and take the result mod 7 to get the weekday.
- Apply this to seven specified test dates ranging from 1800-01-06 to 2101-04-02 and report each day of the week.

## Language Coverage
54 languages implement this task, spanning systems languages, scripting languages, functional languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, JavaScript, and APL.

## Connections
- [[ModularArithmetic]] — the algorithm is built entirely on arithmetic modulo 7.
- [[GregorianCalendar]] — leap-year handling (mod 4/100/400) underpins the anchor-day formula.
- [[DayOfWeekCalculation]] — Doomsday is one of several mental algorithms for weekday determination.
- [[JohnConway]] — the rule's inventor, also known for the Game of Life.

## Contradictions
- None — reference task page.
