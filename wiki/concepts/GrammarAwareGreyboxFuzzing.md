---
title: "Grammar-Aware Greybox Fuzzing"
type: concept
tags: [fuzzing, greybox, grammar, coverage-guided, mutation-fuzzing, security, langfuzz, aflsmart]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# GrammarAwareGreyboxFuzzing

**Grammar-aware greybox fuzzing** (also *structural greybox fuzzing*, *smart greybox fuzzing*) combines two previously separate ideas: the [[CoverageGuidedFuzzing|coverage-feedback loop]] of [[GreyboxFuzzing|greybox fuzzing]] ([[AFL]]) and the *input-structure awareness* of [[GrammarBasedFuzzing|grammar-based fuzzing]]. Where a plain greybox fuzzer mutates inputs at the byte level (fast, but quickly produces invalid inputs), a grammar-aware greybox fuzzer also mutates inputs at the level of their parsed structure — swapping or deleting [[DerivationTree|subtrees]] or byte [[RegionMutation|regions]] that correspond to grammar symbols — so that mutated inputs are more likely to remain *syntactically valid* and reach deeper code, while still keeping any input that increases [[Coverage|coverage]]. It is the convergence point of Parts II and III of *The Fuzzing Book*.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] mints this concept by stacking grammar mutators onto the [[fuzzingbook-06-greybox-fuzzer|Ch 6]] greybox engine. Two fuzzers realize it:

- **`LangFuzzer(AdvancedMutationFuzzer)`** — a *blackbox* (no coverage feedback) fuzzer whose `create_candidate()` stacks 1–4 [[FragmentBasedFuzzing|fragment]] mutations on a scheduled seed. Inspired by [[LangFuzz]], it produces *more valid* inputs but *less coverage* than the byte-level blackbox fuzzer, and is far slower (parsing dominates).
- **`GreyboxGrammarFuzzer(GreyboxFuzzer)`** — the full grammar-aware *greybox* fuzzer. Its constructor takes a `byte_mutator` (a plain [[Mutator|`Mutator`]]), a `tree_mutator` (a [[FragmentBasedFuzzing|`FragmentMutator`]] or [[RegionMutation|`RegionMutator`]]), and a [[PowerSchedule|`PowerSchedule`]]. `create_candidate()` applies 0–4 structural mutations and then (conditionally) up to `1 << random.randint(1,5)` byte mutations, and — inheriting [[GreyboxFuzzing|`GreyboxFuzzer`]] — adds to the population any input increasing [[Coverage|coverage]]. With a [[RegionMutation|region]] tree-mutator and the validity-based [[AFLSmart|`AFLSmartSchedule`]], it reconstructs the [[AFLSmart]] "smart greybox" design.

The chapter's headline result: the integrated `GreyboxGrammarFuzzer` is faster than the fragment-only `LangFuzzer` and gets more coverage than both it and the vanilla blackbox fuzzer — stacking byte-level *and* structural mutation beats either alone.

## Connections
- [[GreyboxFuzzing]] / [[CoverageGuidedFuzzing]] — the coverage-feedback half it fuses; `GreyboxGrammarFuzzer` subclasses `GreyboxFuzzer`.
- [[GrammarBasedFuzzing]] / [[DerivationTree]] / [[EarleyParser]] — the structure half; parsing seeds enables structural mutation.
- [[FragmentBasedFuzzing]] — the [[LangFuzz]]-style tree-mutator (`FragmentMutator`/`LangFuzzer`).
- [[RegionMutation]] — the [[AFLSmart]]-style tree-mutator that works on unparsable seeds.
- [[DictionaryMutation]] — the lightest grammar-awareness: inject keywords (`DictMutator`).
- [[PowerSchedule]] / [[AFLSmart]] / [[DegreeOfValidity]] — `AFLSmartSchedule` weights seed energy by validity.
- [[Mutator]] / [[MutationBasedFuzzing]] / [[SeedInput]] — the mutation substrate it steers.
- [[AFL]] — the byte-level greybox engine extended here.
- [[LangFuzz]] / [[AFLSmart]] — the real-world fuzzers this reconstructs.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where the technique is built.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] / [[fuzzingbook-09-grammars|Ch 9]] — the greybox and grammar prerequisites it merges.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
