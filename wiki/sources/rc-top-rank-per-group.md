---
title: "Top rank per group (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, grouping, data-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Top_rank_per_group
---

## Summary
The task asks the programmer to find the top *N* salaries within each department from a small fixed employee dataset, where *N* is a parameter. The key insight is the "group-by then rank-within-group" pattern: partition records by a grouping key (department), sort each partition by a metric (salary, descending), and emit the top *N* of each group. It mirrors the SQL windowing idiom of ranking rows within partitions.

## Task Requirements
- Use the provided 13-employee dataset (name, ID, salary, department) as a language-native internal data structure rather than parsing it at runtime.
- Accept *N* as a parameter controlling how many top earners to report.
- Group employees by department.
- Within each department, select the *N* highest salaries.
- Output the resulting top-ranked employees per department.

## Language Coverage
92 languages implement this task, showing broad coverage across imperative, functional, query, and scripting paradigms. Representative implementations include Python, Java, C++, Haskell, Ruby, Go, Rust, Perl, SQL, and Mathematica.

## Connections
- [[Sorting]] — each group is ordered by salary to find the top entries
- [[GroupBy]] — records are partitioned by department before ranking
- [[WindowFunctions]] — SQL solutions use partitioned ranking over a window
- [[DataAggregation]] — summarizing and selecting subsets of tabular data

## Contradictions
- None — reference task page.
