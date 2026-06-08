---
title: "GeneratorGrammarFuzzer"
type: concept
tags: [fuzzing, grammar, generators, semantic-constraints, testing, class-hierarchy, syntactic-fuzzing, python]
sources: [fuzzingbook-14-generator-grammar-fuzzer]
last_updated: 2026-06-06
---

# GeneratorGrammarFuzzer

**`GeneratorGrammarFuzzer`** is *The Fuzzing Book*'s grammar fuzzer that **executes the Python functions attached to grammar expansions**. It is a subclass of [[GrammarFuzzer|`GrammarFuzzer`]] ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]) that consumes a [[GeneratorGrammar|generator grammar]] and, while building a [[DerivationTree|derivation tree]], invokes the `pre`, `post`, and `order` functions specified via `opts()` — generating, checking, and repairing produced elements so they satisfy [[SemanticConstraint|semantic constraints]] a context-free grammar cannot express. A plain `GrammarFuzzer` ignores these annotations (and emits a warning), so the same grammar is reusable by either fuzzer.

## What it overrides
```python
class GeneratorGrammarFuzzer(GrammarFuzzer):
    def supported_opts(self):
        return super().supported_opts() | {"pre", "post", "order"}
```
- **`process_chosen_children()`** — pre-expansion hook. Looks up the `pre` function with `exp_pre_expansion_function()`; if it is a Python generator, runs it via `run_generator()`, else calls it directly; then `apply_result()` applies the value to the children.
- **`apply_result(result, children)`** — applies a `pre`/`post` result: a *string* replaces the whole expansion; a *list* `[x_1…x_n]` replaces the i-th nonterminal child with `x_i` (skipping `None`); `None`/booleans are ignored; other types are `repr()`'d into a string.
- **`run_generator()` + `reset_generators()`** — supports [[Generator|Python generators]]: instantiates the generator once per `fuzz_tree()`, keyed by `repr((expansion, function))` in a `generators` dict, and pulls successive values with `next()` so state persists across expansions.
- **`fuzz_tree()` / `run_post_functions()` / `find_expansion()` / `eval_function()`** — post-expansion checking/repair. After the tree is built, `run_post_functions()` recurses over nodes; `find_expansion()` recovers which grammar expansion produced a node's children (by matching `exp_string()` against the concatenated child symbols); `eval_function()` builds the argument list from the nonterminal children's terminal strings and calls the function. If any returns `False`, the whole tree is discarded and rebuilt (`restart_expansion()`).
- **`expand_tree_once()` + `run_post_functions_locally()`** — *local* checking: runs a node's `post` function (`depth=0`) the moment its subtree is complete, retrying up to `replacement_attempts` (default 10, set in the constructor) before raising `RestartExpansionException`. This avoids generating a whole tree only to reject it.
- **`choose_tree_expansion()` + `exp_order()`** — honors `opts(order=[…])` by choosing the expandable child with the lowest order rank, controlling the sequence in which side-effecting functions fire.

## Interface
```python
charge_fuzzer = GeneratorGrammarFuzzer(CHARGE_GRAMMAR)
charge_fuzzer.fuzz()        # a charge with a Luhn-valid credit-card number

credit_card_fuzzer = GeneratorGrammarFuzzer(CHARGE_GRAMMAR,
                                            start_symbol="<credit-card-number>")
assert valid_luhn_checksum(credit_card_fuzzer.fuzz())
```
Constructor adds `replacement_attempts=10` to the inherited `GrammarFuzzer` parameters; `log=True` traces each function call and replacement.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] introduces `GeneratorGrammarFuzzer` as the engine of [[GeneratorGrammar|generator grammars]]. It demonstrates it on numeric-range expressions, Python-generator-driven integers (`iterate()`/`range()`), [[LuhnAlgorithm|Luhn]]-valid credit-card numbers (repair), matched XML tags (repair), negative-only and binary-only expressions (constraints with `eval()`), and a symbol-table def/use grammar (`CONSTRAINED_VAR_GRAMMAR`) where ordering ensures every used variable is first defined. The chapter then composes it with the [[ProbabilisticGrammarFuzzer|probabilistic]] and [[GrammarCoverageFuzzer|coverage]] fuzzers via *multiple inheritance* (`ProbabilisticGeneratorGrammarFuzzer`, `ProbabilisticGeneratorGrammarCoverageFuzzer`) into the all-features [[PGGCFuzzer|`PGGCFuzzer`]] — the latter rebuilding coverage from the *final* tree so discarded expansions don't inflate it.

## Connections
- [[GeneratorGrammar]] — the annotated grammar it interprets.
- [[GrammarFuzzer]] — the base class; it overloads `process_chosen_children()`, `expand_tree_once()`, `choose_tree_expansion()`, and `fuzz_tree()`.
- [[SemanticConstraint]] — the validity-beyond-syntax property its `post` functions enforce.
- [[PGGCFuzzer]] — the all-features fuzzer it is folded into via multiple inheritance.
- [[ProbabilisticGrammarFuzzer]] / [[GrammarCoverageFuzzer]] — the sibling `GrammarFuzzer` subclasses it is combined with.
- [[DerivationTree]] — the tree it builds and whose subtrees `post` functions check/rewrite.
- [[Generator]] — Python `yield`-based generators it supports as `pre` functions.
- [[LuhnAlgorithm]] — the checksum in its canonical credit-card example.
- [[GrammarBasedFuzzing]] — the technique it augments with computation.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — supplies the `GrammarFuzzer` superclass.
- [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] — the declarative-constraints alternative for the same goal.
- [[fuzzingbook-14-generator-grammar-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators."
