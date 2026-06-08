---
title: "The Fuzzing Book Ch 10 — Efficient Grammar Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, grammar, derivation-tree, syntactic-fuzzing]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-10-grammar-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Efficient Grammar Fuzzing

## Summary
Chapter 10 is the central "hub" of *The Fuzzing Book*: it refines the slow, string-rewriting `simple_grammar_fuzzer()` of [[fuzzingbook-09-grammars|Ch 9]] into a fast **tree-based** producer, the [[GrammarFuzzer|`GrammarFuzzer`]] class, built on [[DerivationTree|derivation trees]]. The key data structure is a derivation tree whose every node is a `(symbol, children)` pair — letting the fuzzer track exactly which symbols remain to be expanded and grow the input by cheap in-place tree mutation instead of repeated string search-and-replace. To get *control* over the size and termination of generation, the chapter introduces [[ExpansionCost|symbol/expansion cost]] functions and a **three-phase strategy** (grow at maximum cost to reach `min_nonterminals`, then expand randomly up to `max_nonterminals`, then close at minimum cost), which avoids the infinite-expansion trap that hangs the Ch 9 fuzzer on `expr_grammar`. The chapter reuses the [[Grammar|`Grammar`]] data structure unchanged and is the foundation extended by [[fuzzingbook-11-grammar-coverage-fuzzer|coverage (Ch 11)]], [[fuzzingbook-12-parser|parsing (Ch 12)]], [[fuzzingbook-13-probabilistic-grammar-fuzzer|probabilities (Ch 13)]], and [[fuzzingbook-14-generator-grammar-fuzzer|generators (Ch 14)]].

