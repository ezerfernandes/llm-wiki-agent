---
title: "Discovery Probability"
type: concept
tags: [fuzzing, statistics, estimation, probability, coverage, stads]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Discovery Probability

The **discovery probability** `p₀` is the probability that the *next* generated test input belongs to a **previously unseen species** — for example, that it covers a new execution trace, a new path, or a new statement. It is the central quantity for deciding [[SpeciesDiscovery|when a fuzzing campaign]] has hit diminishing returns: when `p₀` falls too low, further fuzzing is unlikely to find anything new.

## How it is estimated

The [[GoodTuringEstimator|Good-Turing estimator]] gives `p₀ ≈ f₁ / n`, where `f₁` is the number of singleton species (seen exactly once) and `n` is the number of inputs. Three derived quantities follow from one estimate:

1. **Discovery probability** `p₀` — chance the next input is novel.
2. **Complement** `1 − p₀` — *sample coverage*; quantifies progress toward completion. **Abort the campaign when this is high / `p₀` is low.**
3. **Inverse** `1 / p₀` — expected number of inputs before the next discovery.

## In The Fuzzing Book — When To Stop Fuzzing

[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] estimates discovery probability for **trace coverage** (each input → one `getTraceHash`) on Python's `HTMLParser` and plots the Good-Turing estimate against an empirical repeated-sampling estimate over 50,000 inputs; the Good-Turing curve is *highly accurate* and far less noisy. Because it can be computed during the campaign with no extra runs, it is the practical "should I stop?" signal. The chapter further proves (via [[MarcelBohme|Böhme]]'s [[SpeciesDiscovery|STADS]]) that the discovery probability is an upper bound on **[[ResidualRisk|residual risk]]** — the probability of an as-yet-unfound vulnerability.

## Connections
- [[GoodTuringEstimator]] — the estimator used to compute it.
- [[ResidualRisk]] — discovery probability upper-bounds it.
- [[SpeciesDiscovery]] — the framework defining "species" and discovery.
- [[Chao1Estimator]] — uses the same singleton/doubleton counts to estimate total species.
- [[Coverage]] / [[PathCoverage]] — the coverage notions whose growth `p₀` tracks.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
