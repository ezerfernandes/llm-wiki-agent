---
title: "Data Flow"
type: concept
tags: [program-analysis, data-flow, information-flow, taint-analysis, fuzzing, security]
sources: [fuzzingbook-19-information-flow]
last_updated: 2026-06-06
---

# Data Flow

**Data flow** is the dependence of a value on the data it was computed from: a value is *data-dependent* on an input when it is produced by reading or transforming that input (assignment, arithmetic, string operations). It is the *explicit* half of [[InformationFlow|information flow]] and the half that [[DynamicTaintAnalysis|dynamic taint analysis]] can follow directly — by carrying a taint/origin along each operation, a value's label records exactly the input data it flowed from. Its counterpart is [[ImplicitInformationFlow|control flow / implicit flow]], where a value depends on input only through which branches executed, leaving no explicit data dependence to track.

> Note: this concept is *data-flow analysis* (the dependence of values on data). It is distinct from the [[DataflowVariable|dataflow programming]] concept (single-assignment variables that trigger computation), which is unrelated.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] tracks explicit data flow at the character level: the [[CharacterOrigin|`ostr`]] origin list *is* a data-flow record, naming for each output character the input index it derived from. The chapter contrasts this sharply with [[ImplicitInformationFlow|implicit flow]] — its `strip_all_info_again()` example copies a string character-by-character through an `if`/`elif` chain (`if c == 'a': t += 'a'`), producing identical output with *no* data flow between input and output, so taints vanish. It also notes data flow is broken whenever values leave the string/character domain (e.g. `chr(ord(c))`) or cross into Python's internal C code. [[TaintDirectedFuzzing|Taint-directed fuzzing]] then exploits the surviving data flow: by tracing the origins of characters that reach `eval` back to the grammar rules that produced them, it turns a data-flow observation into a fuzzing-guidance signal.

## Connections
- [[InformationFlow]] — data flow is the explicit component of information flow.
- [[ImplicitInformationFlow]] — the control-flow counterpart that data-flow tracking cannot follow.
- [[DynamicTaintAnalysis]] / [[CharacterOrigin]] — the mechanisms that make data flow observable at runtime.
- [[TaintDirectedFuzzing]] — uses data flow (origins reaching a sink) to direct generation.
- [[DataflowVariable]] — a *different* (dataflow-programming) concept; do not conflate.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — symbolic execution reasons about flows (including some implicit ones) that pure data-flow taint misses.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
