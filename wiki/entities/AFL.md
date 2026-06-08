---
title: "AFL (American Fuzzy Lop)"
type: entity
tags: [tool, fuzzer, fuzzing, security, coverage-guided, greybox, mutation-fuzzing]
sources: [fuzzingbook-05-mutation-fuzzer, fuzzingbook-06-greybox-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# AFL

**American Fuzzy Lop (AFL)** is a widely used **[[CoverageGuidedFuzzing|coverage-guided]], [[MutationBasedFuzzing|mutation-based]] greybox fuzzer**, first released by Michał Zalewski (lcamtuf) in November 2013. It became one of the most successful fuzzing tools and was the first to demonstrate, at scale, that vulnerabilities can be found *automatically* across many security-critical real-world programs. AFL works by mutating a corpus of [[SeedInput|seed inputs]] and retaining any mutant that exercises a *new path* through the instrumented program, then continuing to mutate the surviving inputs. Its lineage includes the variants **AFLFast**, **AFLGo**, and **AFLSmart** (associated with book co-author [[MarcelBohme|Marcel Böhme]]), all discussed in *The Fuzzing Book*.

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] introduces AFL as the inspiration for the chapter's technique. It dates AFL to November 2013, credits it with making fuzzing a popular choice for automated vulnerability detection, and reproduces its core heuristic in miniature: the [[MutationCoverageFuzzer|`MutationCoverageFuzzer`]] keeps an input whenever it achieves coverage not seen before — exactly AFL's "success = finding a new path" rule. The chapter notes AFL actually keys on new *branches* rather than the full coverage set (Exercise 4), and references the AFL author's blog post on which byte-level [[Mutator|mutation operators]] are most efficient (Exercise 3). It forwards to [[fuzzingbook-06-greybox-fuzzer|Ch 6]], where AFL's *power schedules* — spending more energy on seeds that hit unlikely paths or sit near a target — are modeled directly.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] reconstructs AFL's full [[GreyboxFuzzing|greybox]] algorithm in miniature. It explains AFL's real instrumentation (a trampoline injected after every conditional jump that assigns each branch a unique ID and increments a coarse hit-counter — usually at compile time, or via QEMU/Intel PinTool on binaries) and codifies the keep-new-coverage rule in the `GreyboxFuzzer` class. Crucially, it adds the [[PowerSchedule|power schedule]]: the base `PowerSchedule` spends fuzzing [[SeedEnergy|energy]] uniformly, AFL's real schedule favors short/fast/coverage-finding seeds, [[AFLFast|`AFLFastSchedule`]] [[BoostedGreyboxFuzzing|boosts]] seeds on rare [[PathCoverage|paths]] (Böhme's Markov-chain model), and `AFLGoSchedule` performs [[DirectedGreyboxFuzzing|directed]] fuzzing toward a target via [[CallGraph|call-graph]] distance. The chapter attributes AFLFast/AFLGo to co-author [[MarcelBohme|Marcel Böhme]] and links libFuzzer as another famous greybox fuzzer.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] extends AFL's byte-level greybox engine with *structure awareness*. It reuses AFL's idea of hand-supplied **dictionaries** of keywords ([[DictionaryMutation|`DictMutator`]], citing AFL author Michał Zalewski's blog posts on "making up grammar with a dictionary in hand"), and builds the AFL-derived [[AFLSmart]] "smart greybox" variant — [[RegionMutation|region-based mutation]] plus a [[DegreeOfValidity|validity]]-weighted power schedule — on top of the [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]]. *Superion* and *Nautilus* are named as concurrent AFL + grammar combinations.

## Connections
- [[MutationBasedFuzzing]] — AFL is the canonical mutation-based fuzzer.
- [[GreyboxFuzzing]] — AFL is the prototypical greybox fuzzer; Ch 6 reconstructs its algorithm.
- [[PowerSchedule]] / [[SeedEnergy]] — AFL distributes fuzzing effort via a power schedule.
- [[AFLFast]] / [[BoostedGreyboxFuzzing]] / [[DirectedGreyboxFuzzing]] — AFL's boosted and directed variants.
- [[MarcelBohme]] — author of the AFLFast/AFLGo variants.
- [[AFLSmart]] / [[RegionMutation]] / [[DictionaryMutation]] — Ch 15's grammar-aware AFL extensions (region mutation, validity schedules, dictionaries).
- [[CoverageGuidedFuzzing]] — AFL pioneered path/branch-coverage-guided input evolution.
- [[MutationCoverageFuzzer]] — the book's small-scale reconstruction of AFL's keep-new-coverage rule.
- [[SeedInput]] / [[Mutator]] — AFL mutates a seed corpus with byte-level operators.
- [[Fuzzing]] — AFL is among the dominant modern fuzzers (alongside libFuzzer).
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — where AFL is introduced.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — models AFL-style power schedules / greybox fuzzing.

## Sources
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing."
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing" (AFL's instrumentation, power schedules, AFLFast/AFLGo variants).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (AFL dictionaries; the grammar-aware AFLSmart variant).
