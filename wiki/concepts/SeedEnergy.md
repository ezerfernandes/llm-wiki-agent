---
title: "Seed Energy"
type: concept
tags: [fuzzing, greybox, afl, power-schedule, seed-scheduling]
sources: [fuzzingbook-06-greybox-fuzzer]
last_updated: 2026-06-06
---

# SeedEnergy

In [[GreyboxFuzzing|greybox fuzzing]], a seed's **energy** is the likelihood that the seed is chosen from the population to be mutated next. "Spending energy" on a seed means fuzzing it. Energy is the quantity a [[PowerSchedule|power schedule]] sets per seed and then normalizes into a probability distribution over the corpus, so that more energy = a higher chance of being selected. Concentrating energy on the most promising seeds — those likely to find new coverage quickly — is the core optimization that makes greybox fuzzing more efficient than uniform mutation.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] attaches `energy` (a float) to the `Seed` class alongside `coverage` and `distance`. The base [[PowerSchedule|`PowerSchedule`]] gives every seed `energy = 1` (uniform selection); `normalizedEnergy()` divides each by the sum so the values become selection probabilities used by `random.choices(...)`. Advanced schedules then *shape* energy: `AFLFastSchedule` sets `energy = 1 / f(p(s)) ** a` ([[BoostedGreyboxFuzzing|boosting]] seeds on low-[[PathCoverage|path]]-frequency paths, [[AFLFast]]), while `DirectedSchedule`/`AFLGoSchedule` set energy inversely proportional to a seed's average [[CallGraph|call-graph]] distance to a target ([[DirectedGreyboxFuzzing|directed fuzzing]]). The chapter shows the boosted schedule assigning the most energy to the seed exercising the lowest-frequency path.

## Connections
- [[PowerSchedule]] — the procedure that assigns and normalizes seed energy.
- [[SeedInput]] — the seed each energy value is attached to.
- [[GreyboxFuzzing]] — the fuzzing model in which energy steers seed selection.
- [[AFLFast]] / [[BoostedGreyboxFuzzing]] — exponential energy for rare paths.
- [[DirectedGreyboxFuzzing]] — distance-based energy toward a target.
- [[PathCoverage]] — path frequency the boosted energy formula divides by.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where energy is defined.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
