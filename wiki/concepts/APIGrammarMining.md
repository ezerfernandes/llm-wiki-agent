---
title: "API Grammar Mining (CallGrammarMiner)"
type: concept
tags: [fuzzing, testing, api-fuzzing, grammar, grammar-mining, carving, code-synthesis, python, tool]
sources: [fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# API Grammar Mining (CallGrammarMiner)

**API grammar mining** automatically builds a [[Grammar|grammar]] of function calls from *recorded* (carved) executions, so the observed arguments can be **recombined** to fuzz an API — synthesizing [[APIFuzzing|API tests]] without writing a call grammar by hand. It is the bridge from plain [[TestCarving|carving]] (replay the exact calls seen) to API-level [[Fuzzing|fuzzing]] (generate new argument combinations).

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] implements this as the **`CallGrammarMiner`** class, initialized with a [[Carver|`Carver`]]:

- **`initial_grammar()`** seeds `<start> ::= <call>` with an empty `<call>` rule.
- **`mine_arguments_grammar(function_name, arguments, grammar)`** collects, per argument variable, the *set* of values observed (each rendered via `call_value()`, with literal `<` escaped to `<langle>`), and emits one rule per variable expanding into those alternatives — returning the per-variable rules plus the list of argument symbols.
- **`mine_function_grammar(function_name, grammar)`** wraps those argument symbols into a call rule `func(<func-a>, <func-b>)`, or a method call `<func-self>.func(...)` if the first argument is `self`.
- **`mine_call_grammar(function_list=None, qualified=False)`** is the client entry point: it repeats the above over all called functions (skipping internal `_`/`<` names) and unions the resulting `<call>` alternatives, asserting a valid grammar.

Fuzzing the mined grammar with a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] produces recombined calls — e.g. mining `power(1,2)` and `power(3,4)` yields a grammar whose `<x> ::= 1 | 3` and `<y> ::= 2 | 4` let the fuzzer emit `power(1,4)`, `power(3,2)`, etc. Applied to `webbrowser()`, it mines a large grammar including a `<urlparse-url>` rule from which the `urlparse()` API can be fuzzed. The chapter's caveat: recombination can **violate implicit preconditions**, yielding *false alarms* that must be weeded out (e.g. by constraining the grammar). `CallGrammarMiner` is a sibling of the input-grammar [[GrammarMiner|`GrammarMiner`]] (Ch 18) — both are tracer-driven [[GrammarMining|grammar miners]], but one mines *call* grammars and the other *input* grammars.

## Connections
- [[TestCarving]] — supplies the recorded calls this mines into a grammar.
- [[Carver]] — the recorder `CallGrammarMiner` is initialized with.
- [[APIFuzzing]] — the technique mined call grammars enable (without hand-written grammars).
- [[CallSequenceFuzzing]] — carved grammars naturally cover call sequences in valid context.
- [[Grammar]] — the mined output.
- [[GrammarCoverageFuzzer]] — fuzzes the mined grammar to recombine arguments.
- [[GrammarMiner]] — the sibling miner for *input* grammars (Ch 18).
- [[GrammarMining]] / [[GrammarInference]] — the broader learn-a-grammar-from-execution family.
- [[fuzzingbook-24-api-fuzzer|Ch 24]] — hand-authors the call grammars this mines automatically.
- [[fuzzingbook-25-carver]] — the chapter introducing `CallGrammarMiner`.

## Sources
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
