---
title: "Periodic table (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lookup-table]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Periodic_table
---

## Summary
Given an atomic number (1 to 118), display its row and column position in the periodic table. The challenge uses a specific table layout where lanthanides and actinides occupy their own dedicated rows (8 and 9), so positions like row 6 column 3 and row 7 column 3 are never returned. The core insight is that this is a lookup/mapping problem rather than chemistry — the mapping from element index to grid coordinates must handle the irregular shape of the table (gaps in periods 1-3 and the displaced f-block).

## Task Requirements
- Accept an atomic number between 1 and 118 inclusive.
- Output the corresponding row and column in the periodic table.
- Use the table representation given, where lanthanides and actinides are placed in their own rows (rows 8 and 9), leaving no element at row 6 column 3 or row 7 column 3.
- Match the provided example cases, e.g. 1 -> 1 1, 2 -> 1 18, 29 -> 4 11, 57 -> 8 4, 72 -> 6 4, 89 -> 9 4.

## Language Coverage
35 languages implement this task, spanning low-level assembly to high-level interpreters. Representative implementations include C, C++, C#, Java, JavaScript, Python, Perl, Raku, Go, Julia, and Wren.

## Connections
- [[LookupTable]] — the mapping from atomic number to coordinates is typically a precomputed table
- [[PeriodicTable]] — the chemistry domain object being modeled
- [[ArrayIndexing]] — translating a linear element index into 2D grid positions
- [[ConditionalLogic]] — special-casing the f-block and early-period gaps

## Contradictions
- None — reference task page.
