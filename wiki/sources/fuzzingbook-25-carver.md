---
title: "The Fuzzing Book Ch 25 — Carving Unit Tests"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, carving, unit-testing, record-replay, serialization, api-fuzzing, regression-testing]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-25-carver.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Carving Unit Tests

## Summary
This chapter introduces **carving**: a [[RecordReplay|record-and-replay]] technique that automatically converts an expensive *system test* into a set of cheap, self-contained [[UnitTesting|unit tests]]. While running an end-to-end execution, a tracer records every function call — its name and its arguments — so that each call can later be *replayed* in isolation, far faster than re-running the whole system. The central worked example is a tiny `webbrowser()` that downloads a URL; carving extracts the internal `urlparse()` call (and hundreds of others) and shows that running `urlparse()` alone is tens of thousands of times faster than driving the whole browser. The chapter then goes further: from carved calls it *mines an API grammar* (one rule per argument, with the observed values as alternatives), so the recorded arguments can be **recombined** to fuzz the API — synthesizing [[APIFuzzing|API tests]] without writing a grammar by hand. It is the automatic-recording counterpart to [[fuzzingbook-24-api-fuzzer|Ch 24]] (which hand-authors call grammars) and builds on the `sys.settrace` machinery of [[fuzzingbook-04-coverage|Ch 4]] and [[fuzzingbook-23-configuration-fuzzer|Ch 23]]; it opens Part V's bridge from system-level to unit-level [[Fuzzing|fuzzing]].

## Key Concepts
- **[[TestCarving|Carving]]** — the umbrella technique: record all calls (name + arguments + read variables) during a system test, then synthesize a self-contained unit test that reconstructs each call and can be replayed efficiently. Invented by Elbaum et al. (2006), originally for Java; this chapter follows their choice of recording/serializing *method arguments only* (ignoring globals and other read state).
- **[[Carver|`Carver` / `CallCarver`]]** — the recorder. `Carver` is a `with`-block context manager that installs a `sys.settrace` tracer (`__enter__`/`__exit__` swap `sys.gettrace()`). `CallCarver.traceit()` filters to `event == "call"` events and stores, per function, a list of argument lists where each argument is a `(parameter_name, value)` pair. Helpers `get_qualified_name(code)` (module-qualified name) and `get_arguments(frame)` (read `frame.f_locals`, reversed to call order) feed it; accessors are `calls()`, `arguments(function_name)`, and `called_functions(qualified=False)`.
- **[[RecordReplay|Record & replay]]** — recorded calls are turned into runnable strings (`simple_call_string()` → `function_name(var=repr(value), ...)`) and re-executed with `eval`. Three replay challenges: making out-of-scope function *names* visible, reconstructing external *resources* (files, sockets), and rebuilding *complex objects*.
- **[[Serialization|Serialization / pickling]]** — the answer to complex objects. `call_value()` detects a non-primitive (its `repr` contains `<`) and emits `pickle.loads(<pickled bytes>)`; `call_string()` additionally turns a leading `self` argument into a method call on the unpickled object. This lets carved calls like `email.parser.Parser.parse(...)` be replayed with their original `Parser` and `StringIO` objects reconstructed.
- **[[APIGrammarMining|`CallGrammarMiner`]]** — given a `Carver`, builds a [[Grammar|grammar]] from observed calls: `initial_grammar()` seeds `<start> ::= <call>`; `mine_arguments_grammar()` makes one rule per argument variable expanding into the *set* of observed values (escaping literal `<` via `<langle>`); `mine_function_grammar()` wraps those into a call rule (a method call if the first var is `self`); `mine_call_grammar()` repeats over all called functions (skipping internal `_`/`<` names). A [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] on the result yields recombined calls — [[APIFuzzing|API-level fuzzing]] of recorded arguments. This is a sibling of the [[GrammarMiner]] line but mines *call* grammars rather than *input* grammars.
- **Coverage of the technique** — for `webbrowser()`, a large majority of calls convert to call strings, but only ~a quarter actually *run*: the rest fail mostly because an internal name is out of scope or a resource cannot be reconstructed. Carving works well precisely when a function is largely a pure transform of its arguments.
- **Exercises** — a `ResultCarver` (subclassing `CallCarver`) that also records `event == "return"` values via a call stack, enabling synthesized `assert call == result` equalities for [[RegressionTesting|regression testing]]; and an argument-abstraction scheme that widens observed values (e.g. `foo(1)`, `foo(2)` → `foo(<int>)`).

