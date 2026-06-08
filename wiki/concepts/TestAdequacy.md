---
title: "Test Adequacy"
type: concept
tags: [testing, test-adequacy, metrics, quality, mutation-testing, software-engineering]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Test Adequacy

**Test adequacy** is the question *"is this test suite good enough?"* — and an **adequacy criterion** ([[AdequacyCriterion]]) is a concrete, measurable rule for answering it. An adequacy criterion defines a set of *test requirements* a suite must satisfy; the fraction satisfied is the **adequacy score**. Common criteria form a rough hierarchy of strength: statement [[Coverage|coverage]] → branch coverage → path coverage → **mutation adequacy** ([[MutationScore|mutation score]]).

The key insight (sharpened by [[fuzzingbook-08-mutation-analysis|Ch 8]]) is that *structural coverage criteria are weak* — they require only that code be *executed*, never that its result be *checked*. Mutation adequacy is stronger because killing a [[Mutant|mutant]] requires the suite's [[Assertion|assertions]]/[[TestOracle|oracle]] to actually observe wrong behavior.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] argues that coverage is an inadequate adequacy criterion: a `weak_oracle()` and a `strong_oracle()` for `triangle()` reach identical [[Coverage|statement coverage]] yet differ enormously in bug-finding power, which only [[MutationAnalysis|mutation analysis]] reveals (20% vs 100% [[MutationScore|mutation score]]). It positions mutation adequacy as a superior criterion that grades the *quality of assertions*, and notes mutation analysis can grade not just hand-written suites but fuzzers and static/symbolic-execution tools — making it a general adequacy yardstick across automated bug-finding techniques.

## Connections
- [[AdequacyCriterion]] — the concrete rule form of adequacy (alias/companion).
- [[Coverage]] — the most common (but weak) structural adequacy criterion.
- [[MutationAnalysis]] / [[MutationScore]] — mutation adequacy, the stronger criterion.
- [[Mutant]] — the test requirements under mutation adequacy.
- [[TestOracle]] / [[Assertion]] — what mutation adequacy grades that coverage ignores.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
