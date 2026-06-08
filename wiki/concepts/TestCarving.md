---
title: "Test Carving"
type: concept
tags: [testing, fuzzing, carving, unit-testing, record-replay, test-generation, python]
sources: [fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Test Carving

**Carving** is a [[RecordReplay|record-and-replay]] technique that automatically extracts a set of fast, self-contained [[UnitTesting|unit tests]] from a single expensive *system test*. The procedure is: (1) while running an end-to-end / [[IntegrationTesting|integration]] execution, **record** every function call — its name, arguments, and read variables; (2) from each recording **synthesize** a stand-alone unit test that reconstructs the call; (3) **replay** that test in isolation, where a single function call runs orders of magnitude faster than the whole system. Carving was invented by Elbaum et al. (2006) and originally implemented for Java.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] implements carving in Python and (following Elbaum et al.) records and serializes *method arguments only*, ignoring globals and other read state. The running example is a one-line `webbrowser()` that downloads a URL; carving the system run lets the chapter pull out the internal `urlparse()` call and replay it alone — measuring it as tens of thousands of times cheaper than re-running the browser. The recorder is the [[Carver|`Carver`/`CallCarver`]] class; replay turns calls into runnable strings (`simple_call_string()` / `call_string()`) executed via `eval`, with [[Serialization|pickling]] used to reconstruct complex object arguments.

For `webbrowser()`, a large majority of carved calls convert to call strings but only about a quarter actually re-run — the rest fail because an internal name is out of scope or an external resource cannot be reconstructed. Carving therefore works best for functions that are largely pure transforms of their arguments. The chapter then lifts plain replay into [[APIFuzzing|API fuzzing]] by mining a grammar from carved calls (see [[APIGrammarMining]]), and a `ResultCarver` exercise records return values to synthesize [[RegressionTesting|regression]] assertions.

## Connections
- [[Carver]] — the `Carver`/`CallCarver` recorder that does the tracing.
- [[RecordReplay]] — the paradigm carving instantiates.
- [[Serialization]] — reconstructs complex object arguments for replay.
- [[APIGrammarMining]] — turns carved calls into a recombinable API grammar.
- [[UnitTesting]] — the cheap test level carving produces.
- [[IntegrationTesting]] — the system/end-to-end level carving harvests calls from.
- [[RegressionTesting]] — the `ResultCarver` exercise adds return-value assertions.
- [[APIFuzzing]] / [[CallSequenceFuzzing]] — carved grammars/sequences fuzz the API without hand-written grammars.
- [[Coverage]] — the `sys.settrace` tracing mechanism carving reuses.
- [[AndreasZeller]] / [[RahulGopinath]] / [[CISPA]] — authors and publisher.

## Sources
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
