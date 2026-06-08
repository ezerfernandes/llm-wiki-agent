---
title: "Leap year (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-and-time, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Leap_year
---

## Summary
This task asks the programmer to determine whether a given year is a leap year under the Gregorian calendar. The key insight is the divisibility rule: a year is a leap year if it is divisible by 4, except that century years (divisible by 100) must also be divisible by 400 to qualify. This collapses to a single boolean expression rather than relying on a built-in date library.

## Task Requirements
- Given an arbitrary year, return whether it is a leap year in the Gregorian calendar.
- Apply the rule: divisible by 4 is a leap year, unless divisible by 100 and not by 400.

## Language Coverage
170 languages implement this task, an exceptionally broad spread covering mainstream languages, assembly, and esoteric ones. Representative implementations include C, Python, Java, JavaScript, Haskell, Rust, Go, COBOL, Fortran, and APL.

## Connections
- [[GregorianCalendar]] — the calendar system whose intercalation rule defines the task
- [[Divisibility]] — the core test uses modular divisibility by 4, 100, and 400
- [[ModularArithmetic]] — the leap-year predicate is expressed via remainder operations
- [[BooleanLogic]] — combining the divisibility conditions into a single predicate

## Contradictions
- None — reference task page.
