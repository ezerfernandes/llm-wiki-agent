---
title: "GrammarCoverageFuzzer"
type: concept
tags: [fuzzing, grammar, coverage, testing, syntactic-fuzzing, class-hierarchy, python]
sources: [fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-23-configuration-fuzzer, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# GrammarCoverageFuzzer

**`GrammarCoverageFuzzer`** is *The Fuzzing Book*'s coverage-driven [[GrammarBasedFuzzing|grammar fuzzer]]: a subclass of [[GrammarFuzzer|`GrammarFuzzer`]] ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]) that, when expanding a [[DerivationTree|derivation tree]], *prefers expansions that yield new [[GrammarCoverage|grammar coverage]]* instead of choosing uniformly at random. Its aim is to **cover every grammar expansion at least once** — maximizing input variety with the fewest inputs — which in turn yields higher [[Coverage|code coverage]]. The chapter recommends it as a near drop-in replacement for `GrammarFuzzer`.

## Class lineage
`GrammarFuzzer` → `TrackingGrammarCoverageFuzzer` (records `covered_expansions`) → `SimpleGrammarCoverageFuzzer` (prefers locally-uncovered alternatives) → **`GrammarCoverageFuzzer`** (adds deep foresight). Each layer overloads the same `choose_node_expansion()` hook of `GrammarFuzzer`.

## How it works — deep foresight
`SimpleGrammarCoverageFuzzer`'s greedy per-rule choice fails when a node's local alternatives are all covered but expanding a *covered* child would still unlock many uncovered productions deeper down (the canonical case: in `CGI_GRAMMAR`, choosing `<percent>` reaches the many `<hexdigit>` expansions, even though `<percent>` itself is covered). This is Burkhardt's (1967) **"shortest path selection."** `GrammarCoverageFuzzer` implements it:

1. `new_child_coverage(symbol, children, max_depth)` — the *new* coverage a candidate expansion would add, computed as `max_expansion_coverage(child, max_depth)` for each child minus `expansion_coverage()` already seen.
2. `new_coverages(node, children_alternatives)` — an **adaptive, breadth-first lookahead**: starting at `max_depth = 0` it increases depth until at least one alternative offers uncovered coverage, returning the per-alternative new-coverage sets. Breadth-first ordering prevents a single expansion with many descendants from dominating the schedule.
3. `choose_node_expansion()` — picks (randomly, via `choose_uncovered_node_expansion()`) among the alternatives tied for the *maximum* new coverage; if `new_coverages()` is `None` (all covered) it falls back to `choose_covered_node_expansion()`.

`expansion_coverage()` returns the covered set; `reset_coverage()` / `reset()` clears it to start anew; subsequent `fuzz()` calls keep pushing toward the remaining `missing_expansion_coverage()`.

## Interface
```python
expr_fuzzer = GrammarCoverageFuzzer(EXPR_GRAMMAR)
expr_fuzzer.fuzz()                   # '-(2 + 3) * 4.5 / 6 - 2.0 / +8 + 7 + 3'  (covers all digits + operators)
expr_fuzzer.expansion_coverage()     # set of 'SYMBOL -> EXPANSION' keys covered so far
```
It accepts the same constructor parameters as `GrammarFuzzer` (`grammar`, `start_symbol`, `min_nonterminals`/`max_nonterminals`, `log`). Empirically it reaches full coverage with shorter total output than the tracking and simple strategies (lower `average_length_until_full_coverage`), and on `cgi_decode()`/`urlparse()` its grammar coverage tracks code coverage at ≈0.9–0.95 correlation.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] combines `GrammarCoverageFuzzer` with the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] in Exercise 1: `ProbabilisticGrammarCoverageFuzzer` inherits from *both* (multiple inheritance) so it first covers every uncovered expansion (systematic, like `GrammarCoverageFuzzer`) and then, once coverage is complete, proceeds by [[ProbabilisticGrammar|probability]]. The exercise routes the three hooks `choose_node_expansion()`, `choose_covered_node_expansion()`, and `choose_uncovered_node_expansion()` to the right parent, and uses `inheritance_conflicts()` to resolve method-resolution-order conflicts between the two `GrammarFuzzer` subclasses. The chapter also separately reuses `GrammarCoverageFuzzer`'s `expansion_key()`/`duplicate_context()` machinery for [[GrammarMining|counting expansions]] and per-occurrence probabilities — positioning coverage-driven and probability-driven selection as complementary, composable axes.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] folds `GrammarCoverageFuzzer` (via its `ProbabilisticGrammarCoverageFuzzer` form) together with the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]] by *multiple inheritance* into `ProbabilisticGeneratorGrammarCoverageFuzzer` — aliased [[PGGCFuzzer|`PGGCFuzzer`]]. Combining coverage with [[GeneratorGrammar|generators]] is the hard case: during expansion the fuzzer may record coverage for an expansion that a `post` function later *rejects*, so the combined class **rebuilds coverage from the final tree** — `fuzz_tree()` saves and restores `covered_expansions` and then re-adds only surviving coverage via `add_tree_coverage()`, with `restart_expansion()` likewise restoring it on a from-scratch restart. This keeps coverage accounting honest when expansions are discarded.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] reuses `GrammarCoverageFuzzer` as the engine of [[ConfigurationFuzzing|configuration fuzzing]]: the chapter's `OptionFuzzer` *subclasses* it, taking an `OptionRunner` whose mined [[OptionGrammar|option grammar]] it then covers — ensuring every command-line option (and every digit/letter in option values) is exercised at least once. For [[CombinatorialTesting|combinatorial (pairwise) testing]], the chapter rewrites the grammar's `<option>` rule into a list of option *pairs* (`pairwise()`), so ordinary grammar coverage by `GrammarCoverageFuzzer` automatically covers all pairs. Exercise 4 notes a limitation — once the fuzzer covers `<int>`/`<digit>` for one option it stops striving to cover them for the next — and proposes duplicating expansions (coverage in context, see [[ContextCoverage]]) to cover each option's parameters independently.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] reuses `GrammarCoverageFuzzer` to make [[GUIFuzzing|GUI fuzzing]] systematic. The chapter models a user interface as a [[FiniteStateMachine|finite state machine]] embedded in a [[Grammar|grammar]] ([[UINavigationModel|UI navigation model]] / [[ModelBasedTesting|model-based testing]]), where each *state transition* is a grammar *expansion alternative*. Therefore `GrammarCoverageFuzzer`'s drive to cover every expansion **automatically covers every state transition** — no GUI-specific coverage machinery is needed. The chapter combines it with [[GUIFuzzer|`GUIFuzzer`]] via **multiple inheritance** (resolved with `inheritance_conflicts()` and a custom `__init__` calling `reset_coverage()`) into `GUICoverageFuzzer`, whose `explore_all()` keeps running until no `<unexplored>` state remains.

