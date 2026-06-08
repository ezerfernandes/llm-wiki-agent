---
title: "The Fuzzing Book Ch 15 — Greybox Fuzzing with Grammars"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, grammar, greybox, mutation-fuzzing, langfuzz, aflsmart, dictionary, fragments, regions]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-15-greybox-grammar-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Greybox Fuzzing with Grammars

## Summary
Chapter 15 — the climax and close of Part III (Syntactic Fuzzing) — fuses the two halves of the book: the [[GreyboxFuzzing|coverage-guided greybox fuzzing]] of [[fuzzingbook-06-greybox-fuzzer|Ch 6]] (its `GreyboxFuzzer`, `Mutator`, `PowerSchedule`, `Seed`) and the [[GrammarBasedFuzzing|grammar/structure awareness]] of [[fuzzingbook-09-grammars|Ch 9]]–[[fuzzingbook-12-parser|Ch 12]] (its [[ContextFreeGrammar|grammars]], [[EarleyParser|`EarleyParser`]], and [[DerivationTree|derivation trees]]). It builds up three increasingly structure-aware mutation strategies on a worked HTML/XML example fuzzing Python's `HTMLParser`: (1) **[[DictionaryMutation|dictionary-based mutation]]** that injects grammar keywords into byte-level mutation (`DictMutator`, AFL-dictionary style); (2) **[[FragmentBasedFuzzing|fragment-based mutation]]** that parses seeds into [[DerivationTree|subtrees]] and splices/swaps subtrees of the same nonterminal type between inputs (`FragmentMutator`/`LangFuzzer`, [[LangFuzz]]-style); and (3) **[[RegionMutation|region-based mutation]]** that assigns grammar symbols to byte regions of *even unparsable* seeds (`RegionMutator`), all integrated into the coverage-guided [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]] with an [[AFLSmart]]-style validity-based power schedule (`AFLSmartSchedule`). The central lessons: structure-aware mutation generates *more valid* inputs but byte-level mutation often gets *more coverage*, so the best fuzzer stacks both — and region-based mutation plus a validity-weighted schedule recovers structure even from the mostly-invalid seeds a coverage-guided fuzzer discovers.

