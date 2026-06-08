---
title: "Averages/Mean time of day (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, circular-statistics, date-and-time]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Mean_time_of_day
---

## Summary
The task asks the programmer to compute the average of several times of day, treating the 24-hour clock as a circle (24 hours mapping to 360 degrees, just as compass bearings or clock angles wrap around). The key insight is that times cannot be averaged arithmetically because they wrap past midnight; instead each time is converted to an angle, averaged as a mean angle (via the mean of the sine and cosine components), and the resulting angle is mapped back to a time of day accurate to one second.

## Task Requirements
- Average the four given times: 23:00:17, 23:40:20, 00:12:45, 00:17:19.
- Map each time of day to an angle, using 24 hours = 360 degrees.
- Apply the mean-angle technique (average the unit vectors / sin and cos components, then take atan2).
- Convert the mean angle back to a time of day.
- Show the result to an accuracy of one second.

## Language Coverage
74 languages implement this task, spanning systems, scripting, functional, and even database query languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Perl, Raku, Ruby, and SQL/PostgreSQL.

## Connections
- [[MeanAngle]] — the circular-mean technique this task directly builds on
- [[CircularStatistics]] — averaging quantities that wrap around a cycle
- [[Atan2]] — recovers the mean angle from summed sine and cosine components
- [[ModularArithmetic]] — handling the wraparound past midnight
- [[UnitCircle]] — mapping times to points on a circle for vector averaging

## Contradictions
- None — reference task page.
