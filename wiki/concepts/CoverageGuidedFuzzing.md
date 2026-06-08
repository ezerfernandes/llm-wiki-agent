---
title: "Coverage-Guided Fuzzing"
type: concept
tags: [fuzzing, testing, coverage, security, feedback, dynamic-analysis]
sources: [fuzzingbook-04-coverage, fuzzingbook-05-mutation-fuzzer, fuzzingbook-06-greybox-fuzzer, fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# CoverageGuidedFuzzing

**Coverage-guided fuzzing** is fuzzing in which [[Coverage|code coverage]] is used not merely to *measure* test effectiveness after the fact, but as a live *feedback signal* to *guide* input generation toward yet-uncovered code. Inputs that reach new coverage are kept and mutated further; inputs that add nothing are discarded. This feedback loop is what separates modern **greybox** fuzzers (AFL, libFuzzer) from the blackbox random [[RandomFuzzer|`RandomFuzzer`]] baseline, and it is far more efficient at exploring deep program states than unguided random testing.

## From The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] is the conceptual seed of coverage-guided fuzzing in *The Fuzzing Book*. Having built the `Coverage` class and used it to *compare* fuzzers by how fast they grow [[LineCoverage|statement-]] and [[BranchCoverage|branch-coverage]] curves, the chapter closes with its load-bearing thesis: *"Coverage is not only a tool to measure test effectiveness, but also a great tool to guide test generation towards specific goals – in particular uncovered code."* It explicitly forwards to [[fuzzingbook-05-mutation-fuzzer|Ch 5]], where coverage guides *mutations* of existing inputs toward better coverage. The set algebra on coverage (`cov_max - cov_run` = "lines still to cover") is exactly the residual a guided fuzzer tries to shrink. Thus this chapter supplies the feedback signal that [[fuzzingbook-05-mutation-fuzzer|mutation]] ([[fuzzingbook-06-greybox-fuzzer|greybox]]) and [[fuzzingbook-07-search-based-fuzzer|search-based]] fuzzers consume.

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] gives the first concrete *implementation* of this idea in the book: [[MutationCoverageFuzzer|`MutationCoverageFuzzer`]]. It feeds each [[MutationBasedFuzzing|mutated]] input through a [[Runner|`FunctionCoverageRunner`]], computes `frozenset(coverage())`, and appends the input to its `population` *only* if the run passed and the coverage set is new (`coverages_seen`). Mutation candidates are then drawn from that growing population, so inputs that found new code get mutated further — the canonical coverage-feedback loop. Run on the `http_program()` URL validator (`trials=10000`), it evolves a population where every input is valid and each has distinct coverage. The chapter ties this directly to [[AFL|AFL]] ("success = finding a new path") and forwards to [[fuzzingbook-06-greybox-fuzzer|Ch 6]]'s power-scheduled refinement.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] turns the coverage-feedback loop into a full [[GreyboxFuzzing|greybox]] fuzzer and then makes it *steerable*. `GreyboxFuzzer` keeps the keep-new-coverage rule (append any input whose `frozenset(coverage())` is new), but the chapter's contribution is adding a [[PowerSchedule|power schedule]] that distributes [[SeedEnergy|energy]] across the seed population: uniform by default, [[BoostedGreyboxFuzzing|boosted]] toward rare [[PathCoverage|paths]] ([[AFLFast]]), or [[DirectedGreyboxFuzzing|directed]] toward a target location (AFLGo). This is the chapter where coverage-guided fuzzing stops being "keep good inputs" and becomes "decide *how much* to fuzz each kept input" — the real-world [[AFL]] algorithm, attributed to co-author [[MarcelBohme|Marcel Böhme]] for the AFLFast/AFLGo refinements.

## From The Fuzzing Book — Grammar Coverage
[[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] applies the "coverage guides, not just measures" idea on the *input/grammar* side rather than the code side: [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] uses the residual [[GrammarCoverage|grammar coverage]] (`max_expansion_coverage() - expansion_coverage()`) as the signal that steers each [[DerivationTree|tree]] expansion toward yet-uncovered productions — the same set-difference feedback loop the lexical fuzzers run against code coverage. It is *not* runtime-feedback-driven (no `Coverage()` instrumentation in the loop); the connection to code coverage is correlational (≈0.9–0.95), so grammar coverage acts as a cheap, white-box-of-the-input proxy for the code coverage greybox fuzzers chase directly.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] turns *grammar* fuzzing — which Parts III had used in a pure black-box way — into a *coverage-guided* technique. The [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]] subclasses the Ch 6 `GreyboxFuzzer`, so it keeps the same keep-new-coverage rule (`FunctionCoverageRunner`, append any input whose coverage set is new) but generates candidates with *structure-aware* mutation ([[FragmentBasedFuzzing|fragments]] / [[RegionMutation|regions]]) layered on byte mutation. This is genuine *runtime* coverage feedback (unlike Ch 11's correlational grammar coverage), now driving grammar-based input generation toward uncovered code — the design behind the real [[AFLSmart]] smart greybox fuzzer.

## Connections
- [[GrammarCoverage]] / [[GrammarCoverageFuzzer]] — the grammar-side analogue: coverage as a residual that *guides* expansion selection.
- [[GrammarAwareGreyboxFuzzing]] / [[FragmentBasedFuzzing]] / [[RegionMutation]] — Ch 15's coverage-guided, structure-aware greybox fuzzing.
- [[Coverage]] / [[LineCoverage]] / [[BranchCoverage]] — the feedback signals a coverage-guided fuzzer maximizes.
- [[GreyboxFuzzing]] / [[PowerSchedule]] — the steerable greybox form built in Ch 6.
- [[MutationCoverageFuzzer]] — the book's first concrete coverage-guided fuzzer (Ch 5).
- [[MutationBasedFuzzing]] — the input-generation method coverage-guidance steers in Ch 5.
- [[AFL]] — the real-world coverage-guided greybox fuzzer this loop reconstructs.
- [[Fuzzing]] — the broader technique; coverage-guidance is its dominant modern form (AFL, libFuzzer, Atheris).
- [[RandomFuzzer]] — the blackbox baseline that coverage-guidance improves upon.
- [[TraceFunction]] / [[DynamicAnalysis]] — how the coverage feedback is obtained at runtime.
- [[fuzzingbook-04-coverage|Ch 4]] — where the "guide, don't just measure" thesis is stated.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — coverage guides input mutation (the explicit Next Step).
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — greybox/AFL-style power-scheduled coverage-guided fuzzing.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — search-based fuzzing using coverage-derived fitness.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — extends the coverage idea to grammar elements.

## Sources
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing" (the first concrete coverage-guided fuzzer, `MutationCoverageFuzzer`).
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing" (power-scheduled, steerable coverage-guided fuzzing — `GreyboxFuzzer`, AFLFast, AFLGo).
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage" (the grammar-side analogue: residual grammar coverage guides expansion selection).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (coverage feedback driving structure-aware grammar mutation — `GreyboxGrammarFuzzer`).
