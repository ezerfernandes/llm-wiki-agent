---
title: "Taint-Directed Fuzzing"
type: concept
tags: [fuzzing, taint-analysis, information-flow, greybox, grammar-fuzzing, security, python]
sources: [fuzzingbook-19-information-flow]
last_updated: 2026-06-06
---

# Taint-Directed Fuzzing

**Taint-directed fuzzing** uses [[DynamicTaintAnalysis|taint]] / [[CharacterOrigin|origin]] information as feedback to steer input generation toward the parts of a program that matter (typically *dangerous sinks*). Where ordinary [[GreyboxFuzzing|greybox fuzzing]] rewards inputs that reach new *code coverage*, taint-directed fuzzing rewards inputs whose data reaches a chosen sink, and — when origins are tracked back to the generator — biases the generator toward the structures that produced that data. It uses information flow as a stronger, more targeted signal than crash-only feedback.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] builds this in two steps. First, *taint-aware* fuzzing: a `Tainted` exception and `TaintedDB.my_eval()` raise whenever a non-`TRUSTED` string reaches the `eval` sink, revealing which SQL statement *kinds* (insert/update/select/delete) get there. Second, *taint-directed* fuzzing, which pinpoints the responsible grammar rules: `TrackingDB` raises on any character with a non-empty `origin`; `TaintedGrammarFuzzer` (a [[GrammarFuzzer|`GrammarFuzzer`]] subclass) tags every grammar key, alternative, and token with a distinct integer origin in `init_tainted_grammar()` (increments of 1000/100/10) and preserves those origins through `tree_to_string()` so the generated string carries per-token provenance. When `eval` is reached, `update_grammar()` intersects the origins that arrived at the sink with each grammar rule's token origins and increments a `use` counter on the matching rules — so rules that repeatedly feed the dangerous operation can be favored in subsequent generation. The chapter notes that symbolic techniques ([[fuzzingbook-20-concolic-fuzzer|Ch 20]]) offer an even better, semantics-aware alternative to this taint-based direction.

## Connections
- [[DynamicTaintAnalysis]] / [[CharacterOrigin]] / [[DataFlow]] — the flow information that supplies the guidance signal.
- [[InformationFlow]] — taint-directed fuzzing turns a flow oracle into a generation strategy.
- [[GreyboxFuzzing]] — the feedback-driven fuzzing family this belongs to (here keyed on data flow, not coverage).
- [[GrammarFuzzer]] / [[Grammar]] / [[DerivationTree]] — `TaintedGrammarFuzzer` propagates origins through the canonical grammar and derivation tree.
- [[CodeInjection]] — the `eval` sink the chapter directs fuzzing toward.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — symbolic/concolic guidance, a more powerful successor.
- [[fuzzingbook-19-information-flow]] — the chapter that introduces taint-directed fuzzing.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
