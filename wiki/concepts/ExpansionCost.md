---
title: "Expansion Cost"
type: concept
tags: [grammar, fuzzing, derivation-tree, algorithm, recursion, syntactic-fuzzing]
sources: [fuzzingbook-10-grammar-fuzzer]
last_updated: 2026-06-06
---

# Expansion Cost

**Expansion cost** (and the related **symbol cost**) is the metric *The Fuzzing Book*'s [[GrammarFuzzer|`GrammarFuzzer`]] uses to decide which grammar [[ProductionRule|expansion]] to apply, so that it can deliberately *grow* or *close* a [[DerivationTree|derivation tree]]. Intuitively, the cost of expanding a [[Nonterminal|nonterminal]] estimates how many further expansions it forces — `<digit>→2` costs little, whereas `<factor>→(<expr>)` reopens deep recursion. Choosing **minimum-cost** expansions terminates a tree with the shortest derivation; choosing **maximum-cost** expansions inflates it with more nonterminals to expand.

## Definition
Two mutually recursive functions, with a `seen` set guarding against infinite recursion:

```python
def symbol_cost(self, symbol, seen=set()):
    expansions = self.grammar[symbol]
    return min(self.expansion_cost(e, seen | {symbol}) for e in expansions)

def expansion_cost(self, expansion, seen=set()):
    symbols = nonterminals(expansion)
    if len(symbols) == 0:
        return 1                         # no nonterminal: cost 1
    if any(s in seen for s in symbols):
        return float('inf')              # recursion detected
    return sum(self.symbol_cost(s, seen) for s in symbols) + 1
```

- `symbol_cost(S)` = the **minimum** cost over all of `S`'s expansions.
- `expansion_cost(e)` = `1` plus the sum of the symbol costs of the nonterminals in `e`; if any of them is already `seen`, the cost is `float('inf')` to flag potentially infinite recursion.

For `EXPR_GRAMMAR`, `symbol_cost("<digit>") == 1` and `symbol_cost("<expr>") == 5` (the chain `<expr>→<term>→<factor>→<integer>→<digit>→1`).

## Cost-driven expansion
`expand_node_by_cost(node, choose)` computes each candidate expansion's cost, applies `choose` (`min` or `max`) to pick the target cost, and randomly breaks ties among same-cost expansions. Two shortcuts wrap it:
- `expand_node_min_cost()` (`choose=min`) — **closes** a tree along the shortest derivation, avoiding the infinite-expansion trap that hangs `simple_grammar_fuzzer()`.
- `expand_node_max_cost()` (`choose=max`) — **grows** a tree, producing as many nonterminals as possible.

## From The Fuzzing Book — Efficient Grammar Fuzzing
[[fuzzingbook-10-grammar-fuzzer|Ch 10]] introduces these cost functions to power its **three-phase `expand_tree()`** strategy: grow at maximum cost until `min_nonterminals`, expand randomly until `max_nonterminals`, then close at minimum cost (asserting zero open expansions at the end). The growth-bounded-then-shortest-path idea is credited to Luke (2000). Because the costs depend only on the grammar, Exercise 2's `EvenFasterGrammarFuzzer` precomputes them once at initialization. Exercise 4 notes that routing random expansion through `expand_node_by_cost(node, random.choice)` changes the distribution — first a cost is picked at random, then an expansion of that cost — giving uniquely-costed expansions a higher chance than the plain uniform `expand_node_randomly()`.

## Connections
- [[GrammarFuzzer]] — uses these functions for its grow/close expansion phases.
- [[DerivationTree]] — cost decides how each tree node is expanded.
- [[ProductionRule]] / [[Nonterminal]] — cost is computed over expansions and the nonterminals they contain.
- [[Grammar]] — costs are a property of the grammar alone (hence precomputable).
- [[GrammarBasedFuzzing]] — cost-based control is what makes efficient grammar fuzzing terminate.
- [[fuzzingbook-10-grammar-fuzzer]] — the chapter that introduces symbol/expansion cost.

## Sources
- [[fuzzingbook-10-grammar-fuzzer]] — *The Fuzzing Book* Ch 10, "Efficient Grammar Fuzzing."
