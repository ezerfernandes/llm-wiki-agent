---
title: "Discordian date (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, calendar-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Discordian_date
---

## Summary
The task asks the programmer to convert a given date from the standard Gregorian calendar to the Discordian calendar used by the parody religion Discordianism. The key insight is that the Discordian year has five 73-day seasons (Chaos, Discord, Confusion, Bureaucracy, The Aftermath), with leap years inserting a special day (St. Tib's Day) between the 59th and 60th day of the first season rather than shifting the season boundaries.

## Task Requirements
- Accept a Gregorian calendar date as input.
- Compute the corresponding Discordian date (season, day-of-season, and Year of Our Lady of Discord = Gregorian year + 1166).
- Correctly handle leap years by emitting "St. Tib's Day" for February 29th instead of a regular season/day designation.

## Language Coverage
66 languages implement this task, showing broad coverage across assembly, systems, scripting, and functional ecosystems. Representative implementations include C, C++, C#, Java, Python, Perl, Haskell, Go, Rust, Ruby, and even low-level entries like 8080 Assembly and PL/M.

## Connections
- [[CalendarConversion]] — mapping between two distinct calendar systems
- [[GregorianCalendar]] — the source calendar for the conversion
- [[LeapYear]] — special-case handling for St. Tib's Day
- [[DayOfYear]] — ordinal day computation underlies the season/day mapping
- [[ModularArithmetic]] — used to derive season index and day-of-season

## Contradictions
- None — reference task page.
