---
title: "Residual Risk"
type: concept
tags: [fuzzing, security, testing, statistics, estimation, risk, stads]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Residual Risk

In fuzzing, **residual risk** is the probability that the *next* test input reveals a **vulnerability that has not yet been found**. It is the formal answer to "we fuzzed for months and found nothing — is the system actually safe?" The answer is never a guarantee: *testing is not verification*, so some residual risk always remains.

## Estimating residual risk

[[MarcelBohme|Marcel Böhme]] (STADS, ACM TOSEM 2018) proves that the [[GoodTuringEstimator|Good-Turing]] estimate of the [[DiscoveryProbability|discovery probability]] is an **upper bound** on residual risk.

**Proof sketch.** Split every observed "species" (e.g. an execution trace) into two sub-species: inputs in it that *expose* a vulnerability and inputs that *do not*. By assumption no vulnerability has been found, so only non-vulnerable sub-species have been observed; *all* vulnerable sub-species and *some* non-vulnerable ones remain undiscovered. Therefore the probability of discovering *any* new species (estimable by Good-Turing) is an upper bound on the probability of discovering a *vulnerable* one. **QED.**

This makes residual risk computable *live* during a campaign from the singleton count `f₁` and sample size `n`, with no separate vulnerability model required.

## In The Fuzzing Book — When To Stop Fuzzing

[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] presents residual risk as the practical payoff of the [[SpeciesDiscovery|species-discovery]] view: once you can estimate the probability of discovering a new execution-trace species, you have an upper bound on the chance the next input trips an undiscovered bug. A campaign can then be stopped when this estimated maximum residual risk drops below an acceptable threshold.

## Connections
- [[DiscoveryProbability]] — its Good-Turing estimate upper-bounds residual risk.
- [[GoodTuringEstimator]] — provides the estimate.
- [[SpeciesDiscovery]] — the STADS framework in which the bound is proved.
- [[MarcelBohme]] — author of the STADS proof.
- [[Fuzzing]] — residual risk is the stopping criterion for a campaign.
- [[Chao1Estimator]] — complements it with a progress-toward-completion percentage.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
