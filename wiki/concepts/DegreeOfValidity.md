---
title: "Degree of Validity"
type: concept
tags: [fuzzing, grammar, parsing, aflsmart, power-schedule, validity, security]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# DegreeOfValidity

The **degree of validity** of an input is the *proportion* of it that can be successfully parsed against a [[ContextFreeGrammar|grammar]] — a continuous measure (0–100%) of how close a (possibly invalid) seed is to being syntactically well-formed. It generalizes the binary valid/invalid distinction into a gradient, which is exactly what a [[GrammarAwareGreyboxFuzzing|smart greybox fuzzer]] needs to *prioritize* the seeds most worth mutating: a seed that is 90% parsable is a better basis for structure-aware mutation than one that is 10% parsable.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] computes the degree of validity from the [[EarleyParser|Earley parser]]'s `chart_parse()` table: the number of columns that still have states equals the length of the longest **parsable prefix**, so `validity = len(parsable) / len(seed)`. This measure drives two things:

- **[[RegionMutation|Region-based mutation]]** uses the same parse table to label byte regions with grammar symbols even when the whole input is invalid.
- The **[[AFLSmart|`AFLSmartSchedule`]]** (a [[PowerSchedule|power schedule]]) calls `degree_of_validity(seed)` (memoized on `seed.validity`) and assigns exponential [[SeedEnergy|energy]] proportional to it: `(degree_of_validity / log(len(data))) ** exponent`. The fuzzer thus *spends more time mutating more-valid seeds*, which the chapter shows raises the share of fully-valid generated inputs.

This is the [[AFLSmart]] "validity-based power schedule" idea, the answer to the low-validity problem that region-based mutation otherwise leaves unsolved.

## Connections
- [[AFLSmart]] — `AFLSmartSchedule` weights seed energy by degree of validity.
- [[PowerSchedule]] / [[SeedEnergy]] — the schedule machinery the validity measure feeds.
- [[RegionMutation]] — computed from the same Earley parse table that yields regions.
- [[EarleyParser]] / [[ChartParsing]] — `chart_parse()` provides the parsable-prefix length.
- [[GrammarAwareGreyboxFuzzing]] — uses validity to prioritize structurally-promising seeds.
- [[SeedInput]] — validity is a per-seed property.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where the measure and schedule are defined.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
