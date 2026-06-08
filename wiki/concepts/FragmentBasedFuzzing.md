---
title: "Fragment-Based Fuzzing"
type: concept
tags: [fuzzing, grammar, derivation-tree, mutation-fuzzing, langfuzz, parsing, security]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# FragmentBasedFuzzing

**Fragment-based fuzzing** generates new inputs by *recombining structural fragments* extracted from existing seed inputs. A **fragment** is a subtree of a seed's [[DerivationTree|parse tree]] — i.e. a complete sub-derivation rooted at some grammar [[Nonterminal|nonterminal]]. The fuzzer (1) [[Parser|parses]] seeds into trees, (2) disassembles them into fragments keyed by their root symbol (a *fragment pool*), and (3) builds new inputs by swapping or deleting subtrees, always replacing a fragment with another fragment of the **same symbol type** so the result stays syntactically well-formed. This is the technique pioneered by [[LangFuzz]] for JavaScript engine fuzzing.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] mints this with the `FragmentMutator(Mutator)` class, which takes an [[EarleyParser|`EarleyParser`]] and maintains `self.fragments: Dict[str, List[DerivationTree]]` (one bucket per grammar symbol):

- `add_to_fragment_pool(seed)` parses a seed (capped at 200 ms via `Timeout`) and, on success, sets `seed.has_structure = True` and recursively adds every fragment via `add_fragment()`; `is_excluded(symbol)` skips terminals, tokens, and non-grammar symbols.
- `swap_fragment(seed)` chooses a random fragment in the seed (via `count_nodes()` and `recursive_swap()`) and substitutes a pool fragment of the *same symbol*; `delete_fragment(seed)` removes a random subtree (`recursive_delete()`).
- Seeds are wrapped as `SeedWithStructure` (`has_structure`, `structure`), and `mutate()` memoizes already-parsed seeds (`seen_seeds`).

The blackbox `LangFuzzer(AdvancedMutationFuzzer)` stacks 1–4 such mutations per candidate. The chapter's finding: fragment mutation yields *more valid (parsable)* inputs but *less code coverage* than byte-level mutation, and is much slower (parsing dominates; ~30× vs. ~10k inputs/sec blackbox). Its key limitation — fragments require a *fully* parsable seed — motivates [[RegionMutation|region-based mutation]] for the (common) unparsable seeds a coverage-guided fuzzer discovers. The chapter notes *deferred parsing* (investing in structural mutation only later in a campaign) as a remedy for the parsing overhead.

## Connections
- [[DerivationTree]] — a fragment is a subtree of a parsed seed's tree.
- [[Parser]] / [[EarleyParser]] — parse seeds into trees to extract fragments.
- [[GrammarBasedFuzzing]] / [[ContextFreeGrammar]] — fragments are typed by grammar symbol.
- [[RegionMutation]] — the complement: derives structure even from unparsable seeds.
- [[GrammarAwareGreyboxFuzzing]] — `FragmentMutator` plugs in as the `tree_mutator` of `GreyboxGrammarFuzzer`.
- [[Mutator]] / [[MutationBasedFuzzing]] / [[SeedInput]] — the mutation framework it extends.
- [[LangFuzz]] — the real-world fragment-recombination fuzzer this reconstructs.
- [[ChristianHoller]] — [[LangFuzz]]'s author and book co-author.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where the technique is built.
- [[fuzzingbook-12-parser|Ch 12]] — the parsing machinery it relies on.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
