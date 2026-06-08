---
title: "The Fuzzing Book Ch 14 — Fuzzing with Generators"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, grammar, generators, semantic-constraints, checksum, syntactic-fuzzing, python]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-14-generator-grammar-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Fuzzing with Generators

## Summary
Chapter 14 extends [[GrammarBasedFuzzing|grammar-based fuzzing]] by **attaching Python functions to individual grammar expansions**, so that values can be *computed by code* rather than only expanded syntactically. This brings together "the best of grammar generation and programming" and is the book's answer to the central limitation of [[ContextFreeGrammar|context-free grammars]]: they cannot express [[SemanticConstraint|semantic constraints]] such as checksums, in-range integers, matching XML tags, or define/use dependencies between fields. Building on the efficient [[GrammarFuzzer|`GrammarFuzzer`]] of [[fuzzingbook-10-grammar-fuzzer|Ch 10]], the chapter mints the [[GeneratorGrammar|generator grammar]] (an expansion annotated with `opts(pre=...)` and/or `opts(post=...)`) and the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]] that interprets those annotations during [[DerivationTree|derivation-tree]] expansion. The running examples are a **credit-card charge grammar** (valid [[LuhnAlgorithm|Luhn]] checksums via a `post` repair), arithmetic expressions with numbers in a fixed range, matching [[GeneratorGrammar|XML tags]], and a variable def/use grammar with a symbol table. It closes by combining generators with the [[fuzzingbook-13-probabilistic-grammar-fuzzer|probabilistic (Ch 13)]] and [[fuzzingbook-11-grammar-coverage-fuzzer|coverage (Ch 11)]] fuzzers via multiple inheritance into the all-features [[PGGCFuzzer|`PGGCFuzzer`]]. It is the imperative-callbacks counterpart to the *declarative* constraints of [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] (ISLa).

## Key Concepts
- **[[GeneratorGrammar|Generator grammar]] (`pre`/`post` annotations)** — using the `opts()` mechanism from [[fuzzingbook-09-grammars|Ch 9]], an expansion `S` is replaced by a pair `(S, opts(pre=F))` or `(S, opts(post=F))`. A **`pre`** function runs *before* expansion and its return value *replaces* the expansion; a **`post`** function runs *after* expansion (receiving the expanded values of the nonterminal children as arguments) and can act as a *constraint/filter* (return `False` → re-expand) or a *repair* (return a string/list → replace). Both can return `None` to leave production untouched.
- **[[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]]** — a [[GrammarFuzzer|`GrammarFuzzer`]] subclass that interprets `pre`, `post`, and `order` opts. `supported_opts()` declares them; `exp_pre_expansion_function()` / `exp_post_expansion_function()` read them via `exp_opt()`. A plain `GrammarFuzzer` simply *ignores* (and warns about) these annotations, keeping generator grammars backward-compatible.
- **Pre-expansion via `process_chosen_children()` / `apply_result()`** — the fuzzer hooks `process_chosen_children()` to call the `pre` function and apply its result: a *string* replaces the whole expansion; a *list* `[x_1…x_n]` replaces the i-th nonterminal child with `x_i` (skipping `None`); `None`/booleans are ignored; other types are `repr()`'d into a string.
- **[[Generator|Python generator]] support** — if a `pre` function is a Python generator (uses `yield`, or is `range()`/a comprehension), `run_generator()` instantiates it once per `fuzz_tree()` (keyed by `(expansion, function)` in a `generators` dict) and pulls successive values with `next()`, preserving state across expansions (e.g. `iterate()` emitting 1, 2, 3, …).
- **Post-expansion checking/repair** — `run_post_functions()` walks the [[DerivationTree|derivation tree]] recursively; `find_expansion()` recovers which grammar expansion produced a node's children; `eval_function()` builds the argument list from the nonterminal children's terminal strings and invokes the function. If any returns `False`, `fuzz_tree()` discards the whole tree and restarts.
- **Local checking and repairing** — to avoid the cost of generating an entire tree only to reject it, `expand_tree_once()` is extended to run a node's `post` function with `run_post_functions_locally()` *as soon as the subtree is complete* (`depth=0`). On failure it returns the symbol unexpanded to retry (up to a configurable `replacement_attempts`, default 10), and after exhausting attempts raises a `RestartExpansionException` to rebuild from scratch.
- **Definitions and uses (symbol table)** — `CONSTRAINED_VAR_GRAMMAR` uses `define_id()`/`use_id()`/`clear_symbol_table()` attached as `pre`/`post` functions so that each *used* variable was previously *defined* — a context-sensitive property impossible in a pure CFG.
- **Ordering expansions (`opts(order=[…])`)** — the `order` attribute assigns each nonterminal in an expansion a rank so side-effecting functions fire in a controlled sequence (e.g. expand the right-hand side of `;` before the left; define an identifier only *after* its expression is built). Implemented by overloading `choose_tree_expansion()` to pick the expandable child with the lowest order, retrieved via `exp_order()`.
- **[[PGGCFuzzer|`PGGCFuzzer`]] — "all together"** — by *multiple inheritance* the chapter builds `ProbabilisticGeneratorGrammarFuzzer` (generators + [[ProbabilisticGrammarFuzzer|probabilities]]) and `ProbabilisticGeneratorGrammarCoverageFuzzer` (also + [[GrammarCoverageFuzzer|coverage]]), the latter rebuilding [[GrammarCoverage|coverage]] from the *final* tree (`add_tree_coverage()`) so discarded expansions don't pollute it. `PGGCFuzzer` is the trivial alias combining all features.

