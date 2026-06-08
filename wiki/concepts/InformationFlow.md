---
title: "Information Flow"
type: concept
tags: [security, information-flow, taint-analysis, dynamic-analysis, fuzzing, testing, python]
sources: [fuzzingbook-19-information-flow, fuzzingbook-20-concolic-fuzzer]
last_updated: 2026-06-06
---

# Information Flow

**Information flow** is the movement of data through a program — from *sources* (where data enters, e.g. functions that read user input) to *sinks* (where it has effect, e.g. an `eval()` call or a network reply). Tracking information flow lets a program answer questions that crashes alone cannot: *did untrusted input reach a dangerous operation?* (integrity / injection) and *did secret data reach output?* (confidentiality / leakage). It distinguishes **explicit flow** (data dependence — a value is computed from input data, the kind [[DataFlow|data-flow]] tracking follows) from **implicit flow** ([[ImplicitInformationFlow|control dependence] — output determined by input via branching, with no direct assignment).

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] frames information flow as the foundation of a *stronger oracle* than crashing: by identifying input functions as taint *sources*, dangerous operations as *sinks*, and blessed functions as *sanitizers*, it can enforce that input never reaches a sink unsanitized and that secrets never reach output. It realizes this with [[DynamicTaintAnalysis|dynamic taint analysis]] — the [[TaintedString|`tstr`]] (whole-string taint) and [[CharacterOrigin|`ostr`]] (per-character origin) `str` subclasses — and applies it to an `eval()`-vulnerable SQL database (rejecting [[CodeInjection|code injection]]), to a Heartbleed-style `heartbeat()` leak (detecting secret characters in the reply by origin), and to [[TaintDirectedFuzzing|taint-directed fuzzing]] that steers a grammar fuzzer toward rules whose output reaches the sink. The chapter is candid that information flow tracked this way is incomplete: conversions, internal C code, and especially [[ImplicitInformationFlow|implicit flows]] break it, motivating the symbolic techniques of [[fuzzingbook-20-concolic-fuzzer|Ch 20]].

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] picks up exactly where Ch 19 left off: it directly reuses Ch 19's `eval()`-vulnerable SQL database (`DB`, `INVENTORY_GRAMMAR`, `db_select`) and addresses information flow's incompleteness by replacing taint labels with *symbolic path conditions*. [[ConcolicExecution|Concolic execution]] captures not just whether input reached a sink but the precise constraints under which it does (e.g. that a query's table must equal `inventory`), and the `ConcolicGrammarFuzzer` lifts those constraints back into the grammar to reach the dangerous `eval()` sink that taint-directed fuzzing only *steered toward*.

## Connections
- [[DynamicTaintAnalysis]] / [[DynamicTaintTracking]] — the runtime mechanism used to track information flow at the character/value level.
- [[ConcolicExecution]] / [[PathConstraint]] — Ch 20's path-condition approach that records *what must be true* of input to reach a sink, not just *that* it does.
- [[TaintedString]] (`tstr`) / [[CharacterOrigin]] (`ostr`) — the concrete carriers of flow information in Ch 19.
- [[DataFlow]] (explicit) vs [[ImplicitInformationFlow]] (implicit / control flow) — the two kinds of flow; only explicit flow is followed by taint tracking.
- [[CodeInjection]] — the integrity violation prevented by source→sink flow checks.
- [[TaintDirectedFuzzing]] — using observed flows to direct a fuzzer.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — symbolic/concolic execution, which can follow implicit flows.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — grammar mining built on flow/taint information.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing" (reuses Ch 19's vulnerable DB; replaces taint with symbolic path conditions to reach the sink).
