---
title: "GrammarFuzzer"
type: concept
tags: [fuzzing, grammar, derivation-tree, testing, python, class-hierarchy, syntactic-fuzzing]
sources: [fuzzingbook-10-grammar-fuzzer, fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# GrammarFuzzer

**`GrammarFuzzer`** is *The Fuzzing Book*'s efficient, tree-based [[GrammarBasedFuzzing|grammar fuzzer]]: a subclass of the abstract `Fuzzer` base class (the same parent as [[RandomFuzzer]]) that takes a [[Grammar|`Grammar`]] and produces syntactically valid input strings by building and expanding a [[DerivationTree|derivation tree]]. It supersedes the slow string-rewriting `simple_grammar_fuzzer()` of [[fuzzingbook-09-grammars|Ch 9]], being both much faster and far more controllable, and it is the **base class** that almost every later grammar-based fuzzer in the book extends.

## Interface
```python
phone_fuzzer = GrammarFuzzer(US_PHONE_GRAMMAR)
phone_fuzzer.fuzz()            # -> '(236)844-1154'
phone_fuzzer.derivation_tree   # the tree behind the last string
```

Constructor parameters: `grammar`; `start_symbol` (default `<start>` — e.g. `start_symbol='<area>'`); `min_nonterminals` / `max_nonterminals` (size limits, default `0` / `10`); `disp` (display intermediate trees); `log` (print intermediate steps). `check_grammar()` validates via `is_valid_grammar()`. `fuzz()` returns a string; `fuzz_tree()` returns the [[DerivationTree|derivation tree]], also stored in the `derivation_tree` attribute afterward.

## How it works
1. `init_tree()` creates the root `(start_symbol, None)`.
2. `expand_tree()` runs a **three-phase strategy** (see [[ExpansionCost]]): grow at max cost to `min_nonterminals`, expand randomly to `max_nonterminals`, then close at min cost — implemented by swapping the `expand_node` method reference between `expand_node_max_cost`, `expand_node_randomly`, and `expand_node_min_cost`.
3. `expand_tree_once()` recurses to an unexpanded node and expands it **in place** (the key to its speed); `expand_node_randomly()` builds children via `expansion_to_children()` and selects one with the overloadable `choose_node_expansion()` (default random).
4. `all_terminals()` flattens the finished tree to the output string.

Subclasses customize behavior by overloading `choose_node_expansion()`, `process_chosen_children()`, or `expand_node()` — the extension points the rest of Part III uses.

## From The Fuzzing Book — Efficient Grammar Fuzzing
[[fuzzingbook-10-grammar-fuzzer|Ch 10]] introduces `GrammarFuzzer` as one of the book's central "hubs." It fixes the two flaws of the naive producer — quadratic slowdown and uncontrolled/infinite growth (the `expr_grammar` parenthesis blow-up) — by representing the partial string as a derivation tree and bounding growth with [[ExpansionCost|cost-based expansion]]. Benchmarks show it is far faster than `simple_grammar_fuzzer()` and yields smaller, controllable inputs, and it succeeds on grammars where the naive fuzzer hangs. The chapter's exercises subclass it into `FasterGrammarFuzzer` (memoizing `expansion_to_children()` with `copy.deepcopy()`) and `EvenFasterGrammarFuzzer` (precomputing grammar-only costs). Downstream, `GrammarFuzzer` is extended by the coverage ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]), probabilistic ([[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]), and generator ([[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]) fuzzers.

## From The Fuzzing Book — Grammar Coverage
[[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] is the first chapter to *subclass* `GrammarFuzzer`, layering [[GrammarCoverage|grammar coverage]] onto its overloadable `choose_node_expansion()` hook. The lineage `GrammarFuzzer → TrackingGrammarCoverageFuzzer → SimpleGrammarCoverageFuzzer → `[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] progressively replaces the base class's *random* expansion choice with one that prefers yet-uncovered expansions and then adds breadth-first *deep foresight*. This confirms `GrammarFuzzer`'s design as a hub: coverage is added purely by overriding selection, reusing its [[DerivationTree|derivation-tree]] expansion machinery unchanged. Because higher grammar coverage yields higher [[Coverage|code coverage]], the chapter recommends `GrammarCoverageFuzzer` as a drop-in replacement for the plain `GrammarFuzzer`.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] is another minimal subclass that exercises `GrammarFuzzer`'s `choose_node_expansion()` extension point: the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] overloads it to make a **weighted** choice (`random.choices(..., weights=...)`) according to the [[ProbabilisticGrammar|`prob` annotations]] on expansions, inheriting all of `GrammarFuzzer`'s tree-growth and `ExpansionCost` machinery unchanged. A plain `GrammarFuzzer` simply *ignores* those annotations (yielding a uniform distribution), which is exactly how the chapter contrasts "natural" Benford-distributed output against random output. Exercise 1 even combines this with [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] by *multiple inheritance* from both `GrammarFuzzer` subclasses (`ProbabilisticGrammarCoverageFuzzer`), underscoring `GrammarFuzzer`'s role as the shared hub of Part III.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] subclasses `GrammarFuzzer` once more into the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]], this time exercising *several* of its extension points rather than just `choose_node_expansion()`: it overloads `process_chosen_children()` (to run `pre` functions before expansion), `expand_tree_once()` (to run `post` functions locally as soon as a subtree completes), `choose_tree_expansion()` (to honor `opts(order=[…])`), and `fuzz_tree()` (to run/restart post-expansion checks). A plain `GrammarFuzzer` simply *ignores* (and warns about) `pre`/`post`/`order` annotations, so the same [[GeneratorGrammar|generator grammar]] is reusable by either. The chapter then composes this subclass with the [[ProbabilisticGrammarFuzzer|probabilistic]] and [[GrammarCoverageFuzzer|coverage]] `GrammarFuzzer` subclasses via *multiple inheritance* into [[PGGCFuzzer|`PGGCFuzzer`]] — the strongest confirmation yet of `GrammarFuzzer`'s role as the shared hub of Part III.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] subclasses `GrammarFuzzer` for a *domain-specific* target rather than to add a new selection strategy: [[WebFormFuzzer|`WebFormFuzzer`]] mines a [[Grammar|grammar]] of valid form-submission URLs from a served HTML page ([[GrammarMining|grammar mining]] from a UI) and hands it straight to the `GrammarFuzzer` constructor, so each `fuzz()` produces a complete `GET` request. `SQLInjectionFuzzer` extends that with attack payloads. The plain `GrammarFuzzer` also serves directly here — fuzzing the hand-written `ORDER_GRAMMAR` and the HTML/XSS/SQL-injection variants — making it the same reusable engine used throughout Part III, now driving a live Web server.

## Connections
- [[WebFormFuzzer]] — Ch 27's subclass that mines a Web-form grammar and fuzzes it over HTTP.
- [[DerivationTree]] — the data structure `GrammarFuzzer` builds and expands.
- [[GeneratorGrammarFuzzer]] — Ch 14's subclass adding `pre`/`post`/`order` function support across several of its hooks.
- [[ProbabilisticGrammarFuzzer]] — Ch 13's weighted-choice subclass layered on the same `choose_node_expansion()` hook.
- [[GrammarCoverage]] / [[GrammarCoverageFuzzer]] — Ch 11's coverage-driven subclass layered on its `choose_node_expansion()` hook.
- [[ExpansionCost]] — the cost machinery driving its grow/close phases.
- [[Grammar]] / [[ContextFreeGrammar]] — the input specification it consumes (unchanged from Ch 9).
- [[GrammarBasedFuzzing]] — the technique it makes efficient.
- [[RandomFuzzer]] — sibling concrete fuzzer sharing the `Fuzzer` base class.
- [[Fuzzing]] — the parent discipline.
- [[GraphViz]] — `display_tree()` visualizes its derivation trees.
- [[fuzzingbook-09-grammars|Ch 9]] — extends and supersedes its `simple_grammar_fuzzer()`.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — first subclass, adding grammar/expansion coverage.

## Sources
- [[fuzzingbook-10-grammar-fuzzer]] — *The Fuzzing Book* Ch 10, "Efficient Grammar Fuzzing."
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage" (first subclass; coverage-driven expansion selection).
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (weighted-choice subclass).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (generator-function subclass; multiple-inheritance into `PGGCFuzzer`).
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications" (`WebFormFuzzer`/`SQLInjectionFuzzer` subclasses for Web-form fuzzing).
