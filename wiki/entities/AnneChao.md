---
title: "Anne Chao"
type: entity
tags: [person, statistician, biostatistics, ecology, species-richness, estimation]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Anne Chao

**Anne Chao** is a theoretical bio-statistician renowned for **species-richness estimation** in ecology. Her 1984 *Scandinavian Journal of Statistics* paper introduced the **[[Chao1Estimator|Chao1 estimator]]** of the asymptotic total number of species/classes in a population from a finite sample; a 1987 *Biometrics* paper extended it to capture-recapture data with unequal catchability, and her 2003 work (with Tsung-Jen Shen and Chih-Feng Lin, *Ecology*) gave a method to **extrapolate** the number of new species in further sampling.

## Role in The Fuzzing Book
[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] imports Chao's ecological estimators into fuzzing under the [[SpeciesDiscovery|STADS]] view. Chao1 estimates the *total* number of execution-trace species a fuzzer can cover (giving a progress-toward-completion percentage `S(n)/Ŝ`), and the Chao–Shen–Lin extrapolator predicts how many more species would be discovered if the campaign ran longer — both shown to be accurate on a Python `HTMLParser` fuzzing experiment.

## Connections
- [[Chao1Estimator]] — her 1984 estimator and the 2003 extrapolation method.
- [[SpeciesDiscovery]] — the framework that applies her estimators to fuzzing.
- [[DiscoveryProbability]] / [[GoodTuringEstimator]] — the per-step counterparts to her total-species estimate.
- [[ResidualRisk]] — her completion % complements the residual-risk stopping signal.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
