---
title: "ProbabilisticGrammarFuzzer"
type: concept
tags: [fuzzing, grammar, probability, testing, class-hierarchy, syntactic-fuzzing, python]
sources: [fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer]
last_updated: 2026-06-06
---

# ProbabilisticGrammarFuzzer

**`ProbabilisticGrammarFuzzer`** is *The Fuzzing Book*'s grammar fuzzer that **respects probability annotations** on expansions. It is a subclass of [[GrammarFuzzer|`GrammarFuzzer`]] ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]) that consumes a [[ProbabilisticGrammar|probabilistic grammar]] and, when expanding a [[DerivationTree|derivation tree]] node, makes a **weighted** choice among the candidate expansions instead of a uniform one.

## How it works
The class needs to override remarkably little of its base class — the whole point of `GrammarFuzzer`'s design as a hub:

```python
class ProbabilisticGrammarFuzzer(GrammarFuzzer):
    def check_grammar(self):
        super().check_grammar()
        assert is_valid_probabilistic_grammar(self.grammar, self.start_symbol)

    def supported_opts(self):
        return super().supported_opts() | {'prob'}

    def choose_node_expansion(self, node, children_alternatives):
        (symbol, tree) = node
        probabilities = exp_probabilities(self.grammar[symbol])
        weights = [probabilities[all_terminals((symbol, children))]
                   for children in children_alternatives]
        if sum(weights) == 0:           # closing phase: no weighted option
            return random.choices(range(len(children_alternatives)))[0]
        return random.choices(range(len(children_alternatives)),
                              weights=weights)[0]
```

- `choose_node_expansion()` — the single behavioral override; it looks up each alternative's probability via `exp_probabilities()` (which distributes any un-annotated mass equally and asserts the rule sums to 1) and calls `random.choices()` with a `weights` argument. The `sum(weights) == 0` fallback handles the **closing phase**, where even a probability-0 expansion must be taken if it is the only way to finish the tree at minimum cost.
- `check_grammar()` adds the `is_valid_probabilistic_grammar()` check on top of the base validity check.
- `supported_opts()` declares `'prob'` as an accepted annotation.

Everything else — tree growth, the grow/close [[ExpansionCost|cost phases]], `all_terminals()` flattening — is inherited unchanged.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] introduces `ProbabilisticGrammarFuzzer` as the engine of [[ProbabilisticGrammarFuzzing|probabilistic grammar fuzzing]]. It demonstrates that the fuzzer faithfully reproduces specified distributions — 10,000 lead digits match the [[BenfordsLaw|Benford]] probabilities almost exactly, whereas a plain `GrammarFuzzer` (ignoring annotations) yields a uniform distribution that a χ²-test flags as "unnatural." It powers [[DirectedFuzzing|directed fuzzing]] (`set_prob()` to favor/disable schemes), consumes [[GrammarMining|mined]] probabilities to test common, uncommon (inverted), or sliced features, and Exercise 1 combines it with [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] via *multiple inheritance* (`ProbabilisticGrammarCoverageFuzzer`) — covering uncovered expansions first, then proceeding by probability.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] combines `ProbabilisticGrammarFuzzer` with the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]] by *multiple inheritance* into `ProbabilisticGeneratorGrammarFuzzer` (and, with coverage, into the [[PGGCFuzzer|`PGGCFuzzer`]] capstone). Because both extend [[GrammarFuzzer|`GrammarFuzzer`]] along *different* axes — weighted choice vs. attached functions — they compose with little friction: the joint `supported_opts()` is the union of both parents' opts (`prob` ∪ `pre`/`post`/`order`) and the constructor chains both `__init__`s, routing `replacement_attempts` to the generator side. The chapter's example sets `opts(prob=0.9)` to favor long identifiers while still enforcing a generator-based def/use constraint.

## Connections
- [[GrammarFuzzer]] — the base class; only `choose_node_expansion()` is overloaded.
- [[PGGCFuzzer]] — the Ch 14 capstone combining it with generators and coverage via multiple inheritance.
- [[ProbabilisticGrammar]] — the annotated grammar it interprets.
- [[ProbabilisticGrammarFuzzing]] — the technique it realizes.
- [[DerivationTree]] — the tree it expands by weighted choice.
- [[ExpansionCost]] — drives the grow/close phases (the zero-weight closing fallback).
- [[DirectedFuzzing]] — its main application: steering by tuned probabilities.
- [[GrammarMining]] — supplies learned probabilities for it to consume.
- [[BenfordsLaw]] — the distribution it is shown to reproduce.
- [[GrammarCoverageFuzzer]] — combined with it via multiple inheritance in Exercise 1.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — supplies the `GrammarFuzzer` superclass.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing."
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (combined with generators/coverage into `PGGCFuzzer`).
