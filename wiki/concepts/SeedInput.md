---
title: "Seed Input"
type: concept
tags: [fuzzing, testing, mutation-fuzzing, corpus, seed-inputs]
sources: [fuzzingbook-05-mutation-fuzzer, fuzzingbook-06-greybox-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# SeedInput

A **seed input** (or just *seed*) is a known-*valid*, representative input supplied to a [[MutationBasedFuzzing|mutation-based fuzzer]] as the starting point for [[Mutator|mutation]]. Because seeds already pass the program's input-parsing checks, perturbing them produces a high proportion of still-valid inputs that reach functionality beyond the parser — the whole reason mutation beats from-scratch random generation. A fuzzer's set of seeds is its initial **corpus** (or *population*); the choice and diversity of seeds strongly influences which program behaviors a campaign can reach, and *seed selection* / *power schedules* — deciding which seeds to mutate and how much energy to spend on each — become central in [[AFL|AFL]]-style [[fuzzingbook-06-greybox-fuzzer|greybox fuzzing]].

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] introduces seeds via the `MutationFuzzer(seed: List[str], ...)` constructor. The running seed is the valid URL `"http://www.google.com/search?q=fuzzing"`. The fuzzer's `population` is initialised to the seed list (`reset()`), and `fuzz()` first emits each seed verbatim (the *seeding* phase, indexed by `seed_index`) before switching to *mutating* via `create_candidate()`. Starting from this one valid seed, the fuzzer reaches `https://` and a variety of valid URL shapes that random generation could not. In [[MutationCoverageFuzzer|`MutationCoverageFuzzer`]] the population is *re-seeded* to empty and then grown only with coverage-improving inputs, turning seeds into an evolving corpus — the precursor to the seed-selection/power-schedule machinery of [[fuzzingbook-06-greybox-fuzzer|Ch 6]].

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] promotes the bare seed string into a first-class **`Seed`** object carrying the attributes advanced [[PowerSchedule|power schedules]] need: `data`, a `coverage` set of [[Coverage|`Location`]] tuples, a `distance` to a target, and an `energy` value. The greybox fuzzer's `population` is a corpus of `Seed`s grown only with coverage-increasing inputs, and a [[PowerSchedule|power schedule]] assigns each seed an [[SeedEnergy|energy]] (its selection probability) — uniform by default, [[BoostedGreyboxFuzzing|boosted]] toward seeds on rare [[PathCoverage|paths]] ([[AFLFast]]), or [[DirectedGreyboxFuzzing|directed]] toward seeds close to a target. This is the realization of the seed-selection/power-schedule machinery this page anticipated.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] enriches the `Seed` with *structure* and adds a *quality* dimension to seed choice. Subclasses `SeedWithStructure` (carrying a parsed [[DerivationTree|`structure`]] and `has_structure`) and `SeedWithRegions` (carrying byte `regions` and `has_regions`) let [[FragmentBasedFuzzing|fragment]] and [[RegionMutation|region]] mutators attach structure to each seed; each seed also gets a [[DegreeOfValidity|degree of validity]] that the [[AFLSmart|`AFLSmartSchedule`]] uses to prioritize mutation. The chapter's "[[SeedMining|Mining Seeds]]" section adds that *where* seeds come from matters: seeding from inputs that caused failures before (as [[LangFuzz]] did from CVE reports) raises the odds of finding related failures.

## Connections
- [[MutationBasedFuzzing]] — seeds are its required starting material.
- [[SeedMining]] / [[DegreeOfValidity]] — Ch 15's seed *sourcing* and *validity-based prioritization*.
- [[PowerSchedule]] / [[SeedEnergy]] — Ch 6's `Seed` carries the energy/coverage/distance a schedule consumes.
- [[Mutator]] — the operators applied to a seed.
- [[MutationCoverageFuzzer]] — evolves the seed corpus by coverage.
- [[AFL]] — popularized seed selection and power-scheduled mutation of a seed corpus.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — where seed-based mutation is introduced.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — power schedules over seeds (greybox).

## Sources
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing."
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing" (the `Seed` class with energy/coverage/distance; power schedules over seeds).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (`SeedWithStructure`/`SeedWithRegions`, degree of validity, and seed mining).
