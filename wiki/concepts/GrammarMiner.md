---
title: "GrammarMiner (Tool)"
type: concept
tags: [fuzzing, grammar, grammar-mining, grammar-inference, tracing, derivation-tree, dynamic-analysis, python, tool]
sources: [fuzzingbook-18-grammar-miner, fuzzingbook-23-configuration-fuzzer, fuzzingbook-25-carver, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# GrammarMiner (Tool)

**`GrammarMiner`** is the concrete tool and Python class hierarchy in *The Fuzzing Book* that implements program-guided [[GrammarInference|grammar inference]]: given a function and a set of sample inputs, it recovers a [[Grammar|`Grammar`]] describing the function's input language. It is the engineering realization of the idea that input-substring-holding variables reveal input structure.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] builds the miner as a small pipeline, in three increasingly precise stages.

**Top-level API.** `recover_grammar(fn, inputs, files=..., methods=...)` runs `fn` on each input under a tracer and returns a `readable()` [[Grammar|grammar]] — the easiest entry point.

**The pipeline classes:**
- **`Tracer`** (subclass of [[Coverage|`Coverage`]]) — hooks `sys.settrace`, filters to chosen `files`/`methods`, and keeps only `str` locals (the variables likely to hold input fragments). A `Context` helper wraps the stack `frame` to expose method name, parameter names, file, and line number.
- **`DefineTracker`** — turns the trace into a `my_assignments` map of variable → input fragment, using `is_input_fragment()`: a value counts as input-derived if it is a substring of the input and at least `FRAGMENT_LEN` (default 3) long.
- **`TreeMiner`** — assembles fragments into a [[DerivationTree|derivation tree]]. `insert_into_tree()` finds the node whose value contains a fragment, `partition()`s it into prefix / match / suffix, and replaces the match with `to_nonterminal(var)`.
- **`GrammarMiner`** — `tree_to_grammar()` converts a tree to a canonical grammar; `add_tree()`/`update_grammar()` merge per-input trees; `readable()` flattens canonical rules for display.

**Robustness stages** (the heart of the chapter):
- **Reassignment-aware** — `CallStack`, `Vars`, `AssignmentVars`, `AssignmentTracker` annotate each variable with its definition **line number** and a per-reassignment sequence index, so a variable whose value changes during parsing (e.g. `urlparse`'s `url`) yields distinct nonterminals like `urlparse@394:scheme`.
- **Scope-aware** — `InputStack`, `ScopedVars`, `ScopeTracker`, `ScopeTreeMiner`, `ScopedGrammarMiner` restrict fragment replacement to the current activation record's in-scope values (with an exception for fragments produced by internal child calls), preventing cross-call mis-attribution. `clean_grammar()` collapses single-token unit rules for readability.

**Extensions (exercises):** `flatten()` unpacks complex objects (e.g. a `Vehicle` object) so hidden fragments are still tracked; `recover_grammar_with_taints()` swaps substring inclusion for [[DynamicTaintTracking|dynamic taints]] using the `ostr` origin-tracking string from [[fuzzingbook-19-information-flow|Ch 19]] (`TaintedInputStack`, `TaintedScopeTreeMiner`).

The chapter demonstrates the miner on the CSV `process_inventory()`/`process_vehicle()` parser from [[fuzzingbook-12-parser|Ch 12]] and on Python's real `urllib.parse.urlparse`, then fuzzes the recovered grammars with [[GrammarFuzzer|`GrammarFuzzer`]] and [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]].

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] introduces a sibling miner with a very different target: where `GrammarMiner` recovers a program's *input-data* grammar by tracing which `str` variables hold input substrings, the [[OptionGrammarMiner|`OptionGrammarMiner`]] recovers a program's *option* grammar (an [[OptionGrammar|option grammar]]) by tracing its `argparse` setup up to `parse_args()`. Both are dynamic, trace-based ([[Coverage|`sys.settrace`]]) [[GrammarMining|grammar miners]] feeding the same [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]], but `OptionGrammarMiner` reads the option *specification* rather than observed input fragments, making it lighter and exact for the `argparse` case.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] adds a third tracer-based [[GrammarMining|grammar miner]] to this family: the [[APIGrammarMining|`CallGrammarMiner`]]. Where `GrammarMiner` (Ch 18) mines a program's *input-data* grammar and [[OptionGrammarMiner|`OptionGrammarMiner`]] (Ch 23) mines its *option* grammar, `CallGrammarMiner` mines a *call* grammar — one rule per function argument, expanding into the values observed while [[TestCarving|carving]] real executions (via a [[Carver|`CallCarver`]]). All three feed the same [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]], but the call miner targets [[APIFuzzing|API-level fuzzing]] by recombining recorded arguments rather than reconstructing an input language.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] adds a fourth tracer-free sibling to this family: the `GUIGrammarMiner`. Where `GrammarMiner` (Ch 18) recovers an input-data grammar by tracing `str` variables, `GUIGrammarMiner` mines a grammar from a *live user interface* via [[Selenium]] — `mine_state_actions()` queries the current page for its interactive elements (text→`fill`, checkbox→`check`, submit→`submit`, link→`click`), and `mine_state_grammar()` turns those actions into a [[Grammar|grammar]] that *embeds a [[FiniteStateMachine|finite state machine]]* of pages (a [[UINavigationModel|UI navigation model]]): each `click`/`submit` introduces a fresh `<unexplored>` state symbol, expanded as exploration reaches it. Unlike the trace-based miners, it discovers structure by *interaction* rather than by `sys.settrace`, and the mined grammar feeds the same [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] ([[GUIFuzzer|`GUICoverageFuzzer`]]) for [[GUIFuzzing|GUI fuzzing]].

## Connections
- [[GUIFuzzer]] — the Ch 28 `GUIGrammarMiner` sibling that mines a grammar from a live UI.
- [[UINavigationModel]] / [[GUIFuzzing]] — the FSM-in-a-grammar UI model the GUI miner produces.
- [[APIGrammarMining]] — the Ch 25 sibling miner (`CallGrammarMiner`) for function-call grammars.
- [[OptionGrammarMiner]] — the Ch 23 sibling miner for command-line option grammars.
- [[GrammarInference]] — the technique `GrammarMiner` implements.
- [[GrammarMining]] — the umbrella term for learning grammars from data/programs.
- [[Coverage]] — the `Tracer` subclasses the [[fuzzingbook-04-coverage|Ch 4]] `Coverage` tracer.
- [[DerivationTree]] — `TreeMiner`'s intermediate output, abstracted into a grammar.
- [[Grammar]] / [[ContextFreeGrammar]] — the miner's final output.
- [[GrammarBasedFuzzing]] / [[GrammarFuzzer]] / [[GrammarCoverageFuzzer]] — consume the recovered grammar.
- [[DynamicTaintTracking]] — the more precise fragment-origin check used in the taint exercise.
- [[Parser]] — the running example whose structure the miner recovers.
- [[RahulGopinath]] / [[AndreasZeller]] — the AUTOGRAM/Mimid researchers behind the approach.

## Sources
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars."
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (the sibling `OptionGrammarMiner`).
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests" (the sibling `CallGrammarMiner`).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (the sibling `GUIGrammarMiner` mining a grammar from a live UI).
