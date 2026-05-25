---
title: "Spider"
type: concept
tags: [benchmark, text-to-sql, evaluation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Spider

**Spider** (Yu et al. 2018) is a benchmark for **text-to-SQL** — generating SQL queries from natural-language questions. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], Spider, like [[BIRDSQL]] and [[WikiSQL]], evaluates models using [[FunctionalCorrectness|functional correctness]]: the generated SQL is executed against a database and the output is compared to the expected output.

## Why text-to-SQL is a functional-correctness fit

Two SQL queries that look textually different may return the same result set, and two queries that look similar may return wildly different results. Surface-overlap metrics ([[bleu|BLEU]], [[ROUGE]]) penalize the former and let the latter pass. **Execution-based evaluation is the only one that reflects what the user actually cares about** — does the query return the right rows?

## Position in the text-to-SQL lineage

| Benchmark | Year | Authors |
|---|---|---|
| [[WikiSQL]] | 2017 | Zhong et al. |
| **Spider** | 2018 | Yu et al. |
| [[BIRDSQL]] | 2023 | Li et al. (Big Bench for Large-scale Database Grounded Text-to-SQL Evaluation) |

Spider sits between WikiSQL (simpler schemas) and BIRD-SQL (larger and more realistic databases).

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FunctionalCorrectness]] / [[ExecutionAccuracy]] — the eval paradigm.
- [[WikiSQL]] / [[BIRDSQL]] — sibling text-to-SQL benchmarks.
- [[HumanEval]] / [[MBPP]] — code-generation siblings using the same paradigm.
- [[SemanticParsing]] — the parent NLP task.
