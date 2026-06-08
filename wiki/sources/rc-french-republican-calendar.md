---
title: "French Republican calendar (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, calendar-conversion, date-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/French_Republican_calendar
---

## Summary
The task is to write a bidirectional converter between the Gregorian calendar and the French Republican calendar, whose year 1 began on 22 September 1792. The key insight is that the Republican year has twelve 30-day months plus five (or six in leap years) intercalary days called Sansculottides, so conversion reduces to counting day offsets from the calendar's epoch and mapping them into this fixed 30-day-month structure.

## Task Requirements
- Convert dates in both directions: Gregorian to Republican and Republican to Gregorian.
- Model twelve 30-day months (Vendémiaire through Fructidor) followed by five Sansculottides (Virtue, Talent, Labour, Opinion, Honours Day).
- Add a sixth Sansculottide (Revolution Day) in leap years 3, 7, and 11.
- Produce correct results at least over the official range 1 Vendémiaire 1 (22 Sep 1792) to 10 Nivôse 14 (31 Dec 1805).
- For later dates, state which leap-year rule is being used since methods diverge after year 14.
- Verify against the five given test dates (including the Rosetta Stone discovery, 27 Messidor 7 = 15 July 1799).

## Language Coverage
20 languages implement this task, a moderate spread covering systems, scripting, and functional styles. Representative entries include C++, Rust, Go, Java, JavaScript, F#, Julia, Perl, Raku, and Wren.

## Connections
- [[CalendarConversion]] — the core operation between two calendar systems
- [[GregorianCalendar]] — the source/target reference calendar
- [[DateArithmetic]] — day-offset counting from an epoch drives the mapping
- [[LeapYearRules]] — divergent post-year-14 leap rules are central to correctness

## Contradictions
- None — reference task page.