## Connections
- [[GUIFuzzing]] / [[GUIFuzzer]] — Ch 28 mixes this fuzzer in (as `GUICoverageFuzzer`) so UI transition coverage = grammar coverage.
- [[UINavigationModel]] / [[ModelBasedTesting]] — the FSM-in-a-grammar UI model whose transitions it covers.
- [[GrammarCoverage]] — the adequacy criterion this fuzzer optimizes.
- [[ConfigurationFuzzing]] / [[OptionGrammar]] — Ch 23 subclasses it as `OptionFuzzer` to cover mined command-line options.
- [[CombinatorialTesting]] — pairwise option coverage achieved by running it over a pairwise-rewritten grammar.
- [[PGGCFuzzer]] — the Ch 14 capstone combining this fuzzer with generators and probabilities (coverage rebuilt from the final tree).
- [[ProbabilisticGrammarFuzzer]] — combined with it via multiple inheritance (`ProbabilisticGrammarCoverageFuzzer`) in Ch 13 Exercise 1.
- [[ContextCoverage]] — pair it with `duplicate_context()` to cover reused symbols per-occurrence.
- [[GrammarFuzzer]] — the base class; coverage is layered onto its `choose_node_expansion()` hook.
- [[DerivationTree]] — the tree it expands, preferring high-new-coverage children.
- [[Grammar]] / [[ProductionRule]] — the expansions it strives to cover.
- [[Coverage]] / [[CoverageGuidedFuzzing]] — the code-coverage payoff of high grammar coverage.
- [[GrammarBasedFuzzing]] — the technique it makes coverage-aware.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — supplies the `GrammarFuzzer` superclass.
- [[fuzzingbook-23-configuration-fuzzer|Ch 23]] — applies it to systematic configuration testing.
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage."
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (combined via multiple inheritance in Exercise 1).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (folded into `PGGCFuzzer`; coverage rebuilt from the final tree).
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (subclassed as `OptionFuzzer`; pairwise option coverage).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (mixed into `GUICoverageFuzzer`; transition coverage = grammar coverage).