## Key Claims
- A complex arithmetic operation like a checksum *cannot* be expressed in a context-free grammar; attaching programmatic functions to expansions is the mechanism that supplies semantic validity beyond syntax.
- Generated 16-digit credit-card numbers fail the [[LuhnAlgorithm|Luhn]] checksum ~9 times out of 10; a `post` *filter* (`valid_luhn_checksum`) still costs ~10 attempts per accepted number, whereas a `post` *repair* (`fix_luhn_checksum`) fixes each number once and is far more efficient.
- Matching XML tags (`<strong>…</strong>`) is a context-sensitive constraint a CFG cannot capture (unless the closing tag is *reversed*, which a CFG *could* describe); a `post` function `lambda id1, content, id2: [None, None, id1]` repairs the closing tag to match the opening one.
- Generating only negative-valued arithmetic expressions is "very difficult" constructively but trivial as a `post` constraint using Python `eval()` (wrapped by `eval_with_exception()` to treat arithmetic errors as `False`).
- Late checking of a whole tree (e.g. filtering binary-digit-only expressions) "can take several seconds"; *local* checking of completed subtrees with bounded `replacement_attempts` makes it practical.
- Expansion *ordering* matters only once functions have side effects — a `post=define_id` with `order=[2,1]` ensures a variable is defined only after its defining expression is produced, so generated assignment sequences are valid when `exec()`'d.
- The integration is possible "mostly because we define and make use of grammars in an all-Python environment"; the authors are "not aware of another grammar-based fuzzing system that exhibits similar features."

## Key Quotes
> "Adding functions to a grammar allows for very versatile test generation, bringing together the best of grammar generation and programming." — chapter introduction

> "A complex arithmetic operation like a checksum cannot be expressed in a grammar alone – at least not in the context-free grammars we use here." — motivation for attaching functions

> "Functions attached to grammar expansions can serve as generators … as constraints … and as repairs …" — Lessons Learned

## Connections
- [[GeneratorGrammar]] — the central data structure minted here: a grammar with `pre`/`post`/`order` annotations on expansions.
- [[GeneratorGrammarFuzzer]] — the fuzzer that interprets those annotations.
- [[SemanticConstraint]] — the validity-beyond-syntax property generators enforce (checksums, lengths, dates, def/use, matched tags).
- [[PGGCFuzzer]] — the all-features fuzzer combining generators, probabilities, and coverage.
- [[LuhnAlgorithm]] — the credit-card checksum used by the running `post`-repair example.
- [[GrammarFuzzer]] — the base class `GeneratorGrammarFuzzer` subclasses and whose hooks (`process_chosen_children`, `choose_tree_expansion`, `expand_tree_once`) it overloads.
- [[Grammar]] — reuses the `opts()` annotation slot; ordinary fuzzers ignore the new keys.
- [[DerivationTree]] — `post` functions traverse and rewrite it; `find_expansion()` maps a node back to its grammar expansion.
- [[ProbabilisticGrammarFuzzer]] / [[GrammarCoverageFuzzer]] — combined with generators via multiple inheritance into `PGGCFuzzer`.
- [[Generator]] — Python's `yield`-based generators are supported as `pre` functions (note: that page is about GAN generators, a different sense).
- [[ContextFreeGrammar]] — the formalism whose context-free limitation motivates the chapter.
- [[GrammarBasedFuzzing]] — the technique this chapter augments with computation.
- [[AndreasZeller]] / [[CISPA]] — lead author and publisher.
- [[fuzzingbook-09-grammars|Ch 9]] — supplies the `opts()`/`extend_grammar()` mechanism reused here.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — supplies the `GrammarFuzzer` base class and derivation-tree machinery.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] / [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] — the coverage and probabilistic fuzzers folded into `PGGCFuzzer`.
- [[fuzzingbook-12-parser|Ch 12]] — supplies `VAR_GRAMMAR`, the basis for the def/use example.
- [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] — the *declarative* (ISLa) alternative to these imperative `pre`/`post` callbacks for semantic constraints.
- [[fuzzingbook-24-api-fuzzer|Ch 24]] / [[fuzzingbook-27-web-fuzzer|Ch 27]] — downstream chapters that use `GeneratorGrammarFuzzer` to build complex API and UI inputs.

## Contradictions
- None identified.