## Key Concepts
- **[[DerivationTree|Derivation tree]]** — the chapter's representation of an in-progress (or finished) expansion. A node is a Python pair `(symbol, children)`: `children = None` marks an unexpanded [[Nonterminal|nonterminal]] (a placeholder for future expansion), `children = []` marks a [[Terminal|terminal]] leaf, and a non-empty list marks an expanded node. The Python type is `DerivationTree = Tuple[str, Optional[List[Any]]]` (recursive types defeat the static checker, hence `Any`). Also called a *parse tree* / *concrete syntax tree*.
- **[[GrammarFuzzer|`GrammarFuzzer`]]** — a subclass of the abstract `Fuzzer` base class ([[RandomFuzzer]]'s parent) that produces strings efficiently via derivation trees. Constructor takes `grammar`, `start_symbol` (default `<start>`), `min_nonterminals`/`max_nonterminals` size limits, and `disp`/`log` debugging flags; `check_grammar()` validates the grammar via `is_valid_grammar()`. `fuzz()` returns a string; `fuzz_tree()` returns the tree, exposed afterward via the `derivation_tree` attribute.
- **Tree helpers** — `init_tree()` builds the singleton root `(start_symbol, None)`; `expansion_to_children()` splits an expansion string (via `re.split(RE_NONTERMINAL, ...)`) into a list of child nodes, with a special case for the *epsilon expansion* `("", [])`; `all_terminals()` concatenates all leaf symbols (including unexpanded nonterminals) into the produced string; `tree_to_string()` does the same but renders unexpanded nonterminals as empty strings.
- **Node expansion** — `expand_node_randomly()` fetches all grammar expansions for a node, converts each to children, and uses the overloadable `choose_node_expansion()` (default `random.randrange`) to pick one, returning a *new* node. `process_chosen_children()` is a no-op hook for subclasses.
- **Tree expansion** — `possible_expansions()` counts unexpanded nodes; `any_possible_expansions()` tests for any; `expand_tree_once()` is the core method: it recurses to an expandable subtree (picked by `choose_tree_expansion()`) and expands it **in place** (mutating the argument — this is what makes it fast).
- **[[ExpansionCost|Cost functions]]** — `symbol_cost()` and `expansion_cost()` mutually recurse to estimate how much expanding a symbol inflates the tree; a `seen` set detects recursion and returns `float('inf')`. `expand_node_by_cost(node, choose)` picks among expansions by cost; `expand_node_min_cost()` (`choose=min`) closes trees with the shortest derivation, while `expand_node_max_cost()` (`choose=max`) grows them.
- **Three-phase `expand_tree()`** — drives the whole production by swapping the `expand_node` method reference: phase 1 grows at max cost until `min_nonterminals`, phase 2 expands randomly until `max_nonterminals`, phase 3 closes at min cost; asserts zero open expansions at the end. The growth-bounded shortest-path idea is credited to Luke (2000).

## Key Claims
- String-based grammar fuzzing is *quadratic* in output length and can produce tens-of-thousands-of-character outputs; the derivation-tree fuzzer is far faster and yields smaller, controlled inputs.
- `simple_grammar_fuzzer()` hangs on `expr_grammar` because every `<factor>` alternative except `(<expr>)` temporarily increases the symbol count, so under a hard symbol cap the only legal choice is `(<expr>)` — an infinite addition of parentheses. `GrammarFuzzer` handles the same grammar with no issue.
- `expand_tree_once()` mutates the tree **in place**, which is the source of its efficiency; by contrast `expand_node_randomly()` returns a new node and leaves its argument unchanged.
- For `EXPR_GRAMMAR`, `symbol_cost("<digit>") == 1` and `symbol_cost("<expr>") == 5` (the chain `<expr>→<term>→<factor>→<integer>→<digit>→1`).
- A node is a `(symbol, children)` pair where `children = None` means "unexpanded nonterminal," `children = []` means "terminal," giving the algorithm a precise, always-available view of remaining work.
- Caching opportunities exist: `expansion_to_children()` is called repeatedly with identical arguments (Exercise 1's `FasterGrammarFuzzer` memoizes it, requiring `copy.deepcopy()` to protect in-place mutation), and grammar-only costs can be precomputed once (Exercise 2's `EvenFasterGrammarFuzzer`).

## Key Quotes
> "In the internal representation of a derivation tree, a _node_ is a pair (`symbol`, `children`). For nonterminals, `symbol` is the symbol that is being expanded, and `children` is a list of further nodes. For terminals, `symbol` is the terminal string, and `children` is empty." — the core data structure.

> "Congratulations! You have reached one of the central 'hubs' of the book. From here, there is a wide range of techniques that build on grammar fuzzing." — on the chapter's pivotal role.

## Connections
- [[DerivationTree]] — minted here; the data structure the whole efficient algorithm rests on (reused by Ch 11–18).
- [[GrammarFuzzer]] — minted here; the efficient tree-based fuzzer that supersedes `simple_grammar_fuzzer()`.
- [[ExpansionCost]] — minted here; the `symbol_cost`/`expansion_cost` machinery enabling cost-driven grow/close phases.
- [[Grammar]] / [[ContextFreeGrammar]] — the (unchanged) input specification this fuzzer consumes.
- [[Nonterminal]] / [[Terminal]] — `children=None` vs `children=[]` nodes correspond to these symbol kinds.
- [[GrammarBasedFuzzing]] — the technique family this chapter makes efficient.
- [[RandomFuzzer]] — sibling concrete fuzzer; `GrammarFuzzer` shares the `Fuzzer` base class.
- [[Fuzzing]] — the parent discipline.
- [[GraphViz]] — `display_tree()` renders derivation trees via the `graphviz`/`dot` package.
- [[AndreasZeller]] — lead author.
- [[fuzzingbook-09-grammars|Ch 9]] — the predecessor whose naive producer this chapter extends and fixes.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — overrides `choose_node_expansion()` to add combinatorial coverage.
- [[fuzzingbook-12-parser|Ch 12]] — parses inputs *into* derivation trees (the inverse of production).
- [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] / [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] — probability- and generator-weighted variants of `choose_node_expansion()`.

## Contradictions
- None identified. This chapter explicitly supersedes the naive `simple_grammar_fuzzer()` of [[fuzzingbook-09-grammars|Ch 9]]; that is a refinement, not a conflict, and both pages already note the relationship.
