---
title: "Region-Based Mutation"
type: concept
tags: [fuzzing, grammar, mutation-fuzzing, parsing, aflsmart, chart-parsing, security]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# RegionMutation

**Region-based mutation** derives input structure from seeds that *cannot be fully parsed*, so structure-aware mutation still applies to them. A **region** is a consecutive sequence of bytes in the input that can be associated with a grammar [[Nonterminal|symbol]] — even if the *whole* input is invalid. Region-based mutators swap a region with a pool [[FragmentBasedFuzzing|fragment]] of the same symbol, or delete a region, just as fragment mutators do — but because regions can be extracted from *partial* parses, region mutation is applicable to *all* seeds, not only the rare ones that parse cleanly. It is the central idea of the [[AFLSmart]] structural greybox fuzzer.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] mints this with `RegionMutator(FragmentMutator)`. The key insight: the [[EarleyParser|Earley parser]]'s `chart_parse()` produces a **parse table** (one [[ChartParsing|`Column`]] per input letter) listing, for each position, the symbols and neighboring letter-ranges that *could* belong to them. From this:

- The number of columns with states gives the **longest parsable prefix**, hence the [[DegreeOfValidity|degree of validity]] (`len(parsable) / len(seed)`).
- `add_to_fragment_pool(seed)` first tries fragment extraction (via the [[FragmentBasedFuzzing|`FragmentMutator`]] superclass); if the seed has *no* full structure, it walks each column's finished states and records `seed.regions[symbol].add((s_col.index, e_col.index))` for each non-excluded symbol spanning more than one letter. Seeds are wrapped as `SeedWithRegions` (`has_regions`, `regions`).
- The overridden `swap_fragment(seed)` and `delete_fragment(seed)` operate on regions when the seed has regions but no full structure: pick a symbol, pick one of its regions `(s, e)`, and either splice in a pool fragment's string (`seed.data[:s] + swap_string + seed.data[e:]`) or excise the region.

The chapter's result: region mutation achieves *higher coverage* than fragment mutation (it can exploit *some* structure of otherwise-invalid seeds) but produces *fewer valid inputs* and runs slower (it applies to every seed). It is the structural mutator typically paired with [[AFLSmart|`AFLSmartSchedule`]] inside [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]].

## Connections
- [[FragmentBasedFuzzing]] — the superclass technique; regions are the fallback when full parsing fails.
- [[EarleyParser]] / [[ChartParsing]] — `chart_parse()` yields the parse table regions are read from.
- [[DegreeOfValidity]] — computed from the same parse table (length of parsable prefix).
- [[GrammarAwareGreyboxFuzzing]] — `RegionMutator` is the `tree_mutator` realizing the AFLSmart design.
- [[AFLSmart]] — the real-world fuzzer that introduced region-based mutation.
- [[GrammarBasedFuzzing]] / [[DerivationTree]] — regions are byte-spans labeled by grammar symbols.
- [[Mutator]] / [[MutationBasedFuzzing]] / [[SeedInput]] — the mutation framework it extends.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where the technique is built.
- [[fuzzingbook-12-parser|Ch 12]] — the Earley parser whose chart it reuses.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
