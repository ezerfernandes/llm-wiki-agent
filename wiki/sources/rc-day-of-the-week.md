---
title: "Day of the week (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-time, calendar]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Day_of_the_week
---

## Summary
This task asks the programmer to determine in which years between 2008 and 2121 December 25th (Christmas) falls on a Sunday. The framing is a company policy that grants extra holidays whenever Xmas lands on a Sunday. The deeper intent is to exercise a language's standard date-handling library and to surface cross-language discrepancies caused by date/time overflow bugs (akin to Y2K-style problems).

## Task Requirements
- Find every year in the inclusive range 2008-2121 where 25 December is a Sunday.
- Use the language's standard date-handling library to compute the weekday.
- Compare results across implementations to expose anomalies from date/time type overflow or representation limits.

## Language Coverage
158 languages implement this task, reflecting near-universal support since computing a weekday is a common date-library operation. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Ruby, Perl, and REXX.

## Connections
- [[GregorianCalendar]] — the calendar system whose rules govern the weekday computation
- [[ZellersCongruence]] — a classic algorithm for determining the day of the week from a date
- [[DateTimeLibraries]] — standard library facilities the task is meant to exercise
- [[IntegerOverflow]] — the source of the date-handling anomalies the task probes

## Contradictions
- None — reference task page.
