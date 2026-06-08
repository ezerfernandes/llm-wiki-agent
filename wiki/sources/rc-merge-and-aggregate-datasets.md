---
title: "Merge and aggregate datasets (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-processing, aggregation, csv]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Merge_and_aggregate_datasets
---

## Summary
The task asks the programmer to join two datasets — a `patients` table (PATIENT_ID, LASTNAME) and a `visits` table (PATIENT_ID, VISIT_DATE, SCORE) — and produce a per-patient summary. For each patient the result must combine the last name, the maximum visit date, and the sum and average of scores. The key insight is that this mirrors a relational LEFT JOIN followed by a GROUP BY aggregation, while correctly handling missing values (blank dates and scores must be excluded from max/sum/avg, and patients with no visits still appear with empty aggregate fields).

## Task Requirements
- Load or hard-code the two `.csv` datasets (patients and visits).
- Merge/join the datasets on PATIENT_ID (keeping all patients, even those without visits).
- Group per patient id and last name.
- Compute the maximum visit date (ISO dates may be compared as text).
- Compute the sum and average of the scores per patient.
- Handle blank/missing dates and scores gracefully.
- Output the resulting dataset to memory, screen, or file as appropriate.

## Language Coverage
36 languages implement this task, spanning data-science languages, general-purpose languages, and dedicated query/database languages. Representative examples include Python, R, SAS, SPSS, F#, SQL, DuckDB, jq, Haskell, Julia, and Wren.

## Connections
- [[RelationalJoin]] — merging on a shared key is a LEFT JOIN
- [[GroupByAggregation]] — grouping rows and reducing to summary statistics
- [[CSVParsing]] — reading the tabular source data
- [[MissingValueHandling]] — excluding blanks from max/sum/average
- [[DataFrame]] — the natural data structure in data-science languages

## Contradictions
- None — reference task page.
