---
title: "Adequacy Criterion"
type: concept
tags: [testing, test-adequacy, metrics, quality, software-engineering, alias]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Adequacy Criterion

An **adequacy criterion** is a concrete, measurable rule that decides whether a test suite is "good enough" by defining a set of *test requirements* and scoring the fraction satisfied. Examples: statement [[Coverage|coverage]], branch coverage, path coverage, and **mutation adequacy** ([[MutationScore|mutation score]]). It is the operational form of the broader question of [[TestAdequacy|test adequacy]].

> See **[[TestAdequacy]]** for the full discussion of why structural-coverage criteria are weak and why mutation adequacy is stronger.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] contrasts the [[Coverage|coverage]] adequacy criterion (require each statement be *executed*) with the mutation-adequacy criterion (require each [[Mutant|mutant]] be *killed*). Because the latter forces the suite's [[Assertion|assertions]]/[[TestOracle|oracle]] to observe incorrect behavior, mutation adequacy is the stronger criterion — it distinguishes suites that coverage rates as equal.

## Connections
- [[TestAdequacy]] — the canonical page this companions.
- [[Coverage]] — a weak structural adequacy criterion.
- [[MutationScore]] / [[MutationAnalysis]] — the mutation-adequacy criterion.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
