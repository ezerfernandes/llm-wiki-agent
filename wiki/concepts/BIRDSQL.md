---
title: "BIRD-SQL"
type: concept
tags: [benchmark, text-to-sql, evaluation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# BIRD-SQL

**BIRD-SQL** — *Big Bench for Large-scale Database Grounded Text-to-SQL Evaluation* (Li et al. 2023) — is a text-to-SQL benchmark designed to push past [[Spider]]'s relatively simple schemas into **realistic, large-scale databases**. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], BIRD-SQL evaluates models using [[FunctionalCorrectness|functional correctness]] — the generated SQL is executed and outputs are compared to expected results.

## Why "Big Bench"

The benchmark name signals its move beyond [[Spider]]: rather than carefully curated small schemas, BIRD-SQL exposes models to the schema diversity and column-naming idiosyncrasies of real databases (think analyst-grade tables, not toy textbook tables). This shifts the difficulty axis from *syntactic SQL generation* to *schema grounding and column disambiguation*.

## Position

Latest entry in the text-to-SQL benchmark lineage (as of Ch 3, late 2024):

| Benchmark | Year | Position |
|---|---|---|
| [[WikiSQL]] | 2017 | Simple schemas, single-table queries |
| [[Spider]] | 2018 | Multi-table, harder joins |
| **BIRD-SQL** | 2023 | Realistic large-scale databases |

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FunctionalCorrectness]] / [[ExecutionAccuracy]] — the eval paradigm.
- [[Spider]] / [[WikiSQL]] — sibling text-to-SQL benchmarks.
- [[SemanticParsing]] — parent task.
