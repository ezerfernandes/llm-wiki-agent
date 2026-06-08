---
title: "Long year (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-time, calendar]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Long_year
---

## Summary
This task asks the programmer to write a function that determines whether a given year is "long" under the ISO 8601 week-date system, meaning it contains 53 ISO weeks rather than the usual 52. The key insight is that an ISO year is long exactly when January 1 falls on a Thursday, or when it is a leap year whose January 1 falls on a Wednesday — equivalently, when December 31 (or the last Thursday) lands in the 53rd week.

## Task Requirements
- Write a function that takes a year and returns whether it is a long year (53 ISO weeks) or a short year (52 weeks).
- Base the determination on the ISO 8601 week-date definition of weeks per year.
- Demonstrate the function on sample years.

## Language Coverage
79 languages implement this task, giving very broad coverage across systems, scripting, functional, and esoteric languages. Representative implementations include C, C++, Java, Python, Rust, Go, Haskell, Perl, Raku, Ruby, JavaScript, and Common Lisp.

## Connections
- [[ISO8601]] — the week-date standard that defines weeks per year
- [[CalendarArithmetic]] — computing weekday of a date and leap-year handling
- [[LeapYear]] — leap years influence which weekday January 1 falls on
- [[ModularArithmetic]] — used in formulas that derive the weekday from the year

## Contradictions
- None — reference task page.
