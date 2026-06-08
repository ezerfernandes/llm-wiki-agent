---
title: "Chao1 Estimator"
type: concept
tags: [statistics, estimation, ecology, fuzzing, species-richness, extrapolation]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Chao1 Estimator

The **Chao1 estimator** is a nonparametric estimate of the **asymptotic total number of species** `S` in a population, developed by bio-statistician Anne [[AnneChao|Chao]] in 1984. In [[SpeciesDiscovery|fuzzing-as-species-discovery]], it estimates the *total* number of execution traces / paths / statements a fuzzer could ever cover, so progress can be reported as a percentage even when the true total is unknown.

## Definition

Given `S(n)` species observed after `n` samples, `f₁` singletons (seen once) and `f₂` doubletons (seen twice):

```
Ŝ = S(n) + f₁² / (2·f₂)            if f₂ > 0
Ŝ = S(n) + f₁·(f₁ − 1) / 2         otherwise
```

Progress toward completion is then `S(n) / Ŝ`. (In the "incidence-frequency" model where each input belongs to one *or more* species, the identical formula is written with `Q₁`, `Q₂`.)

## Extrapolating future discovery

Chao, Shen & Lin (2003) extend Chao1 to *predict* species discovered after `m*` further samples:

```
Ŝ(n + m*) = S(n) + f̂₀ · [ 1 − (1 − f₁/(n·f̂₀ + f₁))^{m*} ]
```

where `f̂₀ = Ŝ − S(n)` estimates the undiscovered species. This answers "if I fuzz for another week, how many more paths will I find?"

## In The Fuzzing Book — When To Stop Fuzzing

[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] computes Chao1 halfway into a 400,000-input campaign against Python's `HTMLParser` (measuring trace coverage) and shows the estimated total closely matches the empirical asymptote, giving a meaningful completion percentage. It then applies the Chao–Shen–Lin extrapolator at `n/4` and finds the predicted curve closely tracks the actual one even at 3× extrapolation — letting teams do a cost-benefit analysis before committing more compute.

## Connections
- [[AnneChao]] — developer of the Chao1 estimator and the extrapolation method.
- [[SpeciesDiscovery]] — the framework in which "total species" = asymptotic coverage.
- [[DiscoveryProbability]] / [[GoodTuringEstimator]] — the per-step counterparts; share singleton counts.
- [[ResidualRisk]] — Chao1's progress % complements the residual-risk stopping signal.
- [[Coverage]] / [[PathCoverage]] — the coverage notions whose asymptote it estimates.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
