---
title: "Mutation Testing"
type: concept
tags: [testing, mutation-testing, test-adequacy, quality, software-engineering, alias]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Mutation Testing

**Mutation testing** is a synonym for [[MutationAnalysis|mutation analysis]] — the practice of seeding small artificial faults ([[Mutant|mutants]]) into a program and measuring what fraction a test suite kills ([[MutationScore|mutation score]]) to judge [[TestAdequacy|test adequacy]]. The two terms are used interchangeably in the literature and in [[fuzzingbook-08-mutation-analysis|Ch 8]] of *The Fuzzing Book*.

> See **[[MutationAnalysis]]** for the full treatment (frameworks, [[MutationOperator|operators]], [[EquivalentMutant|equivalent mutants]], and the contrast with [[MutationBasedFuzzing|mutation-based fuzzing]]). This page exists so the established term resolves to a page.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] uses "mutation analysis" as its primary term; "mutation testing" is the equally common name in tools like PIT, mutmut, and Stryker. Both denote the same idea: grade a test suite by its ability to *kill* mutated copies of the program under test, a stronger [[TestAdequacy|adequacy]] signal than [[Coverage|coverage]].

## Connections
- [[MutationAnalysis]] — the canonical page; this is its alias.
- [[Mutant]] / [[MutationScore]] / [[MutationOperator]] / [[EquivalentMutant]] — the core vocabulary.
- [[TestAdequacy]] — what it measures.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
