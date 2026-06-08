---
title: "Holidays related to Easter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-arithmetic, calendar-computation, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Holidays_related_to_Easter
---

## Summary
The task asks the programmer to compute Easter Sunday and the moveable feasts that derive from it — Ascension Thursday, Pentecost, Trinity Sunday, Corpus Christi (Catholic), and All Saints' Sunday (Orthodox) — for a set of sample years. The core challenge is the *computus*: the arithmetic algorithm that locates Easter as the first Sunday after the first ecclesiastical full moon on or after the March equinox (approximated as March 21). Programs must handle both the Western (Gregorian) computus and the Eastern Orthodox (Julian) computus, and indicate which calendar each result is expressed in.

## Task Requirements
- Calculate the dates of Easter, Ascension Thursday (Easter + 39 days), Pentecost (+49), Trinity Sunday (+56), Corpus Christi (Catholic), and All Saints' Sunday (Orthodox).
- Compute these for the first year of each century from 400 to 2100 CE, and for years 2010 to 2020 CE.
- Use the ecclesiastical approximations (equinox fixed at March 21, arithmetic lunisolar tracking) rather than true astronomical values.
- Support both the Western/Catholic computus and the Eastern Orthodox computus.
- Output must indicate which computus was used and, for historical dates, which calendar (Julian vs. Gregorian) the dates are expressed in.

## Language Coverage
59 languages implement this task, spanning systems, scripting, functional, and BASIC dialects. Representative implementations include C, C++, C#, Java, Python, Go, Rust, Perl, Raku, Ruby, Common Lisp, and REXX.

## Connections
- [[Computus]] — the ecclesiastical algorithm for dating Easter
- [[ModularArithmetic]] — the Gauss/Anonymous Gregorian algorithm relies on modular remainders
- [[GregorianCalendar]] — Western computus operates on the reformed calendar
- [[JulianCalendar]] — Orthodox computus and pre-1582 dates use the original calendar
- [[DateArithmetic]] — derived feasts are fixed day offsets from Easter

## Contradictions
- None — reference task page.