## Key Claims
- Carving **automatically converts system tests into unit tests** by recording calls and replaying them; no hand-written unit tests or grammars are required.
- A single function call can be **orders of magnitude faster** than a full system run — the chapter measures `urlparse()` as tens of thousands of times cheaper than `webbrowser()`, and `urlsplit()` similarly versus the browser.
- **Serialization (pickling)** provides persistent, reconstructable representations of complex objects, making it possible to replay calls whose arguments are non-primitive objects.
- Carving is **hard or impossible** for functions that interact heavily with their environment or access external resources (files, network); the book records arguments only, ignoring globals — about three-quarters of `webbrowser()`'s carved calls fail to re-run.
- From carved calls one can **mine an API grammar** that arbitrarily *recombines* observed arguments, lifting plain replay into API-level fuzzing — but recombination risks **violating implicit preconditions**, producing *false alarms* that must be weeded out (e.g. by constraining the grammar).

## Key Quotes
> "The key idea is to _record_ such calls such that we can _replay_ them later – as a whole or selectively." — the carving thesis.

> "_Serialization_ allows creating persistent representations of complex objects." — Lessons Learned, on pickling arguments for replay.

> "we can _synthesize API tests without having to write a grammar at all._" — combining carving with the grammar mining of [[fuzzingbook-24-api-fuzzer|Ch 24]].

## Connections
- [[TestCarving]] — the chapter's central technique (record system-test calls, replay as unit tests).
- [[Carver]] — the `Carver`/`CallCarver` classes that record calls via `sys.settrace`.
- [[RecordReplay]] — the record-and-replay paradigm carving instantiates.
- [[Serialization]] — pickling complex object arguments so calls can be reconstructed.
- [[APIGrammarMining]] — the `CallGrammarMiner` that turns carved calls into a recombinable API grammar.
- [[UnitTesting]] — carving's output; system tests become fast unit tests.
- [[IntegrationTesting]] — the system/end-to-end level carving harvests calls *from*.
- [[RegressionTesting]] — the `ResultCarver` exercise records return values to build regression assertions.
- [[APIFuzzing]] — carved grammars enable function-level fuzzing without hand-written call grammars.
- [[CallSequenceFuzzing]] — carving naturally records *sequences* of calls in valid application context.
- [[GrammarMiner]] — the sibling input-grammar miner; `CallGrammarMiner` mines call grammars instead.
- [[GrammarMining]] / [[GrammarInference]] — the broader learn-a-grammar-from-execution family.
- [[GrammarCoverageFuzzer]] — fuzzes the mined call grammar to recombine arguments.
- [[Grammar]] — the data structure produced from carved calls.
- [[Coverage]] — the `sys.settrace` tracing mechanism reused (from [[fuzzingbook-04-coverage|Ch 4]]).
- [[AndreasZeller]] / [[RahulGopinath]] / [[CISPA]] — authors and publisher.
- [[fuzzingbook-24-api-fuzzer|Ch 24]] — hand-authors call grammars; carving automates the recording of args/sequences.
- [[fuzzingbook-23-configuration-fuzzer|Ch 23]] — supplies the dynamic call/variable tracing carving builds on.
- [[fuzzingbook-04-coverage|Ch 4]] — the `Coverage`/`sys.settrace` tracer the `Carver` reuses.
- [[fuzzingbook-02-intro-testing|Ch 2]] — the unit-test/oracle foundations carving automates (and the `my_sqrt` running example).
- [[fuzzingbook-16-reducer|Ch 16]] — the next chapter, on reducing failure-inducing inputs.

## Contradictions
- None identified.
