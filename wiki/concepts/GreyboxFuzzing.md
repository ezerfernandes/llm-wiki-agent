---
title: "Greybox Fuzzing"
type: concept
tags: [fuzzing, testing, coverage-guided, greybox, security, afl, power-schedule]
sources: [fuzzingbook-06-greybox-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# GreyboxFuzzing

**Greybox fuzzing** sits between *blackbox* fuzzing (no program knowledge) and *whitebox* fuzzing (heavyweight analysis / constraint solving). A greybox fuzzer uses **lightweight instrumentation** to observe which branches/paths a generated input exercises, and feeds that signal back into input generation: any input that increases [[Coverage|coverage]] is kept in the seed corpus and mutated further. This is the algorithm behind [[AFL|American Fuzzy Lop]] and its variants, and it is the dominant modern form of [[CoverageGuidedFuzzing|coverage-guided]], [[MutationBasedFuzzing|mutation-based]] fuzzing — fast enough to generate thousands of inputs per second while still learning to reach deeper code.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] mints this concept by reconstructing AFL in miniature. It contrasts a blackbox `AdvancedMutationFuzzer` (mutates seeds but ignores coverage) with `GreyboxFuzzer(AdvancedMutationFuzzer)`, which overrides `run()` to add an input to its `population` whenever `frozenset(runner.coverage())` has not been seen before (`coverages_seen`). The new seeds act as "bread crumbs" guiding the fuzzer into deeper regions — from the seed `good`, the greybox fuzzer learns to emit the crashing input `bad!`, covering more statements than the blackbox baseline for the same number of inputs. The chapter explains AFL's real-world mechanism (a trampoline injected after every conditional jump assigns each branch an ID and a coarse hit-count, usually at compile time, or via QEMU/PinTool on binaries; Python needs no instrumentation) and then layers a [[PowerSchedule|power schedule]] on top to *steer* effort — yielding [[BoostedGreyboxFuzzing|boosted]] ([[AFLFast]]) and [[DirectedGreyboxFuzzing|directed]] (AFLGo) variants.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] makes greybox fuzzing *structure-aware*, fusing it with [[GrammarBasedFuzzing|grammar-based fuzzing]] to close Part III. Its [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]] subclasses the Ch 6 `GreyboxFuzzer`, keeping the keep-new-coverage rule but adding a *tree mutator* (a [[FragmentBasedFuzzing|`FragmentMutator`]] that recombines parsed [[DerivationTree|subtrees]], or a [[RegionMutation|`RegionMutator`]] that labels byte regions of unparsable seeds) alongside the byte-level [[Mutator|`Mutator`]]. The [[PowerSchedule|power schedule]] can be a validity-weighted `AFLSmartSchedule` ([[DegreeOfValidity|degree of validity]]). This reconstructs the [[LangFuzz]] and [[AFLSmart]] "smart greybox" fuzzers; the chapter's result is that stacking structural *and* byte-level mutation beats either alone.

## Connections
- [[CoverageGuidedFuzzing]] — greybox fuzzing is the coverage-feedback loop in practice.
- [[GrammarAwareGreyboxFuzzing]] / [[FragmentBasedFuzzing]] / [[RegionMutation]] — Ch 15's grammar-aware, structure-aware extension.
- [[Coverage]] / [[PathCoverage]] — the lightweight signal a greybox fuzzer instruments.
- [[MutationBasedFuzzing]] / [[Mutator]] / [[SeedInput]] — the input-generation substrate it guides.
- [[PowerSchedule]] / [[SeedEnergy]] — the machinery that distributes fuzzing effort across seeds.
- [[BoostedGreyboxFuzzing]] / [[AFLFast]] — boosting via energy for rare paths.
- [[DirectedGreyboxFuzzing]] — steering toward a target location (AFLGo).
- [[AFL]] — the canonical real-world greybox fuzzer this reconstructs.
- [[MarcelBohme]] — author of the AFLFast/AFLGo variants modeled here.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — the mutation prerequisite.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where the technique is built.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — grammar-aware "smart" greybox fuzzing.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (grammar-aware, structure-aware greybox fuzzing — `GreyboxGrammarFuzzer`).
