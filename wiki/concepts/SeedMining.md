---
title: "Seed Mining"
type: concept
tags: [fuzzing, seed-selection, corpus, mutation-fuzzing, langfuzz, security]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# SeedMining

**Seed mining** is the practice of *sourcing* a fuzzer's initial [[SeedInput|seed corpus]] from real, structured inputs — especially inputs *known to have caused failures before* — rather than starting from a single trivial or empty seed. The choice of seeds strongly influences a fuzzing campaign's reach, along two axes: **variability** (cover as many input features as possible to maximize [[Coverage|coverage]]) and **failure-proximity** (inputs near past failures are disproportionately likely to find new failures, because fixes often address the concrete failure but miss surrounding conditions).

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] (section "Mining Seeds") motivates this with [[LangFuzz]]: it seeded its JavaScript fuzzing from inputs in CVE reports — failure-inducing inputs published *after* the underlying bug had been fixed, so they could "do no harm anymore." By mutating and recombining the features of these known-bad inputs (via [[FragmentBasedFuzzing|fragment recombination]]), [[LangFuzz]] repeatedly rediscovered errors in the *vicinity* of past failures. This complements the structure-aware mutators of the chapter: good seeds plus structure-aware recombination is what made [[LangFuzz]] find 2,600+ bugs.

## Connections
- [[SeedInput]] — seed mining is about *where the seeds come from* and which to favor.
- [[FragmentBasedFuzzing]] — recombining features of mined seeds is the [[LangFuzz]] technique.
- [[LangFuzz]] — seeded from JavaScript CVE reports.
- [[PowerSchedule]] / [[DegreeOfValidity]] — seed *prioritization* (which to mutate, how much) is the in-campaign counterpart to seed *selection*.
- [[GrammarAwareGreyboxFuzzing]] — the chapter's fuzzers consume the mined seeds.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where seed mining is discussed.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
