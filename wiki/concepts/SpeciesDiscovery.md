---
title: "Species Discovery (STADS)"
type: concept
tags: [fuzzing, testing, statistics, estimation, ecology, residual-risk, stads]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Species Discovery (STADS)

**Software Testing as Species Discovery (STADS)** is a statistical framework, due to [[MarcelBohme|Marcel Böhme]] (ACM TOSEM 2018), that reframes [[Fuzzing|fuzzing]] as an instance of the **species-discovery** problem from ecology: a sampling process in which each individual drawn belongs to exactly one (or more) **species**, and we want to estimate how many species remain unseen and how likely the *next* sample is to belong to a new one.

## The mapping

| Ecology | Fuzzing |
|---|---|
| Individual sampled | Test input generated |
| Species | Equivalence class of inputs — e.g. an **execution trace** (set of statements covered), a path, or a branch-hash |
| Discovering a new species | Covering a new trace / path |
| Likelihood of an unseen species | [[DiscoveryProbability|Discovery probability]] |
| Total number of species | Asymptotic coverage ([[Chao1Estimator|Chao1]] estimates it) |

By picking the *definition of species* (statements, traces, paths, branches), the same estimators answer different fuzzing questions. The framework's power is that the underlying statistics are almost identical whether each input belongs to *exactly one* species (single-trace model) or *one or more* species (statements/branches, "incidence-frequency" model).

## In The Fuzzing Book — When To Stop Fuzzing

[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] introduces STADS as the conceptual bridge from [[AlanTuring|Turing]] and [[IJGood|I.J. Good]]'s wartime trigram-estimation work to modern fuzzing. It defines an input's species via `getTraceHash()` — an MD5 hash over the covered-statement set — and shows that the [[GoodTuringEstimator|Good-Turing estimator]] then estimates the probability of covering a new trace, that this bounds **[[ResidualRisk|residual risk]]**, and that Anne [[AnneChao|Chao]]'s estimators give the total species count and an extrapolation of future discovery.

## Connections
- [[GoodTuringEstimator]] — estimates the probability of discovering a new species.
- [[DiscoveryProbability]] — the per-step quantity STADS estimates.
- [[ResidualRisk]] — bounded by the discovery probability under STADS.
- [[Chao1Estimator]] — estimates the asymptotic *total* number of species.
- [[MarcelBohme]] — author of the STADS framework.
- [[Coverage]] / [[PathCoverage]] — concrete species definitions (statements, traces, paths).
- [[AnneChao]] — her ecological estimators are the statistical backbone.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
