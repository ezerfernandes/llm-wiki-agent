---
title: "Boosted Greybox Fuzzing"
type: concept
tags: [fuzzing, greybox, afl, power-schedule, optimization, security]
sources: [fuzzingbook-06-greybox-fuzzer]
last_updated: 2026-06-06
---

# BoostedGreyboxFuzzing

**Boosted greybox fuzzing** is [[GreyboxFuzzing|greybox fuzzing]] in which the [[PowerSchedule|power schedule]] is deliberately skewed to assign more [[SeedEnergy|energy]] to seeds that promise more coverage — specifically, seeds exercising **"unusual" (low-frequency) [[PathCoverage|paths]]**. The hope is that mutating these seeds reaches *even more* unusual paths, increasing the number of distinct paths explored per unit time. It is the [[AFLFast]] idea applied as a concrete "boost" over the uniform schedule baseline.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] builds the boosted fuzzer from two pieces: the `CountingGreyboxFuzzer` (a [[GreyboxFuzzing|`GreyboxFuzzer`]] subclass that counts `path_frequency` via `getPathID`) plus the exponential [[AFLFast|`AFLFastSchedule`]]. Running both on the `crashme` example and the Python `HTMLParser`, the chapter shows the boosted fuzzer reaching coverage *much faster* than the original greybox fuzzer with the uniform schedule, because energy concentrates on the lowest-frequency path. Its summary: "By fuzzing seeds more often that exercise low-frequency paths, we can explore program paths in a much more efficient manner." The sibling technique that boosts toward a *target location* (rather than rare paths) is [[DirectedGreyboxFuzzing|directed greybox fuzzing]].

## Connections
- [[AFLFast]] — the exponential schedule that performs the boost.
- [[PowerSchedule]] / [[SeedEnergy]] — boosting reshapes the energy distribution.
- [[PathCoverage]] — boosting targets low-frequency paths.
- [[GreyboxFuzzing]] — the base technique being boosted.
- [[DirectedGreyboxFuzzing]] — the target-directed sibling boost (AFLGo).
- [[AFL]] / [[MarcelBohme]] — origin of the boosting (AFLFast).
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where boosting is built (`CountingGreyboxFuzzer`).

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
