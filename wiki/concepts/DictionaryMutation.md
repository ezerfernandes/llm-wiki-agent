---
title: "Dictionary-Based Mutation"
type: concept
tags: [fuzzing, mutation-fuzzing, greybox, afl, dictionary, keywords, security]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# DictionaryMutation

**Dictionary-based mutation** is the lightest form of structure-awareness in a [[MutationBasedFuzzing|mutation-based fuzzer]]: rather than mutating only at the byte level, the [[Mutator|mutator]] is given a **dictionary** of pre-defined useful tokens — typically the target language's keywords and other important fragments — and injects them into the seed during mutation. This lets a byte-level fuzzer stumble onto valid keywords (e.g. `</a>`) that random byte flips would essentially never assemble, dramatically speeding up [[Coverage|coverage]] growth without any parsing. It is the mechanism behind [[AFL]]'s hand-supplied dictionaries.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] presents `DictMutator(Mutator)` (the same class first defined in [[fuzzingbook-06-greybox-fuzzer|Ch 6]] for the maze target, here applied to HTML). Its constructor takes a `dictionary: List[str]` and appends `insert_from_dictionary` to the mutator's operator list; that operator splices a randomly chosen keyword into the seed at a random position (`s[:pos] + random_keyword + s[pos:]`), *in addition to* the inherited delete/insert/flip byte operators. Plugged into a plain [[GreyboxFuzzing|`GreyboxFuzzer`]] with a dictionary of HTML tags/attributes (`["<a>", "</a>", "<a/>", "='a'"]`), it covers more code than the byte-only fuzzer. The chapter's summary: "informing the fuzzer about important keywords already goes a long way towards achieving lots of coverage quickly," and points to Michał Zalewski's blog posts on "making up grammar with a dictionary in hand." Dictionaries inject keywords but cannot maintain *structural* integrity — motivating the [[FragmentBasedFuzzing|fragment]] and [[RegionMutation|region]] mutators that follow.

## Connections
- [[Mutator]] / [[MutationBasedFuzzing]] — `DictMutator` extends the base mutator with a keyword-insertion operator.
- [[GreyboxFuzzing]] / [[CoverageGuidedFuzzing]] — `DictMutator` plugs straight into `GreyboxFuzzer`.
- [[GrammarAwareGreyboxFuzzing]] — the lightest rung of grammar-awareness, below fragments/regions.
- [[FragmentBasedFuzzing]] / [[RegionMutation]] — the structure-preserving successors.
- [[AFL]] — popularized fuzzing dictionaries of input keywords.
- [[SeedInput]] — the seed a dictionary keyword is spliced into.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where dictionary mutation opens the chapter.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where `DictMutator` is first defined.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
