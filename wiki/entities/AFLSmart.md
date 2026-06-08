---
title: "AFLSmart"
type: entity
tags: [tool, fuzzer, fuzzing, security, greybox, grammar, regions, aflsmart]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# AFLSmart

**AFLSmart** is a *smart (structural) greybox fuzzer* that brings together coverage-based [[GreyboxFuzzing|greybox fuzzing]] ([[AFL]]) and grammar-based structural fuzzing. Presented in *"Smart Greybox Fuzzing"* (Pham et al., 2018), it implements byte-level, [[FragmentBasedFuzzing|fragment-based]], and **[[RegionMutation|region-based]]** mutation together with **validity-based power schedules**. Its signature contribution is region-based mutation: deriving usable structure (byte regions labeled by grammar symbols) even from seeds that *cannot be fully parsed* — the common case for inputs a coverage-guided fuzzer discovers.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] reconstructs AFLSmart's design in its [[RegionMutation|`RegionMutator`]] (regions read from the [[EarleyParser|Earley parser]]'s `chart_parse()` table) and its `AFLSmartSchedule` (a [[PowerSchedule|power schedule]] that assigns exponential [[SeedEnergy|energy]] proportional to a seed's [[DegreeOfValidity|degree of validity]]), both plugged into the [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]]. The chapter reports AFLSmart discovered **42 zero-day vulnerabilities** in widely-used, well-tested tools and libraries, with **17 CVEs** assigned, and points readers to the AFLSmart paper and repository for region-based fuzzing, deferred parsing, and validity-based schedules.

## Connections
- [[RegionMutation]] — AFLSmart's signature region-based structural mutation, reconstructed as `RegionMutator`.
- [[DegreeOfValidity]] / [[PowerSchedule]] — its validity-based schedule, reconstructed as `AFLSmartSchedule`.
- [[GrammarAwareGreyboxFuzzing]] — the technique it exemplifies; the book's `GreyboxGrammarFuzzer` realizes it.
- [[AFL]] — the byte-level greybox engine it extends with structure.
- [[FragmentBasedFuzzing]] / [[LangFuzz]] — the sibling structural approach also reconstructed in Ch 15.
- [[GreyboxFuzzing]] / [[CoverageGuidedFuzzing]] — the coverage-feedback foundation.
- [[EarleyParser]] / [[ChartParsing]] — the parse table its regions are derived from.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where AFLSmart is reconstructed.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