## Key Concepts
- **[[DictionaryMutation|Dictionary-based mutation]]** — `DictMutator(Mutator)` (reused from [[fuzzingbook-06-greybox-fuzzer|Ch 6]]) appends `insert_from_dictionary(s)` to the [[Mutator|mutator]]'s operator list, splicing a randomly chosen keyword (`<a>`, `</a>`, `<a/>`, `='a'`) into the seed at a random position. Plugged into a plain [[GreyboxFuzzing|`GreyboxFuzzer`]], informing the fuzzer of important keywords "goes a long way towards achieving lots of coverage quickly." Mirrors AFL's hand-supplied dictionaries (Michał Zalewski's "making up grammar with a dictionary in hand").
- **[[FragmentBasedFuzzing|Fragment-based mutation]]** — `FragmentMutator(Mutator)` takes an [[EarleyParser|`EarleyParser`]], parses each seed (capped at 200 ms via `Timeout`) into a [[DerivationTree|derivation tree]], and recursively collects every non-terminal/non-token subtree into a per-symbol **fragment pool** (`add_fragment`, `add_to_fragment_pool`, `is_excluded`). `swap_fragment` substitutes a random subtree of the seed with a pool fragment of the *same symbol*; `delete_fragment` removes a random subtree (`recursive_swap`/`recursive_delete`/`count_nodes`). Seeds gain structure via `SeedWithStructure` (`has_structure`, `structure`). This is the [[LangFuzz]] technique: parse → disassemble into fragments → recombine.
- **[[GrammarAwareGreyboxFuzzing|`LangFuzzer`]]** — `LangFuzzer(AdvancedMutationFuzzer)`, a *blackbox* fragment fuzzer whose `create_candidate()` stacks 1–4 structural mutations on a scheduled seed. It generates *more valid (parsable) inputs* than the byte-level blackbox fuzzer but achieves *less code coverage* — and is ~30× slower because parsing dominates.
- **[[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]]** — `GreyboxGrammarFuzzer(GreyboxFuzzer)` integrates a `tree_mutator` (a `FragmentMutator`/`RegionMutator`) with a byte-level `Mutator`. `create_candidate()` applies 0–4 structural mutations then (conditionally) up to `1 << random.randint(1,5)` byte mutations, adding to the [[SeedInput|seed]] population any input that increases [[Coverage|coverage]] ([[CoverageGuidedFuzzing|greybox feedback]]). It runs *faster* than `LangFuzzer` and gets *more coverage* than both `LangFuzzer` and the vanilla blackbox fuzzer.
- **[[RegionMutation|Region-based mutation]]** — `RegionMutator(FragmentMutator)` answers "how to derive structure from invalid seeds that cannot be fully parsed?" Using the Earley parser's `chart_parse()` **parse table**, it labels consecutive byte **regions** with the grammar symbol they could belong to (`SeedWithRegions`, `has_regions`, `regions`), then swaps/deletes regions by symbol. Unlike fragments, regions are derivable from *partially* parsable seeds — so region mutation applies to *all* seeds. The same table yields the **[[DegreeOfValidity|degree of validity]]** = `len(parsable_prefix) / len(seed)`.
- **[[AFLSmart|`AFLSmartSchedule`]]** — a [[PowerSchedule|power schedule]] subclass whose `assignEnergy()` gives a seed exponential [[SeedEnergy|energy]] proportional to its [[DegreeOfValidity|degree of validity]] (`(degree_of_validity / log(len)) ** exponent`), so the fuzzer spends more time mutating *more-valid* seeds — yielding more entirely-valid inputs. Realizes the [[AFLSmart]] "smart greybox" validity-based schedule.
- **[[SeedMining|Mining seeds]]** — reuse inputs *known to have caused failures before* (e.g. [[LangFuzz]] seeded from JavaScript CVE reports): mutations near a past-failure input are disproportionately likely to find related failures, since fixes often miss surrounding conditions.

## Key Claims
- The combination of language-based parsing + generating is "highly successful in practice": [[LangFuzz]] has found **more than 2,600 bugs** in the JavaScript engines of Firefox, Chrome, and Edge, and netted co-author [[ChristianHoller|Christian Holler]] **>USD 50,000 in bug bounties in his first four weeks**.
- Structure-aware (fragment) mutation produces *more valid* inputs but *less code coverage* than byte-level mutation — "there is some value in generating inputs that do not stick to the provided grammar."
- The integrated `GreyboxGrammarFuzzer` (fragment tree mutator + byte mutator + coverage feedback) runs faster than the fragment-only `LangFuzzer`, achieves more coverage than both `LangFuzzer` and the blackbox fuzzer, yet generates fewer valid inputs than even the blackbox fuzzer.
- [[RegionMutation|Region-based mutation]] is applicable to *all* seeds (even unparsable ones) and so achieves *higher coverage* than fragment-based mutation, at the cost of *fewer valid inputs* and lower throughput (it runs on every seed, not just the rare parsable ones).
- A **validity-based power schedule** ([[AFLSmart|`AFLSmartSchedule`]]) raises the share of fully-valid generated inputs by investing energy in higher-validity seeds.
- [[AFLSmart]] (region-based mutation + validity schedules) discovered **42 zero-day vulnerabilities** in well-tested tools (17 CVEs); [[LangFuzz]] inspires the fragment approach; *Superion* and *Nautilus* are concurrent grammar+coverage fuzzers, and Nautilus degenerates to structure-unaware greybox over time because it never re-parses collapsed subtrees.

## Key Quotes
> "The _LangFuzz_ fuzzer for JavaScript has found more than 2,600 bugs in JavaScript interpreters this way." — on the practical payoff of combining parsing and fuzzing.

> "In the first four weeks of running his _LangFuzz_ tool, Christian Holler ... netted _more than USD 50,000 in bug bounties_." — section "How to Make 50,000 USD in Four Weeks."

> "Unlike input fragments, input regions can be derived even if the parser fails to generate the entire parse tree." — the motivation for region-based mutation.

## Connections
- [[GreyboxFuzzing]] / [[CoverageGuidedFuzzing]] — the coverage-feedback half this chapter fuses with grammars; `GreyboxGrammarFuzzer` subclasses Ch 6's `GreyboxFuzzer`.
- [[GrammarBasedFuzzing]] / [[ContextFreeGrammar]] / [[Grammar]] — the structure half; the chapter's `XML_GRAMMAR` drives parsing and fragment typing.
- [[MutationBasedFuzzing]] / [[Mutator]] — the mutation substrate; `DictMutator`/`FragmentMutator`/`RegionMutator` are all `Mutator` extensions.
- [[Parser]] / [[EarleyParser]] / [[DerivationTree]] — parse seeds into trees (fragments) or parse tables (regions); fragments are typed subtrees.
- [[PowerSchedule]] / [[SeedEnergy]] / [[SeedInput]] — `AFLSmartSchedule` is a validity-weighted power schedule over the seed corpus.
- [[FragmentBasedFuzzing]] / [[RegionMutation]] / [[DictionaryMutation]] / [[DegreeOfValidity]] / [[GrammarAwareGreyboxFuzzing]] / [[SeedMining]] — the new concepts this chapter mints.
- [[LangFuzz]] — the fragment-recombination fuzzer (by co-author [[ChristianHoller]]) that inspires `FragmentMutator`/`LangFuzzer`.
- [[AFLSmart]] — the smart-greybox fuzzer that inspires region-based mutation + validity schedules.
- [[AFL]] — the byte-level greybox fuzzer whose dictionaries motivate `DictMutator` and whose engine `GreyboxGrammarFuzzer` extends.
- [[ChristianHoller]] — book co-author and [[LangFuzz]] author, whose CVE-seeded JavaScript fuzzing motivates fragment mutation and seed mining.
- [[AndreasZeller]] / [[MarcelBohme]] / [[CISPA]] — book authors / publisher.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — prerequisite: greybox fuzzing, `Mutator`, `PowerSchedule`, `Seed`, `DictMutator`.
- [[fuzzingbook-09-grammars|Ch 9]] / [[fuzzingbook-12-parser|Ch 12]] — prerequisites: grammars and the `EarleyParser` used to parse seeds.
- [[fuzzingbook-16-reducer|Ch 16]] — the next chapter (reducing failure-inducing inputs), which closes Part III.

## Contradictions
- None identified. The chapter re-presents `DictMutator` (first defined in [[fuzzingbook-06-greybox-fuzzer|Ch 6]] for the maze target) in an HTML/keyword context; this is the same class, not a conflict.
