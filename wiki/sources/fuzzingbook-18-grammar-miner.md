---
title: "The Fuzzing Book Ch 18 — Mining Input Grammars"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, grammar-mining, grammar-inference, dynamic-analysis, tracing, parsing, semantic-fuzzing, python]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-18-grammar-miner.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Mining Input Grammars

## Summary
This chapter opens Part IV (Semantic Fuzzing) and inverts the rest of the book: instead of *writing* a [[ContextFreeGrammar|grammar]] by hand and fuzzing with it ([[fuzzingbook-09-grammars|Ch 9]], [[fuzzingbook-10-grammar-fuzzer|Ch 10]]), it shows how to **automatically infer an input grammar from a program plus a handful of sample inputs**, then fuzz the program with the recovered grammar — a multiplier on whatever seeds you already have. The core insight ([[GrammarInference]]) is that in a hand-written ad-hoc parser, *the variables that hold substrings of the input reveal the input's structure*: a method/variable that processes a given input fragment corresponds to a [[Nonterminal|nonterminal]] covering that span. The chapter dynamically traces execution (reusing the [[Coverage|`Coverage`]] tracer from [[fuzzingbook-04-coverage|Ch 4]]), records every `str` local that is a substring of the input, stitches those fragments into a per-input [[DerivationTree|derivation tree]], and abstracts multiple trees into a grammar — the running examples are the CSV `process_inventory()`/`process_vehicle()` parser from [[fuzzingbook-12-parser|Ch 12]] and Python's real `urllib.parse.urlparse`. It builds the miner in three increasingly precise stages (simple → reassignment-aware → scope-aware), and shows the recovered grammar driving a [[GrammarFuzzer|`GrammarFuzzer`]]/[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]. The chapter is based directly on the **AUTOGRAM** work of Höschele & Zeller, and points to [[fuzzingbook-19-information-flow|Ch 19]] for replacing the substring heuristic with true [[DynamicTaintTracking|dynamic taint tracking]].

## Key Concepts
- **[[GrammarInference]] — learning an input grammar from a program.** Assumes the program is written so that "specific methods are responsible for parsing specific fragments of the input" (true of almost all ad-hoc parsers). By observing the input fragments named in different methods during execution, one recovers the parse structure; abstracting over many inputs yields the grammar. Distinct from black-box grammar induction from samples alone (Higuera; Clark) — here the *program* guides inference.
- **[[GrammarMiner]] — the concrete tool/class pipeline.** Top-level convenience function `recover_grammar(fn, inputs, **kwargs)` takes a function and sample inputs and returns a [[Grammar|`Grammar`]]. Internally a `GrammarMiner` accumulates per-input derivation trees via `add_tree()`/`update_grammar()`, `tree_to_grammar()` turns a tree into a canonical grammar (node name → list of children as one alternative), and `readable()` flattens canonical rules to displayable form.
- **`Tracer` (subclass of `Coverage`) + `Context`.** `Tracer` hooks Python's `sys.settrace` via the [[Coverage|`Coverage`]] machinery, restricting attention to chosen `files`/`methods` and to `str` locals only (the variables most likely to hold input fragments). `Context` wraps the stack `frame` to expose method name, parameter names, file, and line number.
- **`DefineTracker` + `is_input_fragment()`.** Processes the trace into a `my_assignments` dict of variable → input fragment. The heuristic for "this value came from the input" is plain **substring inclusion** (`value in self.my_input`) gated by a minimum `FRAGMENT_LEN` (default 3) to avoid spurious short matches — a cheap stand-in for symbolic execution or [[DynamicTaintTracking|dynamic tainting]].
- **`TreeMiner` + `insert_into_tree()`.** Assembles fragments into a [[DerivationTree|derivation tree]]: start from `(<start>, [(whole_input, [])])`; for each (var, value) it finds the node whose value contains `value`, `partition()`s that value into prefix / matched-part / suffix, and replaces the matched part with a nonterminal node `to_nonterminal(var)`.
- **Reassignment handling — `CallStack`, `Vars`, `AssignmentVars`, `AssignmentTracker`.** The simple miner assumes each variable's value is stable; real code (e.g. `urlparse`'s `url` variable) reassigns. The fix annotates each variable with the **line number** where it was (re)defined and a per-reassignment sequence index, so each distinct value gets a unique nonterminal (e.g. `urlparse@394:scheme`). `CallStack` gives each method invocation a unique id; `AssignmentTracker` dispatches `on_call`/`on_line`/`on_return` events.
- **Scope handling — `InputStack`, `ScopedVars`, `ScopeTracker`, `ScopeTreeMiner`, `ScopedGrammarMiner`.** Even with line numbers, a fragment can be wrongly attributed across *different* method calls that reuse the same value at the same location. `InputStack` tracks which input fragments are *in scope* in the current activation record; replacement is only allowed when the variable's method-sequence scope matches the value's (with an exception for fragments produced by an internal child call). `clean_grammar()` then collapses single-token "unit" rules into readable definitions.
- **Exercise extensions.** `flatten()` recursively unpacks complex objects (the `Vehicle` object example) into `(key, value)` pairs so fragments hidden inside custom objects are still tracked. A second exercise replaces substring inclusion with **[[DynamicTaintTracking|dynamic taints]]** via the `ostr` origin-tracking string from [[fuzzingbook-19-information-flow|Ch 19]] (`TaintedInputStack`, `TaintedScopeTreeMiner`, `recover_grammar_with_taints()`).

