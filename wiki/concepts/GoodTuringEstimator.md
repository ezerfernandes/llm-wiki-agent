---
title: "Good-Turing Estimator"
type: concept
tags: [statistics, estimation, fuzzing, probability, missing-mass, good-turing, history]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Good-Turing Estimator

The **Good-Turing estimator** estimates the probability mass of **unseen events** — the chance that the *next* sample belongs to a species never observed so far. It was invented by [[AlanTuring|Alan Turing]] and his assistant [[IJGood|I. J. Good]] during WWII codebreaking at [[BletchleyPark|Bletchley Park]] and published by Good in 1953 (*Biometrika*).

## Definition

Given `n` samples, let `f₁` be the number of **singletons** — species observed *exactly once*. The estimated **missing probability mass** / [[DiscoveryProbability|discovery probability]] is:

```
p₀ = f₁ / n          (Good-Turing estimate, GT)
```

Related quantities:
- **`1 − p₀`** — *sample coverage*: the fraction of all future samples already accounted for by observed species (Turing's quantity for "how much of all Enigma traffic can we already decrypt").
- **`1 / p₀`** — a maximum-likelihood estimate of how many more samples to expect before the next *new* species appears.

## Why it works

Despite large sampling effort, many species remain seen only once. These rare-but-observed singletons upper-bound the probability of the *even rarer* unobserved species — so the singleton rate `f₁/n` is a good estimate of the unseen mass. It is the foundation of an entire statistical literature on predicting unobserved "species."

## In The Fuzzing Book — When To Stop Fuzzing

[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] derives the estimator from the [[EnigmaMachine|Naval Enigma]] trigram example (`gt = singletons / n`) and verifies it empirically against a costly repeated-sampling estimate, agreeing within ~0.03 at a fraction of the cost — and computable *live* during a campaign. It then applies it to fuzzing by defining each input's species as its **execution trace** (`getTraceHash`), so `f₁/n` estimates the probability that the next input covers a new trace. Per [[MarcelBohme|Böhme]]'s [[SpeciesDiscovery|STADS]] framework, this estimate is an *upper bound* on **[[ResidualRisk|residual risk]]**. The same estimator is used in natural-language processing (probability of an unseen word) and ecology (probability of an unseen species). The chapter's exercise notes the extended ("incidence-frequency") form `C = Q₁ / n` for the case where each input belongs to one *or more* species.

## Connections
- [[DiscoveryProbability]] — the quantity this estimator computes.
- [[SpeciesDiscovery]] — the framework (STADS) that applies it to fuzzing.
- [[ResidualRisk]] — bounded above by the Good-Turing discovery probability.
- [[AlanTuring]] / [[IJGood]] — co-inventors; Good published the bias analysis in 1953.
- [[EnigmaMachine]] — the worked example that motivates the estimator.
- [[Chao1Estimator]] — complements GT by estimating the *total* species count.
- [[MaximumLikelihoodEstimation]] — `1/GT` is an MLE of inputs-until-next-discovery.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
