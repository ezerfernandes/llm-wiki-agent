---
title: "Mayan calendar (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, calendar-conversion, date-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mayan_calendar
---

## Summary
The task asks the programmer to write a reusable routine that converts a Gregorian date into its Mayan calendar equivalents: both the cyclical Calendar Round (Tzolk'in sacred date + Haab' civil date, optionally with the nine-day Lords of the Night cycle) and the linear Long Count. The key insight is that conversion is best done by computing a single absolute day count from a fixed correlation epoch (the GMT correlation, Julian day 584283 = Aug 11, 3114 BCE = Long Count 13.0.0.0.0), then taking modular arithmetic for the cyclic parts and base-20/18 positional decomposition for the Long Count.

## Task Requirements
- Take a Gregorian date and return its equivalent in the Calendar Round and the Long Count.
- Use at least the GMT correlation factor (584283); supporting other correlations is optional.
- Correctly handle Gregorian leap days, covering at least 50 years before and after the Dec 21, 2012 (13.0.0.0.0) rollover.
- Calendar Round output is "number name (Tzolk'in) day month (Haab')", e.g. Dec 21, 2012 = "4 Ajaw 3 K'ank'in G9"; Long Count for that date is "13.0.0.0.0".
- Produce output for a given set of test dates (2004-06-19, 2012-12-18, 2012-12-21, 2019-01-19, 2019-03-27, 2020-02-29, 2020-03-01).

## Language Coverage
21 languages implement this task, spanning systems and scripting languages alongside several BASIC dialects. Representative implementations include C++, Go, Rust, Java, Python, Perl, Raku, Julia, Nim, J, jq, and Wren.

## Connections
- [[ModularArithmetic]] — the Tzolk'in (260-day), Haab' (365-day), and Lords-of-the-Night (9-day) cycles are computed via modulo of the day count.
- [[CalendarConversion]] — mapping between Gregorian and Mayan dating systems via a fixed epoch correlation.
- [[MixedRadixNumber]] — the Long Count is a positional notation in mixed bases (k'in, winal=20, tun=18, k'atun=20, bak'tun=20).
- [[JulianDayNumber]] — the GMT correlation anchors the conversion to an absolute serial day count.

## Contradictions
- None — reference task page.
