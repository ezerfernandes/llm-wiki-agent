---
title: "Biorhythms (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, date-arithmetic, trigonometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Biorhythms
---

## Summary
This task implements the late-1970s pseudoscience of biorhythms, whose underlying math is trivial. Given a birthdate and a target date, it computes three sinusoidal "life cycle" values from the number of days elapsed since birth. The key insight is that each cycle value for day k of an n-day cycle is simply sin(2πk / n), so the whole exercise reduces to a days-between-dates calculation plus a modulo and a sine.

## Task Requirements
- Compute the number of days between the birthdate and the target date.
- Take that day count modulo each cycle length: Physical = 23 days, Emotional = 28 days, Mental = 33 days.
- For each cycle, compute the value in [-1, +1] as sin(2πk / n), where k is the residue.
- Output the three biorhythmic values for the target day.
- Optionally describe position/trend (peak, valley, critical/crossing, rising, falling), report the next notable event date, or graph the cycles.
- Demonstrate with chosen dates.

## Language Coverage
43 languages implement this task, spanning systems, scripting, functional, and legacy BASIC/Lisp dialects. Representative implementations include C, C++, Go, Rust, Java, Python, Ruby, Perl, Raku, Common Lisp, and Fortran.

## Connections
- [[DaysBetweenDates]] — the date-difference subproblem this task builds on
- [[ModularArithmetic]] — residue of the day count modulo each cycle length
- [[Trigonometry]] — sine function generating each cycle's value
- [[SineWave]] — each cycle is modeled as a perfect sinusoid

## Contradictions
- None — reference task page.