## Key Claims
- Given sample inputs and a program that uses a hand-written parser, an input grammar can be learned purely by observing `str` variable values during execution — no source-code analysis or specification required.
- Variable values that are substrings of the input act as a reliable signal for input structure; a variable handling a span of the input maps to a nonterminal over that span.
- Simple **string inclusion** (gated by `FRAGMENT_LEN`) is sufficient to recover reasonably accurate grammars from real-world code such as Python's `urllib.parse`.
- String inclusion is in some ways *more broadly applicable* than dynamic tainting: dynamic taints require binary instrumentation and are frequently lost at the Python/C boundary or via implicit flows, whereas substring checks have no such limitation.
- Naive mining breaks on **variable reassignment** (the `url` variable changing as parsing proceeds) and on **cross-call value reuse**; annotating variables with line number + reassignment index, and enforcing scope, fixes both.
- The recovered grammar is immediately usable by the book's [[GrammarFuzzer|`GrammarFuzzer`]] and [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]/[[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]), turning a few seeds into an unbounded supply of syntactically valid inputs.
- The technique is based on the **AUTOGRAM** approach (Höschele & Zeller, 2017); the earliest program-guided parse-tree recovery is due to Lin et al. (2008).

## Key Quotes
> "We start with the assumption that the program is written in such a fashion that specific methods are responsible for parsing specific fragments of the program — this includes almost all ad hoc parsers." — the foundational assumption of program-guided grammar mining.

> "Being able to automatically extract a grammar and to use this grammar for fuzzing makes for very effective test generation with a minimum of manual work." — the payoff stated in the synopsis.

> "String inclusion has no such problems. Hence, our approach can often obtain better results than relying on dynamic tainting." — on why the simple substring heuristic is competitive with taint tracking.

## Connections
- [[GrammarInference]] — the central new concept: inferring an input grammar from a program + samples.
- [[GrammarMiner]] — the concrete tool/class hierarchy (`recover_grammar()`, `Tracer`, `DefineTracker`, `TreeMiner`, `GrammarMiner`, scoped variants) introduced here.
- [[GrammarMining]] — this chapter is the *whole-grammar* sense of grammar mining (complements [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]'s probability mining); page expanded.
- [[DynamicTaintTracking]] — the precise alternative to substring inclusion; detailed in [[fuzzingbook-19-information-flow|Ch 19]] and used in the chapter's taint exercise (`ostr`).
- [[Grammar]] / [[ContextFreeGrammar]] — the data structure / formalism that mining *outputs*.
- [[DerivationTree]] — the per-input intermediate structure assembled by `TreeMiner` before abstraction to a grammar.
- [[Parser]] — the mirror operation; the chapter's running example is [[fuzzingbook-12-parser|Ch 12]]'s `process_inventory()` parser, and mining recovers what a parser implicitly encodes.
- [[GrammarBasedFuzzing]] — the consumer of recovered grammars; mining feeds the grammar-fuzzing pipeline.
- [[Coverage]] — the `Tracer` subclasses the [[fuzzingbook-04-coverage|Ch 4]] `Coverage` tracer to hook execution.
- [[RahulGopinath]] — book co-author and grammar-mining researcher (Mimid / AUTOGRAM lineage); a natural author of this chapter's techniques.
- [[AndreasZeller]] — lead book author and co-creator of the AUTOGRAM approach this chapter is based on.
- [[CISPA]] — publisher of *The Fuzzing Book* and home of the AUTOGRAM line of work.
- [[fuzzingbook-09-grammars]] — the grammar foundation this chapter recovers automatically.
- [[fuzzingbook-12-parser]] — supplies the `process_inventory()`/`process_vehicle()` running example.
- [[fuzzingbook-19-information-flow]] — the next chapter; supplies the `ostr` dynamic-taint mechanism that upgrades the substring heuristic.

## Contradictions
- None identified. The chapter explicitly *contrasts* (rather than contradicts) [[DynamicTaintTracking|dynamic taint tracking]] with its own substring-inclusion heuristic, and complements (rather than conflicts with) the probability-mining sense of [[GrammarMining]] in [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]].
