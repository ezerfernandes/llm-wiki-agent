---
title: "Power Schedule"
type: concept
tags: [fuzzing, greybox, afl, power-schedule, seed-scheduling, optimization]
sources: [fuzzingbook-06-greybox-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# PowerSchedule

A **power schedule** is the component of a [[GreyboxFuzzing|greybox fuzzer]] that decides how the limited fuzzing time is *distributed across the seed population* — i.e. how often each seed is selected for mutation. It does so by assigning every seed an **[[SeedEnergy|energy]]** value and then choosing seeds with probability proportional to their normalized energy. The goal is to spend effort on the most *progressive* seeds (those likely to yield new coverage soon) and avoid wasting energy on stagnant ones. The choice of power schedule is the main lever for *steering* a greybox fuzzer; [[AFL]]'s schedule, for example, favors seeds that are shorter, run faster, and find new coverage more often.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] introduces the `PowerSchedule` class with three methods: `assignEnergy(population)` (base version sets every seed's `energy = 1`), `normalizedEnergy(population)` (divides each energy by the total so they form a probability distribution), and `choose(population)` (`random.choices(population, weights=norm_energy)[0]`). The uniform base schedule picks each of three seeds ≈⅓ of the time. The chapter then subclasses it twice: `AFLFastSchedule(exponent)` assigns *exponential* energy inversely proportional to a path's exercise frequency ([[BoostedGreyboxFuzzing|boosting]] rare paths, [[AFLFast]]), and `DirectedSchedule` / `AFLGoSchedule` assign energy inversely proportional to a seed's average [[CallGraph|call-graph]] distance to a target ([[DirectedGreyboxFuzzing|directed fuzzing]], AFLGo). Each `Seed` carries its own `energy`, `coverage`, and `distance` attributes for these schedules to consume.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] adds a *validity-based* power schedule for [[GrammarAwareGreyboxFuzzing|grammar-aware greybox fuzzing]]. `AFLSmartSchedule(PowerSchedule)` overrides `assignEnergy()` to give each seed exponential energy proportional to its [[DegreeOfValidity|degree of validity]] (`(degree_of_validity / log(len(data))) ** exponent`), computed from the [[EarleyParser|Earley parser]]'s parse table. The fuzzer thus spends more effort mutating *more syntactically-valid* seeds, which raises the share of fully-valid generated inputs — the [[AFLSmart]] "smart greybox" scheduling idea, complementing Ch 6's frequency-based ([[AFLFast]]) and distance-based (AFLGo) schedules.

## Connections
- [[SeedEnergy]] — the per-seed quantity a power schedule assigns and normalizes.
- [[AFLSmart]] / [[DegreeOfValidity]] — Ch 15's `AFLSmartSchedule` weights energy by parse-validity.
- [[GreyboxFuzzing]] — the fuzzer a power schedule steers.
- [[SeedInput]] — the seeds whose selection probability the schedule sets.
- [[AFLFast]] / [[BoostedGreyboxFuzzing]] — the exponential `AFLFastSchedule` boosting rare paths.
- [[DirectedGreyboxFuzzing]] — `DirectedSchedule`/`AFLGoSchedule` steering toward a target.
- [[PathCoverage]] — path frequencies the boosted schedule weights against.
- [[AFL]] — the real-world fuzzer whose schedules these reconstruct.
- [[MarkovChain]] — the boosted-schedule analysis frames seed scheduling as a Markov chain.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where power schedules are defined.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (the validity-based `AFLSmartSchedule`).
