---
title: "Mutation Score"
type: concept
tags: [testing, mutation-testing, metrics, test-adequacy, quality, software-engineering]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Mutation Score

The **mutation score** is the headline metric of [[MutationAnalysis|mutation analysis]]: the proportion of generated [[Mutant|mutants]] that a test suite **kills** (detects) out of all *valid* mutants produced.

```
mutation_score = killed_mutants / total_valid_mutants
              = (nmutations − surviving_mutants) / nmutations
```

A score of 1.0 means every mutant was killed; 0.2 means only 20% were detected. It is a strictly stronger [[TestAdequacy|adequacy]] signal than [[Coverage|coverage]] because it reflects the quality of a suite's [[Assertion|assertions]]/[[TestOracle|oracle]], not just which lines ran.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] computes it in `score()` as `(self.nmutations - len(self.un_detected)) / self.nmutations`. The chapter's flagship demonstration: on `triangle()`, a `weak_oracle()` and a `strong_oracle()` reach *identical* [[Coverage|coverage]] but mutation scores of **20%** and **100%** respectively, and a `TestGCD` suite scores **42%** on `gcd()`. This separation is the chapter's core argument that mutation score is "a better indicator of the quality of a given test suite than pure coverage." A key caveat: [[EquivalentMutant|equivalent mutants]] (never killable) distort the score — with a reported score of 70%, anywhere from 0–30% of mutants could be equivalent, so the *achievable* score is unknown without estimating the equivalent count (via statistical sampling or Chao's estimator).

## Connections
- [[MutationAnalysis]] — the technique that produces the score.
- [[Mutant]] — the killed/surviving units being counted.
- [[EquivalentMutant]] — inflates the denominator and distorts the score.
- [[Coverage]] — the weaker metric mutation score is shown to dominate.
- [[TestAdequacy]] — mutation score realizes a mutation-adequacy criterion.
- [[Assertion]] / [[TestOracle]] — what the score actually grades (oracle strength).

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
