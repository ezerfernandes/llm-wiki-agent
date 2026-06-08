---
title: "Dynamic Analysis"
type: concept
tags: [dynamic-analysis, testing, instrumentation, coverage, debugging]
sources: [fuzzingbook-04-coverage, fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# DynamicAnalysis

**Dynamic analysis** is the analysis of a program by observing *what actually happens during execution* — which lines run, which values variables take, which paths are exercised — as opposed to **static analysis**, which reasons about the source/binary without running it. Coverage measurement is a canonical dynamic analysis; so are profiling, taint tracking, and dynamic invariant mining.

## From The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] introduces dynamic analysis through Python's `sys.settrace()` [[TraceFunction|trace function]], calling it "an ideal tool for dynamic analysis – that is, the analysis of what actually happens during an execution." The chapter's `Coverage` class is its first concrete instance: by recording every executed `(function, line)` location it answers the dynamic question *"which code did this run touch?"* The chapter contrasts the dynamic `cov_max` proxy for maximum coverage (run the good test cases and union their coverage) with the *static* alternative of analyzing code structure, which it defers to the symbolic-testing chapter ([[fuzzingbook-21-symbolic-fuzzer|Ch 21]]). Dynamic analysis recurs across the book — e.g. tracking [[fuzzingbook-19-information-flow|information flow (Ch 19)]] and mining [[fuzzingbook-22-dynamic-invariants|dynamic invariants (Ch 22)]].

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] is a paradigmatic dynamic analysis: it reuses the very `sys.settrace` machinery from Ch 4, but to capture *values* rather than *locations*. Its `CallTracker` records each function's argument and return values per call (reading `frame.f_locals`), and from these observations it infers [[TypeInference|types]] and [[DynamicInvariant|value invariants]] ([[SpecificationMining|specification mining]]). The chapter draws the explicit dynamic-vs-static line: mined specs hold only for *observed* executions (hence overspecialize without diverse runs), in contrast to the static guarantees a [[StaticAnalysis|static analysis]] / [[SymbolicExecution|symbolic execution]] would provide. The mined types and ranges are themselves *inputs* to the static/symbolic analyses of [[fuzzingbook-21-symbolic-fuzzer|Ch 21]].

## Connections
- [[TraceFunction]] — `sys.settrace` is the dynamic-analysis hook this chapter uses.
- [[Coverage]] — the chapter's flagship dynamic analysis.
- [[StaticAnalysis]] — the complementary "without running it" approach (e.g. MyPy in Ch 3).
- [[Debugger]] — interactive dynamic inspection of a running program.
- [[fuzzingbook-04-coverage|Ch 4]] — where the term is introduced.
- [[fuzzingbook-19-information-flow|Ch 19]] / [[fuzzingbook-22-dynamic-invariants|Ch 22]] — later dynamic analyses (taint, invariant mining).
- [[SpecificationMining]] / [[DynamicInvariant]] / [[TypeInference]] — Ch 22's value-tracing dynamic analysis.

## Sources
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications" (value-tracing dynamic analysis for spec mining).
