---
title: "Carver (CallCarver)"
type: concept
tags: [fuzzing, testing, carving, tracing, record-replay, python, tool]
sources: [fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Carver (CallCarver)

**`Carver`** (and its subclass **`CallCarver`**) is the Python class in *The Fuzzing Book* that records function calls during an execution so they can later be replayed as standalone unit tests — the recording engine behind [[TestCarving|carving]].

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] builds the recorder on the same `sys.settrace` machinery used for [[Coverage|code coverage]] in [[fuzzingbook-04-coverage|Ch 4]]:

- **`Carver`** is a context manager: `__enter__` saves `sys.gettrace()` and installs `self.traceit` via `sys.settrace`; `__exit__` restores the original tracer. It is used as `with CallCarver() as carver: ...`.
- **`CallCarver.traceit(frame, event, arg)`** filters to `event == "call"` events. For each call it records, under both the bare and the module-qualified function name, a list of `(parameter_name, value)` argument pairs.
- Two helpers do the extraction: **`get_qualified_name(code)`** prefixes the module name (e.g. `urllib.parse.urlparse`), and **`get_arguments(frame)`** copies `frame.f_locals` (which, at call time, are exactly the parameters) and reverses them into call order.
- Accessors: **`calls()`** (the full dict), **`arguments(function_name)`** (list of recorded argument lists for one function), and **`called_functions(qualified=False)`** (function names seen, optionally only module-qualified ones).

Recorded calls are rendered to runnable strings by `simple_call_string()` / `call_string()` and replayed with `eval`. The chapter's `ResultCarver` exercise subclasses `CallCarver` to additionally capture `event == "return"` values (via a call stack), enabling synthesized [[RegressionTesting|regression]] assertions; the [[APIGrammarMining|`CallGrammarMiner`]] consumes a `Carver` to mine a recombinable API grammar.

## Connections
- [[TestCarving]] — the technique the `Carver` implements.
- [[RecordReplay]] — the record half of record-and-replay.
- [[Serialization]] — pickles complex argument values for replayable call strings.
- [[APIGrammarMining]] — `CallGrammarMiner(carver)` mines a grammar from a `Carver`.
- [[Coverage]] — the `sys.settrace` tracer `Carver` mirrors (Ch 4).
- [[GrammarMiner]] — the sibling tracer-based miner for *input* grammars.
- [[RegressionTesting]] — the `ResultCarver` subclass records return values.
- [[AndreasZeller]] / [[RahulGopinath]] / [[CISPA]] — authors and publisher.

## Sources
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
