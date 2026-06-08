---
title: "Combinatorial Testing"
type: concept
tags: [testing, fuzzing, configuration, combinatorial-testing, pairwise-testing, k-way, test-adequacy, python]
sources: [fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# Combinatorial Testing

**Combinatorial testing** covers *combinations* of configuration settings rather than each setting in isolation, to expose unwanted **interactions** between them. The most common form is **pairwise** (2-way) testing — exercising every pair of settings at least once — generalized to **k-way** coverage. Its empirical justification is that most configuration-dependent bugs are triggered by the interaction of only two (occasionally three) settings, so pairwise coverage finds the great majority of interference bugs while avoiding the combinatorial explosion of the full configuration space.

## Why not the full space
For `n` options, the number of combinations of length `k` is the binomial coefficient `C(n,k) = n! / (k!·(n−k)!)`. The full space (all subset sizes summed) is `2^n`, which is intractable. Restricting to pairs collapses this to `C(n,2) = n(n−1)/2`, which is quadratic and runnable: in [[fuzzingbook-23-configuration-fuzzer|Ch 23]], `autopep8`'s 30 options need 870 pair tests, and `mypy`'s 140+ options need 20,000+ — "still done in three hours of testing" at one second each.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] implements pairwise testing by **rewriting the grammar**, not by writing a special algorithm. After mining an [[OptionGrammar|option grammar]] (see [[ConfigurationFuzzing|configuration fuzzing]]), it builds the list of option pairs with `itertools.combinations(option_list, 2)` and a `pairwise(option_list)` helper that *concatenates* each pair into a single option string. It then `extend_grammar()`s a copy and replaces the `<option>` rule with this pairwise list, so that running a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] over the new grammar automatically covers all pairs — pairwise coverage falls out of ordinary [[GrammarCoverage|grammar coverage]]. The same trick extends to other targets (e.g. the Exercise-1 C-preprocessor `-D` options). The chapter advises, for programs with very many options, limiting combinatorial testing to options that can plausibly interact and covering the rest (presumably orthogonal) individually. The idea of pairwise testing is "commonplace" in the configuration-modeling literature (Pezzè & Young 2008; Petke et al. 2015).

## Connections
- [[ConfigurationFuzzing]] — combinatorial testing is the interaction-covering layer on top of option fuzzing.
- [[OptionGrammar]] — the option list that gets rewritten into pairs.
- [[GrammarCoverage]] / [[GrammarCoverageFuzzer]] — pairwise coverage is achieved by ordinary grammar coverage over the rewritten grammar.
- [[Grammar]] — `extend_grammar()` clones the grammar so the `<option>` rule can be replaced with pairs.
- [[Testing]] / [[TestAdequacy]] — pairwise/k-way coverage as an adequacy criterion for configuration spaces.
- [[Fuzzing]] — combinatorial coverage drives the configuration fuzzer.
- [[fuzzingbook-23-configuration-fuzzer]] — the chapter that introduces combinatorial option testing.

## Sources
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations."
