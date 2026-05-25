---
title: "WikiSQL"
type: concept
tags: [benchmark, text-to-sql, evaluation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# WikiSQL

**WikiSQL** (Zhong et al. 2017) is one of the earliest large text-to-SQL benchmarks — natural-language questions paired with reference SQL queries against Wikipedia tables. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], WikiSQL evaluates models using [[FunctionalCorrectness|functional correctness]] (execute the SQL, compare output) rather than surface-string match.

## Position in the text-to-SQL lineage

| Benchmark | Year | Position |
|---|---|---|
| **WikiSQL** | 2017 | Single-table queries on Wikipedia tables |
| [[Spider]] | 2018 | Multi-table joins, harder schemas |
| [[BIRDSQL]] | 2023 | Realistic large-scale databases |

WikiSQL is the entry point; [[Spider]] and [[BIRDSQL]] progressively push toward production-grade SQL complexity.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FunctionalCorrectness]] / [[ExecutionAccuracy]] — the eval paradigm.
- [[Spider]] / [[BIRDSQL]] — sibling text-to-SQL benchmarks.
- [[SemanticParsing]] — parent task.
