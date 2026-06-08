---
title: "Worthwhile task shaving (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, table-formatting, time-calculation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Worthwhile_task_shaving
---

## Summary
Recreate the table from XKCD comic #1205 ("Is It Worth the Time?"), which humorously shows the maximum time you can spend automating or optimizing a routine task before the optimization costs more time than it ever saves, measured over a five-year horizon. The table is indexed by how often the task is performed (from 50 times/day down to once/year) against how much time each run saves (from 1 second up to 1 day). The key insight is simply: break-even time = (time saved per run) × (number of runs over five years).

## Task Requirements
- Reproduce the XKCD #1205 grid of break-even times.
- Rows correspond to task frequency (e.g., 50/day, 5/day, daily, weekly, monthly, yearly).
- Columns correspond to time shaved off each run (1s, 5s, 30s, 1min, 5min, 30min, 1hr, 6hr, 1day).
- Compute and format the resulting allowable optimization time over five years, choosing an interpretation of "day" and "week" (8h/5-day work weeks vs. 24h/7-day weeks).
- Aim for playful presentation over rigid scientific accuracy.

## Language Coverage
16 languages implement this task, spanning systems, scripting, and BASIC-family languages. Representative implementations include ALGOL 68, C++, Java, Python, Perl, Raku, Julia, Nim, jq, Wren, and several BASIC dialects (FreeBASIC, FutureBasic, Yabasic, EasyLang) along with Phix and V (Vlang).

## Connections
- [[TableFormatting]] — laying out the frequency-by-savings grid in aligned columns
- [[UnitConversion]] — converting seconds into minutes, hours, days, and weeks
- [[TimeArithmetic]] — computing break-even durations over a fixed five-year window
- [[CostBenefitAnalysis]] — the underlying premise of when optimization pays off

## Contradictions
- None — reference task page.
