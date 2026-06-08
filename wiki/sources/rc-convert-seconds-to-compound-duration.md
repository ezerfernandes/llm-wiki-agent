---
title: "Convert seconds to compound duration (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, time-conversion, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Convert_seconds_to_compound_duration
---

## Summary
The task asks for a function that takes a positive integer of seconds and decomposes it into weeks, days, hours, minutes, and seconds, formatted as a human-readable string. The key insight is greedy decomposition by successive division/modulo against fixed conversion factors (7, 24, 60, 60), giving larger units precedence, then suppressing any unit whose value is zero.

## Task Requirements
- Accept a positive integer duration in seconds (e.g., 100).
- Decompose into the five units week, day, hour, minute, second, using factors 1 wk = 7 d, 1 d = 24 hr, 1 hr = 60 min, 1 min = 60 sec.
- Emit only non-zero quantities (e.g., "1 d", not "0 wk, 1 d, 0 hr, ...").
- Maximize larger units (e.g., "2 min, 10 sec", never "1 min, 70 sec" or "130 sec").
- Format largest-to-smallest, comma+space separated, value and suffix (wk, d, hr, min, sec) separated by a space.
- Pass test cases: 7259 -> "2 hr, 59 sec"; 86400 -> "1 d"; 6000000 -> "9 wk, 6 d, 10 hr, 40 min".

## Language Coverage
94 languages implement this task, spanning systems and scripting languages as well as many BASIC dialects and Lisps. Representative examples include C, C++, Java, Python, Go, Rust, Haskell, Perl, Ruby, Common Lisp, and REXX.

## Connections
- [[ModularArithmetic]] — repeated division and remainder against unit factors
- [[StringFormatting]] — assembling and joining only non-zero terms
- [[GreedyAlgorithm]] — assign to the largest unit first
- [[UnitConversion]] — fixed time-base conversion factors

## Contradictions
- None — reference task page.
